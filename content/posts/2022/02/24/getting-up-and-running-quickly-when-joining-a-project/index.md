---
title: Getting Up and Running Quickly When Joining a Project
date: '2022-02-24T14:07:24-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://thoughtbot.com/blog/getting-up-and-running-quickly
---

[Getting Up and Running Quickly When Joining a Project](https://thoughtbot.com/blog/getting-up-and-running-quickly)  



Getting up to speed when you join a large project is not an easy thing to do.  

In addition to astonishing amounts of code and history, joining a new project  

usually coincides with getting to know new colleagues and wanting to cause a  

great first impression, which raises the stakes and makes things even more  

difficult.

Here are a few things that have worked best for me when trying to get up to  

speed as quickly as possible on the projects I’ve joined over the past few  

years.

## 

Accepting you will never know everything can be a liberating thing. I like to  

remind myself that every situation is unique, and each project is built by  

the people and circumstances around it. That way, I feel less pressure about  

needing to know how a system operates from day 0. How could I?! With enough  

people in the project, you may also not be able to keep track  

of everything that’s been going on even after working on it for years.

At least for me, high-level views of a system and its architecture very seldom  

help while getting started. I prefer to accept it’s impossible to learn  

in two weeks everything about a system that took thousands of hours of work to  

come to its current state. Maybe that’s because I can only keep one thing at a  

time in my head.

However, keeping only one thing at a time in your head might be pretty effective  

when solving problems. It’s easy to get overwhelmed by many unknowns and not  

know what to do. Still, if you’re able to narrow your exploration to one problem  

at a time, you might be successful in solving that problem, and by the time you  

have solved that problem, you will have built knowledge about one specific user  

flow within that system.

That’s my preferred way to get acquainted with complex systems: one small step  

at a time.

My tips are:

1. Ask a lot of questions
2. Start by trying to solve a bug
3. Take notes as you go, especially about what slowed you down
4. Do not make any assumptions
5. Follow the logs

## 

Leverage your ignorance, and go at it with curiosity. When you encounter a term  

you don’t understand or some system behaviour that surprised you, ask a team  

member about it. You can use tools like [git-blame](https://git-scm.com/docs/git-blame) to figure out with whom to talk.

It’s important to try to be as positive as possible about it. There are probably  

valid reasons why some code you’re reading turns out to be complex, but asking  

“Why are we doing this?” might make the authors feel judged. You could say  

something like “I don’t understand what this means. Would you mind helping me  

out?” instead.

## 

With the help of a teammate, pick a bug to solve. Try to maximise first for  

impact and second for how difficult it appears to be.

That last bit might seem counter-intuitive: you may be eager to deploy some code  

you authored as soon as possible to make your presence felt. However, a good ol’  

bug can teach you a lot about an application, and solving it will often require  

you to have access to many systems. That’s an excellent opportunity to put the  

onboarding process through a test. Ideally, this will uncover whether you have  

access to:

* Application logs
* The systems the app uses to monitor errors and performance
* Obfuscated / encrypted data
* All code repositories you might need so you can reproduce the bug
* The platforms used to store relevant information (such as Trello, Jira, Google  
  
  Docs, etc.)

At this stage, you might find opportunities to improve the onboarding process  

for folks coming into the team if you remember to document your pain points.  

And that leads us to my next bit of advice:

## 

As soon as you find you are missing access to a tool you need to do your job, it  

might be tempting to request access and keep moving forward. However, if you do  

that, the next person coming into the project may run into the same issue. Even  

worse: the next person joining the project might not even consider that your  

team has a system for documenting decisions or for monitoring the app’s  

performance, and they might start making assumptions to get on with their work,  

which would directly contradict my next piece of advice.

Talk to others in your team about the things you’ve noted. Try to document the  

issues you overcame and how others can do the same. If you were not able to  

succcessfully address some of these things, It might be a good idea to bring  

them up in retros.

## 

The above is perhaps the most powerful advice I have to give when developing  

software and the most challenging thing to follow.

We make assumptions all the time in our lives, but when dealing with  

one-of-a-kind systems, assuming we understand what is happening in those systems  

might be where we waste most of our time and effort. If I’m being honest, I’m  

incapable of following this rule myself, but it’s something I strive to.

[Bugs usually come from flawed assumptions](https://thoughtbot.com/blog/debugging-listing-your-assumptions), and it’s not a  

stretch to think that someone trying to solve that bug might be making the same  

assumptions that introduced the bug in the first place.

Instead of guessing, make sure you know what’s happening. If you can’t reproduce  

a behaviour, it will be hard to fix the problem, and at best, any attempts you  

put forward will come from educated guesses.

To stop guessing and reliably replicate the behaviours observed in production,  

you will need to follow the logs.

## 

Some bugs only appear with the perfect concoction of stale data, a user  

interacting with an interface in just the right (or wrong) way at just the right  

(or wrong) time on the right (… or wrong) device.

Without a system to aggregate and categorise your logs, it is next to impossible  

to solve this type of bug. Having all of this in place will make it possible,  

but it doesn’t mean it will be easy. With that said, the logs will tell an  

important story that may teach you a lot about the system in question. They  

might show you which endpoints are called as the user interacts with the  

system and which endpoints are called by your system due to that interaction.

Again, it’s paramount not to make assumptions here. Follow the stack traces  

carefully, and you might find what state the application needs to be in for the  

bug to manifest. You will then hopefully be able to reproduce the issue and  

be a step closer to finding out why the problem happened in the first place.

## 

I hope these methods can inspire you, but different people work in  

different ways. While the workflow I am suggesting here works well for me,  

it might not suit you. My goal is not to evangelise these ways of working but  

to cause you to think about what works well for you and maybe pick a thing or  

two out of the advice I’m offering.