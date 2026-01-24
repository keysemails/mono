#!/usr/bin/env python3
"""
Generates a session context snapshot for the memory folder.
Run at session start via hook. Creates a read-only overview.

Updates memory/meta - dynamic context.md
"""

import subprocess
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path(__file__).parent.parent.parent / "memory"
DYNAMIC_CONTEXT = MEMORY_DIR / "meta - dynamic context.md"

def get_recent_changes(days=7):
    """Get files changed in git recently that still exist."""
    try:
        result = subprocess.run(
            ["git", "log", f"--since={days} days ago", "--name-only", "--pretty=format:", "--", "memory/"],
            capture_output=True, text=True, cwd=MEMORY_DIR.parent
        )
        files = set(f.strip() for f in result.stdout.split('\n') if f.strip() and f.endswith('.md'))
        existing = [f for f in files if (MEMORY_DIR.parent / f).exists()]
        return sorted(existing)
    except Exception:
        return []

def get_latest_session():
    """Find the most recent session file."""
    sessions = list(MEMORY_DIR.glob("session - *.md"))
    if not sessions:
        return None
    sessions.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return sessions[0].stem

def get_prior_commit():
    """Get current commit hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=MEMORY_DIR.parent
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"

def generate_context():
    """Generate the session context file."""
    recent = get_recent_changes()
    latest_session = get_latest_session()
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    prior_commit = get_prior_commit()

    content = f"""---
created: 2026-01-23T13:15:00
changed: {now}
prior_commit: {prior_commit}
---

# Session Context

Auto-generated snapshot at session start. Read-only - do not update during work.

## Recent Changes

Files changed in the last 7 days:
"""

    if recent:
        for f in recent[:15]:
            content += f"- [[{f.replace('memory/', '').replace('.md', '')}]]\n"
    else:
        content += "- (none)\n"

    content += "\n## Last Session\n\n"
    if latest_session:
        content += f"[[{latest_session}]]\n"
    else:
        content += "(no previous sessions)\n"

    DYNAMIC_CONTEXT.write_text(content)
    print(f"Updated {DYNAMIC_CONTEXT.name}")
    print(f"  Recent changes: {len(recent)}")

if __name__ == "__main__":
    generate_context()
