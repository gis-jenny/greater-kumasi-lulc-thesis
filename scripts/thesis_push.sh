#!/bin/bash
# =============================================================================
# thesis_push.sh — Initialize GitHub repo (first time) and push latest updates
# Usage:
#   First time:  bash scripts/thesis_push.sh init "your-github-username"
#   Every push:  bash scripts/thesis_push.sh "your commit message"
# =============================================================================

set -e  # Exit on any error

REPO_NAME="greater-kumasi-lulc-thesis"
BRANCH="main"

# ── Helpers ──────────────────────────────────────────────────────────────────
green()  { echo -e "\033[32m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }
red()    { echo -e "\033[31m$1\033[0m"; }

check_gh_cli() {
    if ! command -v gh &> /dev/null; then
        red "❌ GitHub CLI (gh) is not installed."
        echo "   Install it from: https://cli.github.com"
        echo "   Then run: gh auth login"
        exit 1
    fi
    if ! gh auth status &> /dev/null; then
        red "❌ Not logged into GitHub CLI."
        echo "   Run: gh auth login"
        exit 1
    fi
}

check_git() {
    if ! command -v git &> /dev/null; then
        red "❌ Git is not installed. Install Git first."
        exit 1
    fi
}

# ── INIT: First-time repo setup ───────────────────────────────────────────────
init_repo() {
    local USERNAME=$1
    if [ -z "$USERNAME" ]; then
        red "❌ Please provide your GitHub username."
        echo "   Usage: bash scripts/thesis_push.sh init your-github-username"
        exit 1
    fi

    check_git
    check_gh_cli

    yellow "🚀 Initializing thesis GitHub repository..."

    # Init git if not already done
    if [ ! -d ".git" ]; then
        git init
        green "✅ Git initialized"
    else
        yellow "⚠️  Git already initialized — skipping git init"
    fi

    # Create .gitignore if not present
    if [ ! -f ".gitignore" ]; then
        cat > .gitignore << 'GITIGNORE'
CLAUDE.local.md
*.aux
*.log
*.synctex.gz
*.toc
*.bbl
*.blg
.DS_Store
Thumbs.db
__pycache__/
*.pyc
.env
GITIGNORE
        green "✅ .gitignore created"
    fi

    # Create README
    if [ ! -f "README.md" ]; then
        cat > README.md << 'README'
# Greater Kumasi LULC Thesis

**Title**: Assessing the impact of road infrastructure development on Land Use and Land Cover (LULC) change in Greater Kumasi using remote sensing and GIS

**Degree**: MPhil Geographic Information System  
**Institution**: Kwame Nkrumah University of Science and Technology (KNUST)  
**Study Period**: 1995–2024  

## Repository Structure
```
├── CLAUDE.md               # AI memory — project context
├── docs/
│   ├── THESIS_STATUS.md    # Live progress tracker
│   ├── CHAPTER_MAP.md      # Chapter outlines
│   ├── DECISIONS.md        # Key decision log
│   └── SOURCES.md          # References
├── chapters/               # Chapter drafts
└── scripts/                # Automation scripts
```
README
        green "✅ README.md created"
    fi

    # Stage everything
    git add -A
    git commit -m "Initial commit — thesis memory system and project structure" 2>/dev/null || \
        yellow "⚠️  Nothing new to commit on init"

    # Create GitHub repo (private by default)
    if gh repo view "$USERNAME/$REPO_NAME" &> /dev/null; then
        yellow "⚠️  GitHub repo '$REPO_NAME' already exists — skipping creation"
    else
        gh repo create "$REPO_NAME" --private --source=. --remote=origin --push
        green "✅ GitHub repo created: github.com/$USERNAME/$REPO_NAME"
        green "✅ Initial push complete!"
        exit 0
    fi

    # If repo existed, set remote and push
    if ! git remote get-url origin &> /dev/null; then
        git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"
    fi
    git branch -M $BRANCH
    git push -u origin $BRANCH
    green "✅ Pushed to github.com/$USERNAME/$REPO_NAME"
}

# ── PUSH: Regular session push ────────────────────────────────────────────────
push_update() {
    local MSG=$1
    local TODAY=$(date +"%Y-%m-%d")

    if [ -z "$MSG" ]; then
        MSG="Thesis update — $TODAY"
    fi

    check_git

    if [ ! -d ".git" ]; then
        red "❌ No git repo found. Run init first:"
        echo "   bash scripts/thesis_push.sh init your-github-username"
        exit 1
    fi

    yellow "📦 Staging all changes..."
    git add -A

    # Check if there's anything to commit
    if git diff --cached --quiet; then
        yellow "⚠️  No changes to commit — everything is up to date."
        exit 0
    fi

    git commit -m "$MSG"
    green "✅ Committed: $MSG"

    yellow "🚀 Pushing to GitHub..."
    git push origin $BRANCH
    green "✅ Pushed to GitHub successfully!"

    # Show summary of what was pushed
    echo ""
    yellow "📋 Files changed in this push:"
    git show --stat HEAD | tail -n +2
}

# ── Entry point ───────────────────────────────────────────────────────────────
case "$1" in
    init)
        init_repo "$2"
        ;;
    *)
        push_update "$1"
        ;;
esac
