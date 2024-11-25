Resource: https://git-rebase.io/

Interactive rebase is extremely powerful.

```
git switch history/editing
git reset --hard origin/merges/conflictfeature
git rebase -i HEAD~8 # most common: git rebase -i origin/HEAD
```

The above means we will be applying the commits on HEAD~8 (so the 8th parent of
HEAD, e.g. the 9th commit). More precisely, git will "execute" each command
from top to bottom. Each line can hold one command. The default command is
`pick` which just applies the commit, but not all lines need to do anything
with a commit.

Most used ones are: pick, edit, fixup, squash, break, drop (first letters also
work).

The `range-diff` commands below are there so you can check if you got
it right. We always reset history/editing at the end once we see we're
good.

```
# droping a commit
git rebase -i HEAD~8 # drop f032c37 csv: return empty list instead of None
git ll
git range-diff HEAD~8..HEAD origin/history/drop1~8..origin/history/drop1
git range-diff HEAD~8..HEAD ORIG_HEAD~8..ORIG_HEAD
git reset --hard ORIG_HEAD # if it succeeded but you don't want it

# conflicts during rebase
git rebase -i HEAD~8 # drop ef5d945 main: print extra info
git ll # last commit is the one we couldn't apply
git status # detailed info
cat main.py
git rebase --edit-todo
git rebase --abort
git rebase -i HEAD~8 # drop ef5d945 main: print extra info
# resolve conflicts in main by still keeping the verbose output
git add main.py
git rebase --continue
git range-diff HEAD~8..HEAD origin/history/mergeconflict~8..origin/history/mergeconflict
git reset --hard ORIG_HEAD

# squash vs fixup

git rebase -i HEAD~8 # squash 987c013 main: hide extra ouput behind -v
# for squash both commit messages are there
git range-diff HEAD~8..HEAD origin/history/squash~8..origin/history/squash
git reset --hard ORIG_HEAD

git rebase -i HEAD~8 # fixup 987c013 main: hide extra ouput behind -v
# for fixup, only the first message is there
git range-diff HEAD~8..HEAD origin/history/fixup~8..origin/history/fixup
git reset --hard ORIG_HEAD

# edit the commit that we blamed previously
git rebase -i HEAD~8 # edit 5a42e96 csv: make separator passable
vim main.py # change separator -> default=";"
git add main.py
git commit --amend
git rebase --continue
git mergetool
git range-diff HEAD~8..HEAD origin/history/edit~8..origin/history/edit
git reset --hard ORIG_HEAD

# autofixup
vim main.py # change separator -> default=";"
git add main.py
git commit --fixup 5a42e96
git ll
git rebase -i HEAD~8 --autosquash # fixup commit was moved
git mergetool # the parent commit is of course from the original position of the fixup
git add main.py
git rebase --continue
git mergetool
git add main.py
git rebase --continue
git range-diff HEAD~8..HEAD origin/history/autofixup~8..origin/history/autofixup
git reset --hard ORIG_HEAD

# new commit with break
git rebase -i HEAD~8 # add new line after line 3 "break"
git ll
touch explain.md
git add explain.md
git commit -m "add explain.md"
git rebase --continue
git range-diff HEAD~8..HEAD origin/history/break~8..origin/history/break
git reset --hard ORIG_HEAD


# random goodies:

git log --check # check for whitespace errors
git rebase HEAD~8 --whitespace=fix # fix whitespace errors
git rebase -r HEAD~8 --exec 'git commit --amend --no-edit --reset-author' # fix bad commit authors

```
