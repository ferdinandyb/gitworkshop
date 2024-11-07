# Some practical tips for gitlab

## Settings

- Merge method -> fast-forward-merge (resolve conflicts yourself!)
- Squash commits when merging -> Do not allow (do this yourself if needed!)

## Tools

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
