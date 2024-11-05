# Theory and internals

material: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

- DAG
- branches are just labels
- walk through what changes internally for basic operations
- blob, tree, commit, tag

TODO: actual list of commands to go through Two side-by-side terminals might
make this easier for e.g. `tree`.

Note: commit hashes will be different for you!

```
mkdir myrepo && cd myrepo
git init
tree .git # sudo apt install tree; OR: find .git -type f
echo "line1" >> README.md
git add README.md
tree .git
git config set alias.deflate \!"perl -MCompress::Zlib -e 'undef $/; print uncompress(<>)'"
git deflate .git/objects/a2/9bdeb434d874c9b1d8969c40c42161b03fafdc
git deflate .git/objects/a2/9bdeb434d874c9b1d8969c40c42161b03fafdc | sha1sum
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc
git cat-file -p a29bdeb434d874c9b1d8969c40c42161b03fafdc | git hash-object -t blob --stdin
```
