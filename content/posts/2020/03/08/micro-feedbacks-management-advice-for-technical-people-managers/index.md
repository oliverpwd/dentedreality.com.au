---
title: Micro Feedbacks — Management Advice for Technical People Managers
date: '2020-03-08T15:15:41-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/nmc-techblog/micro-feedbacks-92a8ade8ba39
---

[Micro Feedbacks — Management Advice for Technical People Managers](https://medium.com/nmc-techblog/micro-feedbacks-92a8ade8ba39)  



![](https://miro.medium.com/fit/c/96/96/2*EiQRzf8Zn5au2393XYUDSw.png)![](https://miro.medium.com/fit/c/96/96/2*EiQRzf8Zn5au2393XYUDSw.png)
Tal Joffe
Nov 26, 2019 · 10 min read




![]()



# Intro

As technical managers in the software industry, we are accustomed to talking about technical best practices but not so much about management best practices. Most of us started in technical roles, and were trained for that, but when we moved to a managerial position we just had to figure it out by ourselves.

There is a lot of content on management, mostly in book format but a lot of it is very different from the material we are used to. For me, the first encounter I had with practical useful material I can start using was the [Manager Tools podcast](https://www.manager-tools.com/all-podcasts) which I highly recommend.

I’ll take what I’ve learned from Manager Tools (and other similar content) and my personal experience and use technical terms and paradigms from the “micro-services” world to explain how to manage people better, specifically by giving **short, frequent, effective feedbacks.**

*Disclaimer — I tried to use actual technical best practices as examples, so you might accidentally gain some technical knowledge as well* 😬

# Requirements

When designing a product one of the most important questions we need to ask is what is the business value it should provide to clients.

So what is the business value of feedback or performance communication in general?

Our goal is to deliver products that will make our company successful, for that we need an efficient and effective team.

Performance communication helps with that in several ways:

1. It allows for improvement in individual performance by communicating what works well and what doesn’t
2. It allows for alignment on principles and culture
3. When done correctly, it gives employees opportunities to grow and thus improve retention

# “Breaking the Monolith”

We established that we should communicate performance feedback to employees so let’s focus on delivery methods.

Let’s say you communicate performance feedback on the yearly performance review

In this analogy, the performance review is a “monolith” — it stores all the feedback information (and other things) and is the single tool used for performance communication.

In theory, it will contain the same information as much smaller feedbacks, and it will save time on delivery because it will be one time per year so what’s wrong with that?

To understand what is wrong we need to discuss the goal of feedback — to **change future behavior**. We cannot change the past so we shouldn’t care about it. We only care about future improvements.

If I know there is something wrong now, why wait to change it?  
If I know there is something good now, why not try to make sure it will continue?

The same way you keep moving your steering wheel left and right when you are driving to make sure you are on track we would like to give feedback in real-time and not wait until we hit a tree at the side of the road and only then steer left.

# High-level Design

Consider the following class diagram

![]()



We can deliver 2 types of feedback — simple and structured.

**Simple feedback**

Simple feedback will just be either praise (“good job on X” or “thanks for the effort”) or criticism (“X wasn’t that good” or “stop being late”)

Praise and criticism will be delivered similarly and will just state the action and was it good or bad.

**Structured feedback**

This is an extension of simple feedback. On top of addressing the behavior, we explain its effect and request further action.  
Positive and negative feedback will have the same structure and should be delivered the same, the only difference is in the required action. For positive feedback, we would request to keep it up (e.g. “really nice presentation, it really shows your technical expertise. keep it up”) and for negative feedback, we would request to act differently next time (“when you are looking at your phone for the entire meeting, it is disrespectful to the speaker. can you avoid that next time?”).

Please mind that StructeredFeedback is an **abstract class**. This means a concrete instance could either be positive or negative.

If you observed an action that had some good to it and some bad, decide what was more dominant and deliver positive or negative feedback accordingly.

For example, if your employee solved a complex problem but “gold plated” it a little just give good feedback.

***Don’t say\*:*** Great job on feature X, **but** next time try to finish faster  
***Do say:*** When you solve such complex problems, it makes me appreciate your skills. good job!

\**Most people getting this feedback will feel like the overall feedback was negative even though the feedback giver meant it to be positive*

# Single Responsibility

SRP is one of the most important principles when designing software — make sure each function/class/component has a single responsibility. If you need convincing that SRP is important you can watch [this video](https://www.youtube.com/watch?v=tMW08JkFrBA) that shows how most SOLID principles boil down to SRP.

Feedback should also have a single responsibility — to change future behavior.   
Not to argue about the facts, prove you are smarter, blow off steam, make an example of someone or anything else.

For that reason, we only address the observed behavior when delivering feedback regardless of why it happened (“There is no Y in feedback”).

# DRY (Don’t repeat yourself)

A developer and a product manager are both given a task — boil water with a pot faucet and a stove. The product manager takes the pot, pour water in, puts it on the stove, light it up and wait for the water to boil.

The developer does the same (after spending some time on the whiteboard creating a design)

Both are now introduced a similar task — the pot is already filled with water and on the stove and the goal is the same — boil the water.

The product manager lights up the fire, the developer throws away the water and puts the pot next to the sink because he already has a solution for that problem.

The point of the joke was that developers like to re-use code, i.e. don’t repeat themselves. As developers, we should strive to not repeat ourselves also when giving feedback.

Every feedback is a pure function (functional programming FTW!) that only addresses the current observed behavior — *“when you do this, that is the outcome, can you continue/change it?”*. No point in dwelling on the past and bring up feedbacks we already gave over and over again\*.

*\*Sometimes that doesn’t work — the next topic will address that*

# Error handling

As in software, we cannot look only on the happy path, we need to make sure our solution is robust and handles exceptions gracefully

I’ll address the major ones each on its own:

**1. Message not delivered/respond not clear (IO Exception)**

You gave the feedback and instead of listening, the employee tries to argue about the facts, is unwilling to respond or any other defensive behavior.

Here is the error handling code

```
try{  
   giveFeedback(employee, content)  
}catch (Exception e){  
   console.log('You know what? Maybe I was wrong nevermind...')  
}
```

In case you didn’t get my clever analogy (😜) — do nothing and walk away.

If the same behavior will happen again give new feedback if it never happens again, no need to do anything

**2. Endless loop (OOM Exception)**

You gave feedback, requested a change, the employee agreed but these 3 steps keep repeating themselves for the same behavior.

The solution is simple — you should give “systemic feedback” — feedback on the behavior of agreeing to change and not acting on it (regardless of the original behavior).

Giving multiple systemic feedbacks in a row should happen very rarely and when it does it might be a good sign you will need to separate ways with that employee.

**3. Resource not available (404)** — If the employee is in a hurry, very stressed or anything else that makes him unavailable for feedback don’t give the feedback, it will not be effective. If the same behavior will happen again give new feedback. If it never happens again, no need to do anything (sounds familiar?).

If this keeps happening (employee doesn’t have time for feedback), give feedback on not being available. Like the previous error, if you find yourself giving much feedbacks on not being available in a row it is a bad sign.

# Services communication

In a microservices architecture, we can send broadcast messages to other services but if we want to ensure the delivery of the message we would probably do a REST call to a specific service.

Another important concept is message versioning, to reduce coupling we want to support multiple versioning to match different services so that we can change the message without having to re-deploy all microservices at once with the new schema.

Similarly, when giving feedback we should avoid giving group feedback and prefer to do it in person. On top of making sure the message is delivered, we can customize the message (versioning reference 😉 ) to match each individual.

Someone might be motivated by the influence his behavior had on his teammates and someone else might be motivated by the effect of the same behavior on how he is perceived by management as ready for promotion.

Coming back to the messaging analogy I want to talk about delivery capacity. If you have some message bus or queue used to send messages to services, you need to make sure messages are delivered to services faster then they are written to it. If you don’t, you will have an always increasing backlog. This is problematic for 2 main reasons:

1. Some messages will not have meaning if they come too late
2. Backlog has a finite storage space and at some point, data will be lost

So when you have something to say to your employee as a manager, don’t put it in the backlog, deliver it as close to the observed behavior as you can. The longest you should wait is until the next weekly 1:1 meeting you have with them.

# CI/CD

When you write code you should write small PRs (pull requests) with a specific context. After you write it you want to deploy it to production easily with a clear process that everyone understands and follows.

Companies that do CI/CD well take pride in the fact they push small features to production several times a day.

To be able to do that you should make sure your deployment pipelines are short, stable and effective — it is very hard to deploy multiple times a day when the build takes 3 hours to run or fails 3 out of 5 times.

Now let’s apply the same logic on feedbacks.

* Each feedback should be small, quick (~10 sec.) and have a specific context and purpose
* The process of delivering feedback is clear and well known (same structure)
* We give feedback to employees several times a day (or at least several times in a week)

# Documentation

We all know that documentation is important and we all hate writing it (or is it only me 🤔); Understanding the value it can have sometimes helps with the motivation.

Writing down what feedback you gave (I use 1:1 notes for that) helps when you want to have an assessment over a long period. It can be for performance review, promotion consideration or firing consideration.

I usually write down something like this:

> PF/NF — <behaviour>, <effect> — <response from employee>

# Build on strong infrastructure

For our system to be stable productive we should invest in the infrastructure. Without a solid infrastructure, every change you make can cause so many problems that you feel like you are taking 2 steps back for every step forward (I’m sure many of you can think of system they worked on that behaved like this).

For systems, a good infrastructure would be clear architecture, high test coverage, monitoring, etc.

For people, a good infrastructure would be **trust** and **positive** reinforcement.

[Harvard research](https://hbr.org/2013/03/the-ideal-praise-to-criticism) shows that positive feedback should be about ~80% of the feedback you give. Intuitively you can imagine what will happen to an employee getting mostly negative feedback, will it make them feel like they are appreciated and be motivated to produce more for the team? Or will they just stop listening?

Feedback in general works best when there is trust. When employees know their managers care about them and want them to succeed they are more likely to actively listen and not get defensive.

# Release plan

When planning the next releases of our project, we would generally start with the most requested features first and then add the rest after the users got used to the system to build user trust and to encourage adoption.

For major releases, we would usually want to notify users in advance and roll out first to alpha and beta clients that we know are more adaptable to changes.

Similarly, if we intend to change our management style we should notify employees in advance and we should start by only giving positive feedback (or praise) to our top performers. we will continue with giving positive feedback to everyone and when we all feel comfortable we will add negative feedbacks as well.

# Summary

Feedback is one of the most important tools we have as managers to increase productivity and motivation in our teams.

I tried to use software best practices to make my suggestion more amusing and hopefully more memorable but here the main points in plain English in case my analogies weren’t as clever as I thought

1. Focus on **behaviors** — what the employee **did**, avoid speculation on why
2. Explain the **effect** of the behavior and **ask** to keep it up/change it
3. Remember the goal — improving **future** behavior
4. Give **plenty** of feedback, most of it **positive**
5. Keep it **short** and **casual** (preferably same structure always)
6. Modify the message to **match the recipient**
7. Best to deliver **as close** to observed behavior **as possible**
8. Roll out **gradually** — start with **top** performers and **positive** feedback

As I mentioned briefly in one of the paragraphs, feedbacks work best when there is a good relationship between manager and employee. A great way to achieve that is by having weekly 1:1 meetings but that is already a different topic

# Additional Information

I highly recommend [Manager Tools](https://www.manager-tools.com/) as a source of information. They have a free podcast which is great and also a [book](https://www.amazon.com/Effective-Manager-Mark-Horstman/dp/1119244609), conferences all over the world, training sessions and more.

We also have a pretty good internal management course in Nielsen but you will have to get hired here to go.