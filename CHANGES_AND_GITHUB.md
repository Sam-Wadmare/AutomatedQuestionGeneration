# Where to See Changes and GitHub Sync Behavior

## Are changes made directly to GitHub?
No. In this environment, changes are made locally in the repository working tree first.

Typical flow:
1. Files are edited locally.
2. Changes are committed to the current local git branch.
3. A PR message is prepared (title/body metadata).
4. Actual GitHub visibility requires pushing branch/PR through your remote workflow.

## How to inspect changes locally

### Show latest commits
```bash
git log --oneline -n 10
```

### Show what changed in latest commit
```bash
git show --name-only --oneline HEAD
```

### Show full patch in latest commit
```bash
git show HEAD
```

### Compare current branch against another branch (example: main)
```bash
git diff main...HEAD
```

## How to publish to GitHub
After verifying locally:

```bash
git push origin <your-branch>
```

Then open/create a PR on GitHub (or update existing PR for the same branch).

## Update directly to `main` (if you want that flow)

If your branch already has the commits you want, you can update `main` yourself with:

```bash
git checkout main
git pull origin main
git merge --ff-only <your-branch>  # use plain merge if fast-forward is not possible
git push origin main
```

If `--ff-only` fails, either:
- run `git merge <your-branch>` and resolve conflicts, then push, or
- open a PR from `<your-branch>` to `main` and merge on GitHub UI.

## Notes about my access
I can prepare commits and PR metadata in this environment, but publishing to your GitHub `main` branch requires your repository credentials/permissions.
