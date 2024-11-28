# Tools

## gitlab settings

- Merge method -> fast-forward-merge (resolve conflicts yourself!)
- Squash commits when merging -> Do not allow (do this yourself if needed!)

## Tools for gitlab

gitlab-cli: https://docs.gitlab.com/ee/editor_extensions/gitlab_cli/

Much faster to make an MR or view pipeline (instead of going through tons of
menus) as it automatically infers what you want to do (view last pipeline for
current branch, make merge request from current branch to origin/HEAD).

```
glab mr create # option for listing all commits instead of last!
glab ci run --variables CI_PIPELINE_SOURCE:web --variables ENV:dev
glab ci view
```

gcli: https://herrhotzenplotz.de/gcli/

Similar, works with gitlab, github and gerrit, so no need to learn more tools.

Has experimental review feature :)
```
 GCLI_ENABLE_EXPERIMENTAL=yes gcli pulls -i 85 review
```

Commit/diff/patch:
https://gitlab.com/gitlab-org/cli/-/commit/6854709bad9c327d35063d41153f48d740c46258.patch
https://gitlab.com/gitlab-org/cli/-/commit/6854709bad9c327d35063d41153f48d740c46258.diff
https://gitlab.com/gitlab-org/cli/-/commit/6854709bad9c327d35063d41153f48d740c46258

## github

Link to commit: https://github.com/ferdinandyb/git-snapshot/commit/3cbc6da26052aa7d8a41e1570ca69743250fdc9c
Link to commit as diff: https://github.com/ferdinandyb/git-snapshot/commit/3cbc6da26052aa7d8a41e1570ca69743250fdc9c.diff
Link to commit as patch: https://github.com/ferdinandyb/git-snapshot/commit/3cbc6da26052aa7d8a41e1570ca69743250fdc9c.patch



## General

- [lazygit](https://github.com/jesseduffield/lazygit)
- your editor likely has cool stuff
