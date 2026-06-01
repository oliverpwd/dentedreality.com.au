---
title: The Builder’s Trap
date: '2022-10-17T22:44:03-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.patkua.com/blog/the-builders-trap/
---

[The Builder’s Trap](https://www.patkua.com/blog/the-builders-trap/)  



Every developer knows the satisfaction that comes from building a software system. Type in a stream of characters and somehow you’ve built something that appears magical to others. This is the Builder’s dream. The thrill about learning something new. The satisfaction of solving unknown problems through building code. But, the Builder’s dream can quickly become the Builder’s Trap if you’re conscious of the context. In this article, we will explain the Builder’s Trap, where it comes from and three steps to avoid it.

## **What is The Builder’s Trap?**

> “When people fall for the Builder’s Trap, the desire to learn, play and write software takes over.”
> **Source:** The Builder’s Trap
> 
> [Tweet](https://www.patkua.com/)

If you’re a developer, you might think, “Isn’t that the point of software development?” My answer is, “No.” Non-builders know this. Software is only one way to reach a particular goal.

We write software to solve problems. You can solve many problems without writing software. Builder’s forget this, or exclude options because of the Builder’s Trap. When people fall for the Builder’s Trap, the desire to learn, play and write software takes over. Building code becomes the preferred solution, despite simpler or easier alternatives.

## **What does the Builder’s Trap look like?**

In the early days of blogging, there were hosted websites and frameworks like [TypePad](https://www.typepad.com/), [MovableType](https://www.movabletype.com/), [Blogger](https://www.blogger.com/) and [LiveJournal](https://www.livejournal.com/). You either set up an account, or install software to use them. Suddenly you had a blog and could start publishing content.

If you are a developer, you knew someone, or maybe you were the person to fall for the Builder’s Trap. I certainly had many developers in my circle of friends who did. They wanted to write on their own blog. So, what did they do? They decided to write their own blogging software. They spent weeks picking tools, libraries and building code before they published their first entry. Many didn’t even finish building their code and never published one single entry. Sound familiar?

[![](https://www.patkua.com/wp-content/uploads/2022/09/123-yagni-1024x958.png)![](https://www.patkua.com/wp-content/uploads/2022/09/123-yagni-1024x958.png)](https://www.monkeyuser.com/2019/yagni/)

A good example of the Builder’s Trap via [monkeyuser.com](https://www.monkeyuser.com/2019/yagni/)


Blogging websites or frameworks continued to evolve with new features and security patches. Home-grown software was neglected, unmaintained and unused. A few years later and those who wrote their own blogging software abandoned them. Or they migrated to a blogging platform like [WordPress](https://wordpress.org/).

People forgot about the goal: To publish content in a blog format. They succumbed to the Builder’s Trap. We may have come a long way with blogging software, but you can still see this pattern today. You no longer hear software described as blogging software. Today, they’re called, “Static Site Generators”.

## What causes the Builder’s Trap?

As a developer, I have fallen for the Builder’s Trap in the past so I can empathise with this. A lot of these start off with good reasons like a platform missing a feature, or the worry about vendor lock-in and future extensibility. The Builder’s Trap has three key elements:

1. **Over-optimism** – Software estimation is difficult enough. The Builder’s Trap emerges when developers overestimate their ability to write code. “How hard can it be?” is the phrase to watch out for. This compounds when developers also underestimate or do not recognise hidden complexity.
2. **Desire to learn while solving problems** – Writing code is the act of problem solving. Builders love the challenge of solving new problems. Particularly when problems involve learning or solving a technical challenge. Developers learn by solving problems but in particular, through writing code. But sometimes it’s the love of learning that takes over and instead of solving a problem, builders build because they get to learn a new library, framework, or pattern.
3. **Sense of adding value** – Everyone wants to feel like they add value. Particularly when they can do something others cannot. Developers use the Builder’s Trap to underscore their worth. When writing code, non-developers cannot easily contribute to the outcome.

## What to watch out for

Over the years I’ve collected some phrases that might point to the Builder’s Trap. These include:

* “I can easily write this in a couple of hours/days/weeks”
* “How hard can it be?”
* “It’s just not elegant enough?”
* “That’s a horrible system of scripts. We should replace it with a program”
* “We need this one feature this tool doesn’t provide. We need to rewrite the entire thing”
* “This application is written in [X programming language]. We won’t easily be able to maintain it. We’ll need to rewrite it in [Y programming language]”
* “Give me a week. I’ll whip up a prototype to show you what I mean.”
* “We can build XYZ cheaper/ABC is too expensive” ([h/t Adam McKerlie](https://twitter.com/adammckerlie/status/1574850746469818369))

Use these statements as heuristics only. Context matters. Sometimes these statements are an appropriate response.

## The consequences of the Builder’s Trap?

The Builder’s Trap destroys trust between builders and non-builders. Non-builders see builders busy doing something, but they cannot understand what is being built. This leads to non-builders interpreting these activities as “playing around.” The erosion of trust leads to behaviours easily interpreted as micromanagement. This includes increasing the frequency of check-ins and questions about what builders are working on.

It also leads to increased levels of frustration for both builders and non-builders. Builders become frustrated through a constant barrage of questions. Non-builders become frustrated because they don’t understand what builders are working on. Non-builders become frustrated because they don’t see any results. Trust continues to erode as frustration from all sides grows.

## What’s missing from the Builder’s Trap?

There are times when building software is a good choice. What’s missing is context. Not all software systems deliver the same amount of value. Software like email or messaging systems are essential to running a business but rarely add unique value. Every business needs them to function. Software like a marketplace or a product that brings in money does, which differs from business to business.

Value is a function of benefits and costs. In the Builder’s Trap, optimism skews the function. Builders overestimate the benefits the software they build will bring while underestimating the effort to build. On top of the cost of building software, the Builder’s Trap ignores two other costs:

1. **Opportunity Cost** – Time spent writing code for one problem is a missed opportunity to write code for a problem where it is needed. For example, writing your own ticketing system is a lost opportunity to fix bugs or build new features that might earn more money.
2. **Maintenance Cost** – A large cost to software is future maintenance and support. It’s fun to build software but someone must also take care of it in the future. This includes maintaining documentation, updating dependencies, fixing security vulnerabilities and bugs even if there are no major feature changes.

Without a discussion of benefits and all costs, it’s too easy for developers to fall for the Builder’s Trap.

## 3 things you can do to avoid the Builder’s Trap

If you’re a software leader here are three things you can do to minimise the Builder’s Trap.

### 1. Put developers as close to customers as possible

Developers build better solutions when they have a deeper understanding of the problem and its context. So put developers as close to customers as possible. The more disconnected developers are from end users, the less context they have. They cannot truly understand a user’s pain points and build less empathy with them. Count the number of hand-offs from users to developers. Less is often better.

When developers have more context and empathy, they see the impact their solutions have on end users, increasing their motivation. They also see the negative consequences of mistakes on real people. A stronger connection with end users keeps the focus on user needs over the focus on building. As [Tim Ottinger](https://www.industriallogic.com/people/tottinge/) says, “When mastery is divorced from purpose, mastery becomes the purpose.”

> “When mastery is divorced from purpose, mastery becomes the purpose.” from @tottinge
> – Tim Ottinger (Technical Coach at Industrial Logic)
> 
> [Tweet](https://www.patkua.com/)

### 2. Categorise the problem into “Novel” or “Not Novel”

Even when teams focus on user needs, they fail to see how those needs fit into their business context. A business exists to provide value to end users, but often in a narrow context. Before you build a solution, ask if the problem is novel or not novel, relative to the nature of your business.

A novel problem in your industry means you will probably need to build a solution. If the problem is not novel, you should consider outsourcing as there are usually a set of acceptable product or SAAS offerings. As an example, let’s say your business provides recommended content via email. Email is a delivery channel and not novel in this context but the recommended content is. In this context, you want to avoid building an email delivery service. Instead, focus on building the recommendation engine over the email delivery channel.

If, on the other hand, your business was all about selling email services, your choice may be different. Your business will be looking for ways to differentiate its product from competitors. If you used an outsourced email platform, so could your competitors. In this context, the way you offer email is novel, so you’re probably going to build the email delivery engine. We can see these concrete examples in newer email services such as [Superhuman](https://superhuman.com/) and [Hey.com](https://www.hey.com/). Most of you aren’t selling an email service, so you probably shouldn’t be building an email system.

Build solutions for novel problems in your business domain. Consider outsourcing, using open-source libraries/frameworks or PAAS/SAAS software for non-novel problems. You see this recommendation in other business frameworks too. [Geoffrey Moore](http://strategictoolkits.com/strategic-concepts/core-and-context/) uses the terms, **Core vs Context**, more often building systems in the Core domain. [Wardley Mapping](https://en.wikipedia.org/wiki/Wardley_map) describes four phases of product development: **Genesis, Custom-Built, Product and Commodity**. You tend to build systems more often in the Genesis and Custom-Built phases.

Focus on user needs first. Then consider if those needs are novel or not novel in relation to the business you’re in.

### 3. Use small time boxes

In my [time management course](https://techlead.academy/p/time-management), we cover Parkinson’s Law which states, “Work expands so as to fill the time available for completion.” A developer caught in the Builder’s Trap will use all their given time. The more time they have, the more time they use, caught in the thrill of building. The situation degrades as a developer justifies more time as they uncover unknowns. The bigger a time box, a developer will uncover more edge cases, new scenarios or unanticipated technical challenges.

One of the best antidotes to Parkinson’s Law and the Builder’s Trap is to use small time boxes. Use periods between 1 day and at most 2 weeks. At the start of a time box, agree on a lightweight plan between builders and non-builders. The plan should outline the most important priorities and expected outcomes. Review what was actually delivered at the end of that time box. Small time boxes increase the pace of feedback and create a sense of progress. They give us a chance to notice misunderstandings earlier. They also help us recognise when enough value has been delivered.

## Conclusion

Developers don’t fall into the Builder’s Trap with ill intentions. Developers want to solve problems. They want to add value and learn while solving these problems. Watch out for signs of the Builder’s Trap, think deliberately about the context you’re in and use these three tips to help you and your team avoid the Builder’s Trap.

If you enjoyed this article, consider signing up for the free curated newsletter for leaders in tech*: [Level Up](http://levelup.patkua.com/).*