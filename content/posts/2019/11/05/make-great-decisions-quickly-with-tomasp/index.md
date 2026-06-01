---
title: Make Great Decisions Quickly With TOMASP
date: '2019-11-05T10:35:33-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://engineering.shopify.com/blogs/engineering/make-great-decisions-quickly-with-tomasp
---

[Make Great Decisions Quickly With TOMASP](https://engineering.shopify.com/blogs/engineering/make-great-decisions-quickly-with-tomasp)  



As technical leaders and managers, our job is to make the right decision most of the time. Hiring, firing, technology choices, software architecture, and project prioritization are examples of high impact decisions that we need to make right if our teams are to be successful.

This is hard. As humans, we’re naturally bad at making those types of decisions. I’ll show you how you can consistently make great decisions quickly using a simple framework called **TOMASP.** I made up the acronym for the purpose of this blog post but it’s inspired from many great books (see resources) as well as my personal experience of leading engineering teams for almost 15 years.

Let’s start with a concrete real world example:

*Michelle, a technical lead for a popular mobile app is agonizing about whether or not she should direct her team to rewrite the app using Flutter, a new technology for building mobile apps.*

*Flutter has an elegant architecture that should make development much faster without compromising quality. It was created by Google and is already in use by several other reputable companies. If Flutter delivers on its promises, Michelle’s team has a good chance of achieving their goals which seem highly unlikely with the current tech stack.*

*But starting a big rewrite now will be hard. It’s going to be difficult to get buy-in from senior leadership, no one on the team has experience with Flutter and Mike, one of the senior developers on the team is really not interested in trying something new and will probably quit if she decides to more forward with Flutter.*

Before reading further ask yourself, what is the right decision here? What would you advise Michelle to do? Should she rewrite the app using Flutter or not?

I have asked this question many times and I bet most of you have an opinion on the matter. Now think about it, how much do you really know about Michelle and her team? How much do you know about the app and the problem they’re trying to solve? We will get back to Michelle and her difficult decision by the end of this post but first a little bit of theory.

# How We Make the Wrong Decisions

*“The normal state of your mind is that you have feelings and opinions about almost everything that comes your way”*

Daniel Kahneman – Thinking, Fast and Slow

This ability of our mind to form opinions very quickly and automatically is what enables us to make thousands of decisions every day, but it can get in the way of making the best decision when the decision is complex and the impact is high. This is just one of the ways our brain can trick us into making the wrong decision.

Here are some other examples:

* We are highly susceptible to [cognitive biases](https://en.wikipedia.org/wiki/Cognitive_bias#List))
* We put too much weight on short term emotion
* We are over confident about how the future will unfold (when was the last time your project finished sooner than you anticipated?)

The good news here is that it’s possible, through deliberate practice, to counteract those biases and make great decisions quickly even in complex high impact situations.

*“We can’t turn off our biases, but we can counteract them”*

Chip Heath, Dan Heath – Decisive

# What is a Great Decision?

Before I show you how to counteract your biases using TOMASP, we need to get on the same page as to what is a great decision. Let’s go through a couple of examples.

An example of a good decision:

*In 2017 Shopify started to migrate its [production infrastructure to Google Cloud](https://engineering.shopify.com/blogs/engineering/shopify-infrastructure-collaboration-with-google) …* 

*Scaling up for BFCM used to take months, now it only takes a few days*✌️.

In my experience this image is the mental model that most people have when they think of great decisions:

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Make_Great_Decisions_Quickly_-_Single_Impact.jpg?v=1571770230)![](https://cdn.shopify.com/s/files/1/0779/4361/files/Make_Great_Decisions_Quickly_-_Single_Impact.jpg?v=1571770230)  
*A decision has a direct link to the impact*

In the previous example the decision is to move to google cloud and the impact is the reduced effort to prep for [BFCM](https://engineering.shopify.com/search?q=black+friday).

Now let’s look at an example of a bad decision:

*In 2017 Shopify started to migrate its production infrastructure to Google Cloud… 2 years later, [Shopify is down for all merchants due to an outage in Google Cloud](https://status.shopify.com/incidents/tbtk2sk9d5tp) 😞.*

Do you notice how the previous mental model is too simplistic? The same decision often leads to multiple outcomes.

Here is a better mental model for decisions:

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Make_Great_Decisions_Quickly_-_Multiple_Impacts.jpg?v=1571770491)![](https://cdn.shopify.com/s/files/1/0779/4361/files/Make_Great_Decisions_Quickly_-_Multiple_Impacts.jpg?v=1571770491)

*A decision leads to execution which leads to multiple impacts. Moreover, things outside of our control will also affect the outcomes*

Some things are outside of our control and a single decision often has multiple outcomes. Moreover, we never know the alternative outcomes (i.e. what would have happened if we had taken a different decision).

Considering this, we have to recognize that **a great decision is NOT about the outcomes. A great decision is about how the decision is made & implemented**. More specifically a great decision is timely, considers many alternatives, recognizes biases and uncertainty.

# TOMASP

To put that in practice think **TOMASP**. TOMASP is an acronym to remember those specific behaviour you can take to counteract your biases and make better decisions.

## Timebox (T) the Decision

Define ahead of time how much time is this decision worth.

### You Need This If…

It’s unclear when the decision should be made and how much time you should spend on it.

### How to Do It

If the decision is hard to reverse, aim to make it the same week, otherwise aim for same day. One week for a “hard to reverse” decision might sound too little time, and it probably is. The intent here is to focus the attention and to prioritize. In my experience this can lead to a few different outcomes:

1. Most likely, this is actually not a hard to reverse decision and aiming to make it on the same week will lead you to focus on risk management and identify how you can reverse the decision if needed
2. This is truly a hard to reverse decision and it shouldn’t be made this week, however there are aspects that can be decided this week, such as how to go about making the decision (e.g who are the key stakeholders, what needs to be explored)

Multiple decisions are often made at the same time, whenever this happens make sure you’re spending the most time on the most impactful decision.

### This Helps Avoid

* Analysis Paralysis: over-analyzing (or over-thinking) a situation so that a decision or action is never taken, in effect paralyzing the outcome
* Bikeshedding: spending a disproportionate amount of time and effort on a trivial or unimportant detail of a system, such as the color of a bikeshed for a nuclear plant

## Generate More Options (O)

Expand the number of alternative you’re considering.

### You Need This If…

You’re considering “whether or not” to do something.

### How to Do It

Aim to generate at least 3 reasonable options.

Do the Vanishing Option Test: if you couldn’t do what you’re currently considering, what else would you do.

Describe the problem, not the solutions, and ask diverse people for ideas, not for feedback (yet).

### This Helps Avoid

* Narrow framing: making a decision without considering the whole context
* Taking it personally: by truly considering more than 2 options you will become less personally attached to a particular course of action

## Meta (M) Decision

Decide on how you want to make the decision

### You Need This If…

It’s hard to build alignment with your team or your stakeholders on what is the right decision.

### How to Do It

Ask what should we be optimizing for?

Define team values or principles first and then use them to inform the decision.

Look for heuristics. For instance at Shopify we have the following heuristic to quickly choose a programming language: if it’s server side business logic we default to ruby, if it’s performance critical or needs to be highly concurrent we use Go.

### This Helps Avoid

* Mis-alignment with your team or stakeholders: I have found it easier to agree on the criteria to make the decision and the criteria can then be leveraged to quickly align on many decisions.
* Poor implementation: having explicit decision-making criteria will make it a lot easier to articulate the rationale and to give the proper context for anyone executing on it.

## Analyze (A) Your Options

Make a table to brainstorm and compare the “pros” and “cons” of each options.

### You Need This If…

There is consensus very quickly or (if you’re making a decision on your own) you have very weak “pros” for all but one option.

### How to Do It

Make your proposal look like a rough draft to make it easier for people to disagree.

Nominate a devil’s advocate, someone whose role is to argue for the opposite of what most people are leaning towards.

Make sure you have a diverse set of people analysing the options. I’ve gotten in trouble before when there were only developers in the room and we completely missed the UX trade-off of our decision.

For each option that you are considering, ask yourself what would have to be true for this to be the right choice.

### This Helps Avoid

* Groupthink
* Confirmation bias
* Status-quo bias
* Blind spots

## Step (S) Back

Hold off on making the decision until the conditions are more favorable.

### You Need This If…

It’s the end of the day or the end of the week and emotions are high or energy is low.

### How to Do It

Go have lunch, sleep on it, wait until Monday (or until after your next break if you don’t work Monday to Friday).

Do 10/10/10 analysis: this is another trick I learned from the book Decisive (see resources). Ask yourself how you would feel about the decisions 10 mins later, 10 months later and 10 years later. The long term perspective is not necessarily the right one but thinking about those different timescales help put the short term emotion in perspective.

Ask yourself these two questions:

1. What would you advise your best friend?
2. What would your replacement do?

### This Helps Avoid

* Putting too much weight on short term emotions
* Irrational decision making due to low energy or fatigue

# Prepare (P) to be Wrong

Chances are, you’re over-confident about how the future will unfold.

### You Need This If…

Always do this 🙂

### How to Do It

Set “tripwires”: systems that will snap you to attention when a decision is needed. For example a development project can be split into multiple phases with clear target dates and deliverable. At Shopify, we typically split project into **think**, **explore**, **build** and **release** phases. The transition between each phase acts as a tripwire. For example, before moving to **build** the team and stakeholders review the technical design (the deliverable for that phase) and have to make a conscious decision to continue the project or pause it.

Whenever a phase is expected to be over 4 weeks, I like to break it down further into **milestones**. Again, it’s essential that each milestone has a clear target date and deliverable (e.g 50% of the tasks are completed by Oct 10th) so that it can act as a tripwire.

You can setup additional tripwires by doing a pre-mortem analysis: imagine the worst case scenario, now brainstorm potential root causes. You now have leading indicators that you can monitor and use as tripwires.

### This Helps Avoid

* Reacting too slowly: setting tripwires will help you detect early when things are going off the rails.

# TOMASP in Action

At the beginning of this post, I gave the following example:

*Michelle, a technical lead for a popular mobile app is agonizing about whether or not she should direct her team to rewrite the app using Flutter, a new technology for building mobile apps.*

*Flutter has an elegant architecture that should make development much faster without compromising quality. It was created by Google and is already in use by several other reputable companies. If Flutter delivers on its promises, Michelle’s team has a good chance of achieving their goals which seem highly unlikely with the current tech stack.*

*But starting a big rewrite now will be hard. It’s going to be hard to get buy-in from senior leadership, no one on the team has experience with Flutter and Mike, one of the senior developers on the team is really not interested in trying something new and will probably quit if she decides to more forward with Flutter.*

Here is how Michelle can use TOMASP to make a Great Decision Quickly:

* **Timebox (T)**:

* This feels like a hard to reverse decision, so Michelle aims to make it by the end of the week.

- **Generate More Options (O)**:

* Michelle uses the Vanishing Option Test to think of alternatives. If she couldn’t rewrite the whole app using Flutter what could she do?
* Use a hybrid approach and only rewrite a section of the app in Flutter.
* Have the iOS and Android developers systematically pair-program when implementing features.
* Use another cross-platform framework such as React Native or Xamarin.

- **Meta (M) Decision**:

* What should Michelle optimize for? She comes up with the following hierarchy: 1) cross-platform consistency 2) performance 3) development speed

- **Analyze (A) Options**:

* Michelle concludes that for Flutter to be the right choice, a developer should be able to deliver the same level of quality in 50% or less of the time (to account for the risk and learning time of using a new technology).

- **Step (S) Back**:

* Michelle decides to make the decision first thing Friday morning and do a 10/10/10 analysis to ensure she’s not putting too much weight on short term emotion.

- **Prepare (P) to be Wrong**:

* Michelle decides to timebox a prototype: over the next 2 weeks she will pair with a developer on her team to build a section of the app using Flutter. She will then ask her team members to do a blind test and see if they can guess which part of the app has been rebuilt using Flutter.

That’s it! Even if Michelle ends up making the same decision, notice how much better she’s prepared to execute on it.

Thanks for reading, I hope you find this decision framework useful. I would be very interested in hearing how you’ve put TOMASP to use, please let me know by posting a comment below.

Some great resources:

* [Decisive](https://heathbrothers.com/books/decisive/) by Chip Heath and Dan Heath
* [Thinking Fast & Slow](https://www.penguinrandomhouse.ca/books/89308/thinking-fast-and-slow-by-daniel-kahneman/9780385676533) by Daniel Kahneman
* [When](https://www.danpink.com/books/when/) by Daniel Pink
* [Who is in the Room?](https://www.oreilly.com/library/view/whos-in-the/9781118067871/) by Bob Frisch

We’re always looking for awesome people of all backgrounds and experiences to join our team. Visit our [Engineering career page](http://www.shopify.com/careers/specialties/engineering?itcat=EngBlog&itterm=Post) to find out what we’re working on.