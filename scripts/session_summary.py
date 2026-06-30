#!/usr/bin/env python3
"""
Session Summary Hook — runs automatically when a Claude Code session ends (Stop event).
Reads the session transcript piped via stdin, summarizes what was done,
appends a bullet-point log entry to docs/THESIS_STATUS.md,
then automatically commits and pushes all changes to GitHub.
"""

import json
import sys
import os
import re
import subprocess
from datetime import date

def extract_transcript(data: dict) -> str:
    """Pull assistant messages from the hook payload."""
    messages = []
    for item in data.get("messages", []):
        if item.get("role") == "assistant":
            content = item.get("content", "")
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        messages.append(block.get("text", ""))
            elif isinstance(content, str):
                messages.append(content)
    return "\n".join(messages)

def extract_tool_actions(data: dict) -> list:
    """Pull file edits and tool uses as concrete actions."""
    actions = []
    for item in data.get("messages", []):
        content = item.get("content", "")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    name = block.get("name", "")
                    inp = block.get("input", {})
                    if name in ("Write", "Create", "str_replace_based_edit_tool"):
                        path = inp.get("path", inp.get("file_path", "unknown file"))
                        actions.append(f"Edited/created `{os.path.basename(path)}`")
                    elif name == "Bash":
                        cmd = inp.get("command", "")[:80]
                        actions.append(f"Ran command: `{cmd}`")
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for a in actions:
        if a not in seen:
            seen.add(a)
            unique.append(a)
    return unique

def build_summary(transcript: str, tool_actions: list) -> list:
    """
    Build bullet points from the transcript.
    Looks for patterns like completed tasks, decisions, and file changes.
    Falls back to tool actions if transcript is sparse.
    """
    bullets = []

    # Look for explicit "completed", "done", "finished", "created", "updated", "wrote" signals
    done_patterns = [
        r"(?:completed?|finished?|drafted?|wrote|created?|updated?|added?|revised?)[^.]{5,80}\.",
        r"(?:Chapter \d|Section \d+\.\d+)[^.]{5,80}\.",
        r"(?:LULC|Landsat|QGIS|buffer|classification|change detection)[^.]{5,80}\.",
    ]
    for pattern in done_patterns:
        matches = re.findall(pattern, transcript, re.IGNORECASE)
        for m in matches[:5]:  # cap at 5 per pattern
            cleaned = m.strip().rstrip(".")
            if len(cleaned) > 15:
                bullets.append(cleaned)

    # Add tool actions as concrete evidence
    for action in tool_actions[:5]:
        bullets.append(action)

    # Deduplicate
    seen = set()
    unique = []
    for b in bullets:
        key = b.lower()[:40]
        if key not in seen:
            seen.add(key)
            unique.append(b)

    if not unique:
        unique = ["Session completed — no specific actions detected (update manually if needed)"]

    return unique[:8]  # Keep summary tight

def append_to_status(bullets: list, status_path: str):
    """Append a dated session log block to THESIS_STATUS.md."""
    today = date.today().strftime("%Y-%m-%d")

    entry_lines = [f"\n### Session — {today}"]
    for b in bullets:
        entry_lines.append(f"- {b}")
    entry_lines.append("")  # trailing newline

    entry = "\n".join(entry_lines)

    # Read existing file
    if os.path.exists(status_path):
        with open(status_path, "r") as f:
            content = f.read()
    else:
        content = "# Thesis Status\n"

    # Insert after the "Recent Changes" section header if it exists, else append
    marker = "## 🔁 Recent Changes"
    if marker in content:
        insert_pos = content.index(marker) + len(marker)
        # Move past the header line
        next_newline = content.index("\n", insert_pos)
        content = content[:next_newline + 1] + entry + content[next_newline + 1:]
    else:
        content += entry

    with open(status_path, "w") as f:
        f.write(content)

    print(f"[session_summary] ✅ Appended {len(bullets)} bullet(s) to {status_path}")

def auto_push(bullets: list):
    """
    Stage all changes, commit with a session summary message, and push to GitHub.
    Skips gracefully if git is not initialized or there's nothing to push.
    """
    today = date.today().strftime("%Y-%m-%d")

    # Build a compact commit message from the first 2 bullets
    summary_lines = bullets[:2]
    summary = "; ".join(summary_lines) if summary_lines else "Session update"
    # Trim commit message to 72 chars (git convention)
    commit_msg = f"[{today}] {summary}"[:72]

    try:
        # Check git repo exists
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print("[auto_push] ⚠️  No git repo found — skipping push. Run: bash scripts/thesis_push.sh init your-username")
            return

        # Stage everything
        subprocess.run(["git", "add", "-A"], check=True)

        # Check if there's anything to commit
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            capture_output=True
        )
        if diff.returncode == 0:
            print("[auto_push] ℹ️  No changes to commit — working tree clean.")
            return

        # Commit
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"[auto_push] ✅ Committed: {commit_msg}")

        # Push
        push = subprocess.run(
            ["git", "push", "origin", "main"],
            capture_output=True, text=True
        )
        if push.returncode == 0:
            print("[auto_push] ✅ Pushed to GitHub successfully!")
        else:
            # Common case: remote not set up yet
            print("[auto_push] ⚠️  Push failed — remote may not be set up yet.")
            print("   Run once: bash scripts/thesis_push.sh init your-github-username")
            print(f"   Error: {push.stderr.strip()}")

    except FileNotFoundError:
        print("[auto_push] ⚠️  Git not found — install Git to enable auto-push.")
    except subprocess.CalledProcessError as e:
        print(f"[auto_push] ⚠️  Git error: {e}")


def main():
    # Claude Code pipes the session payload as JSON on stdin
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        data = {}

    transcript = extract_transcript(data)
    tool_actions = extract_tool_actions(data)
    bullets = build_summary(transcript, tool_actions)

    # Step 1 — Write session summary to THESIS_STATUS.md
    status_path = os.path.join("docs", "THESIS_STATUS.md")
    append_to_status(bullets, status_path)

    # Step 2 — Auto commit and push everything to GitHub
    auto_push(bullets)

if __name__ == "__main__":
    main()
