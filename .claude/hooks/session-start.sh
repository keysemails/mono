#!/bin/bash

# Session start hook - loads context BEFORE first user message
#
# This hook reads INIT.md and all required session-start files,
# outputting their contents so Claude has full context immediately.
# Dynamic context collection happens AFTER first user message (see INIT.md flow).

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Read .PROJECT file if it exists (default project selection)
DEFAULT_PROJECT=""
if [[ -f "$REPO_ROOT/.PROJECT" ]]; then
    DEFAULT_PROJECT=$(cat "$REPO_ROOT/.PROJECT")
fi

# Read INIT.md
INIT_CONTENT=""
if [[ -f "$REPO_ROOT/INIT.md" ]]; then
    INIT_CONTENT=$(cat "$REPO_ROOT/INIT.md")
fi

# Read required session-start files (as specified in INIT.md)
FILE_CONVENTIONS=""
if [[ -f "$REPO_ROOT/memory/meta - file conventions.md" ]]; then
    FILE_CONVENTIONS=$(cat "$REPO_ROOT/memory/meta - file conventions.md")
fi

# Argument syntax and processing instructions
ARG_SYNTAX='@(some file name)
may be a file path
it may be the name of a file somewhere in the dir
it may be missspelled
it may exist in a place not accessible
try to resolve the argument via the terminal, with the less costly trys first
tell the user that you could not find the file with approach x and will now try y
if multiple options exist in the end present as options to the user
and ask for a selection before continuing

p(some prompt that can contain whitespace)
will contain instructions or questions'

PROCESSING_SYNTAX='{{
files may contain further prompts in these double brackets
{{
which me be nested
}}
{{2020-12-12 12:20
which may be tagged by date
}}
}}
if nothing else is mentioned in combination with @file
process those prompts that are not yet tagged with a date
unless asked to include certain date ranges.
after processing, unless stated otherwise, tag the current date (use the terminal to get an accurate timestamp)'

FILE_PROCESSING='if processing a file (e.g. resolved via @file) <file-name>
create a folder <file-name>/ if it not already exists
then move the <file-name> into that folder
and create a new file in its stead where you make requested changes

if processed files come in this naming scheme:
prefix - yyyy-mm-dd-hhmm - claim.md

then update the date (and potentially claim) for the new file you create in its stead

make sure to rename the name of the version folder as well
to match the new file'

# Build the full context - escape for JSON
# Using jq for proper JSON escaping
FULL_CONTEXT=$(cat << 'CONTEXT_EOF'
# Session Context (loaded before first message)

## INIT.md

CONTEXT_EOF
)
FULL_CONTEXT="$FULL_CONTEXT
$INIT_CONTENT

---

## memory/meta - file conventions.md

$FILE_CONVENTIONS

---

## Argument Syntax

$ARG_SYNTAX

---

## Processing Syntax

$PROCESSING_SYNTAX

---

## File Processing

$FILE_PROCESSING"

# Add default project info if .PROJECT exists
if [[ -n "$DEFAULT_PROJECT" ]]; then
    FULL_CONTEXT="$FULL_CONTEXT

---

## Default Project (.PROJECT)

$DEFAULT_PROJECT

**Note:** This is the default project set via \`/default-project\`. Skip project selection and use this context unless the user's request clearly involves a different project."
fi

# Use jq to properly escape the content for JSON
ESCAPED_CONTEXT=$(echo "$FULL_CONTEXT" | jq -Rs .)

# Output hook JSON
cat << EOF
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": $ESCAPED_CONTEXT
  }
}
EOF
