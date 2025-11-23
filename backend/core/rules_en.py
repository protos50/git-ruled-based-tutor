# English rules for the Git Assistant (Professional Level)
# Structure mirrors rules.py

GIT_RULES = {
    "main": [
        ("status",
         "📊 Repository Status (git status)\n\n"
         "`git status` is essential to understand what's going on.\n"
         "What variant do you want to see?\n\n"
         "1. `git status` (Standard - Detailed)\n"
         "2. `git status -s` (Short - Compact)\n"
         "3. `git status -sb` (Short + Branch info)\n"
         "4. Back to main menu",
         "status_menu"),

        ("log",
         "🕰️ Change History (git log)\n\n"
         "Visualize your project's history.\n"
         "Recommended options:\n\n"
         "1. `git log` (Standard)\n"
         "2. `git log --oneline` (One line per commit)\n"
         "3. `git log --graph --oneline --all` (Visual graph)\n"
         "4. `git log -p` (Show diffs per commit)\n"
         "5. Back to main menu",
         "log_menu"),

        ("commit",
         "💾 Saving Changes (git commit)\n\n"
         "Create a point in the project's history.\n"
         "Useful variants:\n\n"
         "1. `git commit -m 'message'` (Standard)\n"
         "2. `git commit -am 'message'` (Add + Commit tracked files)\n"
         "3. `git commit --amend` (Fix last commit)\n"
         "4. Back to main menu",
         "commit_menu"),

        ("diff",
         "🔍 Inspecting Changes (git diff)\n\n"
         "Compare versions of your code.\n"
         "What do you want to compare?\n\n"
         "1. `git diff` (Working Dir vs Staging Area)\n"
         "2. `git diff --staged` (Staging vs Last Commit)\n"
         "3. `git diff HEAD` (Working Dir vs Last Commit)\n"
         "4. Back to main menu",
         "diff_menu"),

        ("conflict",
         "🔧 Conflict Management\n\n"
         "Conflicts happen when Git cannot merge automatically.\n"
         "What kind of conflict do you have?\n\n"
         "1. Content conflict (both modified same lines)\n"
         "2. File deleted by one, modified by another\n"
         "3. Back to main menu",
         "conflict_menu"),
        
        ("push",
         "🚀 Push Changes (git push)\n\n"
         "Send your commits to the remote.\n"
         "Pick your issue or variant:\n\n"
         "1. Push Rejected (non-fast-forward)\n"
         "2. `git push -u origin <branch>` (Set upstream)\n"
         "3. `git push --force` (⚠️ Dangerous: Overwrite history)\n"
         "4. Back to main menu",
         "push_menu"),
        
        ("branch",
         "🌿 Branch Management (git branch)\n\n"
         "Branches allow parallel work.\n"
         "What do you want to do?\n\n"
         "1. Create a new branch\n"
         "2. Switch branches (checkout/switch)\n"
         "3. List branches\n"
         "4. Delete a branch\n"
         "5. Back to main menu",
         "branch_menu"),
        
        ("help",
         "🎓 Git Learning Assistant - Main Menu\n\n"
         "I'm here to help. Available topics:\n\n"
         "- Status: `status`\n"
         "- History: `log`\n"
         "- Changes: `diff`\n"
         "- Save: `commit`\n"
         "- Branches: `branch`\n"
         "- Conflicts: `conflict`\n"
         "- Remote: `push`\n\n"
         "Type the command or topic you want.",
         "main"),
        
        ("menu",
         "🔙 Main Menu\n\n"
         "Which topic do you want to review today? (status, log, commit, diff, branch...)",
         "main")
    ],

    "status_menu": [
        ("1",
         "📊 `git status`\n\n"
         "Shows working directory status.\n"
         "- Modified but unstaged files (red)\n"
         "- Files staged for commit (green)\n"
         "- Untracked files\n\n"
         "Run this often.",
         "main"),
        ("2",
         "📊 `git status -s` (Short)\n\n"
         "Compact output, great for scripts or quick glance.\n"
         "- `M ` (green): Modified in staging\n"
         "- ` M` (red): Modified in working dir\n"
         "- `??`: Untracked",
         "main"),
        ("3",
         "📊 `git status -sb` (Short + Branch)\n\n"
         "Combines short view with current branch info.\n"
         "Shows ahead/behind vs remote.\n\n"
         "Example:\n"
         "`## main...origin/main [ahead 1]`",
         "main"),
        ("4", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ],

    "log_menu": [
        ("1",
         "🕰️ `git log`\n\n"
         "Full commit history (hash, author, date, message).\n"
         "Use arrows to navigate and `q` to quit pager.",
         "main"),
        ("2",
         "📜 `git log --oneline`\n\n"
         "One line per commit (short hash + title).",
         "main"),
        ("3",
         "📜 `git log --graph --oneline --all`\n\n"
         "Great for visualizing branching and merges.",
         "main"),
        ("4",
         "📜 `git log -p` (Patch)\n\n"
         "Shows not only commit messages, but also diffs per commit.",
         "main"),
        ("5", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ],

    "commit_menu": [
        ("1",
         "💾 `git commit -m 'message'`\n\n"
         "Creates a commit with files currently in staging.\n"
         "Use descriptive, imperative messages.",
         "main"),
        ("2",
         "💾 `git commit -am 'message'`\n\n"
         "Shortcut combining `git add` (tracked files) + commit.\n"
         "Does not include new (untracked) files.",
         "main"),
        ("3",
         "💾 `git commit --amend`\n\n"
         "Modify the last commit.\n"
         "- Forgot a file? `git add` then `git commit --amend`\n"
         "- Want to change the message? Run and edit.\n"
         "Do not use if you've already pushed it.",
         "main"),
        ("4", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ],

    "diff_menu": [
        ("1",
         "🔍 `git diff`\n\n"
         "Shows changes in your working directory that are NOT staged.",
         "main"),
        ("2",
         "🔍 `git diff --staged` (or --cached)\n\n"
         "Shows changes that ARE staged and will go into the next commit.",
         "main"),
        ("3",
         "🔍 `git diff HEAD`\n\n"
         "Shows all changes (staged + unstaged) compared to the last commit.",
         "main"),
        ("4", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ],

    "conflict_menu": [
        ("1",
         "📝 Content Conflict\n\n"
         "1. Run `git status` to see conflicted files.\n"
         "2. Open files and find `<<<<<<<`, `=======`, `>>>>>>>`.\n"
         "3. Edit to keep the correct final version.\n"
         "4. Remove conflict markers.\n"
         "5. `git add <file>` to mark as resolved.\n"
         "6. `git commit` to finish the merge.",
         "main"),
        ("2",
         "🗑️ Modified/Deleted Conflict\n\n"
         "One user modified a file that another deleted.\n"
         "- To keep the modified file: `git add <file>`\n"
         "- To confirm deletion: `git rm <file>`\n"
         "Then commit.",
         "main"),
        ("3", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ],

    "push_menu": [
        ("1",
         "🚫 Push Rejected (Non-fast-forward)\n\n"
         "Someone else pushed to the same branch.\n"
         "Standard fix:\n"
         "1. `git pull --rebase origin <branch>`\n"
         "2. Resolve conflicts, `git rebase --continue`\n"
         "3. `git push origin <branch>`",
         "main"),
        ("2",
         "📤 `git push -u origin <branch>`\n\n"
         "The `-u` option links your local branch with the remote.\n"
         "Then you can just `git push` or `git pull`.",
         "main"),
        ("3",
         "⚠️ `git push --force`\n\n"
         "Forces pushing, overwriting remote history.\n"
         "Use only if you're the only one on that branch and know why history diverged.",
         "main"),
        ("4", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ],

    "branch_menu": [
        ("1",
         "✨ Create Branch\n\n"
         "- `git branch <name>`: Creates the branch but does not switch to it.\n"
         "- `git checkout -b <name>`: Creates and switches (recommended).",
         "main"),
        ("2",
         "🔀 Switch Branch\n\n"
         "- `git checkout <name>` (Classic)\n"
         "- `git switch <name>` (Modern, since Git 2.23)",
         "main"),
        ("3",
         "📜 List Branches\n\n"
         "- `git branch`: Local branches\n"
         "- `git branch -a`: Local + remote\n"
         "- `git branch -v`: Shows last commit per branch",
         "main"),
        ("4",
         "🔥 Delete Branch\n\n"
         "- `git branch -d <name>`: Deletes if already merged (safe).\n"
         "- `git branch -D <name>`: Force delete (danger: can lose changes)",
         "main"),
        ("5", "🔙 Back...", "main"),
        ("menu", "🔙 Back...", "main")
    ]
}

DEFAULT_RESPONSE = (
    "❓ Command not recognized\n\n"
    "Try main menu keywords:\n"
    "- `status`, `log`, `diff`, `commit`\n"
    "- `branch`, `push`, `conflict`\n\n"
    "Or type `help` to see options."
)
