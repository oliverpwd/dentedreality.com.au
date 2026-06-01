---
title: Taking the Mystery out of Scaling a Company
date: '2018-10-28T22:35:02-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://a16z.com/2010/08/02/taking-the-mystery-out-of-scaling-a-company/
---

[Taking the Mystery out of Scaling a Company](https://a16z.com/2010/08/02/taking-the-mystery-out-of-scaling-a-company/)  



> “What you got a dollar in your pocket  
> 
> A twenty in your wallet?  
> 
> See me I’m stacking money  
> 
> Matter of fact, I’ll let you watch it  
> 
> Get big  
> 
> Get big  
> 
> Get big  
> 
> Get big”  
> 
> —Dorrough, *[Get Big](http://genius.com/Dorrough-get-big-lyrics)*

If you want to build an important company, then at some point you have to scale. People in startup land often talk about the magic of how few people built the original Google or the original Facebook, but today’s Google employs 20,000 people and today’s Facebook employs over 1,500 people. So, if you want to do something that matters, then you are going to have to learn the black art of scaling a human organization.

Often board members give entrepreneurs two bits of advice regarding scale:

*1. Get a mentor.*

*2. Find some “been there, done that” executives who already know how to scale.*

These answers, while fine as far as they go have some important limitations. First, if you don’t know anything about scaling an organization, then it will be very difficult for you to evaluate people for that job. Imagine trying to find a killer engineer if you’d never written a single program. Second, many investor-board members don’t know anything about scaling a company either and can be suckers for people who have the experience but not the skills. If you’ve ever worked in a large organization, you know that there are plenty of people with experience running them, but possess none of the requisite skills to run them well.

The above advice is still good, but the right way to pick both the best mentors and best employees is by first learning the basics.

In this post, I will discuss the basics of scaling an organization. In doing so, I will lay out the fundamentals, but not go as far as writing a how-to guide. Hopefully, this will give you the context to apply the myriad of scaling techniques in the management literature appropriately. I will save for later posts more advanced topics such as:

*Managing senior people*

*Corporate politics and how to limit them*

*Systemic incentives*

*Incentive alignment*

*Hiring function heads for functions that you’ve never done*

*Re-organizing*

*Software system implementation and adoption*

## The Basic Idea—Give Ground Grudgingly

When an organization grows in size, things that were previously easy become difficult. Specifically, the following things that cause no trouble when you are small become big challenges as you grow:

*Communication*

*Common knowledge*

*Decision making*

In order to get a clear understanding of the problem, let’s start with the boundary condition. Imagine a company of one employee. That employee writes and tests all the code, does all the marketing and sales, and manages herself. She has complete knowledge of everything in the company, makes all the decisions, needn’t communicate with anyone and is totally aligned with herself. As the company grows, things will only get worse from here in each dimension.

Still, if the company doesn’t expand, then it will never be much of a company, so the challenge is to grow and degrade as slowly as possible.

There is a great analog to this concept in American Football. An offensive lineman’s job is to protect the quarterback from onrushing defensive linemen. If the offensive lineman attempts to do this by holding his ground, the defensive lineman will easily run around him and crush the quarterback. As a result, offensive linemen are taught to lose the battle slowly or *to give ground grudgingly*. They are taught to back up and allow the defensive lineman to advance, but just a little at a time.

When you scale an organization, you will also need to give ground grudgingly. Specialization, organizational structure, and process all complicate things quite a bit and implementing them will feel like you are moving away from common knowledge and quality communication. It is very much like the offensive lineman taking a step backwards. You will lose ground, but you will prevent your company from descending into chaos.

## How to Do It

At the point when adding people into the company feels like more work than the work that you can offload to the new employees, the defensive lineman has run around you and you probably need to start giving ground grudgingly. The first scale technique to implement is specialization.

### Specialization

In startups, everybody starts out as a jack-of-all-trades. For example, engineers write code, manage the build system, test the product, and, increasingly, deploy it and operate it. This works great in the beginning, because everybody knows everything and the need to communicate is minimized; there are no complicated hand-offs, because there is nobody to hand anything to. As the company grows, it becomes increasingly difficult to add new engineers, because the learning curve starts to get super steep. Getting a new engineer up-to-speed starts to become more difficult than doing the work yourself. At this point, you need to specialize.

By dedicating people and teams to such tasks as the build environment, the test environment, and operations, you will create some complexity—hand offs across groups, potentially conflicting agendas, and specialized rather than common knowledge. In order to mitigate these issues, you will need to consider other scale techniques like *organizational design* and *process*.

### Organizational Design

The first rule of organizational design is that all organizational designs are bad. With any design, you will optimize communication among some parts of the organization at the expense of other parts. For example, if you put product management in the engineering organization, you will optimize communication between product management and engineering at the expense of communication between product management and marketing. As a result, as soon as you roll out the new organization, people will find fault with it and they will be right.

Still, at some point, the monolithic design of one huge organization runs out of gas and you will need to split things into smaller sub-groups. At the most basic level, you’ll want to consider giving groups that you’ve specialized their own managers as they grow. You may want a QA manager for example. After that, things become more complex. Do client engineering and server engineering have their own groups or do you organize by use cases and include all technical components? When you get really big, you’ll need to decide whether to organize the entire company around functions (e.g. sales, marketing, product management, engineering) or around missions—self-contained business units that contain multiple functions.

Your goal is to choose the least of all evils. Think of the organizational design as the communications architecture for your company. If you want people to communicate, the best way to accomplish that is to make them report to the same manager. By contrast, the further away people are in the organizational chart, the less they will communicate. The organizational design is also the architecture for how the company communicates with the outside world. For example, you might want to organize your sales force by product to maximize communication with the relevant product groups and maximize the product competency of the sales force. If you do that, then you will do so at the expense of simplicity for customers who buy multiple products and will now have to deal with multiple sales people.

With this in mind, here are the basic steps to organizational design:

**1. Figure out what needs to be communicated** – Start by listing the most important knowledge and who needs to have it. For example, knowledge of the product architecture must be understood by engineering, QA, product management, marketing and sales.

**2. Figure out what needs to be decided** – Consider the types of decisions that must get made on a frequent basis: feature selection, architectural decisions, how to resolve support issues, etc. How can you design the organization to put the maximum number of decisions under the domain of a designated manager?

**3. Prioritize the most important communication and decision paths** – Is it more important for product managers to understand the product architecture or the market? Is it more important for engineers to understand the customer or the architecture? Keep in mind that these priorities will be based on today’s situation. If the situation changes, then you can re-organize.

**4. Decide who’s going to run each group** – Notice that this is the fourth step not the first step. You want to optimize the organization for the people—for the people doing the work—not for the managers. Most large mistakes in organizational design come from putting the individual ambitions of the people at the top of the organization ahead of the communication paths for the people at the bottom of the organization. Making this step 4 will upset your managers, but they will get over it.

**5. Identify the paths that you did not optimize** – As important as picking the communication paths that you will optimize is identifying the ones that you will not. Just because you de-prioritized them doesn’t mean that they are unimportant. If you ignore them entirely, they will surely come back to bite you.

**6. Build a plan for mitigating the issues identified in step 5** – Once you’ve identified the likely issues, you will know the processes that you will need to build to patch the impending cross-organizational challenges.

These six steps should get you pretty far. When we examine advanced organizational design, we’ll also need to consider trade-offs such as speed vs. cost, how to roll out organizational changes, and how often one should re-organize.

### Process

The purpose of process is communication. If there are five people in your company, you don’t need process, because you can just talk to each other. You can hand off tasks with a perfect understanding of what’s expected, you pass important information from one person to another, and you can maintain high quality transactions with no bureaucratic overhead. With 4,000 people, communication becomes more difficult. Ad hoc, point-to-point communication no longer works. You need something more robust—a communication bus or, the conventional term for human communication buses, a process.

A process is a formal, well-structured communication vehicle. It can be a heavily engineered six-sigma process or it can be a well-structured regular meeting. The size of the process should be scaled up or down to meet the needs of the communication challenge that it facilitates.

When communication in an organization spans across organizational boundaries, processes will help ensure that a) the communication happens and b) that it happens with quality. If you are looking for the first process to implement in your company, consider the interview process. It usually runs across organizational boundaries (the hiring group, human resources—or wherever the recruiter lives, and supporting groups), involves people from outside the company (the candidate), and is critically important to the success of the company.

Who should design a process? The people who are already doing the work in an ad hoc manner. They know what needs to be communicated and to whom. Naturally, they will be the right group to formalize the existing process and make it scalable.

When should you start implementing processes? While that varies depending on your situation, keep in mind that it’s much easier to add new people to old processes than new processes to old people. Formalize what you are doing to make it easy to onboard new people.

There is much written about process design, so I won’t repeat that here. I have found Chapter 1: The Basics of Production from Andy Grove’s High Output Management to be particularly helpful. For new companies, here are a few things to keep in mind:

**Focus on the output first** – What should the process produce? In the case of the interview process, an outstanding employee. If that’s the goal, what’s the process to get there?

**Figure out how you’ll know if you are getting what you want at each step** – Are you getting enough candidates? Are you getting the right candidates? Will your interview process find the right person for the job? Once you select the person, will they accept the job? Once they accept the job, will they become productive? Once they become productive, will they stay with your company? How will you measure each step?

**Engineer accountability into the system** – Which organization and which individual is responsible for each step? What can you do to increase the visibility of their performance?

## Final Thought

The process of scaling a company is not unlike the process of scaling a product. Different sizes of company impose different requirements on the company’s architecture. If you address those requirements too early, your company will seem heavy and sluggish. If you address those requirements too late, your company may melt down under the pressure. Be mindful of your company’s true growth rate as you add architectural components. It’s good to anticipate growth, but it’s bad to over-anticipate growth.