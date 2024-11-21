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

The `range-diff` commands below are there so you can check if you got it right.

```
# droping a commit
git rebase -i HEAD~8 # drop f032c37 csv: return empty list instead of None
git ll
git range-diff HEAD~8..HEAD origin/history/drop1~8..origin/history/drop1
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


```
