---
title: The most common problem I’ve seen in product/engineering process
date: '2018-05-20T15:46:01-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://hackernoon.com/the-most-common-problem-ive-seen-in-product-engineering-process-debd821a423f
---

[The most common problem I’ve seen in product/engineering process](https://hackernoon.com/the-most-common-problem-ive-seen-in-product-engineering-process-debd821a423f)  



![](https://i2.wp.com/cdn-images-1.medium.com/max/2000/1*mKvqk_l9I7JgH-6fwBRWNw.png?w=607&ssl=1)![](https://i2.wp.com/cdn-images-1.medium.com/max/2000/1*mKvqk_l9I7JgH-6fwBRWNw.png?w=607&ssl=1)

[Image from here](https://www.pexels.com/photo/schedule-planning-startup-launching-7376/)


The first time I became aware of this problem wasn’t at work at all. In fact, this is a common problem in any sort of situation where one party is seeking help from another party.

I was in Seattle with my boyfriend for Thanksgiving couple years ago. On Wednesday night, I realized mid-dinner I had forgotten to bring my toothbrush and toothpaste. I asked the waitress:

*“Do you know if there’s any open convenience store around here?”*

The waitress answered: *“I don’t know. Sorry.”*

*“Why did you ask about convenience store?”* My boyfriend asked me.

*“Because I can buy a toothbrush there.”*

*“Right, so why didn’t you just ask about the toothbrush?”*

*“Umm…”*

*“Have you heard of the XY problem?”*

*“No…”*

> The XY Problem — the XY Problem is asking about your attempted *solution* rather than your *actual problem.*

***“You are trying to solve problem*** `X`***, and you think solution*** `Y` ***would work, but instead of asking about*** `X` ***when you run into trouble, you ask about*** `Y`***.”***

The XY problem can lead to significant waste of time and energy for both the person asking for help and the person providing help. Here’s a good example related to coding from [stackexchange](https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem).




I’ve seen the XY problem happening more than a couple times in the past at the companies I have worked at.

#### How do you know whether your company is experiencing this problem?

In my experience, often, the consequence of this problem took the form of features that rarely or never got used, features that did not provide any learning for the company, or features that did not provide any value to the customers.

I’ve seen dozens of different types of events getting tracked but never getting looked at because they were either not actionable, hard to analyze, or both. I’ve seen features worth over 1000 lines of React code get implemented, deployed to production, never getting used, and then getting completely scraped by new code within weeks. I’ve spent days on small but complicated UX requests that could have been replaced with much simpler solutions (or needn’t be there in the first place).

All of these events and wasted effort happened because somewhere in the product/engineering process, the real *why* got lost and the team shipped a feature `Y` that did not solve the real issue `X`.

I’ve indeed been guilty of that myself: not digging deep into the why before starting the implementation of something that, ultimately, had to get scraped because it didn’t solve anything.




#### So how can you avoid this problem?

I’m still young in my career and I don’t have all the wisdom. However, I do think that a product/engineering process that’s implementation-based tend to fall prone to the XY problem more often than a product/engineering process that’s problem-based.

Here’s the difference.

A product/engineering process that’s implementation based tends to be more linear and assembly-line like. Product owners make decisions on what features to build. Designers then come up with mockups. Only once the design is done are the engineers building the features told about the said features.

What’s wrong with this workflow? For one, people down the chain don’t get a clear context into the root problem (i.e. `X`). If a falsey assumption (i.e. `Y`) is made at the beginning of the chain, then everyone involved are going to blindly follow order and do `Y`.

On the other hand, in a problem-based workflow, the role of the product owner is to keep the team focused on the *why*. Product, design, and engineering collaborate and brainstorm together to define and solve a problem.

> Behind every what is a why.

All the times I’ve seen the XY problem happen is because the people involved failed to live by this principle.

Why are we doing this feature?

Why is this feature helpful for customers?

Why is this feature helpful for our own learning?

If the why is not thought out or communicated clearly, that’s a recipe for over-engineered implementations that ultimately don’t solve the root problem.