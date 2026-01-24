#!/usr/bin/env python3
"""Convert Claude Code session JSONL to markdown."""

import json
import re
import sys
import os
from datetime import datetime
from pathlib import Path

def get_project_path_encoded(project_path):
    """Encode project path the way Claude Code does it."""
    return project_path.replace("/", "-")

def find_session_file(project_path, session_id=None):
    """Find the session JSONL file."""
    claude_dir = Path.home() / ".claude" / "projects"
    encoded = get_project_path_encoded(project_path)
    project_dir = claude_dir / encoded

    if session_id:
        return project_dir / f"{session_id}.jsonl"

    # Find the most recent session
    sessions = list(project_dir.glob("*.jsonl"))
    if not sessions:
        raise FileNotFoundError(f"No sessions found in {project_dir}")
    return max(sessions, key=lambda p: p.stat().st_mtime)

def fix_vertical_text(text):
    """Fix text that has been split character-by-character or word-by-word onto separate lines.

    This handles cases like XML tags split across lines:
    <
    c
    o
    m
    m
    a
    n
    d
    >

    Should become: <command>
    """
    # First pass: use regex to find and collapse vertical character sequences
    # Pattern: newline followed by single character/short word, repeated 3+ times
    def collapse_vertical(match):
        lines = match.group(0).split('\n')
        # Filter out empty lines and join
        chars = [l.strip() for l in lines if l.strip()]
        return ''.join(chars)

    # Match sequences of lines where each line is a single char or very short word
    # This handles: \n<\nc\no\nm\n-\nm\ne\ns\ns\na\ng\ne\n>
    pattern = r'(?:\n[^\n]{1,2}){3,}'
    text = re.sub(pattern, collapse_vertical, text)

    # Second pass: fix any remaining broken XML-like tags
    # Pattern: < followed by fragmented content followed by >
    # This catches cases where < is at end of a line
    def fix_broken_tag(match):
        content = match.group(0)
        # Remove newlines within the tag
        return re.sub(r'\s+', '', content)

    # Match broken tags like "< \n command \n - \n message \n >"
    tag_pattern = r'<(?:\s*[a-zA-Z0-9_/-]*\s*)+>'
    text = re.sub(tag_pattern, fix_broken_tag, text)

    return text


def format_tool_block(tool_calls):
    """Format a list of tool calls as a code block."""
    if not tool_calls:
        return ""
    return "```tool\n" + "\n".join(tool_calls) + "\n```"


def consolidate_tool_calls(messages):
    """Consolidate consecutive tool-only messages into a single code block."""
    result = []
    tool_buffer = []

    for role, content, tools in messages:
        if role == "assistant":
            # If this message has only tools and no text
            if tools and not content.strip():
                tool_buffer.extend(tools)
            else:
                # Flush tool buffer first
                if tool_buffer:
                    result.append(("assistant", format_tool_block(tool_buffer), []))
                    tool_buffer = []

                # If this message has both text and tools, append tools after text
                if tools:
                    combined = content.strip()
                    if combined:
                        combined += "\n\n"
                    combined += format_tool_block(tools)
                    result.append((role, combined, []))
                else:
                    result.append((role, content, []))
        else:
            # Flush tool buffer before user message
            if tool_buffer:
                result.append(("assistant", format_tool_block(tool_buffer), []))
                tool_buffer = []

            result.append((role, content, []))

    # Flush any remaining tool buffer
    if tool_buffer:
        result.append(("assistant", format_tool_block(tool_buffer), []))

    return result


def format_tool_call(item, project_path=None):
    """Format a tool call with its relevant arguments."""
    name = item.get("name", "unknown")
    inp = item.get("input", {})

    def shorten_path(path):
        """Shorten absolute paths relative to project."""
        if project_path and path.startswith(project_path):
            return path[len(project_path):].lstrip('/')
        # Also try home directory
        home = str(Path.home())
        if path.startswith(home):
            return '~' + path[len(home):]
        return path

    if name == "Bash":
        cmd = inp.get("command", "")
        # Truncate very long commands
        if len(cmd) > 100:
            cmd = cmd[:97] + "..."
        return f"bash: {cmd}"
    elif name == "Read":
        path = shorten_path(inp.get("file_path", ""))
        return f"read: {path}"
    elif name == "Edit":
        path = shorten_path(inp.get("file_path", ""))
        return f"edit: {path}"
    elif name == "Write":
        path = shorten_path(inp.get("file_path", ""))
        return f"write: {path}"
    elif name == "Glob":
        pattern = inp.get("pattern", "")
        path = inp.get("path", "")
        if path:
            return f"glob: {pattern} in {shorten_path(path)}"
        return f"glob: {pattern}"
    elif name == "Grep":
        pattern = inp.get("pattern", "")
        path = inp.get("path", "")
        if path:
            return f"grep: {pattern} in {shorten_path(path)}"
        return f"grep: {pattern}"
    elif name == "TodoWrite":
        return "todo: update task list"
    elif name == "AskUserQuestion":
        return "ask: user question"
    elif name == "Task":
        desc = inp.get("description", "")
        return f"task: {desc}" if desc else "task: spawn agent"
    else:
        return f"{name.lower()}"


def extract_text_content(content_array, project_path=None):
    """Extract text, thinking, and tool calls from content array."""
    text_parts = []
    thinking_parts = []
    tool_calls = []

    for item in content_array:
        # Handle string items directly
        if isinstance(item, str):
            text_parts.append(item)
            continue
        # Handle dict items
        if not isinstance(item, dict):
            continue
        if item.get("type") == "text":
            text_parts.append(item.get("text", ""))
        elif item.get("type") == "thinking":
            thinking_parts.append(item.get("thinking", ""))
        elif item.get("type") == "tool_use":
            tool_calls.append(format_tool_call(item, project_path))

    return "\n".join(text_parts), "\n".join(thinking_parts), tool_calls

def convert_session(jsonl_path, include_thinking=False, project_path=None):
    """Convert JSONL session to markdown."""
    messages = []

    with open(jsonl_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            entry_type = entry.get("type")

            if entry_type == "user":
                content = entry.get("message", {}).get("content", [])
                text, _, _ = extract_text_content(content, project_path)
                if text.strip():
                    # Clean up system tags for readability
                    text = text.replace("<ide_opened_file>", "").replace("</ide_opened_file>", "")
                    text = text.replace("<system-reminder>", "").replace("</system-reminder>", "")
                    # Fix vertical text (characters on individual lines)
                    text = fix_vertical_text(text)
                    messages.append(("user", text.strip(), []))

            elif entry_type == "assistant":
                content = entry.get("message", {}).get("content", [])
                text, thinking, tools = extract_text_content(content, project_path)
                if text.strip() or tools or (include_thinking and thinking.strip()):
                    msg = ""
                    if include_thinking and thinking.strip():
                        msg += f"<details><summary>Thinking</summary>\n\n{thinking}\n\n</details>\n\n"
                    if text.strip():
                        msg += text
                    messages.append(("assistant", msg.strip(), tools))

    # Consolidate consecutive tool-only messages
    messages = consolidate_tool_calls(messages)

    # Build markdown
    md_lines = []
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    md_lines.append("---")
    md_lines.append(f"created: {timestamp}")
    md_lines.append(f"changed: {timestamp}")
    md_lines.append(f"prior_commit: null")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"# Session Export")
    md_lines.append("")

    for role, content, _ in messages:
        if role == "user":
            md_lines.append(f"> **User:** {content}")
            md_lines.append("")
        else:
            md_lines.append(content)
            md_lines.append("")
            md_lines.append("---")
            md_lines.append("")

    return "\n".join(md_lines)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert Claude session JSONL to markdown")
    parser.add_argument("--project", "-p", default=os.getcwd(), help="Project path")
    parser.add_argument("--session", "-s", help="Session ID (defaults to most recent)")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--thinking", "-t", action="store_true", help="Include thinking blocks")
    args = parser.parse_args()

    try:
        session_file = find_session_file(args.project, args.session)
        markdown = convert_session(session_file, args.thinking, args.project)

        if args.output:
            with open(args.output, "w") as f:
                f.write(markdown)
            print(f"Exported to: {args.output}")
        else:
            print(markdown)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
