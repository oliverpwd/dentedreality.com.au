---
title: What You Need to Know About Continuous Integration
date: '2019-11-04T19:13:26-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://angel.co/blog/what-you-need-to-know-about-continuous-integration
---

[What You Need to Know About Continuous Integration](https://angel.co/blog/what-you-need-to-know-about-continuous-integration)  



The most popular software applications on the planet have a few things in common. They solve a real problem, they’re (usually) easy to use, and they offer a best-in-class customer experience. Sounds simple, right? Even if you’re just starting your career, you probably know that the opposite is true. In most cases, the “best” apps are often sophisticated projects that require ongoing testing and software updates.


This puts programmers in a tricky position. Business leaders really want to get their products to market as quickly as possible, but it’s virtually impossible to release stable code without a sustainable testing process in place. In response, many teams rely on continuous integration (CI), a software development practice in which individuals commit changes into a central repository multiple times per day. Although this idea was originally conceived in the early 1990s, CI has entered the mainstream over the last few years. A recent study by DigitalOcean found that [58% of developers](https://sdtimes.com/cicd/developers-using-ci-cd-report-finds/) reported using a CI process at work.


With so many companies using CI today, it’s important to understand its nuances as you begin your career. In this post, we’ll give you a high-level overview of how continuous integration works, as well as some best practices that will help you stand out from Day 1.


## What is continuous integration?


We’ve established that one of the key principles of continuous integration is that developers commit multiple changes per day to a shared repository. But what happens next? And what’s the point of all of this work? At first glance, CI sounds like a really good way to generate a lot of bad code from a team of developers. And to some degree, that’s true. But the basic mechanics of continuous integration are really interesting.


Let’s start with what happens after developers commit changes in a CI environment. A typical continuous integration involves a series of automated systems and tests. When a developer commits new code, that prompts the automated system to create a new build of the source code, which is then run through a series of tests. If the system detects any errors, the entire development team is notified.


OK, that sounds neat, right? But why does it matter? Ultimately, this reduces the need for a lot of manual work. Without a CI process, developers would constantly need to coordinate with each other to avoid working on the same feature and committing conflicting code. With a continuous integration process in place, multiple developers can work on the same feature at the same time. Not only does this reduce friction, but it makes it much easier for teams to resolve customer issues and ship software updates quickly.


Table of Contents

1. What is continuous integration?
2. Continuous integration vs. Continuous deployment
3. Best practices for continuous integration
4. Final thoughts




#### The Weekly Newsletter

Top jobs & tech news—delivered






## Continuous integration vs. Continuous deployment


Continuous integration is just one strategy that software development teams use to iterate quickly and ship new software. The word “continuous” can be found in a variety of software development practices. This can lead to a lot of confusion, especially since many teams practice all of them.


Before we go any further, let’s take a closer look at some of the strategies that are often associated with continuous integration. Many of the following definitions will look similar, but it’s important to understand their subtle differences as you begin your first job.


* **Continuous integration**: As we’ve discussed, CI integrates changes from multiple developers through automated tests and builds
* **Continuous deployment**: There’s often the most confusion between CI and continuous deployment. Unlike CI, which integrates commits every day, continuous deployment is the practice of ensuring that code can be deployed at any given time.
* **Continuous delivery**: Continuous delivery is an extension of continuous deployment, in which software development teams ensure that they can deploy an entire application to customers with the click of a button. Sten Pittet at [Atlassian adds](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment), “In theory, with continuous delivery, you can decide to release daily, weekly, fortnightly, or whatever suits your business requirements.”

## Best practices for continuous integration


In 2006, Martin Fowler wrote one of the first whitepapers on continuous integration. Today, Fowler’s whitepaper is still recognized as an authority on the best practices of CI. Many of his guidelines are geared towards engineering managers that are considering implementing a continuous integration process, but there are also a few tips for individual contributors.


While we’ve talked through a lot of the technical nitty-gritty of continuous integration, let’s take a closer look at a few of Fowler’s suggestions for individual contributors in a CI working environment. We’ve gone ahead and distilled some of his thoughts for the sake of brevity, but you can also read his entire whitepaper [here](https://www.martinfowler.com/articles/continuousIntegration.html).


* **Make your build self-testing.** Include a few lines of code in your commits that can test a large part of the entire code base for bugs and inconsistencies.
* **Commit to the mainline every day.** We’ve touched on this already, but Fowler is an advocate of daily commits from each member of a software development team. Not only does this maximize team-wide output, but it makes it easier for teams to identify and resolve bugs as quickly as possible.
* **Commits should build the mainline on an integration machine.** This is a really technical way of saying that you should test every commit on your desktop to ensure that it won’t break the main repository before considering it done. He suggests that you shouldn’t even leave work for the day unless the mainline build passes with the commit(s) you’ve added.
* **Keep your builds fast.** Although some builds can take upwards of an hour, Fowler strongly suggests ensuring that your builds take around 10 minutes.
* **Fix broken builds immediately.** This one’s fairly simple to understand. If your build fails, or if you’re the first one to notice a failed build, jump in and resolve the issue.

The concept of continuous integration is fairly straightforward, but it can seem like a daunting task for any new developer to adhere to. But with a strong understanding of the basics of CI and how developers prefer to work together, you’ll find it easier to get up to speed quickly and endear yourself to your new teammates.


## Final thoughts


That was a lot of information to digest. If this guide made continuous integration seem a bit intimidating, don’t worry—you’re not alone. Even some of the most experienced software developers shudder at the thought of committing changes so many times every day. While you’re bound to make a few mistakes along the way, here are a few tips for anyone doing CI for the very first time:


* **Ask for help, especially in your first few weeks.** Many companies offer robust onboarding programs for new developers that include things like [pair programming](https://angel.co/blog/agile-methodology-a-primer-on-moving-fast) and [mentorships](https://angel.co/blog/best-first-jobs-in-tech). But even when you’re not participating in these activities, raise your hand and ask for help when you need it. We’ve reviewed some of the basics of CI, but your new company likely has unique wrinkles in its process that we haven’t covered here.
* **Don’t be afraid to break things.** You’d be hard-pressed to find a developer who hasn’t broken something really important at one point in his or her career. The beauty of CI is that it requires you to ship small changes every day. If you ship broken code, CI makes it easy for your team to identify any issues quickly and review them with you.
* **Run linting programs on all of your code.** [Linting](https://stackoverflow.com/questions/8503559/what-is-linting) is a technical term to describe the process of running your code through a program that tests it for errors **before you commit**. Senior-level developers tend to do this frequently, even when they feel confident that their commit is error-free.

Above anything else, don’t forget that you were hired because you can write quality code. Although there’s a lot to know about CI, trust your instincts and jump right in. You’ll probably learn some tough lessons, but eventually continuous integration will become second nature to you. Plus, if you get lost along the way, you can always refer back to this guide.


*[Rich Moy](http://www.richmoywrites.com/) is a freelance writer. You can find his work on AngelList, Stack Overflow, and The Muse.*