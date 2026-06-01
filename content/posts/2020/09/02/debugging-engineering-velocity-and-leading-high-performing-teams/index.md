---
title: Debugging Engineering Velocity and Leading High-Performing Teams
date: '2020-09-02T22:40:06-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://leaddev.com/debugging-engineering-velocity-and-leading-high-performing-teams
---

[Debugging Engineering Velocity and Leading High-Performing Teams](https://leaddev.com/debugging-engineering-velocity-and-leading-high-performing-teams)  



## Problem

You have a solid set of engineers, you’ve embraced OKRs and Agile, you’ve got standups, and you also do Sprint planning and retrospectives. But have you still felt frustrated by your team’s speed of execution? Have you asked yourself, perhaps in the middle of a Sprint planning session, *are we stuck*?

Why do some teams seem to work faster than others? Why do some people perceive a team as too slow, while others think the same team is working at a good pace? And why do engineers on some teams appear to be more satisfied and more motivated than those on other teams?

When debugging slowness in engineering execution a naive view is to ship faster, but speed is only one component. In this article, I’ll define engineering velocity in terms of shipping software with precision, speed, quality and impact. What are you shipping and why? How frequently are you able to ship? What is the failure rate or quality of your software? What is the impact of your software on the goals you are trying to achieve?

I don’t believe engineers lack motivation, I believe it is the systems that fail to create an environment for engineers to make magic. So instead of looking at engineering velocity as an individual problem, I’ve found it useful to apply the systems-thinking lens[[1]](#ipfootnote0) to identify the set of interconnected elements, their relationships, and its function or purpose. But how does one debug these systems?

I’ve experienced a wide variety of engineering velocities and shipping styles, and worked across various cultures; from an enterprise release every two years to deploying multiple times a day at a software native company.

In this article, I’ll share how to recognize problems surrounding engineering velocity, why it is important to solve them, and present a step-by-step guide for managers and ICs to ask the right questions towards identifying the systems in which skilled, motivated engineers thrive.

We’ll cover guiding policies around the planning, execution and delivery phases of software development, and the specific actions to take for each.

## Why is engineering velocity important?

The theory of intrinsic motivation at an individual level talks about competence (the ability), autonomy (choice and independence to pursue interesting work), and purpose (why does it matter?). We’ll assume you have solved the hiring problem and built an inclusive team that has at least 5–8 highly skilled engineers with the right domain expertise and career goals. The team is set up for success, with its own charter that has a lack of overlap between existing teams to ensure that it isn’t fraught with conflicting interests. We’ll also assume that your management and leadership practices lean toward a healthy culture which provides the right blend of growth mindset[[2]](#ipfootnote1), radical candor[[3]](#ipfootnote2) and psychological safety for individuals to thrive. So competence and autonomy are more or less solved, but how do you then address *purpose,* and how does engineering velocity fit into solving for this; the northstar, the *why*?

## How can you identify the problem?

The first step in debugging is to diagnose the potential engineering velocity problem. Your team is working hard, and shipping *something* at a regular cadence. However, you are seeing certain markers at your team or a broader organizational level. Some questions you could ask are:

* Is the metric that you and the team are accountable for in line with the business goals?
* Are you hearing discontentment or lack of engagement in your regular 1:1s?
* Does the team feel unsure of the impact they are driving?
* Are you seeing unexpected or regretted attrition on your team?
* Is the broader organization questioning the value of your team? Are you seeing some of this manifest through shrunken headcount or budget allocation, lower buy-in into the promotion nominations of your senior engineers, or in general, lower trust in the team’s ability to meaningfully move the needle?
* Is your team feeling stagnant, in terms of growth and recognition?

If you answered *yes* to one or more of these, it is time to debug the function or purpose of your system.

## How do you debug the problem?

Identify the phase of your software lifecycle – planning, execution or delivery. At each of these phases, there are different higher order objectives to aspire for, and different challenges to overcome.

### Planning

#### **Alignment**

*Why should your team exist? Is the problem worth solving for? What do you not want to solve?*

The most crucial element of developing organizational trust and credibility is to first seek alignment on what the team is trying to deliver. Seeking early organizational buy-in to what the team owns (and doesn’t) will also help situations where context could be lost in translation across the management hierarchy.

To do this, identify a northstar metric in line with the business requirements, and set an aspirational target. For one of the teams I manage, our charter was to optimize our company’s overall AWS costs. We defined our metric as ‘AWS efficiency’, measured in terms of growth in AWS spend indexed to our growth in business. This helped gain wider sponsorship into the broad cross-organizational metric which my team only partially had control over. It was also important for us to be aware of broader company-wide priorities and constraints and to understand the extent of our agency in driving to those targets. Owning a company-level metric for a problem that the business deemed important and setting expectations upfront through targets set up the team for future success.

Another side to setting expectations is to clearly establish what you *don’t* want to be responsible for. One of my teams did routine engagements (4–6 weeks long) with other engineering teams to understand the gap in our tooling and establish a pattern of typical user asks. We soon got perceived as a body shop of readily available engineers who’d show up for the grunt work. However, when we sat down as a team to identify our charter and the things we wanted to provide and accomplish, this was not it. So we listed out our vision, outlining what we would (and wouldn’t) own, driving with explicit exit criteria for technical debt reduction or ‘n’ engagements for educational purposes. After a few back-and-forths with the broader organization, we arrived at a healthy balance where the team could exercise our autonomy while ensuring business success.

#### **Prioritization**

*Are you building the right thing? And for whom?*

Some teams (e.g. infrastructure) have a very wide scope, and such teams often hear consistent concerns that a certain set of users are unsatisfied which can be extremely demotivating to engineers. This is a typical prioritization problem. It is better to have 10 delighted users than to have 1000 partly-satisfied users, and this applies whether your users are internal or external.

To better assess which users to focus on, we sampled different cohorts and cross-checked our assumptions with senior leaders. We prioritized a specific cohort, conducted interviews with them to understand their thoughts, and prioritised their needs. This helped us assess how to manage user asks across various cohorts, and also understand who viewed us as being “stuck”. We consciously made some hard decisions. The lack of dilution of our effort and consequently, feature behavior, also had an unexpected result. It enabled us to make those focused sets of users extremely awesome at what they did, with the tools we shipped, leading to increased adoption, and in some cases a migration of certain users into this focused cohort. (Kathy Sierra talks a lot about this in her book ‘Badass – Making Users Awesome’[[4]](#ipfootnote3))

If you are aggressive about prioritization, then you must also be willing to change priorities and adapt, otherwise you can lose sight of what’s important. There could be times when your team isn’t in full control of your priorities, or it may be over-indexed on the wrong metrics or feeling thrashed about on account of changing metrics. This can sometimes cause engineers to lose faith in the system: “if you keep changing what’s important, is it even important?”. Big and frequent changes in priority can demotivate engineers and make them take the priorities themselves less seriously. But such change is a reality in a fast-growing company. How do you reduce the feeling of being ‘thrashed about’ as well as increase adaptability to change? Train engineers to adapt and to expect goals to change. Understand that metrics can be an imperfect tool to achieve tactical or strategic prioritization. Evaluate if the set of metrics is accurate and measuring what’s truly needed. From there, develop the right feedback loops to iterate and validate your metrics.

### Execution

Once you’ve identified the “why”, and “what”, it’s time for “how”. Dr. Nicole Forsgren et al.[[5]](#ipfootnote4), highlight four metrics to track high performing and productive teams to help track the “how”:

* Lead time: the time taken from code committed to running in production
* Change rate: frequency of deployments to production
* Failure rate: frequency of deployment failures needin rollback, fixes, etc.
* Mean time to recover: average time to recover from a failure

#### **Focus**

*Are you building or doing too much? Are you doing too little?*

Every few Sprints, at the time of planning, evaluate if the team is doing too much at any given time. Is the team keeping too many projects active at the same time? Does the team have a tendency to ship multiple different projects or features around the same time?

If so, reduce your WiP (work in progress). This is easier said than done, and it creeps up on me every so often even though I’m aware of this problem’s existence. Some of the tricks I use include setting explicit goals for every Sprint in terms of deliverables; using colors to represent logical units of work, and keeping an eye out for an unusually colorful Sprint (if this occurs, drop a few colors *aggressively*). A good metric to track for your features is *lead time*, which we can expand to include time taken from planning and scoping a feature, to shipping it to your focused set of users.

#### **Need for speed**

*Are you blocked on yourself, other teams, or lack of support? Build it first, then make it better.* 

**Unblock:** There are often times where you can be blocked by your own team, on other teams, or due to lack of tools and support.

* **Establish team norms and roles:** Are you seeing conflict between certain engineers on your team? Is the team unsure of who needs to make a certain decision? Enable effective team communication and collaboration through codified norms, around how individuals work with each other. Enable decision-making and transparency, by setting expectations around roles and responsibilities for those working on the project — leverage a venn diagram for shared responsibilities and a RACI (Responsible, Accountable, Consulted, Informed) framework for who’s doing what on a project[[6]](#ipfootnote5).
* **Managing technical debt:** For your hosted service, is your page load unsustainable? Are the support tickets piling up? Is your service implicated frequently in incidents? To manage technical debt or the “keep the lights on” kind of work, I’ve used run rotations or padding in Sprint deliverables, depending on the shape or extent of the work. If technical debt is creeping up, it is important to assess cost-benefit analysis of solving it now and to sacrifice temporary speed over a longer-term increase in velocity.
* **Tightly aligned, loosely coupled:** Are you blocked by other teams to ship your software? If so, establish loose coupling in your software abstractions and seek alignment with said teams through service level commitments, e.g. the latency and throughput required to support a scale of ‘n’ requests per second. Or is inter-team collaboration slowing you down and negatively impacting your individual autonomy? Organization redesign or re-orgs are a tool at your disposal (though this is a heavy hammer which can impact many individuals, so wield it sparingly).
* **Lack of tools:** You could also just lack some tools or systemic, dependendable provisions to tap into, e.g. a continuous build and delivery system. In these cases, surfacing the impact of the lack of such support to leadership, early and often, is your only recourse.

**Iterate:** Some engineering velocity problems simply manifest because some projects are naturally slow projects and take a long time (e.g. building a database abstraction interface), and this is especially true for infrastructure work. In this context, it’s important to develop a product mindset to build infrastructure and demonstrate value early. Engage with users and go deep (before going broad) by picking 1-3 specific-use cases. Do those extremely well and iterate. Then, go back to the selected user cohort to validate what they care about and see if their needs are met. After that you can go broad by prioritizing work that enables highly automated migration or faster onboarding.

**De-risk:** Are you dealing with inherently complex problems which run over multiple years (eg: migrating from a monolith to a service-oriented architecture)? Managing such projects requires adding incremental value, and uncovering unknown unknowns at each stage. Obtain enough data to be able to (re)evaluate next steps, and reduce future risks, while having meaningful impact. Eg: building a prototype of a service which can work extremely well on one server, with the potential to scale over more, in future iterations.

For all these, you can use ‘*change rate*’ as a metric to track your ability to ship software.

#### **Quality**

*Does it work as you need it to?*

If precision ensures that you’re solving the right problem, and speed confirms you are, quality is what keeps you accountable. ‘*Failure rate*’ (how often are breaking changes introduced) and ‘*mean time to recover’* help assess the overall quality of your work.

Having started as an automation engineer, I’ve come to deeply value the importance and predictability that can come with a focus on quality. One of the enterprise products I led had a typical release (to customers) of 1–2 years with a waterfall delivery model. Assessing the typical failure points of this product and the interfaces most suited to integration scale issues, I frontloaded most of the scale and performance testing toward the beginning of the development process. We were able to ship key features within 5 months as a result of this shift.

### Delivery

#### **Impact**

*It’s ‘Done’ and ‘Shipped’ – But are folks using your stuff? Are you actually seeing movement toward your northstar?*

Remember, you had started off by deciding whether it was worth solving the problem that you have now developed the software for. So this is your time to cash in. Go back to the metrics identified in the planning phase and evaluate how shipping the code has impacted those. You’ll also find that this exercise can be extremely gratifying and energizing as you see the metrics move as a result of your work. Quite recently, we shipped some work expecting to see change, and moved onto solving other problems. Looking back retrospectively at the last six months, we realized that we had needed to build adjacencies to the shipped work to actually capitalize on all the effort. Sometimes, you need to evaluate what the last 5–10% looks like to realize the most impact; this could be a marketing strategy, a small UX improvement or a small optimization (e.g. making load times much faster).

Lastly, I’d be remiss if (as an engineering leader) I didn’t call out ineffective management. We need to hold senior engineers and managers accountable for building and driving engineering velocity and leading high performing teams. And if they are not working out then it is time to let them go, as hard as that may be. I worked on an enterprise release which had consistently slipped severalquarters and then *years* of delivery. This was because one of the managers was fairly new to engineering management, and didn’t demonstrate a growth mindset. Due to the inaction in addressing this, the company canceled the whole project after years of huge engineering investment. As organizational leaders, it is our responsibility to provide the right, timely, actionable feedback to help individuals course-correct and avoid downstream pitfalls.

## Conclusion

Quite recently, one of my teams shipped Solis, a user facing canonical cost dashboard to give teams observability into their AWS costs. We aligned with our leadership, prioritized product teams at Stripe over Finance & Strategy (F&S), and iterated with a few users before broadly making it available. We made noise about it at our All Hands and engineering org meetings, and we even made it a mandate for teams to talk about their costs for their quarterly business review metrics. A couple of quarters down, we are now seeing an organizational awareness into respective AWS spend, which we didn’t have a year ago. Our northstar metric of AWS efficiency is at its target, and F&S has a clear line-of-sight into business drivers.

Debugging engineering velocity requires analyzing the broader system you operate in, its various components and their interconnectedness. To summarize:

* At planning stage, drive precision through early organizational alignment, and prioritization of user cohorts
* During execution:
  + Drive speed through focus, iteration, unblocking and de-risking your projects
  + Drive quality through early and rigorous testing
* For delivery, drive impact through realization of adjacent work streams (even outside engineering).

As a manager or lead developer, you now have a playbook to analyze and work on your team’s engineering velocity, and ultimately, to create an environment where people work together at their highest potential.

1. [1]
2. [2]
3. [3]
4. [4]
5. [5]
6. [6]