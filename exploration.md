# Repository exploration

material: https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection


, specifying specific files, exploring a repository (e.g. git diff, git log)

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
```