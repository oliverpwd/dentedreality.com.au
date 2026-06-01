---
title: A Blueprint for Internal Open Source
date: '2020-02-28T08:29:50-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@SkyscannerEng/a-blueprint-for-internal-open-source-7169745018c2
---

[A Blueprint for Internal Open Source](https://medium.com/@SkyscannerEng/a-blueprint-for-internal-open-source-7169745018c2)  



![](https://miro.medium.com/fit/c/96/96/2*70ZWEkQbb0oXWTwabNJcYg.png)![](https://miro.medium.com/fit/c/96/96/2*70ZWEkQbb0oXWTwabNJcYg.png)
Skyscanner Engineering
Mar 13, 2018 · 5 min read



*By Chris Downey*

Internal Open Source (aka [Inner source](https://en.wikipedia.org/wiki/Inner_source)) is a topic that I’ve seen come up in lots of different places, but I’ve never seen it first-hand translate into anything beyond an interesting discussion.

In Skyscanner, an internal blog generated a slack discussion, which soon became a working group of interested people from different parts of the company. We all shared a desire to create a workable Inner source approach for Skyscanner and this is how we went about it.

# A fellowship of the willing

We started out with an invite to those who had been active in the discussion to form an initial working group.

In our first session together, we started to frame the discussion around the core problems that we were trying to solve. A stand out area was to be able to simplify the path to production for innovative ideas. In addition, how can those ideas make a business impact with minimal blocking dependencies and frustrations.

That particularly resonated for me as it sums up the whole agile movement:

> *To deliver value in the most friction-less of ways.*

# Getting Going

![](https://miro.medium.com/max/1340/1*TkYRdRwOQQ9rS3GNTv_-WA.png)![](https://miro.medium.com/max/1340/1*TkYRdRwOQQ9rS3GNTv_-WA.png)


Our aims of the group

A few months prior to the group forming, we had invited [Dan North](https://dannorth.net/) to Skyscanner to give a talk to the company on scaling. One concept that really resonated, was that of guiding principles. Guiding principles can be a useful mechanism to help align an organisation, helping people of every level make a consistent decision.

![](https://miro.medium.com/max/1930/1*ylAUvM5L_Hmmp-HUc7XUPQ.jpeg)![](https://miro.medium.com/max/1930/1*ylAUvM5L_Hmmp-HUc7XUPQ.jpeg)


Dan North at Skyscanner Office in Edinburgh

In the working group we felt that defining some guiding principles would help bring inner source to life. At this stage, there was already some inner source activity happening, but it wasn’t pain free. To create the guiding principles, we started to collect some examples of real problems, dilemmas and friction that was being felt both from contributors and service owners. We have a couple of squads in the company who do not own any services, so inner source was their only mode of working, providing a great source of insights.

![](https://miro.medium.com/max/890/1*aFU02oazzjhJsMOchD4c_g.png)![](https://miro.medium.com/max/890/1*aFU02oazzjhJsMOchD4c_g.png)


Our guiding principles

## **Guiding Principle:** Make each other’s life easier

**Context:** There had been some delays and frustrations with both the service owners and for those contributing to a service.

**Intent:** Based on some pain points felt from both parties, our guidelines gave some basic advice on the importance of

*Contributors*

* discuss with service owner any changes in advance
* don’t reinvent the wheel
* follow the service owner’s standards
* make sure tests pass
* add good alerting
* demo before a merge request (if a demo doesn’t make sense/is feasible, what about some screenshots or a little video?)
* small merge requests make it easier for everyone

*Service Owners*

* invest time in creating and maintaining good readme + contributing files
* set expectations to the contributor — timelines, release schedules

*All*

* be clear about as much as possible e.g. by default, service owner owns the code after contribution

## **Guiding Principle:** Leave things better than you found them

**Context:** What do you do if you spot a problem or identify missing information.

**Intent:** For the quality of the codebase and supporting artefacts to improve. If you spot problems, try to make it smoother for the next contributor and for the service owner — e.g. improve a readme/contributing file, improve the codebase, add those missing unit tests etc.

## **Guiding Principle:** Reduce scope, not standards

**Context:** Some contributors were looking for some standards to be relaxed for short lived experiments (e.g. dropping code style for learning experiments)

**Intent:** To keep the quality of the code base as high as possible, regardless of the type of change that is being worked on. If the overhead in doing that is too high, then look to reduce the scope of what you are trying to deliver. Use automated tools as much as possible to make things easier.

## Guiding Principle: Create it, clean it

**Context:** It came from a scenario where service owners were spending lots of time, removing code from failed experiments.

**Intent:** To make it clear that it is the contributor’s responsibility to clean up a change after an experiment has taken place.

## **Guiding Principle:** Evolve or decommission

**Context:** Longer term, we want to have all services to be in a state where anyone in the company can contribute to them. There are some legacy parts of the overall system that are not quite inner source friendly at this stage.

**Intent:** Is for legacy parts of the system to have a strategy to evolve or be decommissioned. Our guideline also includes ways of incrementally improving e.g. [strangler application](https://www.martinfowler.com/bliki/StranglerApplication.html)

## **Guiding Principle:** Lower the barrier to experimentation

**Context:** Skyscanner is live in 50+ country specific domains. What we find is that markets change frequently and have different characteristics. Across Skyscanner, there are hundreds of different experiments taking place each day. Over time what worked or didn’t work in the past is no guarantee for the future.

**Intent:** Is to make it as easy as possible for contributors to run scientific experiments. We want previous experiments to be shared, but with the contributor having the final say whether to proceed or not with an experiment. The principle also included our guidelines on what makes an experiment scientific.

# Internal Open Source

This is part 2 in a series of 3 posts

* Monoliths and Microservices
* A Blueprint for Internal Open Source
* Data Driven Inner Source

# SEE the world with us

Many of our employees have had the opportunity to take advantage of our Skyscanner Employee Experience (SEE) — a self-funded, self-organized programme to work up to 30 days during a 24 month period, in some of our 10 global offices. There is also the opportunity to work for 15 days per year from their home country, if an employee is based in an office outside of the country they call home.

Like the sound of this? Look at our current [Skyscanner Product Engineering job roles.](https://www.skyscanner.net/jobs/current-jobs/)

![]()

Look at our current [Skyscanner Product Engineering job roles.](https://www.skyscanner.net/jobs/current-jobs/)

# About the Author

Hi, my name is Chris Downey and thanks for reading my post. Here are some of my previous Skyscanner blogs :

* Are you having any Impact
* Getting ahead with an Agile approach to growth
* The culture of Growth squads in Skyscanner

[@chrisjdowney](https://twitter.com/chrisjdowney)

![]()

Chris Downey