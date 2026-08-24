# Claude Code Cheat Sheet

Commands and habits I've actually used, Days 1-4.

## Starting and stopping
- `claude` — start a session in the current folder (it can see your files)
- `/exit` — leave Claude Code, back to the plain shell prompt

## Plan mode (review before it edits anything)
- `/plan <request>` — Claude proposes an approach first, doesn't touch files until approved
- Shift+Tab — cycle permission modes during a session

## Useful requests I've made
- "explain what [file] does" — plain-English walkthrough of existing code
- "refactor [file] for readability" — suggests changes as a diff; review before accepting
- "/plan create a [file] appropriate for this project" — propose-first version of the above

## Habits worth keeping (learned the hard way)
- Never trust a Claude Code summary of what it did — verify independently: `cat`, `git status`, `git log`
- Review a diff/plan before approving — don't keep code you can't personally explain
- Claude Code can edit files correctly without committing anything — check `git log` to confirm nothing was committed without you
