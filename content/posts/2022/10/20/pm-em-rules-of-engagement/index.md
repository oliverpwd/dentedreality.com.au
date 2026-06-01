---
title: 'PM & EM: Rules of Engagement'
date: '2022-10-20T07:30:17-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://segment.com/blog/product-manager-engineering-manager-rules-of-engagement/
---

[PM & EM: Rules of Engagement](https://segment.com/blog/product-manager-engineering-manager-rules-of-engagement/)  



Picture this: you just landed the Product Management (PM) job of your dreams. On day one, you meet your partner-in-crime Engineering Manager (EM) at your new gig. Before you know it, you’ve been assigned your first problem to solve. Now, it’s time to get to work.

Naturally, as you get started, you realize there’s actually a *ton* to work out. What exactly are we building? How are we going to build it? What’s the timeline? You schedule time with your EM to work out how to tackle these questions. In both of your heads, the same questions start to percolate: Should *I* be responsible for all of this? Maybe just some of it? Should everything be shared? What do we collaborate on vs. own individually?

*You may not* *realize it at the time, but getting this relationship right actually goes an incredibly long way in your future in shared product development, team building, accountability, and more.*

A strong PM & EM partnership is at the heart of all high-achieving software development teams. While the specific titles may be different in different-sized organizations, we’ve found that great software teams consistently need the same leadership ingredients. Too often, building this partnership is left to chance and months (or years) of trial and error. This seems short-sighted given its importance, so we encoded what we’ve learned into a guiding framework for how EMs + PMs can partner together.

We call it the **PM & EM: Rules of Engagement Framework**.

This was created as an internal document at Segment a year ago and it’s been incredibly well-received. It’s used by new PMs + EMs looking to build a successful partnership, by seasoned PM + EM pairs looking to debug specific responsibility and ownership issues, and by managers wanting to help their teams understand how to become better functional partners.

By sharing this framework publicly, we are optimistic that more incredible partnerships and software development teams can be built, not just at Segment, but across the industry.

The framework draws from the collective experience of myself,[Gerhard Esterhuizen](https://www.linkedin.com/in/gesterhuizen/),[Kevin Niparko](https://twitter.com/n2parko?lang=en), and Segment’s broader Product and Engineering teams. It is informed by the good, the great, and the most disastrous partnerships we’ve seen, both within and outside of Segment.

## The foundational rules

Good relationships between PMs and EMs are built on trust, joint accountability, and separate lines of ownership.

#### 1. **Trust**

If we could single out only one success factor in a PM & EM relationship, it would be trust.

Trust is the basis on which the relationship will live or die. With enough trust in each other, a pair can overcome every obstacle and jointly steer towards successful outcomes.

Without trust, the relationship will rarely deliver successful outcomes. No amount of process or documentation of roles and responsibilities will overcome the need for a partnership grounded in trust. The more trust you have, the less time and effort you’ll need to spend on aligning on the rules of engagement.

#### 2. **Joint accountability**

In a software business — like Segment — Engineering and Product leaders decide on the most important problems to solve to drive the business forward.

As the leaders of the development team that actually build the software, the EM and PM are responsible for delivering products that solve these problems. Together, they have the latitude to adjust course as they learn from customers, redefine the problem, grapple with the technical solution, etc. But at the end of the day, the company holds both accountable to the outcomes of the team. They succeed and fail as a unit.

#### 3. **Separate ownership**

A clear separation of functions means that the PM and EM retain individual and final authority over particular decisions.

Although they should jointly discuss the various trade-offs involved in a decision, each decision has a single owner. You may be wondering — why is separate ownership so important if there’s a deep sense of joint accountability? Can’t you own these decisions together as a pair?

Theoretically, this sounds great, but in practice, it creates confusion, slows teams down, and leads to worse decisions. **When everyone is responsible for a decision, no one is responsible for a decision.** You want the person with the most context to own the decision and the outcome of the decision.

Of the three foundational rules, separate ownership — and specifically working out who owns what — is the least intuitive.

That’s why we’ve chosen to focus the meat of this article on:

* **Defining ownership areas**: What are separate ownership areas, what do they mean, and what are examples?
* **How to show up as a great owner and partner**: What behaviors can you implement today?

## **Defining ownership areas**

There are several key decisions needed to build successful products.  

Each can be owned by either the PM or the EM, and the owner should take responsibility for getting their partner’s input and alignment on key decisions.

Here’s how we break them down at Segment:

![](https://images.ctfassets.net/i8bfc4nr05rq/eElXkp5uT1jFtkev0bVfd/d3707eb1859acfa31a9348be7b1bafb9/Zz-MZbj9.png)![](https://images.ctfassets.net/i8bfc4nr05rq/eElXkp5uT1jFtkev0bVfd/d3707eb1859acfa31a9348be7b1bafb9/Zz-MZbj9.png)

#### **Why?**

##### ***Owned by the PM.***

The “Why?” question is at the heart of our Product vision and strategy. Why are we working on this area? Why is this a problem worth solving? What change are we as a team hoping to produce in the world?

*Example: Let’s say our business needs to expand into the healthcare industry to support its revenue growth goals. To purchase our software, all healthcare companies* *require* *that the product is HIPAA compliant, which it isn’t today. No HIPAA, means no revenue from healthcare, means not hitting our growth goals.* 

Answering this question of “Why?” with conviction requires a strong understanding of the needs and wants of our customers (present and future), the market direction, the overall business strategy, as well as a deep understanding of the current product. The importance of the vision and strategy fueling the team can’t be underestimated. It’s what gets teams through the hard times and is what the company ultimately measures success against.

Developing the vision and strategy is the job of the PM. But true success is when the whole team clearly understands and contributes to this narrative. A team that understands and is bought into the direction they are heading will get there twice as fast, and chances are the end product will be much higher quality too.

#### **What?**

##### ***Owned by the PM.***

The “What?” relates to the specific features or products that a team is planning on releasing. What are we building to solve the problem we have pinpointed in the “Why”?

*Example: We need to build HIPAA compliance into our product ASAP to hit our growth goals as a company for the year.*

The “What?” goes beyond the basic functional requirements (we need to be HIPAA compliant), and into the specific requirements of a product to be ready for general availability (what specifically needs to happen for us to be HIPPA compliant). These details are critical to inform the key decisions the EM must own like “When?” “How?” and “Who?”. More on these below.

The “What?” and the “Why?” are best encapsulated in a PRD — a Product Requirements Document.

Every Product organization uses a slightly different template or acronym, but this is a detailed document that covers the problem the team is trying to solve, in addition to the required capabilities, the rollout plan, design, metrics of success, and many other important details.

#### **How?**

##### ***Owned by the EM.***

The “How?” defines the technical solution which delivers the stated requirements in the PRD.

This is codified in the Solution Design Document (SDD), along with the “Who?” and the “When?”. Similar to a PRD, this document may have a different name in your company. Though all three areas — “How?” “Who?” and “When?” — are distinctly important decisions, the solution a team ships is very tightly coupled to who builds it and when it will be available.

As such, it’s common to decide these at the same time, after close collaboration and iteration with the PM and the broader Engineering team.

*Example: There are three viable paths for the team to build HIPAA compliance into the product:* 

* *Option 1: Integrate with a 3rd-party HIPAA compliance tool. It’s expensive, but we can do it quickly in 3 months.*
* *Option 2: Build compliance into our existing systems. It’s inexpensive, but it introduces more tech debt and it takes 6 months.*
* *Option 3: Rewrite key systems to allow for HIPAA compliance and remove tech debt. It’s inexpensive, but takes 8 months.*

To decide which option to choose, the EM needs input from the PM on things like the cost and timeline sensitivity of the organization. However, to choose the optimal solution, we need to look beyond the stated requirements and consider the architecture of the solution and its impact on:

1. **Dev velocity**: a particular architecture can make certain types of changes easy while inhibiting other types.
2. **Dev experience**: certain architecture decisions influence the experience the engineers have when building and interacting with the solution (e.g. amount of manual steps when deploying a small change).

Not adequately considering the above leads to the accumulation of technical debt.  

The EM is the ultimate custodian of this technical debt and brokers the conversation between the PM and the engineers. Together, these factors require the EM to have the final say on the “How?”.

#### Who?

##### ***Owned by the EM (and often causes the most PM/EM tension).***

The “Who?” question answers which engineers will lead the project to deliver the agreed-upon solution (“What?”) by the timeline decided (“When?”). This is codified in the SDD.

*Example: If we pursue Option 1, the required team is Albert, Vanessa, and Sarah. If we pursue Option 2 the required team is Alan, Osama, Tracy, Albert, Vanessa, and Tatiana.* 

On the surface, this looks like an easy decision to the PM. Just pick the next engineer(s) with the relevant skills to get started on the project. If we were purely optimizing for short-term product velocity, this might be a reasonable approach.

But there are other constraints that an EM needs to balance. Career development, team dynamics, work-life preferences are all factors that need to be weighed in staffing a project, and contribute to the long-term success of the team.

#### **When?**

##### ***Owned by the EM (based on trade-off conversations with the PM).***

The “When?” question answers the date by which we can expect a shipped feature or solution. Shipped here means that it is available to the relevant subset of customers (e.g. pushing a feature to beta availability for a limited subset of customers).

*Example: According to the options outlined above, there are three possible timelines. Option 1: 3 months; Option 2: 6 months; Option 3: 8 months.*

Although the timeline decision is owned by the EM, it’s a close and iterative collaboration with the PM. In the example above, you can see both options have different timelines. To make the decision in the example above, the EM will require the PM to weigh in on the relative importance of speed vs. cost, which is business context they likely won’t have.

## **How to show up as a great owner & partner**

Now that we know the different ownership domains, how can you best partner as PM & EM?

While there are many behaviors we could highlight here, we asked Segment’s PMs and EMs to share the most consistently valued behaviors from both sides.

#### If you’re a PM, your EM needs you to…

* **Build a compelling roadmap to build a motivated team:** Clearly communicating what the team needs to build and how it ties to the company goals is critical to motivating your existing team, and recruiting new folks to join! It also helps the Engineering team understand longer-term technical needs so they can plan thoughtfully.
* **Clarify priorities to help the Engineering team stay focused:** There will always be tons of competing priorities. You need to quickly and confidently help the team decide the most important thing to focus on. Doing this well requires clear and logical explanations your stakeholders can understand.
* **Define an MVP to allow quick shipping:** Decide what is “good enough” to ship to customers, cutting anything that isn’t absolutely required. This kind of scoping helps the Engineering team get things out the door as fast as possible with great momentum, leaving time for iteration after the first release.

#### If you’re an EM, your PM needs you to….

* **Deliver a predictable development process to inspire trust with customers and the company:** At the heart of any high-functioning team is the ability to efficiently and predictably build software. Our customers and internal teams are often reliant on the release timelines we share. Meeting or beating these deadlines inspires confidence. Missing them erodes it.
* **Drive the technical vision for the team to avoid mountains of tech debt:** The EM needs to own the active prioritization of stability, scalability, and developer experience work. The PM rarely has a full line of sight into these issues and their impact on the team or customer, so relies on the EM to represent this perspective during planning.
* **Keep the development process sane so stakeholders know how projects are tracking**: EMs are responsible for the development process on the team. For team members, this means maintaining a good planning system that helps folks understand who is doing what and when. Ideally, the system can also be used by stakeholders in other teams to track the status of projects or bugs they’re tracking.

We hope that this has provided actionable ways to build and keep a healthy PM and EM relationship. Let us know how it goes!

*Contributors: A big thank you to the many members of the Segment Product and Engineering organization who contributed, edited, and refined this framework including Kevin Garcia, Lauren Reeder, Albert Strasheim, and Hareem Mannan.*