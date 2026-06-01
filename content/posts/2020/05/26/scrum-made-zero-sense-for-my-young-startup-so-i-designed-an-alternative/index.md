---
title: Scrum Made Zero Sense for My Young Startup. So I Designed an Alternative.
date: '2020-05-26T00:08:01-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://builtin.com/software-engineering-perspectives/scrum-startup-alternative
---

[Scrum Made Zero Sense for My Young Startup. So I Designed an Alternative.](https://builtin.com/software-engineering-perspectives/scrum-startup-alternative)  



Nowadays there are more opinions on how to develop software than there are firms actually doing the development. Some people call programming a science. Others call it engineering, a craft, or even art. Just as coding’s 70-year history has produced hundreds (if not thousands) of languages, it’s also spawned countless processes and frameworks purporting to have the best model for guiding a team to build software.

In recent times, no framework has seen broader adoption and more hype than the scrum implementation of agile. Agile — at its core — is very simple: a focus on collaboration, functionality, and flexibility over formality, documentation, and extensive planning. But just like software development overall, there are more variations on agile than you can shake a stick at. Scrum, one such variant, has proven very popular.

Since co-founding 4Degrees three years ago, I have spent a lot of time with my team working out what software development process would work best for us. Agile overall makes a lot of sense: It ensures that we’re talking to customers, collaborating internally, and staying nimble; it’s a good match for our core values. Scrum, on the other hand, really didn’t match our needs very well. While scrum may be perfect for many organizations, we found that it didn’t suit us — and likely isn’t a good fit for most other startups either.

## Roles

In scrum, there are three distinct roles: the product owner (who decides what features should be prioritized), the technical team (who actually builds the product), and the scrum master (who coordinates the process). Right from the get-go, this division of labor didn’t make sense at 4Degrees. In the early days, we didn’t even have that many people on the team, much less all devoted to a specific type of functionality development. My co-founder, Ablorde, and I decided early on that we would share the role of product owner in the organization. But I was also doing most of the actual programming. If we were to have a scrum master, that probably would have fallen to me as well. Clearly it didn’t make sense for me to be *all three* of the distinct scrum roles.

We decided to set up our team a bit differently than the scrum structure. Ablorde and I still share product owner responsibilities, though our ultimate goal is to bring in a head of product (similar but slightly different from scrum’s product owner, which is often tied to the business in some other official capacity). We envision the head of product and the other people in the “product” organization as playing the role of both product owner and scrum master: coordinating across engineering, design, sales, marketing, and everyone else to figure out what features should be prioritized and then bringing the team together to execute.

## Speed

Oftentimes, scrum is thought of as a very fast-paced framework for software development. And indeed, when shifting from a waterfall process with six-month-long development cycles, then deploying every two weeks feels like lightspeed. Not so in the startup world. When you’re just getting started, you might be a completely different company in two weeks. Planning to update your production application only twice a month is a recipe for disaster and unhappy customers. At 4Degrees, we deploy *much* more frequently: typically two to five times per day. That allows us to get out important updates quickly and divide work into more atomic units with fewer dependencies. Accordingly, we do not use any formal “definition of done” — tasks are “complete” when they’re live in production and at least modestly tested.

Accordingly, we don’t structure our product development cycle into “sprints,” one of the most fundamental components of scrum. The idea is to have the full team focus on one problem for a set period of time (most often two weeks). That just didn’t work for us; we couldn’t take two weeks to put out new functionality, and many times, it just doesn’t make sense to have the whole team focused on one set of tasks. Our back-end engineer may be doing some data science experimentation at the same time as our designer is conducting user interviews for some potential new functionality slated for weeks down the road.

Instead of sprints, we structure our development cycles into one-week and one-quarter increments. Every Monday morning, we check in to hear the latest on what customers are saying and prioritize/discuss the tasks that the team will be working on for the week. The meeting helps everyone stay up to speed on what’s happening, but it’s not the end-all-be-all: Tasks and priorities often shift over the course of the week as we continue to talk to customers and iterate on the code we’ve deployed.

In addition to our weekly cadence, we take a step back once a quarter to think about our platform a little more strategically. We analyze our customer insights and brainstorm major initiatives that may improve the project. That effort results in a roadmap of new functionality for the quarter. That roadmap is often more aspirational than realistic: Changing information and capacity over the quarter mean that oftentimes half of the roadmap won’t be completed on time. But that’s OK, it still provides us a path to follow to make sure the platform is headed in the right direction.

## Tasks

The structural differences between our process and scrum manifest in a very different approach to how work is organized. Scrum prescribes epics, stories, and tasks to ensure that the customer perspective is translated into functionality. Stories (“As a user, I need…”) have become an infamous hallmark of scrum, and even agile more broadly.

At 4Degrees, all technical work is simply recorded as tasks: line items in our Airtable database. Customer centricity is the first of our five corporate values and is deeply integrated into our process. As such, we haven’t seen any need for artificially wording tasks as if they’ve come straight out of the mouth of a specific user.

Rather than relying on team consensus for bringing tasks into a sprint, we use a centrally determined priority and point value. Specifically, whenever a new task is added, I will assign that task a priority and point value. Higher priority tasks are sorted to the top of the task tracker and provide a slight bump to the “raw” point value of a task. Point targets are set and measured at the individual level rather than the team level. We’ve found that this works better because our team is so small and relatively divided in its responsibilities. We have a front-end engineer, a back-end engineer, a mobile engineer, and a designer; each of these team members has relatively little ability — much less desire — to guess the points that a task should be worth to someone else on the team.

## Do What Works

Due to scrum’s popularity, many practitioners have forgotten that the agile manifesto says “individuals and interactions over processes and tools” and “responding to change over following a plan.” While scrum works for many organizations, it has been force-fed to all startups, even when it’s far from ideal.

The most important concept to take from agile is being quick and responsive to things that don’t work. For many startups, the overly structured and relatively slow nature of scrum just doesn’t make sense. Instead, they’ll be better served by taking a faster, more iterative approach to experimenting and figuring out a software development process that is best suited to their specific needs.

Expert Contributors

Built In’s expert contributor network publishes thoughtful, solutions-oriented stories written by innovative tech professionals. It is the tech industry’s definitive destination for sharing compelling, first-person accounts of problem-solving on the road to innovation.



[Learn More](https://builtin.com/contributors)