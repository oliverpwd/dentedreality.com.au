---
title: Stepping Stones Not Milestones
date: '2020-07-26T09:12:01-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@jamesacowling/stepping-stones-not-milestones-e6be0073563f
---

[Stepping Stones Not Milestones](https://medium.com/@jamesacowling/stepping-stones-not-milestones-e6be0073563f)  



A mythology often develops around [successful large engineering projects](https://www.wired.com/2016/03/epic-story-dropboxs-exodus-amazon-cloud-empire/). We celebrate the end results and reflect on the positive steps taken to get there but quickly forget about all the missteps and uncertainty along the way. These “moonshot projects” teach engineers a terrible anti-pattern: Large projects addressed via completely disjoint phases of design, execution, and delivery.

This anti-pattern typically manifests itself in one of two ways:

1. The team that is paralyzed at the prospect of designing a solution to a multi-year problem. The warning signs are months of iteration on design proposals, increasingly complex architectures before a single line of code has been written, optimizations for problems we aren’t even sure exist yet, and an ever-increasing demand for “engineering resources” before we can start building stuff.
2. The team that has a complete system design and execution plan but doesn’t plan to deliver any value to the company or any means for reevaluation until the very end of the project. The warning signs are usually surprise that a VP is hesitant to green-light the project, or an increasing backlog of dependencies from other teams getting stalled on project completion.

In both cases it’s *possible* to successfully deliver on a project like this, but it’s a huge risk.

The solution to delivering on complex projects without over-engineering, over-resourcing, over-designing and overly risk-taking is often re-scoping the project into a cleverly formulated set of *stepping stones*.

# Unknown unknowns

Sometimes glimmers of genius can emerge from the darkest of places. Regarding an inability to link Iraq to Weapons of Mass Destruction, in 2002 Donald Rumsfeld said:

> Reports that say that something hasn’t happened are always interesting to me, because as we know, there are known knowns; there are things we know we know. We also know there are known unknowns; that is to say we know there are some things we do not know. But there are also unknown unknowns — the ones we don’t know we don’t know. And if one looks throughout the history of our country and other free countries, it is the latter category that tend to be the difficult ones.

If we strip away the unfortunate context, this turns out to be one of the most insightful statements ever made on project management and the development of complex systems.

**Known knowns** are the easy stuff. Things you have to build. Check-boxes you need to check. Just go do that stuff.

**Known unknowns** aren’t too scary either. Don’t know whether the database will scale to our workload? Go test it. Don’t know how long it’ll take to build a certain feature? Welcome to engineering.

**Unknown unknowns** are the killer though. The stuff you never saw coming. The features you don’t even know that you’ll need to develop. The roadblocks you have no idea are hiding around the corner. The design challenges that are so far in the distance that you can barely see them.

You don’t know your unknown unknowns! No amount of staring at a blank whiteboard will materialize them. You need to go out and find them. This should be the basis for much of your planning.

# Strategy is a Cone

Thinking that “serious engineering” involves picking a point on the horizon and charting a straight-line path to get there is a tragically optimistic view. Engineering challenges are called that because they’re *challenging*; this stuff is meant to be hard! We don’t know what we don’t know. You can’t just sit there scratching your chin for a couple of days and come up with a flawless step-by-step plan — you’re going to need to figure some stuff out as you go!

You always need to invest in design and planning ahead of time, but you need to accept that the solution to your end goal is much hazier than a single point and that the path to get there isn’t a straight line. Your project strategy defines an approximate solution space. Your job is to make your way towards an acceptable solution while not deviating from that strategy.

![]()


Project execution isn’t a straight-line endeavor, it’s a sometimes-meandering journey through a cone defined by project strategy.

It’s alright if you drift left or right along your way to the goal, just don’t veer right out of the cone. You need to stay directionally on track. At each step we eliminate unknown unknowns while making progress towards our end goal.

# Stepping Stones

Here’s the problem with arbitrary project milestones: They’re kinda useless. Sure you need to figure out a project plan and do some estimating and track progress and send out emails to half the company about how you just successfully completed Milestone M2b and are making great progress towards Milestone M3. Milestones are good for tracking execution, but do they actually help de-risk a project or eliminate unknown unknowns? Not really.

Forget about this milestone stuff and jump on the stepping stone bandwagon. All the cool kids are doing it.

The key thing about a “stepping stone” is that it’s not just an arbitrary checkpoint along a project timeline, it’s a vantage point where you can re-situate yourself and evaluate next steps. It’s a point where unknown unknowns start to fall away. Think of them as a place to stand; you’ll be amazed at how far you can see from there.

# What makes a good Stepping Stone?

This is basically the entire point of this blog post. These bullet points right here. Here we go:

* Stepping stones are a cohesive, concrete deliverable. They involve the *completion* of something, generally a simplified version of a final system.
* Stepping stones deliver real value. If the company decides to pull the plug on the project, we should have got something out of the stepping stone version. This could be a system that works at smaller scale or a useful standalone component.
* Stepping stones reside in the *cone of strategy*. The road to success will likely take a meandering path, but each step should be directionally consistent with where we want to go.
* Stepping stones allow us to learn something! By building a smaller version of the project, we drastically reduce the scope of unknown unknowns. Problems that seemed open-ended and intractable at the start now just seem like obvious next-steps once the solution space has been trimmed down.

Deploying a simpler but less efficient version of a storage system is a **concrete deliverable** that we can start using now. Refactoring an API to decouple clients from a backend and simplify application development **brings real value** and **allows us to learn** what API works for applications. Using an off-the-shelf component instead of something custom is still **directionally consistent** with where we want to go. All these stepping stones take us closer to our end goal and reduce the scope of unknowns along the way.

# Leveraging Stepping Stones

A well-articulated set of stepping stones is the gift that keeps on giving.

**Got a VP breathing down your neck about how long a project will take?**Put their mind at rest by demonstrating that you’ll be delivering incremental value along the way and that each stepping stone presents an opportunity to see if the project is running successfully.

**Got a project depending on you that’s causing timeline pressure?**Build a simplified system that unblocks them so you can focus on improving the core of your system without constant cross-team coordination.

**Got an engineer who wants to over-optimize and build fancy stuff?**  
Convince them just to build the simple thing first. Maybe you don’t need a custom-built key/value store, and MySQL will just work fine in the meantime. There’ll always be an opportunity to optimize later, and by the time we get to that point we’ll know whether or not we *need* to optimize! If we don’t need it, don’t do it!

**Need to cancel a project or direct resources elsewhere?**  
Phew, good thing we didn’t just waste 18 months of work! Go ahead and cancel it or put it on hold, at least we got value out of the previous stepping stones.

**Struggling to motivate a team to work hard towards a distant goal?**  
We all struggle to get excited about goals that seem out of grasp. Instead, get a team excited about shipping a stepping stone. Launching a real system or real component, albeit one that’s been scoped down, is far more exciting than satisfying an arbitrary incremental milestone.

**Don’t know how to solve a problem in advance?**  
Neither do I! The Dropbox file storage system uses a custom-designed Vandermonde matrix for erasure coding that minimizes the cost of cross-region data reconstruction, taking into consideration our network topology and the relative costs of hard drives and network bandwidth. This sounds kinda complicated. I promise you that we weren’t thinking about linear algebra when designing the first prototypes of the system! We just got the basics in place and improved them over time in subsequent stepping stones.

# Pursue Simplicity

If you’ve read this far and decided that it’s time to stop planning and just build whatever the hell you want then you’ve missed a crucial point. Don’t forget about the cone of strategy! (*ok that phrase sounds cheesy already)* A stepping stone is only a stepping stone if it delivers forward directional progress.

When we first designed the Dropbox storage system we weren’t thinking about erasure coding or shingled magnetic recording or any advanced cost savings techniques, but it would have been an *absolute disaster* if we weren’t able to retrofit these later. The key was that we designed earlier stepping stone versions in a simple and extensible way, with an eye towards our long-term goal. **This is an art.** Typically the best engineers in a company will distinguish themselves by the ability to do this.

Extensible architecture is too big a topic to describe in a single blog post but the most fundamental tenant is to **focus on simplicity**. Cleverly designed systems are characterized by elegance and simplicity, not complexity. The simpler a stepping stone is, the less chance it has to paint you into a corner and the more amenable it is to being adapted in response to unknown unknowns.

# Stepping stones Gone Bad

You’re going to need to use some common sense here. The three biggest risks involved in designing stepping stones are:

## Wasting time

Stepping stones are meant to simplify a project. If you’re spending all your time building something that we’re just going to throw away, that sounds like a step in the wrong direction. The cone of strategy is your friend.

Not all projects need stepping stones. No project should have a *lot* of stepping stones. They’re called stepping *stones,* not stepping-pebbles or stepping-gravel. Sometimes you just need to take the time required to do big things.

## Getting stuck in local maxima

Truth be told, you can often make bigger changes if you’re not trying to deliver incremental value along the way. Sometimes you just need to take a huge risk and change everything, but understand that it’s a huge risk. Most large projects are better off adopting useful stepping stones that don’t significantly compromise the end goal.

## Moving without thinking

If you don’t think hard about strategy and design before coding then it’s likely you’ll drift out of the cone of strategy… in fact you might not even know what it *means* to be directionally consistent with your end goal. Stepping stones aren’t an excuse to avoid thinking, they’re a tool to consciously and deliberately stage out a project and avoid excess complexity before unknown unknowns have been identified.

# Summary

Instead of splitting a project up into arbitrary milestones, consider delivering incremental value by shipping concrete stepping stones. Stepping stones can serve to de-risk a project by minimizing dependencies and providing standalone checkpoints. Most importantly however they help to simplify a complex project by providing a means to structure deliverables around eliminating unknown unknowns. Formulating useful stepping stones is an art and often requires an intense focus on simplicity to avoid deviating out of the cone of strategy along the way to an end goal.