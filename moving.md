
```
# using fixup

git switch patch
cat fix.diff # git diff > fix.diff
cat 0001-fix-default-separator.patch # git format-patch HEAD~
# git send-email HEAD~ git-send-email.io
git switch blame
git switch -c fixblame/diff
git show patch:fix.diff | git apply -3
# the -3 is technically not needed here but could be in other cases
diff <(git show patch:fixup.diff) <(git diff)
git add -u
git commit -m "fix default sep from diff"
git diff fixblame/solution
git switch -c fixblame/patch blame
git show patch:0001-fix-default-separator.patch | git apply -3
git status
git restore main.py
git restore --source HEAD~3 main.py
git restore main.py
git show patch:0001-fix-default-separator.patch | git am -3
# the -3 threeway is again technically not needed here
git show
git diff fixblame/solution
git switch -c fixblame/cherry-pick blame
git log --oneline fixedseparator
git cherry-pick 56cfc63

```