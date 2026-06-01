---
title: Solving the Engineering Strategy crisis.
date: '2023-10-22T19:59:02-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/solving-the-engineering-strategy-crisis/
---

[Solving the Engineering Strategy crisis.](https://lethain.com/solving-the-engineering-strategy-crisis/)  



*[These are speaking notes for my October 4th, QCon talk in San Francisco.](https://qconsf.com/keynote/oct2023/use-engineering-strategy-reduce-friction-and-improve-developer-experience)*  
*[Slides for this talk.](https://docs.google.com/presentation/d/1r7blxxZcDnNwHRLUB3Pu76VZFfgdqh10Jlw8YcNgQIQ/edit?usp=sharing)*

Over the course of my career, I’ve frequently heard from colleagues, team members  

and random internet strangers with the same frustration: the company doesn’t have  

an Engineering strategy.  

I don’t think this problem is unique to Engineering: it’s also common to hear  

folks complain that they’re missing a strategy for Product, Design or Business.  

But, whereas I don’t feel particularly confident speaking to why so many companies  

are missing a clear Business or Product strategy, I’ve come to have some clear opinions about  

why so many engineering organizations don’t have a written strategy.

![](https://lethain.com/static/blog/2023/where-is-eng-strategy.png)

I’ve been fortunate to be involved in architecture at many companies,  

including designing several iterations of Stripe’s approach to architecture  

([which taught me some lessons](https://lethain.com/scaling-consistency/)).  

From that experience, I’ve tried writing about this topic quite a few times:

* [Magnitudes of exploration](https://lethain.com/magnitudes-of-exploration/) documented a public version of Stripe’s Engineering strategy
* [Write five, then synthesize](https://lethain.com/good-engineering-strategy-is-boring/) presents a methodology to drive Engineering strategy  
  
  while operating as an individual contributor
* [Writing an engineering strategy](https://lethain.com/eng-strategies/) describes how Engineering executives can lead  
  
  Engineering strategy at their company
* I also collected [engineering strategy resources written by others](https://staffeng.com/guides/learning-materials/)  
  
  into *Staff Engineer*’s appendix

In this talk, I hope to pull those ideas together, into a unified theory of  

Engineering strategy, with a particular emphasis on how you can drive  

strategy even if you’re not the company’s CTO.  

Another way to think about this talk, is that I hope to “Solve the Engineering Strategy Crisis”  

that so many people keep emailing me about.

## What I will talk through

In this talk, I’ll work through five topics around engineering strategy:

1. Eng strategy is honest diagnosis + practical approach
2. It’s useful (↑dev velocity, ↓friction)
3. It’s everywhere, although rarely written
4. Written strategy is much more effective
5. You can advance strategy at your company

## What is Engineering strategy?

Whenever I think about strategy, I start from  

Richard Rumelt’s [Good Strategy, Bad Strategy](https://www.amazon.com/dp/B004J4WKEC),  

which three pillars of effective strategy:

1. **Diagnosis** – a theory describing the nature of the challenge. This is trying to identify the root cause(s) at play, for example “high work-in-progress is preventing us from finishing any tasks, so we are increasingly behind each sprint” might be a good diagnosis
2. **Guiding policy** – a series of general policies which will be applied to grapple with the challenge. Guiding policies are typically going to be implicit or explicit tradeoffs. For example, a guiding policy might be “only hire for most urgent team, do not spread hires across all teams.” If a guiding policy doesn’t imply a tradeoff, you should be suspicious of it (e.g. “working harder to get it done” isn’t really a guiding policy, the relevant guiding policy there might be “work folks hard and expect high attrition”)
3. **Coherent actions** – a set of specific actions directed by guiding policy to address challenge. This is the most important part, and I think the most exciting part, because it clarifies that a strategy is only meaningful if it leads to aligned action

I’ve found that definition extremely useful, and Rumelt’s views have shaped how I think about Engineering strategy.  

In particular, I believe that Engineering strategy comes down to two core components:

1. **Honest diagnosis** that engages with the reality your organization’s current needs and challenges
2. **Practical approach** to move forward while addressing the circumstances raised in the diagnosis

Sure, that sounds nice, but what does that *mean*? To clarify that a bit, let’s work through  

an example scenario. This is a scenario that many folks have experienced in their career:

1. You join a new company
2. Your team works in a Python monolith to build the Widget product
3. Your CTO hates monoliths, mandates service migration
4. You join a team building a brand new Hammer product in a new service
5. 2 years later, your old team and Widget are still in the monolith
6. You have no idea how to share code between Widget and Hammer

I believe this sequence of events keep reoccuring because of bad strategy,  

and is preventable with good strategy. Lets work into the components of  

strategy to look at how strategy could cause *and* prevent this scenario from happening.

Starting with “honest diagnosis” and in particular, looking at what a bad honest diagnosis  

would look like for this scenario. (For the record, I don’t think “dishonest” is the opposite of an “honest”  

diagnosis, they tend to be “bad” rather than “dishonest.”)

Here’s a bad diagnosis:

1. “We can migrate from our monolith to services in three months.”
2. “We’ve derisked our approach by moving a meaningfully complex component out of our monolith.”
3. “We’re willing to invest heavily in migrating to services, even if it means slowing down product velocity in the short term.”
4. “We are willing to expand our Developer Tools team to build new tools for services in addition to supporting our existing monolith.”

OK, but then let’s briefly consider what a good diagnosis might look like:

1. “We can migrate from our monolith to services in three months.”
2. “We’ve derisked our approach by moving a meaningfully complex component out of our monolith.”
3. “We’re willing to invest heavily in migrating to services, even if it means slowing down product velocity in the short term.”
4. “We are willing to expand our Developer Tools team to build new tools for services in addition to supporting our existing monolith.”

Disappointingly, this is the same list in both cases. In a small startup with only one simple product,  

you probably *can* migrate from a monolith to services in a few months, maybe even less.  

In a larger startup, that’s almost certainly impossible.

An honest diagnosis is a reality-based assessment of your circumstances.  

Nothing is universally honest. (Neither is anything universally bad.)

Once you find a reality-based assessment to inform your honest diagnosis,  

the second half of your strategy, a practical approach.  

The most important thing to keep in mind is that a practical approach  

makes explicit tradeoffs that acknowledge your real constraints,  

for example, here are some good approaches, even if they are a bit painful to write:

* “We want to migrate to services, but are unwilling to staff Dev Tooling more, so the migration will happen in 12 months after tooling gets finished.”
* “We don’t adopt additional programming languages, even if we prefer them, because we don’t have capacity to support them.”

What makes these good is not that they’re beautiful, ambitious statements of how we work.  

These are not loft [“engineering values”](https://lethain.com/setting-engineering-org-values/),  

they are specific acknowledgments of how you’ll navigate your constraints.

Thinking back to our scenario with Hammer and Widget products, our practical  

approach might look like:

1. Expand Developer Tooling team by 2 engineers for next year
2. Those additional engineers will focus on tooling for services
3. Before committing to our services migration, we’ll validate by moving the Widget product to a service, and operating it as a service
4. If we can’t exceed monolith productivity within Widget, we’ll migrate back
5. No other products are allowed to spin up new services until we’ve validated the Widget migration was successful and a significant improvement (as measured by % of product eng team’s time spent on features combined with number of major Widget product ships relative to last year)

Once again, tragically, a practical approach depends on your company and your circumstances.  

You could write the same exact practical approach and have it go very badly indeed,  

which is why [senior leaders often fail when they reapply familiar strategies at new companeis](https://lethain.com/grand-migration/).

Hopefully you’ll accept the definition of “engineering strategy = honest diagnosis + practical approach”.  

Next, is to try to convince you that this definition is actually useful.

## Engineering strategy is useful

Let’s start making the case for engineering strategy by talking through  

some practical examples of enginering strategy that I’ve encountered in  

my career.

### Stripe – “We run a monolith in a monorepo.”

Diagnosis:

1. We work in a business with dynamic external forces–regulators across each country, numerous financial partners like banks, and growing enterprise customers–that change frequently and unexpectedly
2. We integrate with thousands of external financial infrastructure that are filled with bad, inconsistent, buggy technology and numerous human-driven processes
3. We have a meaningfully complex financial platform (e.g. money movement) internally that our other products (e.g. Stripe Connect) are built on

Approach:

1. We need our entire risk budget to respond to external changes
2. We reduce technology risk by running a Ruby monolith in a monorepo
3. Our developer tooling team invests heavily in running Ruby and our monorepo at scale
4. Exceptions to the above are narrow and rare (data engineering, tokenization environment)

Impact of Stripe’s strategy:

1. Innovation budget (mostly) went into product, not infrastructure
2. Avoided the decade-long journey into (micro)services that distracted most contemporaneous technology companies
3. Narrow technology landscape made it possible to concentrate investment into technologies like the Sorbet (static typing for Ruby) without an outsized investment with developer tooling

### Calm – “We’re a product engineering company.”

Diagnosis:

1. We’re spending a lot of time arguing about adopting new technologies
2. We seem to be adopting new technologies out of interest in using and learning about new technologies
3. We have a long-running services migration, but only small infrastructure and platform components have been moved out. All product engineering code remains in our monolith
4. Our developer tooling team is split between supporting monolith and service workflows

Approach:

1.. We are a product engineering company  

2. We adopt new technologies to create valuable product capabilities  

3. We do not adopt technologies for other reasons  

4. We write all code in the monolith unless there is a functional requirement that makes it extremely difficult to do so  

5. Exceptions to the above are granted exclusively by the CTO, who will approve in writing in the #engineering channel

Impact of Calm’s strategy:

1. We stopped arguing about technology investments
2. We exited several engineers who didn’t want to follow our strategy
3. Combined, this meant we could consolidate our tooling investments into our TypeScript monolith
4. We started spending our innovation chips on product enhancements, culminating in ML-powered algorithm to determine best content for each user based on their behavior, UI to allow content team to self-service content management rather than require engineering support, and so on
5. This was initially viewed, by some, as making it “less fun”, but ultimately meant we spent a lot more time having doing fun work that both stretched us as engineers and helped our users

### Uber – “We run our own hardware.”

Diagnosis:

1. Uber was going through a period of rapid geographic expansion
2. Some of those geographies lacked a meaningful cloud presence
3. We were operating at a scale, X0,000s of servers, where economic impact of 20-30% lower cost of ownership from managing our own hardware was meaningful
4. We were willing to incur the cost of not having access to useful cloud

Approach:

1. Run exclusively on our own hardware in dedicated colo space
2. Do not store data or compute in the cloud
3. It’s OK to do networking (e.g. TLS termination) on cloud, along the line of a Point of Presence (POP)
4. Any cloud experiments beyond POPs will require CTO approval

Impact of Uber’s strategy:

1. We were able to enter, and remain within, regions that cloud-reliant competitors would be unable to maintain operations within in the case of shifting data locality regulatory changes
2. Concretely, we were able to spinup datacenter in China in ~6 months, without colocating our US or EU data
3. (Aside – this was very painful, I don’t recommend it)
4. We did a lot of Not Invented Here (NIH) to replace common cloud tooling
5. (Life is tradeoffs: even good strategies have undesirable consequences!)

## Why do these strategies work?

These strategies are effective for a few reasons:

1. Many interesting properties only available through universal adoption (“we run our own hardware”)
2. Concentrate tooling investment onto smaller space (“we run in a mono repo”)
3. Reduce energy lost on conflict (“we are a product engineering company”)
4. Control your innovation budget (all three)
5. New hires, especially senior new hires, forced to engage explicitly with strategy rather than having option of ignoring it (all three)

This is the power of making explicit, consistent tradeoffs across an entire organization.

## Absence shows value as well

In addition to arguing the value of strategy from these positive examples,  

it’s easy to find negative examples where a missing or inconsistent strategy  

caused a great deal of pain:

1. Digg’s 3+ year migration to V4, onto a 100% new codebase with a new database, new frontend, new backend, and new algorithms. Honest diagnosis about challenges, but highly impractical approachs
2. Stripe’s introduction of Java had unclear evaluation criteria, took years to assess effective. Rooted in inaccurate diagnosis about problems at hand
3. Uber’s invested heavily in competing routing technologies, causing significant friction. Rooted in simultaneous following conflicting approaches without aligning on approach

I’m sure you can think of examples from your careers as well!

## Strategy is everywhere. *Written* strategy is rare

Interestingly, Uber and Stripe are well-known technology companies,  

and I wrote a bit above about their technology strategies were, but  

neither were particularly proactive at writing their strategies down.

I’ve come to believe that:

* Most companies *do* have an engineering strategy
* Awareness of that engineering strategy is often inconsistent
* It’s very rare for a company to have a written engineering strategy

This is the first really important takeaway from this talk: **you  

can solve half the engineering strategy crisis by just writing stuff down**.

We’ll get to solving the other half in a second.

## Written strategy is more powerful

There are probably an infinite number of reasons why written strategy  

outperforms implicit strategy, but a few that I’ve seen matter in particularly  

important ways are:

1. You can get feedback on it
2. You can make updates to it
3. You can explain why you made updates to it!
4. You can clarify points of confusion
5. Nuance is important, and almost impossible in unwritten strategy
6. It democratizes technical decision making beyond a small caste of architects
7. You can hold people accountable for not following it
8. New hires can learn proactively rather than “fail their way into learning”

## *You* can drive Engineering strategy

Two primary ways:

1. From below: how you can rollout strategy without being the CTO engaging
2. With above: how you can rollout if the CTO’s bought in

### Top-down

This strategy is a modified version of the one  

describes in [Writing an engineering strategy](https://lethain.com/eng-strategies/).  

At it’s core, the thing to recognize is:  

it’s easy to get CTO buy-in if you write the strategy that the CTO wants.

To do that:

1. Align up frequently, and take time to debug their feedback
2. Be trustworthily curious: folks know you’ll listen hard to understand their point
3. Be pragmatic rather than dogmatic
4. Have a track record of Doing The Work to build buy-in
5. Frame it as a low-risk experiment, “We’ll try for 3 months then reevaluate”
6. Let CTO decide how to break ties

If you’re reading this and your biggest thought is,  

“My CTO will never let me do this”, then  

7 out of 10 times, I promise you that either you’re not writing the strategy that the CTO wants.  

The other 3 out of 10 times, there’s some internal conflict that the CTO just  

isn’t willing or able to resolve, which is a bit trickier, but you can approach  

via the next strategy.

### Bottom-up

The approach to bottoms-up rollout is  

described in [Write five, then synthesize](https://lethain.com/good-engineering-strategy-is-boring/):

1. Write 5 design docs
2. Synthesize those design docs into a “narrow strategy”
3. Do the above five times, until you have 5 “narrow strategies”
4. Synthesize those five into a “broad strategy”
5. You just wrote a really good engineering strategy

This approach definitely takes a long time, but I’ve seen it work a number of times.  

Even if your current strategy has some gaps in it, birthing it into an explicit strategy  

document will always make it much easier to address those gaps.

## Recap

Here’s what we talked about:

1. Eng strategy is honest diagnosis + practical approach
2. It’s useful (↑dev velocity, ↓friction)
3. It’s everywhere, although rarely written
4. Written strategy is much more effective
5. You can advance strategy at your company

Within those topics, the two disappointingly  

straightforward steps that you can talk to solve the engineering strategy crisis are:

1. Writing down the existing strategy
2. Using either tops-down or bottoms-up approach to improve the quality of your existing strategy

This might not be what you were excited to do when you wrote about getting  

more strategic in [your annual goals](https://lethain.com/tags/year-in-review/), but it’s what  

actually works.