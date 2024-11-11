# Repository exploration

material: https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection

```
git clone https://github.com/ferdinandyb/git-snapshot.git
cd git-snapshot
git log --oneline --format="%h %an %ae %s" --author="@.\+hu>"
git log --grep="remote:"
git log --oneline --since=2023-08-12 --until=2023-08-15
git log --oneline # what was merged?
git log --oneline --topo-order # there you are
git config set pretty lineauthor '%C(auto)%h %C(auto,cyan)%ad %C(auto,magenta)%<(14,trunc)%'
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
git log origin/v12
git notes show origin/v12
git notes edit origin/v12
git diff origin/v11 origin/v12
git range-diff master..origin/v11 master..origin/v12
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
git log -Sset -- Documentation/git-config.txt
git log --grep="^builtin/config:"
git log --grep="^builtin/config:" --root 00bbdde141f

# If the commits do not have proper information in them, these commands are _much_ less useful! See post on commits.

# bisect and workspace
cd /path/to/gitworkshop
git branch
# we want to switch to another branch without leaving this one
git worktree add ../gitwswtree blame
cd ../gitwswtree
git checkout 9793
python3 main.py test/test.csv # should say 9
git checkout blame
python3 main.py test/test.csv # should say 5
# git bisect start <good> <bad>
git bisect start HEAD 9793
# git bisect good/bad
git bisect reset
```
