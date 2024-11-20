# Why?

- parallel development (how many people?)
- controlling deployment (how do you deploy?)
- governance (who can commit where?)
- how do you share your code?


## parallel development

(talk a bit about how linux and git are developed)

- companies will have a central repository -> everybody pushing to master is bad
- feature branches should be as short-lived as possible

## deployment strategies

- each version that needs to be maintained is on it's own branch
- there is a branch for each environment (dev, prod etc)
- releases are cut from master with tags
- what is deployed is actually managed with feature flags

## to merge or not to merge?
