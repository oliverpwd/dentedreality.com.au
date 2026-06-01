---
title: 6 Lessons I Learned While Implementing Technical RFCs as a Decision Making
  Tool
date: '2021-02-15T19:49:13-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://buriti.ca/6-lessons-i-learned-while-implementing-technical-rfcs-as-a-management-tool-34687dbf46cb
---

[6 Lessons I Learned While Implementing Technical RFCs as a Decision Making Tool](https://buriti.ca/6-lessons-i-learned-while-implementing-technical-rfcs-as-a-management-tool-34687dbf46cb)  



# Process is what I ship 🚢

This situation was the result of a process failure, and given that process is what I ship as the VP of Engineering, I was also responsible for improving the process so the team doesn’t find itself in these positions. We needed a way to make decisions as a team that would allow us to:

* enable individual contributors to make decisions for systems they’re responsible for
* allow domain experts to have input in decisions when they’re not directly involved in building a particular system
* manage the risk of decisions made
* include team members without it becoming design by committee
* have a snapshot of context for the future
* be asynchronous
* work on multiple projects in parallel

We weren’t the first people to encounter this problem, so we looked at how open source software projects dealt with these situations, and came to the conclusion that adopting the [RFC](https://www.ietf.org/rfc.html) process would help us make better decisions together.

The RFC process has become one of my favorite tools in managing distributed engineering teams. I implemented it shortly after joining [Splice](https://splice.com) and adopted it [Elizabeth & Clarke](https://elizabethandclarke.com) too. I’m still learning about how it can help the organizations I lead to make decisions. Given my overall positive experience over the past 3 years using RFCs “in production”, I thought I’d share some practical lessons in case you want to try it out.

# Learning from RFCs “in production”

## **Deciding when to RFC is difficult**

Given the complexity of decisions, exposure to context, the variance of expertise of engineers and frequent lack of subject matter understanding determining when to write an RFC is the most challenging question of the whole process.

> Should I write an RFC for this?

My general answer to this question is, “If you need to ask you probably should”. To facilitate the process we’ve arrived at some guidelines to decide when to write a proposal.

You should write an RFC if you:

* are building something from scratch. New endpoint, component, system, library, application, etc.
* the need rewrite has crossed your mind
* will impact more than one system or other team members.
* would like to define a contract or interface between clients or systems.
* are adding a new dependency.
* are adding or replacing languages or tools to the stack
* are in doubt of whether you should write one

## Inclusion requires responsibility

I’ve found no better way yet to generate the sense of belonging in teams than by including people in decision making. Having an impact at work is important, and some of this impact happens through decision making. If we’re involved in important decisions, our work has the potential to be more impactful and this gives it a sense of purpose. By giving team members the opportunity to comment on decisions proposed by others, RFCs become excellent tools for inclusion and enable participation that can result in impact at work.

> *If you want to be included, you must participate*

Our implementation of RFCs recommends that proposals remain open for comments for a minimum of two days and a maximum of a week, but shorter or longer are allowed depending on context. In addition, engineers are not required to participate, but if they don’t do it in time they lose the opportunity of being included.

RFCs have reduced the number of times managers find themselves with the dreaded “Why wasn’t I consulted about X” question. In addition, when there is a document they can refer to, individual contributors (ICs) can be given concrete feedback on performance if important decisions which are part of their responsibilities were not on their radar.

Something worth measuring is the rate of participation on RFCs. A low participation rate (participants/total team size) may be the indicator for a few problems lurking in the background. If you see a low participation rate, you team members may be dealing with the following challenges:

* 😵 They have too much going on.
* 😱 They are not interested.
* 🔨 Tools used for process management are not providing them great UX.
* 🕰 They may need better personal time management.

I’ve found that some engineers increase their participation if you schedule review slots in a regular interval during the week and help members organize themselves around it.

## Trust issues become more evident

Making technical decisions that materialize into software and experiencing the consequences of these decisions is an important way to learn how to build software. In some cases, team members may be preventing teammates from making decisions because of lack of trust. We’ve found RFCs increase visibility into who is making decisions in a system and has helped managers identify situations where trust issues are preventing ICs from making decisions. Detecting trust issues early in teams is important in maintaining effective collaboration.

## Power dynamics can be managed

Using RFCs has allowed us to create spaces for team members who wouldn’t normally take the lead in technical decisions. Managers and senior ICs are encouraged to appoint less dominant members as authors of RFCs. Being an author makes it clear that you are the person who is responsible for the proposal. This is an explicit way of being empowered to take the lead without the need to be the loudest or most dominant member of a team.

Having a visible record of non-dominant member participation also allows me to evaluate how managers are handling power differentials, which has an impact on overall team happiness.

## The newbie tag enables psychological safety

To be inclusive, engineering processes design should consider the experience of people with different levels of experience, at both career level and technical depth. For example, I may have been writing JavaScript for several years, but not have much context into the Go way of things.

As a team, we agreed that any comment or proposal tagged with **[newbie]** indicated that its author was coming from a vulnerable place. Whether motivated by lack of expertise, context or confidence, this tag allowed for us to make mistakes while knowing we were in an environment of [psychological safety](https://rework.withgoogle.com/blog/how-to-foster-psychological-safety/), that was supportive of learning for both senior and junior members.

## Engineering leadership can participate at right level of abstraction

When I was at Ride I was expected to run the engineering organization and provide technical direction, hybrid VPE/CTO role (full-stack exec? 😂). In this case, I used RFCs to understand decisions being made at the architecture level and I would approve or delegate approval of these decisions without the need to micromanage or dictate how problems were to solved. If the risk to the business was high, like in the case of large rewrites/refactor or the addition of a tool to the stack I could reject a proposal or approve if I could see learning opportunities at a manageable risk. This is how it works today Elizabeth & Clarke, where I’m Chief Technical Husband on the weekends.

At Splice, I’m only responsible for the engineering organization and partner with [Matt](https://twitter.com/mattetti), our CTO, who is responsible for our technical direction. As senior leaders, we’re accountable for decisions made at all levels of engineering and technology. RFCs have particularly enabled Matt to have visibility into how members of our team think through technical direction, allow him to manage risk and be involved in technical decisions at the right level, with the option to dig deeper or delegate when necessary. It’s also nice that he doesn’t constantly need have the entire system in his head.

# RFCs are my jam

Giving team members, present, and future, the context into why and how decisions have been made has allowed me to run happier and more effective distributed engineering organizations. Now, instead of trying to inadequately respond when I’m asked “what were these people thinking?”, I point to files that may be able to resolve all doubts and allow members of my team to wear the software historian hat.

Just like building software, I like iterating on processes and how you’ve improved technical decision making with your teams.