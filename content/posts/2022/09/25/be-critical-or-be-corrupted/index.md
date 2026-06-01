---
title: Be Critical or Be Corrupted
date: '2022-09-25T11:24:11-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.cenizal.com/be-critical-or-be-corrupted/
---

[Be Critical or Be Corrupted](https://www.cenizal.com/be-critical-or-be-corrupted/)  



What does a 2002 HBO crime drama have to do with software engineering?

On the surface, “[The Wire](https://en.wikipedia.org/wiki/The_Wire)” is about homicide detectives and the Baltimore drug trade. But on a deeper level, these motifs are just stage dressing for the show’s exploration of the city’s institutions and how corruption inevitably sprouts like weeds within them. I recently rewatched this series and, aside from hours of entertainment and a deeper butt-impression on my couch, I also had an epiphany about how I’ve observed this theme first-hand.

## Rise of the rotation

Rotations are commonly used in software engineering to fairly distribute undesirable duties among team members. They suck but they work!

In “The Wire”, Police Superintendent Rawls explains the rotation used by the homicide division to divvy up murder cases, and chastises Detective McNulty for bucking this rotation and burdening the rest of the team.

> Superintendent Rawls: “We work murders cases here, Detective. We work them as they come in. One at a fucking time, it’s called a rotation. You’re up ’til you catch one. When you catch one, you step down, you work it for a while, someone else steps up. It’s a simple, but effective way to do business in a town that has 250 to 300 cases a year.
> 
> Detective McNulty: “Yes, sir.”
> 
> Rawls: “But if someone gets it into his head to leave the rotation, it puts an unfair burden on the other detectives, who have to pick up their casework. Overworked cops make mistakes, mistakes lower the unit-wide clearance rate. And that can make someone who is otherwise as reasonable as me…”
> 
> McNulty: “Unreasonable.”

I used to work in an organization that had an engineering rotation for helping our users work around defects in our product.

This rotation covered the entire surface area of the product, but the engineers on the rotation typically specialized in particular product areas. This meant an engineer on rotation would spend most of their time working on problems that they didn’t have a clue about. So they’d spend a lot of time simply learning about new domains instead of figuring out how to fix problems. In many cases, they’d give up and re-route the problem to another engineer who knew the domain better.

As an engineer on this rotation, you felt like you were fighting fires. You didn’t have the time or knowledge to actually fix root causes. You just wanted to do the bare minimum to put the fire out (or hand it off!) and get through your day on the rotation.

But the rotation served its purpose because users’ problems got solved.

## People fixate on the numbers

Two numbers determine the homicide division’s success: the number of open cases and the rate at which they’re closed. The number of open cases improves as the case closure rate increases. It gets worse when new murder cases are opened.

This creates a perverse incentive of encouraging the police to ignore dead bodies to prevent them from becoming open cases. Sergeant Landsman makes this explicit in episode 12 of season 4.

> Sergeant Landsman: “There’s three weeks left in the year, and our unit clearance rate is under 50%. We do not go looking for bodies, especially moldering fucking John Does. We do not put red up on the board voluntarily.”

This is an example of [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law), which predicts that a metric will become useless or even harmful once it becomes a target.

In the company where I worked, our rotation consisted of helping customer support resolve difficult support cases, triaging GitHub issues, and answering community questions on the public forums. These were all wonderful sources of data about the defects in our products, each of which was an opportunity to improve our product and increase user value.

But by definition, the purpose of the rotation was to resolve users’ issues. An engineer on rotation had one job: resolve as many issues as possible. This approach was so simple and effective that the organization never adopted the rotation as a driver for change. Ironically, treating users’ problems as mere symptoms of an underlying problem and then solving the root causes would have reduced the number of problems in the long-term.

## The system contorts itself around its metrics

What began as the homicide division’s initial reaction to a problem becomes a chain reaction. More metrics blossom and breed bad behavior. The department measures crime in terms of felonies, so they show a reduction in crime by reclassifying felonies as misdemeanors, thus letting violent criminals off the hook. Meanwhile they use their arrest rate to measure effectiveness, so they demonstrate an effective police force by arresting people for minor infractions like loitering.

The metrics incentivize counterproductive behavior and, over time, develop into a self-perpetuating culture. This is corruption.

> Commissioner Daniels: “But the stat games, that lie, it’s what ruined this department. Shining up shit and calling it gold, so majors become colonels and mayors become governors. Pretending to do police work while one generation fucking trains the next how not to do the job.”

I haven’t been in a situation nearly as bad as Daniels describes, but I see his point. In a system, everything connects. A perverse incentive in one component affects the components it connects to. Bad behaviors that hit targets are rewarded, which encourages other bad behaviors in response. Eventually, the organization develops a web of behaviors with these metrics at the root, and the mission goes unserved.

Here’s a thought exercise. Imagine your team is using a specific metric to determine success or failure. After your team ships a feature, this metric moves in a positive direction. The organization celebrates your team’s success and everyone gets rewarded. However, you realize that a number of [confounding variables](https://en.wikipedia.org/wiki/Confounding) influence the metric and there’s no way to correlate your team’s work with changes to the metric. Would you be able to improve things? What would it cost you?

## Think critically

What can we do about this entropic tendency of organizations towards corruption?

**We can carefully design our metrics and think critically about the behaviors we expect them to incentivize.** This one’s obvious. I’m reminded of the Bill Gates quotation: “Measuring programming progress by lines of code is like measuring aircraft building progress by weight.”A metric can go bad over time, so we should also regularly revisit them and fix the ones going sideways.

**We can extend self-awareness and critical thinking to all decisions made within an organization.** We just have to consider every decision’s [second-order effects](https://fs.blog/second-order-thinking/). In “The Wire”, the police department responds to budget cuts by shutting down the Major Crimes Unit and directing its detectives to rack up arrests of low-level drug-dealers. But the unit’s high-level case against a big drug kingpin gets mothballed when the unit is shut down, which guarantees an endless stream of new drug-dealers onto the streets.

**We can look beyond metrics by *qualifying* success and failure.** This begins with asking people questions. As Tara Scott says in the “Finding Agility Through Psychological Safety” episode of the [Product Thinking](https://produxlabs.com/product-thinking) podcast: “The most important thing is leading with curiosity.” Want to know what/how/why things are broken in your organization? Ask people!