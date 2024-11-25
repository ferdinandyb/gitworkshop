# Repository exploration

material: https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection

```
git clone https://github.com/ferdinandyb/git-snapshot.git
cd git-snapshot
git log --format="%h %an %ae %s" --author="@.\+hu>"
git log --grep="remote:"
git log --grep="^remote:" --oneline
git log --oneline --since=2023-08-12 --until=2023-08-15
git log --oneline # what was merged?
git log --oneline --topo-order # there you are
git config set pretty.lineauthor '%C(auto)%h %C(auto,cyan)%ad %C(auto,magenta)%<(14,trunc)%an%C(auto)%d %C(auto,reset)%s%C(auto,cyan) %C(auto,reset)'
git log --pretty=lineauthor
git config set alias.ll "log --pretty=lineauthor --date=short"
git ll
git ll --topo-order
git ll --graph
git ll --graph master origin/v12 origin/v11
git ll --graph --first-parent master origin/v12 origin/v11
git ll origin/v11..origin/v12
git ll origin/v12..origin/v11
git ll origin/v11...origin/v12
git ll origin/v12...origin/v11
git log origin/v11
git notes show origin/v11
git notes edit origin/v11
git diff origin/v11 origin/v12 # shows a difference, but that actually comes from having branched off from different places on master
git range-diff master..origin/v11 master..origin/v12 # only shows diff between the given ranges
git diff origin/v8 origin/v9 --stat
git range-diff master..origin/v8 master..origin/v9
git ll origin/v12~4..origin/v12
git ll master..origin/v12 -- builtin/remote.c
git diff master origin/v12 -- builtin/remote.c
git show origin/v12:builtin/remote.c

# when was git config _set_ introduced and why?

git blame -- Documentation/git-config.txt
git blame 95ea69c67b6~ -- Documentation/git-config.txt
git show 00bbdde141f
git log -Sset --oneline -- Documentation/git-config.txt
git log --grep="^builtin/config:"
git log --grep="^builtin/config:" --root 00bbdde141f

# If the commits do not have proper information in them, these commands are _much_ less useful! See post on commits.

# workspace
cd /path/to/gitworkshop
git branch
git branch -a
# we want to switch to another branch without leaving this one
git worktree add ../gitwswtree origin/blame
cd ../gitwswtree
git switch -c blame
cat .git # just file, not a folder pointing to the original .git folder
tree ../gitworkshop/.git/worktrees

# bisect: find the commit that introduced a bug
git checkout 9793
python3 main.py test/test.csv # should say 9 which is the output we want
git checkout blame
python3 main.py test/test.csv # should say 5 (oh no, we're not backwards compat!)
# git bisect start <good> <bad>
git bisect start HEAD 9793
# git bisect good/bad -> 5a42e96
git bisect reset
```
