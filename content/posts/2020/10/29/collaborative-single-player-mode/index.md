---
title: Collaborative Single Player Mode
date: '2020-10-29T21:06:12-06:00'
format: link
service: instapaper
tags:
- read
external_url: http://blog.rstankov.com/collaborative-single-player-mode/
---

[Collaborative Single Player Mode](http://blog.rstankov.com/collaborative-single-player-mode/)  



The Product Hunt engineering team has always been remote and it’s surprisingly small for all the features and products we are shipping. One of our “secret” weapon for this is what we call “collaborative single-player mode”.

The single-player mode was something I heard for the first time from [Andreas Klinger](https://twitter.com/andreasklinger), the previous CTO of Product Hunt. He often [talks about it](https://www.youtube.com/watch?v=EKSGhOBnRPw&ab_channel=RunningRemote).

The core of the idea is simple – everyone should be able to execute without depending on other people. Especially in a remote environment, when people work at different times, this is essential.

The “Collaborative” prefix is my extension to “Single Player” to signify that we work as a team, not just as individuals.

*The following is literally copy-pasted from our engineering principles document* 😎

## Process

The process is not about blindly following procedures. It is about having:

* **Automatic decisions for trivial questions**
* **Eliminating blockers**
* **Making it obvious who owns which decision**

*The way we work is not set in stone. When you have ideas on how we can improve – share those with the team.*

![](https://rstankov-blog.s3.amazonaws.com/collaborative-single-player.png)![](https://rstankov-blog.s3.amazonaws.com/collaborative-single-player.png)

## Single Player Mode

A developer should be able to execute a feature from start to finish — from the database to the backend, API, frontend, and CSS. The goal is never to get blocked.

* If you are missing a design, mock the UI, designers can fill this in later
* If you don’t know how to do something technically, hack it or fake it
* If a product decision is missing, try to make this decision yourself – it’s better to ask for forgiveness rather than permission

## Enablers for single player mode

To have a sustainable work pace and produce a consistently high-quality product done in Single Player Mode, we have the following enablers

### Ownership

You own whatever you are working on. At PH, we treat people as capable, independent knowledge workers.  

If you work on something, you drive decisions.

* Take a feature and find solutions
* Pull in people you need for feedback
* Suggest solutions if you can

What to work on?

* Whenever unsure what you should pick to work on, go for “impact”
* What is the thing with the most significant effect I could work on right now? – Work on that

### Small checkpoints

* We use trunk driven development
* A demo is worth a thousand words, and a working prototype is worth a hundred demos
* Get feedback from the team early and often
* Try to get the feature to production as quickly as possible.
* Split feature into multiple smaller releasable features
* Always start a feature with a feature flag and try to get something to production on day 1
  + even if it’s only feature flagged to you
  + usual feature flag timeline
    - week 1 – developer and people interested in a feature
    - week 2 – all admins
    - week 3 – release or do beta with users

### Coding best practices

We play in single-player, but collaboratively.

* Follow the coding rules
* At least one fellow developer should see every code change
* Write tests
* Prefer explicit code
* Write code as if you are going to remove it tomorrow
* If code style can’t be enforced by linter, don’t argue about it
* Automate decisions
* Look for places where reusable utilities or components can be extracted and used later
* We do not optimize for speed or quality – we optimize our codebase for confidence
  + For the next person to make changes
  + For everyone to be able to reason about it
  + For everyone to be informed enough to ask questions (leave your name next to notes)

### Boy-scout rule

[Leave the code cleaner than you found it](http://wiki.c2.com/?BoyScoutRule) or better said, pick up any trash lying on the floor.

Clean up code as you go and develop more code. If you don’t, you will find yourself in a mess shortly (much more likely than camping sites).

* Any mistake you leave – is now also your mistake
* Any “wtf-moment” you run into is a chance to avoid that for the next person (add notes, introduce best practices)
* If you can’t take ownership, then we most likely have a more significant structural (process) problem at hand. Please address it to the team
* Don’t ask if you can refactor
* We have an old application, some of the rules and conditions of the system have changed, and the code doesn’t always reflect that

### Data driven decisions

When possible, always make sure you are backing your decisions with data.

* Try to validate if the feature is worth being developed
  + use experiments to see if there is a demand for a feature
    - example: Ship custom domains, Google login
* Always set up metrics for your features to make sure users use those as expected
* When I doubt do an A/B test
  + try to understand the result from an A/B test and validate with follow up tests

## Conclusion

During the years, Product Hunt has changed a lot. There have been many product, process, and team changes. So far, those principles have stayed relatively stable.