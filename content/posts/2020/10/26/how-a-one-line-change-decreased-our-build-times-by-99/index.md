---
title: How a one line change decreased our build times by 99%
date: '2020-10-26T08:06:44-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/pinterest-engineering/how-a-one-line-change-decreased-our-build-times-by-99-b98453265370
---

[How a one line change decreased our build times by 99%](https://medium.com/pinterest-engineering/how-a-one-line-change-decreased-our-build-times-by-99-b98453265370)  



[![](https://miro.medium.com/fit/c/96/96/1*FNWs-r9nA_QNtBbYvUkAtg.png)![](https://miro.medium.com/fit/c/96/96/1*FNWs-r9nA_QNtBbYvUkAtg.png)](https://medium.com/@Pinterest_Engineering?source=post_page-----b98453265370--------------------------------)
[Pinterest Engineering](https://medium.com/@Pinterest_Engineering?source=post_page-----b98453265370--------------------------------)
[Oct 23](https://medium.com/pinterest-engineering/how-a-one-line-change-decreased-our-build-times-by-99-b98453265370?source=post_page-----b98453265370--------------------------------) · 3 min read



Urvashi Reddy | Software Engineer, Engineering Productivity Team  
Adam Berry | Tech Lead, Engineering Productivity Team  
Rui Li | Software Engineer, Engineering Productivity Team

*The Engineering Productivity team at Pinterest came across a small change that had a large impact in reducing build times across pipelines. We found that setting the refspec option during git fetch reduced our build times by 99%.*

The Engineering Productivity team at Pinterest is responsible for supporting the engineers who build and deploy software at the company. Our team maintains a number of infrastructure services and often works on large scale efforts — migrating all software at Pinterest [to Bazel](https://medium.com/pinterest-engineering/developing-fast-reliable-ios-builds-at-pinterest-part-one-cb1810407b92), creating a Continuous Delivery platform called [Hermez](https://www.youtube.com/watch?v=KkKSoQBp2oQ), and maintaining [the](https://medium.com/pinterest-engineering/building-a-python-monorepo-for-fast-reliable-development-be763781f67) monorepos that get committed to a few hundred times a day, to name a few.

All our larger efforts are designed to progress on the goal of making software development and delivery at Pinterest a fast and painless experience. Recently, we were reminded of how small details can also have a large impact on that goal. We discovered an overlooked Git option that significantly reduced the build times in our continuous integration pipelines. In order to understand how this small change had such a large impact, we need to share a little information on our monorepos and our pipelines.

# **Monorepos and Pipelines**

We have six main repositories at Pinterest: Pinboard, Optimus, Cosmos, Magnus, iOS, and Android. Each one is a monorepo and houses a large collection of language-specific services. Pinboard is as old as the company and is the largest monorepo. Pinboard has more than 350K commits and is 20GB in size when cloned fully.

Cloning monorepos that have a lot of code and history is time consuming, and we need to do it frequently throughout the day in our continuous integration pipelines. For Pinboard alone, we do more than 60K git pulls on business days. Most of our Jenkins pipeline configuration scripts (written in Groovy) start with a “Checkout” stage where we clone the repository that the later stages will build and test. Here’s what a typical “Checkout” stage looks like:

![](https://miro.medium.com/max/1656/1*-_Iv_H2-DiHp6ncVoQzhqw.png)![](https://miro.medium.com/max/1656/1*-_Iv_H2-DiHp6ncVoQzhqw.png)



If we were using the Git CLI directly, it would translate to:

![](https://miro.medium.com/max/1656/1*P05GTXZaD2j3tUuUjJ8p-Q.png)![](https://miro.medium.com/max/1656/1*P05GTXZaD2j3tUuUjJ8p-Q.png)



“`

Even though we’re telling Git to do a shallow clone, to not fetch any tags, and to fetch the last 50 commits, we’re still not running this operation as fast as we could be. That’s because we aren’t setting [the refspec](https://git-scm.com/book/en/v2/Git-Internals-The-Refspec) option. Notice that by not setting it in the pipeline configuration script, we’re telling Git to fetch all refspecs: **+refs/heads/\*:refs/remotes/origin/\*.** In the case of Pinboard, that operation would be fetching more than 2,500 branches.

By simply adding the refspec option and specifying which refs we care about (master, in our case), we can limit the refs to the branch we care about and save a lot of time. Here’s what that looks like in our pipeline code:

![](https://miro.medium.com/max/1656/1*8rJX1Ij56JBNiFcPy8EUyg.png)![](https://miro.medium.com/max/1656/1*8rJX1Ij56JBNiFcPy8EUyg.png)



This simple one line change reduced our clone times by 99% and significantly reduced our build times as a result. Cloning our largest repo, Pinboard went from 40 minutes to 30 seconds. It goes to show that sometimes our small efforts can have a big impact as well.

# **Learnings**

Like most developer productivity teams, we work on large services that have a big impact on our day-to-day experience. However, it’s sometimes the one line fixes that can make a huge difference. Our work is about understanding that.

If you have a passion for improving developer productivity, join our team! We’re hiring for engineering roles on our Engineering Productivity team.

*To learn more about Engineering at Pinterest, check out our* [*Engineering Blog*](https://medium.com/pinterest-engineering)*, and visit our* [*Pinterest Labs*](https://labs.pinterest.com/) *site. To view and apply to open opportunities, visit our* [*Careers*](https://www.pinterestcareers.com/homepage) *page.*