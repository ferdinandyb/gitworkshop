# Theory and internals

material: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

- DAG
- branches are just labels
- walk through what changes internally for basic operations
- blob, tree, commit, tag
- ref vs symref

TODO: actual list of commands to go through Two side-by-side terminals might
make this easier for e.g. `tree`.

Note: _commit_ hashes will be different for you!

```
mkdir myrepo && cd myrepo
git init
tree .git # sudo apt install tree; OR: find .git -type f
rm .git/hooks/* # so we have less output later
echo "line1" >> README.md
git add README.md # adds to index and object storage
tree .git
git config set alias.deflate \!"perl -MCompress::Zlib -e 'undef $/; print uncompress(<>)'"
cat .git/config
git deflate .git/objects/a2/9bdeb434d874c9b1d8969c40c42161b03fafdc
git deflate .git/objects/a2/9bdeb434d874c9b1d8969c40c42161b03fafdc | sha1sum
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc | git hash-object -t blob --stdin
echo "line2" >> README.md # does not change object already stored
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc
git add README.md
tree .git
git cat-file -p c0d0fb45c382919737f8d0c20aaf57cf89b74af8 # not a diff, fully there
git commit -m "title" -m "body" # records a commit based on the index
tree .git
git log
cat .git/COMMIT_EDITMSG
cat .git/HEAD
cat .git/refs/heads/master
git deflate .git/objects/23/85d8b6cab6137807b6b501a26e99e1d43a51fb
git deflate .git/objects/23/85d8b6cab6137807b6b501a26e99e1d43a51fb | sha1sum
git cat-file -p 2385d8b
git cat-file -p 2385d8b | git hash-object -t commit --stdin
git cat-file -p 2385d8b
git cat-file -p ed236ae04ac58304fc5c1a5eb5f53120f1fc83a4
mkdir subdir
echo "something" > subdir/somefile.md
git add subdir/somefile.md
git commit -m "title2" -m "body2"
git log --oneline
git cat-file -p e27a16
git cat-file -p e27a16 | git hash-object -t commit --stdin
git cat-file -p d15e6e38ec3d015c5e5d28a8bb8bfeaecaa7362b # tree
git cat-file -p 8f26ca961bd88864bbd4f31484c34819672fc9f2 # tree
git cat-file -p e27a16 # parent, tree, message, author, committer, time
# cryptography!
tree .git
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc # still there
git prune # don't worry about this see `git gc`
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc # not there anymore
tree .git # why 7 objects?
git switch -c otherbranch
git log --oneline
tree .git
cat .git/refs/heads/otherbranch
cat .git/HEAD
git switch -c feat/something
tree .git
cat .git/refs/heads/feat/something
cat .git/HEAD
git log --oneline
echo "line3" >> README.md
git add README.md
git commit -m "title3" -m "body3"
git log --oneline
cat .git/HEAD
cat .git/refs/heads/feat/something
cat .git/refs/heads/master
git remote add origin git@gitlab.com:bferdinandy/myrepo.git
cat .git/config
git push --all
tree .git
git cat-file -p master
git cat-file -p refs/heads/master
git show refs/heads/feat/something
git show HEAD
git show origin/feat/something
git show refs/remotes/origin/master
git remote set-head -a origin
git show origin/HEAD # same objects, if remote had other things they are downloaded
git switch master
cd ..
git init --bare upstream.git # the .git is just customery
tree upstream.git
cd myrepo
git remote add upstream ../upstream.git
git push upstream --all
tree ../upstream.git
tree .git/refs/remotes
echo "line4" >> README.md
git add README.md
git commit -m "title4"
git log --oneline --graph --all
git commit --amend
cat .git/logs/HEAD
git reflog
git reflog HEAD
git reflog feat/something
git show feat/something@{2}
git show @
git show @{upstream}
```
