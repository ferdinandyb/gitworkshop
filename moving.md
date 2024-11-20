Resources: https://git-send-email.io/

Various ways to move/send a specific commit to somebody/another branch.


```
# diff and patch
git switch patch
cat fix.diff # create with: git diff > fix.diff
cat 0001-fix-default-separator.patch # create with: git format-patch HEAD~
    # also possible to directly send: git send-email HEAD~

# using the diff
git switch blame
git switch -c fixblame/diff
git show patch:fix.diff | git apply -3
# the -3 is technically not needed here but could be in other cases
diff <(git show patch:fixup.diff) <(git diff)
git add -u
git commit -m "fix default sep from diff"
git diff fixblame/solution

# using the patch as a diff
git switch -c fixblame/patch blame
git show patch:0001-fix-default-separator.patch | git apply -3
git status

# getting various states from other sources
git restore main.py
git restore --source HEAD~3 main.py
git restore main.py

# apply the patch properly
git show patch:0001-fix-default-separator.patch | git am -3
# the -3 threeway is again technically not needed here
git show
git diff fixblame/solution

# cherry-picking
git switch -c fixblame/cherry-pick blame
git log --oneline fixedseparator
git cherry-pick 56cfc63

```
