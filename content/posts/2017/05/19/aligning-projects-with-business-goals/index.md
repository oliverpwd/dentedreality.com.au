---
title: Aligning Projects with Business Goals
date: '2017-05-19T09:18:48+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://blog.dnsimple.com/2017/02/aligning-business-goals-with-projects/
---

[Aligning Projects with Business Goals](https://blog.dnsimple.com/2017/02/aligning-business-goals-with-projects/)  



If you’ve read our blog, or heard us speak at conferences, you probably know by now that DNSimple is a completely distributed team. We have team members all over the world, often travelling from one location to another while still working. Trying to keep everyone on the same heading, aligned with the overall strategic goals of the business, is a challenge, even with our small team of twelve. Starting in December, we began experimenting with a new system for ensuring that we work on projects that are most likely to help us achieve our business goals. It all starts with a project template and a spreadsheet.

## The project template

Up until recently, projects at DNSimple were mostly driven by one or more team members who felt the project was worth doing. While I would share big yearly strategic goals at the beginning of the year, the actual projects to accomplish those goals were not outlined. This system mostly worked, but also lead to some stressful moments—with projects slowly moving towards completion and a big, crazy burst at launch, trying to bring all of the final pieces together. It can be fun to do once, but after a while it starts to get tiring. This culminated with multiple members of the team expressing their frustration when being dragged in multiple directions at once, without a clear sense of what was important, and when things should be completed.

Enter the first part of this new system we are trying: the project template. The template came to us courtesy of Sebastian, who initially described it as a tool for himself to better understand what the goals of a particular project were. When he described the template, I was so intrigued that I suggested we should try to apply it to *all* of our projects. The template consists of 6 questions:

* What is the problem we are trying to solve?
* What does success look like, and how does it fit in the big picture?
* What are the MUST DO and the MUST NOT DO items?
* What is the deadline?
* Who should I talk to for help and get feedback?
* Have we done this before? Something we already have to get started?

The first question defines the problem. We usually keep it to a few, short, clear sentences. Here is an example:

> Currently access keys have the same level of access control: full access to all resources in an account. Businesses want to be able to control access to specific domains, and specific actions on those domains. To do this, access keys must be scoped.

The second question describes what constitutes successful completion of the project. For example:

> A successful implementation provides scoped access to resources (domains at minimum, but also contacts, templates, webhooks, etc) and specific actions. For example, a key may be able to read a domain’s attributes, but not make changes on that domain. Or, a key may be able to create domains, but not contacts.

Next, we list the MUST and MUST NOT DO items for the project. This might have one item, or many items. In the case of the example project I’m using right now, there is currently only one (but more will likely be added):

> MUST allow scope control in both the UI when creating keys manually as well as through OAuth

Next, we enter a deadline *if one exists*. The deadline only matters if the project is tied to a specific event (such as a conference).

> Who should I talk to for help and get feedback?

Here we list team members who have specific knowledge about the project.

> Have we done this before? Something we already have to get started?

Finally, if we’ve done something like this before, it’s good to note that down, so that whomever is responsible for the project can look at other existing material before getting started (or during development).

Notice that not all of the details of the project are laid out here. We wait until we’ve accepted a project and then create issues in different repos in GitHub depending on where the tasks fit (application development, operations, marketing, etc). It’s also reasonable to add additional information to the project proposal, even if it doesn’t fit these six questions.

This project proposal becomes a single GitHub issue in our business repository. It is labeled as a “Proposal” and then added to the spreadsheet.

## The spreadsheet

The second part of this system is a simple Google spreadsheet with the following columns:

* Title
* Description
* Effort
* Urgency
* Impact
* Risk Factor
* Innovation
* Priority
* Status

The first two columns hold the title from the GitHub issue and short description of the project. Effort, urgency, impact, risk factor and innovation each hold numeric values (more on that below). The Priority field holds a calculated value and the Status field holds a status indicator (right now we have New, In Progress, and Paused).

Before I describe each of the scoring columns, it’s important to understand what the current strategic goals are at DNSimple:

* Ensure continuity of business
* Grow profit margins
* Innovate

As you will see shortly, the scoring is defined primarily in the context of these three goals.

Let’s take a look at the fields used to score the project.

### Effort

This value is based on a combination of time it would take to implement as well as the number of people from the team that need to be involved. The scale is currently defined as:

* 1: Small
* 2: Medium
* 3: Large

### Urgency

Urgency defines time sensitivity, with the following scale:

* 0: no deadline
* 1: deadline within the next 6 months
* 2: deadline within the next 3 months

### Impact

The impact value indicates the potential impact on profitability.

* -2: significant negative impact
* -1: negative impact
* 0: little to no impact
* 1: some impact
* 2: significant impact

Note that the values may be negative. That indicates that the project could have a negative impact on profitability. This doesn’t necessarily mean the project won’t get done, but as you’ll see in a bit, it means the project must give greater benefits in other ways.

### Risk Factor

This indicates the risk factor if the project is *NOT* implemented.

* 0: Little or no risk
* 1: Some risk
* 2: Significant risk

### Innovation

Indicates innovation level, which considered we consider a positive influence on long term growth.

* 0: little or none 😒
* 1: ahead of the curve 😎
* 2: groundbreaking 💥

### Scoring for priority

With these individual scores defined, we can now calculate a priority value. We consider this priority value to be a guide, not a rule. As a guide though, it’s quite helpful when making decisions about what to do next.

Here is the formula:

```
(Impact * 3) + (Urgency * 3) + (Risk Factor * 4) + (Innovation * 2) - (Effort * 3)

```

Each value has a multiplier. The multiplier gives the value more or less weight in the calculation. A high risk factor number (which would indicate that we may potentially cause disruption to the continunity of business if we fail to implement it) gets more weight than a high innovation number. Consider that if the business stops operating then nothing else matters, giving it the highest importance. On the other hand, innovation has slightly less value than profit impact or time sensitivity.

The calculation is based on the goals of the business as it is today, and it took some experimentation with the formula before we arrived at a useful value.

In the end, we have a spreadsheet with each project scored by the formula described above. The Priority field is given a conditional format from green at the high end, to red at the low end, and is typically sorted by Priority from Z to A and then by Status from A to Z.

![](https://i0.wp.com/blog.dnsimple.com/files/2017/project-index-scoring.png?w=607&ssl=1)

Here is a zoomed out view when sorting just by priority:

![](https://i1.wp.com/blog.dnsimple.com/files/2017/project-index-zoomed-out.png?w=607&ssl=1)

## Making decisions as a team

Projects can be added to the list as members of the team come up with them. When they’re added, they should be written up in a project proposal immediately. If a project cannot be described well yet, then it may not make sense to add it to the project list.

With the project list in hand, the next step is actually picking the projects to work on. When we first started this system in December, we already had a number of projects that were in progress, so we re-evaluated each of them and paused the ones we thought were not relevant for the moment. We then continued work on the selected projects.

Once projects are completed, they are moved to a separate sheet on the same spreadsheet document. We retain the scores as well for historical reasons. Next, we decide as a team which projects we want to work on, starting at the top of the sorted list. Selection comes from a short discussion about which projects the team members feel are the most valuble and timely. As I mentioned previously, the items scored with the highest priority will not necessarily be the ones we work on first, however it is a good starting point to make a decision on where to begin.

Currently we do not have a fixed schedule to review the list. At minimum we will likely review the list at our team meetups, but we have already had cases where team members have finished projects and are ready to select a new one. We will likely continue pulling off projects in a ad-hoc fashion until we get into a groove with this system and better understand how often we need to perform a review and select new projects.

## So why not use project management tool X?

Before deciding to use a spreadsheet for this job, I looked around at a number of different project management tools. I was really hoping I would find something that would do this job well, but nothing fit the bill. All of our issue management occurs in GitHub Issues. This means that any tool we select would need to work well with GitHub issues. I looked at a number of kanban dashboards that integrate with GH, but all of them imported *all* of the issues from a project, rather than allowing me to select which issues I wanted to view. Some allowed filtering by labels, but we have not used labels consistently enough, across multiple repos, for this to work. None of the systems had a flexible scoring system that allowed us to define priority based on our business goals. For these reasons (and others) I went with a simple spreadsheet.

Initially one of the project proposals was done in Google Docs, but after getting feedback from the team, I moved the project porposals back into GitHub as individual issues. This allows for us to have deeper conversations about projects as they evolve, use labels, reference team members, and in general it fit into our issue management processes that we already have.

## Conclusion

The million dollar question is, of course: does it work? So far the results are promising, even though we’ve only begun to use this new system. It is definitely easier for me, as the person responsible for the strategic direction of DNSimple, to have a more accurate high-level view of what projects are in the pipeline, and how they fit into the bigger picture. It also helps the team stay aware of projects that are outside of their primary responsibilities. Without a doubt, we will need to tweak this system as we use it more, but the early results are promising.