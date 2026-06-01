---
title: No Code Reviews by Default
date: '2021-06-25T23:03:47-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://raycast.com/blog/no-code-reviews-by-default/
---

[No Code Reviews by Default](https://raycast.com/blog/no-code-reviews-by-default/)  



At Raycast, we do not require code reviews. Engineers push to the main branch and request reviews when they think it’s necessary. In this blog post, I outline how we built an engineering culture that is based on trust and allows us to move incredibly fast.

## The beginning

When Petr and I started Raycast, we were sitting next to each other in the same flat for three months. Every day, we built features to iterate as fast as possible to something users want. At this time, we didn’t do any code reviews and trusted each other blindly. If there was a technical question, we solved it in person, committed the code to the main branch and moved on to the next problem.

When we started to grow our distributed team, we asked ourselves if we should adopt code reviews. Common wisdom tells you that pull requests are best practice in high-performing engineering teams. But we liked the trust, collaboration and speed of our “process” and decided to ***not*** require code reviews. Instead, every engineer has the right to push their changes to the main branch. They can request a review if they want somebody else to take another look at their code. Sometimes this happens after the change has landed in the trunk.

## Responsibility over convention

We use GitHub for source control, which comes with the concept of pull requests (PR) for code reviews. Typically, an engineer works on a task and then proposes their changes to the repository. After a discussion and potential changes, the engineer merges their changes into the base branch. This model works great for open source and allows strangers to contribute to projects. However, we found it impractical for our team for a few reasons:

* **Pull requests discourage trust.** Proposing every code change that somebody else has to approve doesn’t feel encouraging for teams that should operate with a high degree of trust. There are more efficient ways to collaborate on code.
* **Pull requests don’t prevent bugs.** Reviewing code is hard! You can catch obvious mistakes, but you won’t have consistent in-depth scrutiny. Many issues reveal themselves only after extensive use, which doesn’t happen during code reviews. We rely on fast iterations with [user feedback](https://raycast.com/blog/feedback/).
* **Pull requests slow down.** Code reviews aren’t high priority for engineers. They have to make time to clean up their review queue. In reality, PRs are an afterthought and not what you want to spend your time on as an engineer.

We value [full responsibility](https://raycast.com/jobs#what-we-offer) and all our engineers own features from ideation to maintenance. Our engineering culture reflects this by giving engineers the freedom to push to the main branch and only request code reviews if they think it’s necessary.

## How does this work in practice?

Our goal is to dogfood changes as quickly as possible. For this, everybody works on the main branch. This produces a constant stream of changes that can be immediately tested by others. Our continuous integration builds and tests every commit. In addition, we trigger an internal release every night which includes all changes that got committed during the day. Each release is automatically installed for the entire team. This allows us to test new changes within 24 hours.

The daily internal releases make it simple to collect a lot of feedback to iron out bugs or usability issues. If the team is happy with the quality of a feature, it gets released as part of our next public release. If it needs further iterations, we use a feature flag to keep it internal. This workflow helps us to consistently ship [updates every other week](https://raycast.com/changelog).

**Side note:** We use rebase instead of merge to keep a much cleaner project history and eliminate unnecessary merge commits.

There are some situations when we request code reviews. If we touch a new part of the codebase, we open a pull request. A good example for such a change is adding a database migration for the first time. Nobody wants to screw up the production environment and rather double checks it. Often new team members request code reviews for the first couple of weeks to familiarize themselves with our codebase. Over time, they gain confidence to work on bigger changes and start pushing to the main branch directly.

It doesn’t always have to be a PR. Sometimes it’s enough to make a teammate aware of a particular change with a “post-commit message”. After somebody committed their change, they link the relevant person in a Slack channel that is subscribed to our repository or on the commit on GitHub itself. This is useful for changes that could affect the work of others. This is also a great way to avoid blocking code reviews due to time differences. If there is some problem that needs the input of multiple engineers, we hop on a quick [Around](https://www.around.co/?ref=raycast) video call and use screen sharing to collaborate. This is handy to sort out bigger topics such as refactoring parts of the codebase or aligning on features that depend on each other.

We found this way of working more effective. It avoids isolated work on long-lived branches and creates momentum through the continuous updating of the app.

## Make your own rules

Every company or team is different, but one thing is the same: They all want to build the best product in the shortest time possible. There are different ways to achieve this. Ours is to bet on our team and give all engineers the trust to do their best job. This includes letting them decide whenever they want their code reviewed by somebody else. This might be not the right process for other teams that have more strict security requirements. So far, this works well for us. It allows us to rapidly iterate on features, attract great engineers who want to tackle big problems, and establish an asynchronous communication culture that fits our fully distributed team.

It’s up to you and your colleagues to set the rules for your team. Don’t adopt best practices in a dogmatic fashion. Rather, ask yourself if the circumstances of others apply to you. There is a high chance that they won’t, and you find a more suited way to do things.