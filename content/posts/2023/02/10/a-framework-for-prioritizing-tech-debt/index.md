---
title: A Framework for Prioritizing Tech Debt
date: '2023-02-10T06:21:26-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt
---

[A Framework for Prioritizing Tech Debt](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt)  



## The Importance of Leverage

Having spent over a decade building tech startups, I’ve come across my fair share of tech debt: The gnarly Ember.js code no one wants to touch, the bespoke cloud infrastructure maintained entirely by hand, or the solitary Elixir service left behind by a long-gone former teammate.

While these may be painful today, at one point in the past they were likely important accelerants that pushed the product forward in a meaningful way. In fact, tech debt is arguably a necessary evil–if a growing company isn’t taking on some measure of leverage, then it’s likely not shipping as fast as it should be. However as a company begins to see traction, there will come an inflection point where it becomes important to start prioritizing tech debt.[1](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fn-1)

Usually this time will come as your business starts to scale and earlier decisions made for the sake of time start to become bottlenecks to new work. But then the question becomes, how do we prioritize paying down some of the debt we’ve accrued when it’s competing with our bandwidth to build new features?

## Surveying the Debt

First we want to draft a map of the landscape. Our goal here is to understand the system and how its individual components relate to one another. This needn’t be overly detailed, but should provide enough specifics that we can start to examine pieces of it in terms of how components support our product workflow. As an example, if we can answer the question, “Is this a bottleneck?” then we’re on the right track

Some parts of this map may require extra attention in order to understand what parts of a specific component are causing us issue. For instance, is the data model scaling with our system or is the database technology itself the problem?[2](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fn-2) Examine pain points and understand not just the symptom but the underlying cause: We chose a naive data model which doesn’t work at scale.

It’s often helpful to structure this an exercise involving folks from across the wider set of teams. Ask a few representatives from each team to document various pain points and [toil](https://sre.google/sre-book/eliminating-toil/), especially things that are thematic or come up repeatedly. Collate this into a survey of the landscape of debt.[3](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fn-3)

## Interest Rates

Once we have an idea of the landscape and where within it we’re experiencing pain it’s time to conduct the next exercise. Enumerate each piece of debt. Perhaps you identify a fragile relationship between two services–write this down. Go through your holistic system and document each deficiency. The goal here is not to ascribe importance just yet and instead to be comprehensive.

Now with a complete list of your tech debt as it stands go through each and answer the following questions:

* If we choose to do nothing, will this issue become worse, remain the same, or improve?
  + If it’ll become worse, how quickly will it degrade?
  + If it remains the same, how much disruption is it causing today?
  + If it’ll improve, at what point will it improve to the degree it’s no longer an obstruction?

![](https://www.maxcountryman.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdo-nothing.6ffdb3e2.png&w=3840&q=75)![](https://www.maxcountryman.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdo-nothing.6ffdb3e2.png&w=3840&q=75)

Assuming we decide to do nothing, then how much worse do things become? This is effectively our “interest rate” on tech debt.

* Is this part of the system active or dormant–are we building new features on it today or is it in maintenance mode?
  + If it’s dormant, how much time is spent on maintenance each engineering cycle?
  + If it’s active, take note of that: you’re building on a foundation that may not be stable.

![](https://www.maxcountryman.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdormant-or-not.2e783b38.png&w=3840&q=75)![](https://www.maxcountryman.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdormant-or-not.2e783b38.png&w=3840&q=75)

If the debt isn’t part of an active area of development, then we want to understand how it’s impacting development velocity. If it is, then we might be building on a rocky foundation.

Answering these questions helps us form a rubric for grading technical debt and can then be used as a key input to prioritization alongside other work, like net-new features.

There’s no one-size-fits all here, so you’ll have to decide exactly how you want to weight these criteria. However as a high-level guide, you will generally want to prioritize things that are becoming worse and which you’re actively building on more aggressively. These items tend to be like high interest rates on a credit card. Whereas items that aren’t degrading quickly and aren’t part of the actively developed system are a more healthful form of debt.[4](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fn-4) For things somewhere in between, these will require more careful balancing relevant to your precise circumstances as a company.

![](https://www.maxcountryman.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhigh-priority.e81d94b2.png&w=3840&q=75)![](https://www.maxcountryman.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhigh-priority.e81d94b2.png&w=3840&q=75)

When things are rapidly becoming worse and they involve active areas of development we can expect challenges.

Another surprising thing you may find in conducting this exercise is that there are even a few items that are essentially self healing. These almost certainly don’t require attention with the caveat that it’s still important to understand how they impact product development velocity.[5](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fn-5) The benefit of identifying such things is that you can know to deprioritize these things in favor of the more costly items above.

## Staying Solvent

It’s important to point out that leverage is a powerful tool. Technical debt is a kind of leverage and most startups will want it if not need it. So the goal of this framework is to provide a more structured view into that debt such that we can identify “good” and “bad” debt and decide how to proceed in addressing it.

While there’s no universally correct answer, we’ll generally want to prioritize the high interest rate items and can continue to leverage lower interest rate items so long as they don’t impede us too much.

In the end the key thing here is to use frameworks like this to remain solvent in terms of our code base and product workflow. With tools like this, we can avoid bankruptcy (literally and figuratively).

## Footnotes

1. Sooner or later your rate of building new features will slow to crawl, buckling under the weight of all the short cuts and quick fixes that came before. [↩](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fnref-1)
2. It’s probably not the database. [↩](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fnref-2)
3. You might put this together as a document which can be referenced later. Having an artifact like this is important because it can serve as input to future iterations of this exercise. [↩](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fnref-3)
4. Jettison this debt last, unless there are other compelling reasons to prioritize it. Healthful debt is usually the lowest priority. [↩](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fnref-4)
5. It’s unlikely to be the case, but even something that improves over time can do so at a velocity that artificially holds back product development–in this instance it may merit a closer look. [↩](https://www.maxcountryman.com/articles/a-framework-for-prioritizing-tech-debt#user-content-fnref-5)