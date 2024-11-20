Resources:
- https://git-rebase.io/
- https://git-scm.com/book/en/v2/Git-Tools-Rerere

- types of merges
- merge conflict resolving
- rerere

The branches `merges/mcno_master` and the like will be representing the default
(`master|main|trunk`) branch and will be trying different merge strategies both
when there's no conflict and when there is conflict.

```
TODO: no conflict branch and conflict branch
# explain diff markers
# do a rerere example


# no conflicts

## creating a merge commit

git switch -c merges/myfeature origin/fixedseparator
git switch -c merges/mcno_master origin/merges/noconflictbase
git ll --graph merges/mcno_master merges/myfeature
git merge fixedseparator
git log --oneline --graph merges/mcno_master merges/myfeature
git cat-file -p HEAD # 2 parents, can be more

## fast-forwarding without a merge commit

git switch -c merges/myfeature2 origin/fixedseparator
git switch -c merges/mcno_master2 origin/merges/noconflictbase
git ll --graph merges/myfeature2 merges/mcno_master2
git merge merges/myfeature2 --ff-only # can't do it, need to rebase first
git switch merges/myfeature2
git ll --graph merges/myfeature2 merges/mcno_master2
git rebase merges/mcno_master2
git ll --graph merges/myfeature2 merges/mcno_master2
git reset --hard ORIG_HEAD # this is how we can go back if something went wrong
git ll --graph merges/myfeature2 merges/mcno_master2
git rebase merges/mcno_master2
git switch merges/mcno_master2
git merge merges/myfeature2 --ff-only
git ll --graph merges/myfeature2 merges/mcno_master2

# conflicts

# make sure everything is set to defaults
git config set rerere.enabled false
git config set merge.conflictstyle merge


git switch -c merges/conffeature origin/merges/conflictfeature
git switch -c merges/mc_master origin/merges/conflictbase
git ll --graph merges/conffeature merges/mc_master
git show merges/mc_master
git show merges/conffeature

# let's learn about conflict markers

git merge merges/conffeature
git status # read carefully!
cat main.py # simple conflict markers, top is HEAD, bottom is what we're merging
git ll
git merge --abort
git merge merges/conffeature # let's solve it!
git commit

# better markers imho
git config set merge.conflictstyle zdiff3
git switch -c merges/mc_master2 origin/merges/conflictbase
git merge merges/conffeature
cat main.py # simple conflict markers, top is HEAD, bottom is what we're merging
git mergetool

# rebase -> the logic is different
git switch -c merges/mc_master3 origin/merges/conflictbase
git switch -c merges/conffeature2 origin/merges/conflictfeature
git rebase -i merges/mc_master3
git status
git ll
cat main.py # notice the parent commmit could be different
git rebase --abort

# setting this remembers merge conflict resolutions
git config set rerere.enabled true
```
