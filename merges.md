- types of merges
- merge conflict resolving
- rerere
```
git config set merge.conflictstyle = zdiff3
TODO: no conflict branch and conflict branch
# explain diff markers
# do a rerere example

git config set rerere.enabled false

# no conflicts

git switch -c merges/myfeature fixedseparator
git switch -c merges/mcno_master merges/noconflictbase
git log --oneline --graph merges/mcno_master merges/myfeature
git merge fixedseparator
git log --oneline --graph merges/mcno_master merges/myfeature
git cat-file -p HEAD # 2 parents, can be more

git switch -c merges/myfeature2 fixedseparator
git switch -c merges/mcno_master2 merges/noconflictbase
git log --oneline --graph merges/myfeature2 merges/mcno_master2
git merge merges/myfeature2 --ff-only # can't do it
git switch merges/myfeature2
git rebase merges/mcno_master2
git log --oneline --graph merges/myfeature2 merges/mcno_master2
git switch merges/mcno_master2
git merge merges/myfeature2 --ff-only
git log --oneline --graph merges/myfeature2 merges/mcno_master2

# conflicts
```
