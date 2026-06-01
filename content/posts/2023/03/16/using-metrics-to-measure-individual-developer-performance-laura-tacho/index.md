---
title: Using Metrics to Measure Individual Developer Performance — Laura Tacho
date: '2023-03-16T21:19:41-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lauratacho.com/blog/using-metrics-to-measure-individual-developer-performance
---

[Using Metrics to Measure Individual Developer Performance — Laura Tacho](https://lauratacho.com/blog/using-metrics-to-measure-individual-developer-performance)  



*“What metrics should leaders use to measure the individual performance of developers on their teams?”*

I get asked this question a lot. I’ve asked myself this question before, too – both as a developer and then later as a leader.

A lot of research and “best practice” will tell us that metrics like lines of code, story points completed, or deployment frequency are not appropriate to measure individual performance. This is true. These metrics came out of research and studies to measure different things, like devops maturity, software delivery capability, and overall delivery performance. Applying them to individuals is unfair at best.

But here’s the question we don’t talk about enough:

*“What data are you going to use to evaluate my performance?”*

This is the question that really counts — coming directly from your team members. There’s a better answer than “best practice says not to use metrics,” which doesn’t spark a lot of trust in a fair performance review.

So if not metrics like PRs and commits, then what? I’ll break down arguments against using common metrics to measure performance of individuals, and then walk you through how I approach developing an evidence-based performance management system.

#### Software is written by teams, not individuals

Even if a feature or component is owned by an individual, it’s likely that their code depends on systems written by others. This is the main reason why applying team-level metrics to an individual is unfair. An individual cannot fully control their performance within a system where they are just one contributor. If the metrics aren’t satisfactory, they need to be addressed on a team or system level, not an individual level.

Additionally, team practices can vary widely. Lines of code, story points completed, and deployment frequency are examples of team or system performance metrics that are sometimes applied to individuals. And here’s another layer of trickiness: how can you fairly and effectively measure individual performance when teams have different estimation practices? For example, what might be a 3-point story to one team is a 5-point story to another. So is the individual on the team who calls it a 5-point story a better performer, because they close down more points?

Along with this, we often measure the wrong metrics altogether; that is, metrics that we think will give us a strong indication of performance, but have low correlation to impact and outcomes. Abi Noda, CEO and co-founder of DX, talks about the “Flawed Five” metrics that will lead you astray, both on a team level but especially on an individual level: [The elusive quest to measure developer productivity – GitHub Universe 2019](https://www.youtube.com/watch?v=cRJZldsHS3c)

#### Wrong metrics mean losing trust

But is it harmful to use these metrics in order to get a “close enough” understanding of individual performance?

Yes.

A fast way to reassure your team that you don’t understand their job is to pick what they perceive as arbitrary and unfair metrics to measure their performance:



> A friend’s org (at bigco) has decided to track these metrics to track IC productivity:
> 
> – number of jira tickets closed  
> – number of changes pushed  
> – number of comments on code review
> 
> I predict a round of promotions for some very simple python scripts
> 
> — Adam Leventhal (@ahl) [January 24, 2021](https://twitter.com/ahl/status/1353452565770366976?ref_src=twsrc%5Etfw)



Aside from losing trust in you, your team will be concerned about the implications of these metrics. If I pair with someone and therefore don’t commit the code myself, am I penalised? What if I’m working on a design document or coordinating a release? Responsibilities of developers often go beyond data that can be scraped from GitHub. You don’t want metrics that encourage the wrong behaviours.

#### Gaming the system?

Do you know about New York subway dogs? The NY metro banned dogs from the subway, unless they can fit in a bag. It’s not hard to imagine what happened next.



> MTA only allows dogs on Subway trains if they fit in bags. 🐶😀😀😀 [pic.twitter.com/sIIBBc9CmD](https://t.co/sIIBBc9CmD)
> 
> — Tamara Torres (@tamaratorresnyc) [September 16, 2019](https://twitter.com/tamaratorresnyc/status/1173387736180412417?ref_src=twsrc%5Etfw)



Humans are wired to maximise incentive, and also we are pretty creative. I’m not suggesting that your teams will intentionally start to game the system when it comes to improving these metrics. But it might happen, both as a function of self-preservation, but also because you picked the wrong metrics to begin with.

[Goodhart’s law](https://en.wikipedia.org/wiki/Goodhart%27s_law) states that when a measure becomes a target, it ceases to be a good measure. If you measure a factory based on weight output, expect heavy products. If you measure it based on the number of items produced, expect tiny, tiny products. A practical example: if the number of commits is a target for individual performance, expect to see some very dirty git histories. You’d probably do the same thing.



![](https://images.squarespace-cdn.com/content/v1/60aa35591e471f054bc53f9c/f0043cb4-3f62-47c2-94f3-0e2d3d878661/GoodhartsLaw.png)![](https://images.squarespace-cdn.com/content/v1/60aa35591e471f054bc53f9c/f0043cb4-3f62-47c2-94f3-0e2d3d878661/GoodhartsLaw.png)






Another danger comes from metrics that encourage behaviours that have a negative impact on your business. They punish desired behaviour while incentivising damaging behaviour.

* Code coverage is a target, so development hours are spent on writing more tests, but the Change Failure Rate stays the same
* More story points are pushed out, but maintainability suffers
* Your team hits aggressive deadlines, but ⅓ of the team resigns within 2 months
* More PRs are closed, but you’re not acquiring new customers

In this case, not only can your team lose trust in your leadership capabilities, but it’s likely that your own leadership team will lose trust in your judgement, as well.

#### Evidence doesn’t have to mean activity data

So, what to do instead?

It’s reasonable for an individual contributor to ask about the metrics which will be used to evaluate their performance. And it is important to have a transparent answer to this question. But, it doesn’t have to involve activity data from tools like GitHub and JIRA alone. They may tell one part of the story, but it’s unlikely that activity data alone can give you a clear picture of performance across all competencies that you expect from your team.

Evidence doesn’t have to mean activity data.

Instead of looking for a list of metrics to determine how you measure performance, figure out how you want to measure performance and then find metrics that help you measure the stuff that’s important to your company. While engineering roles do share common traits and objectives across companies, there’s not really a one-size-fits-all approach that will definitely fit your company’s objectives.

#### Work backwards

Time for a practical example. Here’s a job posting for a [Senior Ruby on Rails Engineer](https://apply.workable.com/treatwell/j/6D0B347829/) at [Treatwell](https://treatwell.com).

(Side note – [a list of over 1300 of companies that are still hiring](https://docs.google.com/spreadsheets/d/1SMKjAgYxG1iAi_G4E3DJik17-EkO8QiTo6obeZCiBAQ/edit#gid=882540374).)

Looking at the responsibilities listed in the job description, I’ll work through how I arrive at a list of metrics, and other sources of evidence, to evaluate performance.

* You’ll work as part of a cross-functional squad, collaborating to deliver incremental, meaningful changes to our customers.

Most software engineering roles have this type of delivery objective as part of its core performance expectations, but each role has different expectations of what’s being delivered. First, we need to break this down into smaller objectives that are more easily supported with evidence. Since this is both the top responsibility, and also the most complex one, I’ll spend more time breaking it down. I’m going to focus on some keywords here:

* *Cross-functional, collaborating*: working as part of a cross-functional delivery team implies that this role is responsible for more than just writing code; they are responsible for making decisions and delivering business results as an equal partner to product management and design.
* *Incremental*: The team should deliver small changes at a rapid pace. Given the cross-functional nature of the team, competencies like estimation and prioritisation are just as important as pure execution skills.
* *Meaningful*: Simply put, the software should perform its business function. This aligns closely to the Performance (P) category in the [SPACE framework](https://queue.acm.org/detail.cfm?id=3454124), which covers criteria like user adoption but also quality and stability.

Considering only output-based metrics from GitHub and JIRA just isn’t appropriate for the full scope of this role.

So instead, my rough list might start to look like this:

* *Project on-time delivery*, measured by % of projects that are delivered +/- 1 week of forecasted deadline
* *Satisfaction with engineering partnership,* measured by feedback from cross-functional partners.
* *Quality and reliability*, measured by incident, bugs, or even customer support ticket volume.
* *Business performance of features*, measured by user adoption and other team-defined usage metrics.

What I’m not measuring is also important.

I’ve made a choice here not to directly measure things like PR count, commits, or even story points, though delivery is part of the role. What this role description emphasised is value delivered to the user. If the value is not there, I might debug why that is with specific activity metrics. I might also look into them if I receive peer feedback that this person is not able to keep up with the pace of development.

For the other areas in the role description, I’ll go through the same process. My brief notes below:

* You’ll help your team in designing the system architecture for large scale applications.

* *Participation in architecture decisions*, with consideration for the number of decisions with direct responsibility. This would be a sum measurement, where I just count the number of times it happened.
* *Outcomes of these decisions*, measured by quality of software and ability to deliver on-time (at this point, we start seeing the interconnectedness of some of these performance criteria)
* *Communication and collaboration*, measured by feedback from the engineering team as well as cross-functional partners.

* You’ll support and mentor junior team members, helping them create well thought out and robust solutions.

* *Quality of junior team members’ outcomes*, measured by quality of software as outlined above, but filtering by projects where this person played a large role in mentoring and guiding junior team members
* *Satisfaction with learning opportunities*, measured by gathering feedback from junior team members

* You’ll help your team identify opportunities to improve their ability to deliver all kinds of changes to their users.

* *Leadership and participation in retros, post-mortems, and other continuous improvement processes*, measured by instances of participation.

* You’ll help with the running and maintenance of your team’s applications in production.

* *Operational stability*, measured by the quality metrics mentioned above, and also other appropriate team-defined metrics.

This list is already getting a bit long, and this doesn’t include evidence from my own observations yet.

With so many objectives and sources of information, it’s likely that some performance cycles won’t touch on every single one. That’s fine – as long as you plan for it, and make expectations clear about what happens when that’s not the case. Some things might be fine to drop off (like architectural leadership, if there were no large architecture projects during the evaluation period) but not operational stability or project on-time delivery.

#### Metrics for senior vs. junior roles

The more senior a role is, like the one used in the example above, the more likely it is that the role’s responsibilities focus on strategic *outcomes* rather than task *output*.



![](https://images.squarespace-cdn.com/content/v1/60aa35591e471f054bc53f9c/7de39937-68ce-41df-8788-6ffda4bf0ac4/seniorityscope.png)![](https://images.squarespace-cdn.com/content/v1/60aa35591e471f054bc53f9c/7de39937-68ce-41df-8788-6ffda4bf0ac4/seniorityscope.png)






Whereas a junior engineer will have duties on the task level, a staff engineer is responsible for building systems of software that enable other teams to execute effectively. It may be perfectly reasonable to look at task-level metrics for a junior engineer, but not for that staff engineer.

Treatwell doesn’t have a published career ladder that I can reference here, but chances are that you’ll be looking at a career ladder along side a job expectations document (and if not, you can find a lot of them for reference on [progression.fyi](https://progression.fyi)).

The next step with these metrics would be to double-check that they’re also aligned to the role’s seniority and scope. Sometimes it can be the case where job descriptions, career ladders, and performance management processes don’t actually align to each other, but they should all be reinforcing the same things.

For example, looking at [Medium’s career ladder](https://docs.google.com/spreadsheets/d/1EO-Dbsayn8Nz9Ii3MKcwRbt-EIJ2MjQdpoyhh0tBdZk/edit#gid=1441368371) for the mobile and web engineering tracks, we see a big difference in scope between criteria for those on Track 1 vs Track 4.

Track 1 examples

* Delivers features requiring simple local modifications
* Adds simple actions that call server endpoints
* Uses CSS appropriately, following style guide
* Reuses existing components appropriately

The scope of Track 1 is at the task level, and working within well-defined systems.

By Track 4, the problems are far beyond the task level.

* Makes architectural decisions that eliminate entire classes of bugs
* Designed and pioneered proto-based model storage
* Migrated Android persistance layer to reactive programming

A senior role is responsible for managing whole projects and strategy, while a junior engineer is responsible for managing their tasks. As expectations change, so should the metrics for evaluating performance.

If I were a Track 4 engineer, I would find it a bit silly/annoying if my commit history was taken into consideration for my performance, as long as I was hitting the objectives laid out in my role description.

#### Using system-level metrics to measure performance of managers and senior technical leaders

But as a Track 4 engineer at Medium, I don’t think it’s unreasonable to use the team’s total number of bugs, or total amount of time spent on bugs, as a success metric for my performance.

And that takes me to one exception: using team metrics to measure individual performance is generally unfair *unless* it’s the explicit role of the individual to influence the system performance metrics.

Usually, this happens at a staff+ or management level. If your role’s main objective is to support teams by improving performance of CI/CD systems, and you’ve been given resources, time, and autonomy to do so, it’s reasonable that metrics like Change Failure Rate or Build Time would be used to evaluate how effective you’ve performed your role.

#### No shortcuts

If you’ve read this far, hoping for a list of metrics that you can grab and start using on your teams, you won’t find one. There’s no shortcut here, but you can eliminate some trial and error by following these principles:

* Instead of looking for a list of metrics to determine how you measure performance, figure out how you want to measure performance and then find metrics that help you measure the stuff that’s important to your company.
* Focus on outcomes, not output, but you might use output metrics like activity from GitHub and JIRA to debug why outcomes were missed.
* It might be appropriate to use team-level metrics to evaluate the performance of senior technical leaders and managers, depending on their scope of responsibility.
* Watch out for Goodhart’s Law, or other cases where you metrics may encourage the wrong behaviour.
* Metrics are one thing, but not everything. You still need to do the hard work of active performance management, setting expectations, giving regular feedback, and supporting your team.