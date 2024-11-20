Resource (and why in detail): https://bence.ferdinandy.com/gitcraft

tldr; insure that blame, log search and stuff are actually useful

```
git switch -c history/editing
git reset --hard origin/blame # another way to set your branch where you want to

# reset
echo "random" >> main.py
git add main.py
git status
git reset --hard  # assumes HEAD
git status

echo "random" >> main.py
git add main.py
git status
git reset  # assumes --mixed flag
git status

git add main.py
git status
git reset HEAD~
git ll
git status
git diff

git reset origin/blame
git status
git ll
git add main.py
git reset --soft # doesn't do anything this way
git status

git diff
git diff --cached
git reset --soft HEAD~ # keeps even the index
git ll
git status
git diff --cached


# amending: change message or add on top

git reset --hard origin/merges/conflictfeature
git commit --amend # change the text
touch explain.md
git add explain.md
git commit --amend # --no-edit

# Note:
# pushing this branch to the remote (if it had one) now requires
# git push --force or git push --force-with-lease


# hunks and removing stuff from the last commit

git reset --hard origin/merges/conflictfeature
git reset HEAD~
git add -p # ? n y
git status
git diff
git diff --cached
git commit --reuse-message=ORIG_HEAD
git show

# another way
git reset --hard origin/merges/conflictfeature
git reset -p HEAD~ # y n (notice the different order)
git status
git diff
git diff --cached
git commit --amend --no-edit
git show

# set one specific file to another version

git restore --source=HEAD~3 main.py
git ll
git status
git diff
```
