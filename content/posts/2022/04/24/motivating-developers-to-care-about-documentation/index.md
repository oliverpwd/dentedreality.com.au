---
title: Motivating Developers to Care About Documentation
date: '2022-04-24T22:44:28-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://getdx.com/best-practices/documentation-culture-engineering
---

[Motivating Developers to Care About Documentation](https://getdx.com/best-practices/documentation-culture-engineering)  



*The following is a transcription of our interview with* [*Paulo André*](https://www.linkedin.com/in/paulorlandre/)*. Paulo is a former VP of Engineering who now coaches CTOs, VPs of Engineering, and Engineering Managers. He also writes a weekly newsletter for technical leaders (*[*sign up for it here*](https://hagakure.substack.com/)*).*

**Paulo:** Let me set the stage here. Internal documentation is something I’m passionate about because I’ve seen how important it is. But in most of my roles I’ve been fairly reactive, having created documentation after there was an apparent need for it. (Being a coach now, I don’t have the opportunity to be more intentional about documentation but if I do join another company I will be.)

‍

## **What *is* documentation?**

“Documentation” can mean different things, so let’s start by defining **what documentation is not.** To do that, I like to dispel what I call the myths of documentation: “documentation is bureaucracy,” “documentation is a nice-to-have,” and “documentation takes too much time.” All of these are myths. Documentation, done well, helps the team move faster with less rework. If you want to scale, you need documentation, it’s not a nice-to-have. And if it takes too much time it’s because the process isn’t set up right.

What documentation *is* can be boiled down to this: **documentation is writing down “what we do right now” or “how something works”.** The point of documentation is to enable automatic and decentralized decision-making, which is essential for scaling up.

Probably the best and most familiar example of good documentation comes from GitLab. It’s the best system I’ve come across because it’s ever-evolving, it clearly outlines [how documentation can be updated](https://about.gitlab.com/handbook/handbook-usage/#flow-structure), and it relies on a [roadmap](https://gitlab.com/groups/gitlab-org/-/epics/4602) for the areas the team plans to dedicate time towards.

One of the interesting things about GitLab’s documentation is that it has a broad scope. It’s not just technical explanations. It also organizes team goals, team workflows, and makes transparent their career ladders. These are the types of things that can get locked in someone’s brain but would save the team a lot of time if written down.

A few quick examples from my experience: At HelloFresh, we had over a hundred developers before I set out to document career ladders. You can probably imagine the impact that codifying the behaviors we wanted to see had on that large of a team. When I was at TourRadar, I realized that big technical decisions were happening somewhat haphazardly — and a lot of rework would have to be done when those decisions were actually getting implemented. I brought in a standard RFC process where we could document the choices we were making and, through the process of writing and getting comments, decisions could be made more collaboratively. All that’s to say, documentation has a broad scope.

> One of my core principles as a VP of Engineering was to make the implicit explicit. As people work, it’s natural to make assumptions that may or may not be right. So documenting things explicitly is important, especially the things that lead to better decisions.

‍

## **How do you create a culture where everyone works on improving documentation?**

There’s certainly a change management process that’s needed if a team is going to maintain a new documentation process. That’s because the problem with internal documentation isn’t usually that people don’t know it’s important — because they do know it’s important — it’s that they don’t have the time, they don’t have the incentive, and they don’t see other engineers spending time on docs. It’s a culture problem.

So here’s how I think about shifting culture towards one that values documentation:

### **Answer this: Why do we need documentation in the first place?**

**‍**There’s a difference between compliance and commitment, and the goal is to get commitment from the team. What we want from the team is for developers to voluntarily write and contribute to docs, and for that they need to see the value in it.

In the past, my “why’s” have included 1. making better decisions across the organization, 2. helping people get the right information when they need it, and 3. making our onboarding process more self-service (my opinion is that onboarding should be 80% self-serve).

Choosing reasons like the three I listed can be helpful in the day-to-day when we’re actually writing documentation. If we’re deciding whether to write something, we should ask whether writing it will help us with one of those objectives. Is this actually going to help us make better decisions? Is it actually going to help us onboard people better? Is it actually going to help people get the information they need when they need it?

> There’s a difference between commitment and compliance, and the goal is to get commitment from the team.

Then, we can pair those high-level reasons with a specific initiative. Sometimes the team surfaces more specific problems with documentation, like:

* We keep having to redo work because the requirements aren’t clear
* Docs are out of date or poorly written
* We’re missing documentation about certain areas of the codebase or important technical decisions or team processes
* Documentation exists but it’s nearly impossible to find

Pick one area to work on, and continue pointing to the higher-level reasons why we’re making the investment. That way we start making improvements while also building a culture that can maintain the process.

### **Tips for helping teams maintain the practice**

**Make documentation easy.** Lower the barrier to writing docs by providing templates. [Confluence](https://www.atlassian.com/software/confluence/templates), [Notion](https://www.notion.so/templates/docs-eng), [Almanac](https://almanac.io/categories/2398/engineering), and [Coda](https://coda.io/gallery/engineering) all have templates you can use as a starting point.

**Treat documentation like a discipline.** Just as much as you incentivize shipping code you need to incentivize good documentation. That means the ability to write documentation is considered in the hiring and promotion processes.

If you’re taking documentation really seriously, put it on the scorecard. Look for good writers. Over time you’ll bring on more people that voluntarily write good documentation but also good code reviews, well-written emails or slack conversations. Then put it in your career ladders too. It’s a competency that individuals need to develop if they’re to move to the next level.

On this note, I’d also add that when leaders consider it as a discipline for themselves, they lead by example. The better they write, the better everyone writes.

**Reinforce the behavior.** One problem I’ve experienced: I demanded good documentation from people, but they didn’t know what good looked like. Particularly more junior people. And that was my failure as a leader. So it was my job to give examples, and one way I did that was through a “top of mind” email. I actually wrote about this for an issue of in Gergely Orosz’s [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/) newsletter:

![](https://global-uploads.webflow.com/622e9926ab27e10fa174ef99/624b5432202719bf19a2e151_Screen%20Shot%202022-04-04%20at%202.11.39%20PM.png)![](https://global-uploads.webflow.com/622e9926ab27e10fa174ef99/624b5432202719bf19a2e151_Screen%20Shot%202022-04-04%20at%202.11.39%20PM.png)

‍

One part of the weekly top of mind email was showcasing what ‘good’ looks like. If someone created or contributed to documentation and it was really well written, I’d highlight it as an example for others to see.

‍

## **Parting words**

We’re not yet post-covid, but I think we can safely say that any company that’s founded moving forward is founded in a context where remote and distributed work is more widespread. They’re starting from a more asynchronous perspective where documentation is an absolutely necessary practice. So as an industry I think we’ll see companies start taking documentation a lot more seriously.

‍