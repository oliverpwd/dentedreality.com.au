---
title: Why We’ve Ditched Scrum Sprints (And You Should Too)
date: '2022-05-23T08:21:17-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@michalikmartin/why-weve-ditched-scrum-sprints-and-you-should-too-cdf5678e5199
---

[Why We’ve Ditched Scrum Sprints (And You Should Too)](https://medium.com/@michalikmartin/why-weve-ditched-scrum-sprints-and-you-should-too-cdf5678e5199)  



![](https://miro.medium.com/max/1400/1*UaCE2TKd-EkA95KVYGmW4A.jpeg)![](https://miro.medium.com/max/1400/1*UaCE2TKd-EkA95KVYGmW4A.jpeg)

*There’s probably no other framework that impacted modern software development as much as Scrum. For many organizations, it’s the first step towards a mature product development organization and you will find a bazillion articles explaining what Scrum is and how you can implement it in your organization. I dare to say it’s so popular that almost every software organization tried at some point to implement one of its core principles — the two-week sprints.*

*While I totally recognize the principles on which the scrum sprints are built, their implementation by-the-book wasn’t good for us. And in this article, I want to talk about problems we saw with the traditional two-week scrum cycles and why we decided to ditch the scrum sprints altogether.*

## It’s just way too short

The first problem was also the root cause of the majority of other problems we saw — the two-week cycle is way too short to build **meaningful** **functionality**. Yes, you could argue that Scrum doesn’t necessarily dictate the length of the sprint cycle, but most organizations I’ve had the pleasure talking to, opted for the two-week cycle.

Now, you could argue that if you’re a startup in “feature-race” mode, then a lot can be done in two weeks. But I dare to say that if your product is a mature platform with functional dependencies you’ll have a really hard time building something meaningful that you can ship to your customers at the end of each sprint, especially if your teams are on the smaller side (5 people and less).

Moreover, shorter sprints suffer from any “further shortening” such as public holidays, vacations, mandatory all-hands meetings & training, or illness in the team. You will also experience increased overhead that is connected with all the ceremonies that are part of the Scrum.

As a result, there’s a high chance that you will be forced to spread the needed development work over several sprints. Unfortunately, this will make the predictability of the final release date & scope of the new functionality quite challenging and will complicate communication and coordination with other departments that are essential for the launch success. Most importantly, spreading the release over several sprints leads to another, more serious problem….

## You’re not working on the most important thing

Based on the interviews I had with numerous Product Owners, it’s not rare that the usual sprint planning looks as follows: You take the team’s velocity and start filling the sprint with estimated stories. At a certain point, you hit the limit which is either the team’s velocity or an artificial ratio that you have in your organization (eg. only 70% is dedicated to working on new functionality, the rest is maintenance) so the next most important stories won’t fit in. Now, what do you do? You fill the rest with bugs, technical debt, other less important stories. Or even worse, you start adding stories from another project.

If you do that — congratulations, **you just killed your team focus!** Without the focus & clarity on priorities you can expect that some less important things are going to be addressed first, some major stories are going be delayed and you shouldn’t be surprised if in 3 sprints you feel like the work on the solution to the customer problem is dragging forever. I know that because I’ve been there too.

**Not having one clear goal for a development iteration is for me the most dangerous risk of software development.** If your teams don’t have clarity from you as a product leader on what is priority number one, you’re only preparing for chaos, future delays, and team problems. That’s why I am a strong advocate of teams having only one problem to solve at a time and why I can 100% recommend separating build and maintenance work into different product development iterations.

## The focus is often on closing stories, not solving the problem

Another of the traps I have seen many organizations fall for is focusing on “closing all the stories” instead of asking whether you’ve actually reached your objective. We’ve been guilty of this sin as well. Our understanding of the customer’s problem was measured by the number of estimated user stories in the backlog. Our retrospectives focused on why we had user stories overflowing into the next sprint. Our success was measured in the number of timely closed user stories.

And you know what? Your customers don’t care how many story points you delivered in the last sprint, how many stories were closed on time, and how your burn-down chart looked like. All they care about is whether the problem they told you about “3 sprints ago” is finally solved and when they can expect it to be released.

Don’t get me wrong. I completely understand why you should split your work into smaller chunks and why it’s important to focus on closing them. However, if you focus on closing the artificial units of work too much, it’s easy to lose the track of the bigger picture. So next time, when you have your sprint retrospective, ask your team how closer are they to solving the problem rather than how happy are they with closing the stories.

![](https://miro.medium.com/max/1000/1*2nv947XNytsP71o6UIzqew.png)![](https://miro.medium.com/max/1000/1*2nv947XNytsP71o6UIzqew.png)
## The hard stops are killing your momentum

Scrum sprints are by definition fixed time-boxes that limit how much time you can spend working on a new value. And while I am 110% in favor of time-boxing the development time, I really dislike how many organizations approach it when implementing Scrum. In these organizations, the sprint can feel like an episode of Masterchef — with a ceremonial start everyone starts cooking simultaneously, the more time passes the more frantic the cooking is, and once the time runs out completely, everyone stops at the same time whatever they were doing and put their hands up.

But software development isn’t a culinary competition, it’s a complicated process that often involves solving complex problems with non-trivial solutions. And there’s no chance you’ll finish all your tasks at the same time. So what happens then? Some teams will take the next priority stories into the sprint that might not finish on time and thus hurt their own karma, some will not risk it and take less important work that they can finish on time, and some will keep working on the next priority but secretly. None of these outcomes is something you want.

That’s why I am much more in favor of sliding start and finish dates of the implementation time-box with a fixed release date (we release after each development time-box). This way some team members can be wrapping their work on the current release while others can be already working on the next big thing (with others joining them in a matter of single days). As long as the priorities are respected and we can keep the agreed release date, it’s fine by me.

# So, what’s the alternative?

My goal in this article wasn’t to bash Scrum and its principles and disdain it completely. I actually believe it’s a great foundation that even us leverage in our product development process. I wanted to pinpoint the problems that I see with following it “by-the-book”. And I think it would be only fair to also briefly describe how we do it in our organization.

We follow a continuous cycle of two-type iterations where each iteration has to have an objective defined before it starts. The first type is **Build iterations** that are 6–8 weeks long and their goal is always to solve some customer problem. The problem is captured in a “problem definition” resulting from our product discovery process that precedes the build iteration. During the iteration whole team solely focuses only on this goal and each build iteration is finished with a release into the production environment. After the release, the iteration smoothly transitions into the other type that is **Refine iterations.** These are up to 4 weeks long during which each team has time to address technical debt, bugs, or small UX improvements. Every two weeks, we sync with the teams on the progress and their main challenges, so we can adjust the course of action if needed.

![](https://miro.medium.com/max/1400/1*RV52D6e8UYXjYVUbEZOj1A.png)![](https://miro.medium.com/max/1400/1*RV52D6e8UYXjYVUbEZOj1A.png)

Kontent by Kentico’s development process in a nutshell

This process is obviously bringing new challenges and requires quite mature development teams, but it also eliminates the discussed challenges of scrum sprints. What was the thinking behind the design of this process is, however, content for another article…