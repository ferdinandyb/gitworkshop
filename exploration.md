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
```
