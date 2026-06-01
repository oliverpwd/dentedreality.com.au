---
title: How to Safely Think in Systems
date: '2021-10-15T19:33:07-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/how-to-safely-think-in-systems/
---

[How to Safely Think in Systems](https://lethain.com/how-to-safely-think-in-systems/)  



The second most impactful book I’ve read is George Lakoff’s [Don’t Think of an Elephant](https://www.amazon.com/ALL-NEW-Dont-Think-Elephant-ebook/dp/B00NP9LHFA/) which lays out his theory of communication. Lakoff explores a fundamental organizational challenge: as you grow, it becomes increasingly difficult to communicate when you’re not in the room where a discussion happens. I once worked with a staff engineer who described their most significant contribution as giving initiatives catchy names and slogans to propel ideas further than any supporting data might.

That said, *Don’t Think of an Elephant* is my second most influential book, [so there is one ahead of it](https://lethain.com/best-books/). That book is Donella Meadows’ [Thinking in Systems](https://www.amazon.com/Thinking-Systems-Donella-H-Meadows/dp/1603580557). Communicating effectively is a valuable leadership skill, but Meadows focuses on an even more fundamental skill: how to think correctly. Since reading *Thinking in Systems*, I’ve spent a lot of time doing what the title recommends: starting with [an introduction to systems thinking](https://lethain.com/systems-thinking/), implementing a [small language for modeling systems](https://github.com/lethain/systems), and modeling [why work-in-progress limits work](https://lethain.com/limiting-wip/), [system reliability](https://lethain.com/modeling-reliability/), and [hiring funnels](https://lethain.com/modeling-hiring-funnel-systems/).

While there are a decent number of folks out there modeling systems, there’s a much larger group of folks who think of themselves as systems thinkers but utilize techniques like modeling rather casually (a polite way of saying that they don’t use them). Even with modeling tools available, I’ve often taken the shortcut of intuitive modeling, which over time has given me quite the education in making well-intentioned reasoning errors.

Here are a few rules I’ve collected for thinking in systems safely.

## 1. When your model and reality conflict, reality is always right

Occasionally you’ll encounter a systems thinker who anchors on their intuitive model of how things *ought* to work to the extent that they ignore how things are *actually* working. When they run into serious trouble, they get stuck explaining that they shouldn’t be running into trouble.

To avoid that trap, remember that *when your model and reality conflict, reality is always right*.

At Stripe, we developed a [model to guide our reliability strategy](https://lethain.com/modeling-reliability/). The model was intuitively quite good, but its real-world results were mixed. Attachment to our early model distracted us (too much time on collecting and classifying data) and we were slow to engage with the most important problems (maximizing impact of scarce mitigation bandwidth, and growing mitigation bandwidth). We’d have been more impactful if we engaged directly with what reality was teaching us rather than looking for reasons to disregard reality’s lessons.

## 2. Models are immutable, but reality isn’t

Models live forever, but the real world never stops changing. Over time this creates skew between modeled and real outcomes. Safely using models to guide real-world behavior requires proactively detecting skew. Intuitive models are quite hard to check this way, and typically require convincing the model’s creator that their reasoning is (freshly) wrong. Accurate, explicit models are much easier: just compare the predictions against the reals.

For example, I once joined an organization investing tremendous energy into hiring but nonetheless struggling to hire. Their intuitive model pushed them to spend years investing into top of funnel optimization, and later steered them to improving the closing process. What they weren’t able to detect was that [misalignment in interviewer expectations](https://lethain.com/getting-to-yes/) was the largest hurdle in hiring.

Even if they’d built a one-time [explicit hiring model](https://lethain.com/modeling-hiring-funnel-systems/), they’d have only detected one of these problems. Detecting all three would require routinely checking the model against reality. With an explicit model, it’s relatively easy to compare model results against reality. With intuitive models, you’ll often find yourself in a conflict of belief with the model’s author.

## 3. Every model omits information; some omit critical information

There are a number of areas where it’s hard to measure outcomes, and designing models in these areas is particularly difficult. Security is a particularly good example: how do you meaningfully measure your security risk? I explored this topic in [Metrics for the unmeasurable](https://lethain.com/metrics-for-the-unmeasurable/), and I *love* Ryan McGeehan’s post on [measuring security impact by forecasting risk](https://medium.com/starting-up-security/killing-chicken-little-measure-and-eliminate-risk-through-forecasting-ecdf4c7e9575).

More subtly complex are problems where only a subset of the system is easy to model, which is a good description of the service migration I worked on at Uber.

The team I joined at Uber was responsible for the infrastructure portion of migrating a monolithic Python application to a services architecture. I learned quite a bit about [running large migrations](https://lethain.com/migrations/) from that experience. The first thing to highlight here is that we were extraordinarily successful at our goal. Working on an on-prem infrastructure in a pre-Kubernetes world, we facilitated the rapid shift from monolith to *thousands* of services. We did this with a fairly small team, relying on self-service tooling and automation. It’s a testament to the team who did the work and also the power of systems thinking to identify an effective approach to large, complex problems.

However, and this is a huge however, the negative externalities to product engineering created by migrating to a massive population of services was quite high. For a problem I thoroughly modeled to identify our path forward, I was blindsided by the extent of the challenges that I didn’t include in the model. Systems thinking will always miss issues that its models don’t consider.

Models are necessarily incomplete, and the process of making a model is simplifying reality into a useful reasoning tool. Once you’ve developed a model, you can only tell if it’s useful by getting right back into the mess of reality. If you priviledge a model’s narrow viewpoint over reality’s actual results, your reasoning tool will soon become a reasoning trap. Effective systems thinking comes from the tension between model and reality, without a healthy balance you’ll always lose the plot.