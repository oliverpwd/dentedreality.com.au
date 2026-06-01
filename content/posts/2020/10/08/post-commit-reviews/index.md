---
title: Post-Commit Reviews
date: '2020-10-08T23:12:09-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@copyconstruct/post-commit-reviews-b4cc2163ac7a
---

[Post-Commit Reviews](https://medium.com/@copyconstruct/post-commit-reviews-b4cc2163ac7a)  



[![](https://miro.medium.com/fit/c/96/96/2*Mb4iezdIzZIfBSgjulILnQ.jpeg)![](https://miro.medium.com/fit/c/96/96/2*Mb4iezdIzZIfBSgjulILnQ.jpeg)](https://medium.com/@copyconstruct?source=post_page-----b4cc2163ac7a--------------------------------)
[Cindy Sridharan](https://medium.com/@copyconstruct?source=post_page-----b4cc2163ac7a--------------------------------)
[Jul 12](https://medium.com/@copyconstruct/post-commit-reviews-b4cc2163ac7a?source=post_page-----b4cc2163ac7a--------------------------------) · 9 min read



I recently read an [excellent article in the Amazon Builder’s Library](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/) by [Clare Liguori](https://twitter.com/clare_liguori) which goes into great detail about AWS’s CI/CD architecture. It’s a truly brilliant post and I recommend everyone interested in CI/CD infrastructures read the article. The article covers the gamut from unit testing to integration testing (in production) to staged rollouts in “waves” to automated rollbacks. I guarantee there’s *something* valuable you’ll learn from the article even if you’re not building the largest distributed systems in the world like AWS does.

The only surprising thing to me about the article was that it stated code review was *mandatory* before merging a change to the main branch.

> All changes going to production start with a code review and **must be approved by a team member before merging into the mainline branch** (our version of “main” or “trunk”), which automatically starts the pipeline. The pipeline enforces the requirement that all commits on the mainline branch **must be code reviewed and approved by a member of the service team for that pipeline.** **The pipeline will block any unreviewed commits from being deployed.**
> 
> With fully automated pipelines, the code review is the last manual review and approval that a code change receives from an engineer before being deployed to production, so this is a critical step. Code reviewers evaluate the code’s correctness and also evaluate whether the change can be safely deployed to production. They evaluate whether the code has sufficient tests (unit tests, integration tests, and canary tests), whether it is sufficiently instrumented for deployment monitoring, and whether it can be safely rolled back.

![]()


Pre-Commit Code Review Workflows

While mandatory *pre-commit* code review is generally not uncommon at many organizations (as a matter of fact, it’s pretty much the *norm* for many open source projects and organizations), the reason I was surprised was because I’d assumed the *extremely* robust testing environments and infrastructure detailed in the post would’ve afforded *more* latitude when it came to merging code to the main branch.

## Code Reviews and Developer Velocity

There are myriad benefits to code review. As a [2016 paper from Microsoft](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE202013-codereview.pdf) details:

> Our results show that, although the top motivation driving code reviews is still finding defects, the practice and the actual outcomes are less about finding errors than expected: Defect related comments comprise a small proportion and mainly cover small logical low-level issues. At the same time, code review additionally provides **a wide spectrum of benefits to software teams**, such as knowledge transfer, team awareness, and improved solutions to problems. Moreover, we found that context and change understanding is the key of any review.

While there are [studies that estimate](https://static1.smartbear.co/smartbear/media/pdfs/best-kept-secrets-of-peer-code-review_redirected.pdf) effective code review can detect about 90% of bugs, *mandatory* pre-commit code review hinders developer velocity almost invariably.

In the best case scenario, a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) can be merged to mainline in a matter of seconds after it’s submitted. This requires that:

* CI run all tests of a project in a matter of seconds
* turnaround time for code review is in the order of a few seconds

But more commonly, both the CI and the code review phase take minutes to hours to complete, requiring the developer to wait that long to merge their pull request. This is especially true for larger feature branches, though sometimes, even a relatively small patch can get bogged down for days in code review for a number of different reasons (the code owner might be on vacation, the project in question might be a completely volunteer driven open source project, there might be a lot of back and forth between the reviewer and the reviewee on the change and so forth).

On average, I’d argue a code review slows a developer down from a few minutes to a few hours, and in the worst case scenario, a few days or even *months* (when a change results in a long-running pull-request requiring the developer to rebase off of the main branch multiple times to avoid merge conflicts).

An alternative to pre-commit reviews is *post*-commit reviews, which lets a developer merge changes to trunk, and address reviewer comments in follow-up pull requests.

In many ways, post-commit reviews offer the best of both worlds: developer velocity is not sacrificed at the altar of waiting for an approval, and reasonable concerns get addressed in short order by the developer in follow-up commits.

While there are a number of caveats to post-commit reviews (detailed in the following sections of this article), *preponderantly* favoring post-commit reviews can allow developers to rapidly iterate on features they’re developing while also keeping their changes small.

It’s a commonly held misconception that post-*commit* reviews automatically means post-*deploy* reviews — i.e., code being reviewed after it’s deployed. This doesn’t necessarily have to be the case.

![]()


Post-Commit Pre-Deploy Reviews

Post-commit reviews offer a lot more flexibility than people imagine. “Post-commit” review can mean:

* leaving code-review to be the *very last step* of the deployment pipeline, before the code is deployed to production
* or in cases where it’s not necessary for an audit-trail or mandatory sign-off on changes (for prototype projects, internal tools that don’t handle customer sensitive data and so forth), for code review to happen post-deployment.

In both of the aforementioned scenarios, post-commit reviews offers plenty of benefits.

## Focus

By far and away, the biggest benefit of post-commit reviews is developer focus.

Being able to merge pull requests in quick succession ensures that the developer can iterate faster on the feature they are developing. It also encourages the developer to keep pull requests small, ensuring a feature is developed in many small pull requests (or at the very least comprising of many atomic commits).

Another benefit of post-commit reviews is *reviewer focus.* In a culture where pull requests are small and numerous, being pinged every 10 or 15 minutes for a review can hinder the productivity of both the *reviewer* and the *reviewee.*

Moving to a post-commit review format frees the developer from requiring approval for every pull request. It also allows the reviewer to batch reviews, so they are reviewing a number of changes in one fell swoop, as opposed to being constantly interrupted for code reviews. Furthermore, this incentivizes reviewers to only comment on merged pull requests that raise concerns or have logical bugs. In my own experience, this reduces nitpicking on the reviewer’s part, and in the event the reviewer does nitpick, it allows the developer to address the minor concerns at their leisure.

## Encourages Better Development Practices

There’s a case to be made for the fact that post-commit reviews encourage better development practices.

Getting to a point where post-commit reviews are a reality requires a strong cultural scaffolding. At the very least, it requires:

* a culture of collaborating on aspects like API design prior to code implementation via a design document.
* consensus around aspects like style-guide, coding idioms, concurrency primitives etc.
* investment in better automation practices and tooling.

If a design document has been clearly fleshed out and agreed upon before the code is implemented, the implementation will not comprise of any major *surprises* to the reviewer. This in turn minimizes (or even eliminates) the need for reverting commits due to API design or implementation specific disagreements between the reviewer and the reviewee.

For post-commit reviews to be truly effective, it’s also important to minimize code review comments pertaining to code style or idioms. This eliminates the need for the reviewer to comment on the automatable aspects, as it were, of code review.

One can argue that all these are the hallmarks of a good development culture anyway (and for many projects, these are already implemented as a part of the pre-commit CI workflow). That post-commit review makes them *inevitable* only acts as a forcing function to foster better development practices.

Often, code is only merged to trunk once all unit-tests have passed. This is no different for post-commit reviews than it’s for pre-commit reviews.

The reason why “post-commit” tests are required is because unit-tests (while incredibly effective at preventing many forms of [critical failure](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf)s), lint tests and the like aren’t sufficient to detect certain categories of bugs that only surface in real environments when testing against real dependencies.

By “post-commit” testing, I’m referring to all the tests a code change is subjected to post-commit but pre-deploy: integration tests, load tests, soak tests, shadow tests, exception tracking and so forth.

There’s no reason why most of the “post-commit” testing needs to happen *after* code-review. There’s a stronger likelihood that sufficiently sophisticated “post-commit” testing can detect *more* bugs and alert the developer of the bug (or even better, automatically revert the commit in source control), allowing the developer who wrote the code to understand the nature of the bug and fix it, before a reviewer has even looked at the code.

This means that the reviewer can have a fair degree of confidence that the change is functionally correct and has undergone extensive testing before they review it. The reviewer can then truly only focus on trying to find the categories of bugs that even the most advanced forms of “post-commit” testing doesn’t flag: security bugs, a bug in the implementation of business logic not caught by any of the tests and so forth.

There might even be scenarios where it’s not necessary for a code reviewer to sign-off on a change before it’s deployed to production. This is true for most prototype projects, projects without compliance requirements, projects that don’t handle customer data or sensitive data and so forth. In such cases, a “post-commit” code review can actually even be a “post-deploy” code review, where code is only reviewed once it’s been deployed to production. A concrete example of a company that practices *post-commit, post-deploy* reviews is Quora. [This blog post](https://www.quora.com/q/quoraengineering/Moving-Fast-With-High-Code-Quality) details a lot more about Quora’s post-commit review approach.

Post-commit reviews can provide many benefits but also pose some challenges.

## High-Functioning, High-Trust Environments

Needless to say, post-commit reviews work best in teams where there’s a high degree of trust among the team members. Building trust and learning how to work well as a team takes time. It also poses unique challenges on how to onboard new team members or junior engineers, who might not be familiar enough with the problem domain, programming language, frameworks, tools, testing guidelines, or even the company’s CI/CD infrastructure to be able to adapt to a post-commit review culture right away.

In such cases, it might help to begin onboarding a new team-member by starting with “pre-commit” reviews and work towards the goal of bringing the team member up-to-speed enough to gradually switch to doing post-commit reviews. Open-source projects can work in a “mixed-mode”, where maintainers of the project can rely on post-commit reviews while new contributors can be onboarded by offering them pre-commit reviews. Part of attaining maintainership of a project can involve progressing from requiring pre-commit reviews to requiring post-commit reviews.

## Investment in Automation

The next requirement for fostering a successful “post-commit” review culture is a heavy investment in automation and monitoring infrastructure. Requiring developers to *manually* revert changes and work around merge conflicts if a commit proves to be problematic can undo almost all the gains in developer productivity a post-commit review culture brings in the first place. Reverting commits needs to be automated, which requires close integration between the testing infrastructure and the source control management (SCM) tool.

This is arguably even harder to achieve in organizations that have embraced the monorepo, since reverting a single offending commit could involve having to revert tens or hundreds of commits across the codebase. Most organizations that have adopted a monorepo have extensive automation and tooling to this end. An example is how [Uber keeps the main branch green at scale at all times](https://www.dropbox.com/s/w88eccvm2gthyfk/eurosys19uber.pdf?dl=0) using a system called SubmitQueue. SubmitQueue, in a nutshell, is a meta-build system, a load balancer and a speculative executor rolled into one, with a dose of data science thrown in for good measure, which guarantees “an always green master branch at scale” via serializability of commits to the main branch when there could be hundreds of concurrent commits.

In my own experience, managing commits becomes a lot easier in non-monorepo environments, since the automation required to revert commits doesn’t require research paper levels of complexity.

# Conclusion

Walking the tightrope between developer productivity and high quality code is always going to be a challenging undertaking, requiring smart choices and tradeoffs. Iteration speed of developers can be improved by either flavor of post-commit reviews, viz.,

* *post-commit, pre-deploy* reviews
* *post-commit, post-deploy* reviews

As with all good things, it requires time and investment to get right, but for teams or organizations trying to improve the developer productivity, it’s certainly an avenue worth exploring.