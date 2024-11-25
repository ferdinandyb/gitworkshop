Disclaimer: I'm no expert and this is half-baked at best :)

Resources:
- obligatory Drew Devault post: ["What is a fork?"](https://drewdevault.com/2019/05/24/What-is-a-fork.html)
- [some nice figures](https://medium.com/@sreekanth.thummala/choosing-the-right-git-branching-strategy-a-comparative-analysis-f5e635443423)

# Things to consider:

- parallel development (how many people?)
- controlling deployment (how do you deploy?)
- governance (who can commit where?)
- how do you share your code?


## parallel development

(Note to self: talk a bit about how linux and git are developed, i.e.
when companies choose to have a single central repository on a forge
they've already contrained themselves considerably, and sourcehut and
email and stuff)

- companies will have a central repository -> everybody pushing to master is bad
- feature branches should be as short-lived as possible

## deployment strategies

- each version that needs to be maintained is on it's own branch
- there is a branch for each environment (dev, prod etc)
- releases are cut from master with tags
- what is deployed is actually managed with feature flags

## to merge or not to merge?

- to merge master to feature branch is a very definite no-no
- at least try to rebase before merging to master


## so what to do?

- usually git flow vs trunk-based
