#!/bin/bash
# Detect project context for Claude Code sessions
# Outputs structured information about current project and available subprojects

# Determine MONO_ROOT relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MONO_ROOT="$(cd "$SCRIPT_DIR" && git rev-parse --show-toplevel 2>/dev/null || echo "$SCRIPT_DIR")"

echo "=== CURRENT CONTEXT ==="
echo "pwd: $(pwd)"
echo "git_root: $(git rev-parse --show-toplevel 2>/dev/null || echo 'none')"
echo "branch: $(git branch --show-current 2>/dev/null || echo 'none')"
echo "uncommitted: $(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')"

echo ""
echo "=== SUBPROJECTS ==="

for dir in "$MONO_ROOT"/repo/*/; do
    [ -d "$dir" ] || continue
    name=$(basename "$dir")

    # Check properties
    has_git="false"
    has_memory="false"
    has_external_memory="false"
    branch="none"
    uncommitted="0"

    [ -d "$dir/.git" ] && has_git="true"
    [ -d "$dir/memory" ] && has_memory="true"
    [ -d "$MONO_ROOT/repo/$name.memory" ] && has_external_memory="true"

    if [ "$has_git" = "true" ]; then
        branch=$(git -C "$dir" branch --show-current 2>/dev/null || echo "none")
        uncommitted=$(git -C "$dir" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    fi

    echo "- name: $name"
    echo "  path: repo/$name/"
    echo "  git: $has_git"
    echo "  branch: $branch"
    echo "  uncommitted: $uncommitted"
    echo "  memory: $has_memory"
    echo "  external_memory: $has_external_memory"
done

echo ""
echo "=== MONO ==="
echo "path: $MONO_ROOT"
echo "memory: $([ -d "$MONO_ROOT/memory" ] && echo 'true' || echo 'false')"
echo "branch: $(git -C "$MONO_ROOT" branch --show-current 2>/dev/null || echo 'none')"
echo "uncommitted: $(git -C "$MONO_ROOT" status --porcelain 2>/dev/null | wc -l | tr -d ' ')"