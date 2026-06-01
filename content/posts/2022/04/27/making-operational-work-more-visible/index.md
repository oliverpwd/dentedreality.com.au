---
title: Making Operational Work More Visible
date: '2022-04-27T19:35:49-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://github.com/readme/guides/ops-work-visible
---

[Making Operational Work More Visible](https://github.com/readme/guides/ops-work-visible)  



*“If I have seen further it is by standing on the shoulders of giants.”* – Sir Isaac Newton

### Chasing down a ‘blipperdoodle’

It’s 2019, back when I was on the CORE team at Netflix. I’m watching a teammate, the on-call site reliability engineer (SRE), investigate a spike in video playback errors reported by a number of smart TVs. The temporary spike lasted just a few minutes. But investigating these sorts of transient operational issues—“*blipperdoodles”* asthe team sometimes calls them—can reveal operational issues. It’s also good practice for the newer team members. The SRE on call happens to be new, so he digs in.

He looked at the error rates of relevant microservices, but none of them show a jump in service errors. Next, he checks to see if there was an operational change that lined up with the device errors. Did a new version of a microservice get deployed around the same time as the spike? Was there a config change that looks like it might be related?

There’s one potential candidate, a critical service that deployed right around the time of the error spike. The SRE reaches out to the service owner on call over Slack, who says she has not noticed any issues: The service metrics look healthy after the deployment. She notes that this service will be deploying in another region later in the day (deploys are staged by geographical regions to reduce the blast radius). When that happens, there’s no corresponding error spike. The correlation in time was just a coincidence. It’s a dead end.

Or is it? Another teammate digs in further. He brings up the generic performance dashboard for the service. There are over 40 graphs on the first tab of the dashboard, and there are multiple tabs. It’s a big dashboard.

In the 13th row, he sees a spike in retries for outbound traffic. This service was trying to call another service, and those calls were failing, so it was retrying. But the performance dashboard for the inbound service doesn’t show a concomitant increase in errors. That’s odd. What’s happening to those requests? Another teammate suggests graphing the retry metric by splitting it out by *node*. This is a cluster that has about 60 nodes in it, and all of the retries are coming from a single node!

### The invisible nature of our work

Most of the software engineering work that we do is invisible. Unless we’re pair programming, even our teammates typically only get small glances at our working processes. This invisible nature of work is even more true for operations. At least in software development, people see generated artifacts like source code and pull request comments. For operations, often the only visible aspect of the work is a set of Slack messages that go back and forth while we’re trying to remediate. The issue above was memorialized in a ticket, but that ticket has only a tiny fraction of the detail described above. It describes the final diagnosis (“*All errors were from one bad node*”), but not the process that got there.

This invisibility is a tragedy, because it robs us of the opportunity to learn from our colleagues. The best way to improve at a skill is through direct experience, but we can also learn from the experiences of others. To do that, we need opportunities to watch them in action, solving real problems*.*

### You build it, you run it

Netflix uses an operations model called “*you build it, you run it.*” The software engineers who write the services are also responsible for operating those services. This means they must be [full-cycle developers](https://netflixtechblog.com/full-cycle-developers-at-netflix-a08c31f83249), capable of doing both the development and operations work. This is different from the SRE model, where engineers who specialize in operations assume the responsibility of the operations work.

The advantage of “you build it, you run it” is that incentives align well. Traditionally, developers are rewarded for delivering new features, and operators are rewarded for keeping the system up and running. These are opposing forces. Developers need to change the system to deliver features, so they want to make as many changes as possible. But every change carries a risk that it could bring down the system, and so operators want to make fewer changes. When the same engineers are responsible for both development and operations, they are in a better position to make tradeoffs between these conflicting goals.

The disadvantage of “you build it, you run it” is that development and operations are separate skill sets. Companies that use this model traditionally focus on the development skill set when hiring, which means that the developers are likely to have much less operational experience than a traditional SRE.

This was certainly the case for me when I joined the company. I had some operational experience from previous jobs, but operations wasn’t my area of expertise.

### Onto the CORE team

Three years prior to the error spike investigation, I had been hired onto a different team at Netflix: the Chaos Team. This is the team that builds internal tools, like [Chaos Monkey](https://netflixtechblog.com/netflix-chaos-monkey-upgraded-1d679429be5d) and [ChAP](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f), which verify that Netflix can handle failures by injecting them directly into the production environment in a controlled way. It sounded so cool to me: building tools that intentionally cause failures in production! After being on the Chaos team for a while, what I discovered was that I was much more interested in natural failures than synthetic ones. It was the failures that happened organically that captivated me. I would spend my spare time reading through incident tickets trying to understand how failures happened. The problem was that the tickets didn’t have the kinds of detail I was looking for.

Because there wasn’t good historical information on incidents, I was looking to analyze the new ones. We had an infrastructure team that built tools, so incident analysis wasn’t their charter. If I wanted to devote time to this sort of analysis, I had to switch teams.

Even though software engineers are responsible for operating their services, it isn’t always obvious which service is the source of problems in the overall system, or there’s an interaction problem between multiple services, or both. To help handle these types of cases, there is a centralized incident management team at Netflix, called the CORE team, made up of SREs.

CORE is the team that “holds the pager for Netflix”: These expert incident responders get paged for significant issues. The CORE team doesn’t own any services. Instead, they help manage incidents, coordinating among the participants. Most importantly to me, CORE is responsible for follow-up work, memorializing the details of the incident in tickets and holding incident retrospective meetings (“IRs”) when warranted. This is the work I wanted to do. But, in order to join the team, I had to join the CORE on-call rotation. This meant I had to get better at operations.

### Ramping up on operations

CORE team members are very good at operations work. Specifically, they are experts at using the Netflix observability tools: navigating the various dashboards and running queries against the Netflix telemetry system, Atlas, to try to localize problems in the microservice architecture that made up the service.

Part of that work was simply becoming familiar with the dashboards and the Atlas query language. Beyond that, a lot of the work involved looking at signals and making judgments: looking at the shapes of graphs and when certain events happened, and following leads.

This type of work is very different from development work. For one thing, a lot of operations work takes place at a much higher tempo, especially when there’s an active or imminent problem. For another, a lot of the relevant experience is extremely local to whatever context you’re working on. You don’t just become an expert at operations, you become an expert in operations on a particular system. Yes, some of that knowledge is transferable to other systems, but a lot of it isn’t. Recognizing that the shape of a particular graph is “choppy,” and that isn’t right, is an observation that’s very context-specific.

This meant that new hires to the team, even with their years of SRE experience, had to ramp up in order to become effective at Netflix. The team employed a lot of explicit shadowing as a mechanism for onboarding new team members. They would start by explicitly shadowing an established team member. When an “interesting” event happened, the new members would typically crowd around the monitor of the on-call to watch what they did. That’s what happened with the device error spike.

### This week in operations

Because operations work is so often unseen, we need to put in additional effort to make it visible. Shoulder-surfing is a great way to do this, but in the age of remote work, this has gotten harder to do opportunistically. The open-office floor plan has many disadvantages, but it does make it easy to look over someone’s shoulder.

Every week, the members of the CORE team would meet for what they called the “weekly incident management meeting.” This was not an incident retrospective meeting; those sorts of meetings were scheduled ad-hoc, and involved participants from many different teams. The incident management meeting was only for members of CORE.

The team would use this time to talk through the handling of incidents over the past week. Was there anything particularly difficult? Any ongoing problems that other on-calls should know about? The meeting was an information channel that enabled the team members to share experience and context with each other.

I eventually left the CORE team for a more traditional software engineering team at Netflix. I was so taken with the weekly incident management meeting that I started running a weekly meeting on my new team called “This week in Managed Delivery Operations.” We discuss any interesting operational surprises from the past week, even if they had no customer impact.

Here’s the standing agenda for each issue:

* Brief recap
* How did you figure out what the problem was?
* How did you resolve it?
* Anything notable/challenging? (e.g., diagnosing, resolving)

My goal with this meeting is to create a way to retrospectively look over the shoulders of the engineers who dealt with the operational surprise, to have them walk the team through the surprise, how it unfolded from their perspective, what they saw, and what they did.

By providing a space for our colleagues to share these insights, we can learn from their experiences—and are all empowered to get better at what we do.