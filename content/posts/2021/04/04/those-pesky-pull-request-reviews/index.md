---
title: Those Pesky Pull Request Reviews
date: '2021-04-04T11:48:32-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://jessitron.com/2021/03/27/those-pesky-pull-request-reviews/
---

[Those Pesky Pull Request Reviews](https://jessitron.com/2021/03/27/those-pesky-pull-request-reviews/)  



![](https://i0.wp.com/jessitron.com/wp-content/uploads/2021/03/File-Mar-27-9-15-51-AM.png?fit=1200%2C913&ssl=1&resize=40%2C40)![](https://i0.wp.com/jessitron.com/wp-content/uploads/2021/03/File-Mar-27-9-15-51-AM.png?fit=1200%2C913&ssl=1&resize=40%2C40)

They’re everywhere. In Slack: “hey, can I get a review on this?” In email: “Your review is requested!” In JIRA: “8 user stories In-Progress” (but code-complete). In your repository: 5 open pull requests. They’re slowing your delivery. They’re interrupting your developers.

#### How can we get people to review pull requests faster??

We could [blame the people](https://twitter.com/dkubb/status/1372219111451762693?s=21). We could [nag them more](https://twitter.com/sacodergirl/status/1372054037110067206?s=21). We could even [automate the nagging](https://twitter.com/karaluton/status/1371976632215465984?s=21)!

Let’s face it: nobody wants to review pull requests. And for good reasons! It takes a lot of time and work. Chelsea Troy describes how to do pull request review right:

> In addition to pulling down, running, and modifying the code myself… A maximally effective pull request suggests solutions…*in code*. It points out what’s working and what’s not, and links to documentation where useful. It highlights laudable work by the original developer, and asks questions before making assumptions or judgments. It explains the reasoning behind suggestions, whether that reasoning affects functionality or adheres to convention. In short, it demands the reviewer’s full participation in finishing the solution that the original developer started. And it prepares the reviewer to take responsibility for this code in the event that the original developer were unable to complete it.
> 
> [Reviewing Pull Requests – Chelsea Troy](https://chelseatroy.com/2019/12/18/reviewing-pull-requests/)

Reviews, [done right](https://chelseatroy.com/2019/12/18/reviewing-pull-requests/), have all the painful parts of a software change: understanding what the change is for, loading up the relevant code and tests into working memory, getting my local environment up to see the change, making the tests run. They have none of the fun parts: refactoring to clarity, changing code and seeing a difference. They take hours of time and all my concentration away from whatever it is that I’m personally trying to do.

On top of that, they’re a social interaction minefield! This variable name confused me at first but now I see why they called it that. Should I suggest a change, and require the other developer to do a whole context switch again to improve it? Probably an asshole move. This test doesn’t cover all the cases; I can see one that’s missing. Request another, like the pedant I am? or figure out how to write it myself, adding another hour?

There’s a cost to every comment, a cost to the submitter’s sense of belonging. A responsible reviewer looks at consequences far beyond the code.

Of course I never want to review pull requests. It’s mentally taxing, takes a lot of time, might damage relationships, and gets me nowhere on the task that has my name on it.

So the twitterverse is asking, how do we get people to do it anyway?

> What makes it easier to do work that is not centered on your immediate priorities?
> 
> — christina b. just one planet (@csageland) [March 18, 2021](https://twitter.com/csageland/status/1372375886926807043?ref_src=twsrc%5Etfw)


If this is what we’re asking, maybe something is wrong with our priorities.

#### Maybe we’re asking the wrong question.

What does it say about us that no one wants to review pull requests?

> What is powerful question that sits above this more specific question? <https://t.co/jxvuOTFUtO>
> 
> — John Cutler (@johncutlefish) [March 18, 2021](https://twitter.com/johncutlefish/status/1372373908129677315?ref_src=twsrc%5Etfw)


Maybe it says that we trust each other.

> Hot take: in-house development has been influenced too much by the GitHub open source PR driven development process. A process driven by zero trust doesn’t fit well in a team with trust.
> 
> — Patricia Aas, MSc. (@pati\_gallardo) [March 20, 2021](https://twitter.com/pati_gallardo/status/1373343835330383878?ref_src=twsrc%5Etfw)


Maybe it says that our team has too many concurrent tasks. And by “too many” I mean “more than one”!

#### We use pull requests to ensure code is understandable by the whole team.

What is our goal with this pull request process? There are several, but I think the primary one is: safe, understandable code. It looks safe to deploy, and it is clear enough to be understood by the rest of the team. Tests can give us confidence is safety, but only a person can evaluate “understandable.”

To change code, a developer first has to understand the code, and understand the change. If the developer was the last person to change this code, then they just have to load it into memory. They’ve understood it before. This should also be true if they reviewed that last change — pull request review spreads that understanding a bit.

A developer gathers this knowledge, then uses it to make decisions about the code. They probably iterate on it a few times, and then they submit something they consider safe and understandable.

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

But is that code really safe and understandable?!? We must ensure it! Let’s add this whole process again, except the decisions are approval instead of what to change. We’ll make this asynchronous, yeah, so the submitted can start a whole different task. And if the decision is “no” then we’ll make another asynchronous task and everybody can context switch again!

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

This defies everything we know about product development flow. We just increased WIP and slowed our response time by adding a wait into the process (at least one wait, really an indeterminate number).

### To improve flow, eliminate queues.

Like Patricia said, maybe this process developed for open-source projects isn’t the best for our in-house teams. Maybe there are better ways to work together.

The pull request process results in code that two people understand. What if we aimed higher?

#### Maybe instead of trying to work a *bit* more together, we could *work together*.

How about: the team makes all code changes as a unit. Ensemble working (the practice [formerly](https://www.lisihocke.com/2021/02/ensemble-is-the-new-mob.html) known as [mob programming](https://www.agilealliance.org/glossary/mob-programming)), with one shared work product and all the shared knowledge. It will be as safe as everyone can make it, and more than understandable: it’ll be understood by the whole team.

Not every team member will be present every day. Let’s take a page from distributed systems and require a quorum of team members present when we make code changes. At least 2 developers on a team of 3, at least 3 on a team of 5, etc. That way, whenever it’s time to change that code again, someone present was involved in the most recent change.

Then there are no queues or waiting, only collaborating on getting the best name, the complete-enough test suite. Every refactor increases the whole team’s understanding of the code. The team develops a common understanding of the code and where it is going, so they can do gradual improvements in a consistent direction.

Does that sound inefficient? Consider the inefficiencies in the queuing for pull requests, the task switches. Not to mention the merge conflicts we get after the pull request sits open for days.

Does it sound wasteful? All that programmer-time dedicated to just one task, when we could be doing three! Well, ask: which of those three is the most important? Why not get that out as quickly as possible and then work on the others? And it is faster, when you never have to ask permission or wait for answers because all the relevant knowledge is right there. (It helps to bring in other people too, when you need knowledge from an adjacent team or specialist.)

Does it sound miserable? Many people hate pair programming; this sounds even worse. Strangely though, it’s better. When there are three or more in a session, there’s less pressure to stare at the screen every second. One person’s attention can wander while the group attention stays. A person can go to the bathroom or answer an urgent question on Slack, while the ensemble remains an ensemble. Pair programming is more exhausting.

Does this seems like an all-day meeting? No, only when we’re changing code. There’s a lot more we do in a day. There’s still email! Each of us has knowledge to acquire and knowledge to share with other teams. I only have six hours of focused brainpower in me on a day. I’d aim for five hours of direct collaboration, and not change production code outside of it.

Does this seem impossible remote? It is harder. Set up a shared development environment that everyone can [connect](https://devblogs.microsoft.com/visualstudio/introducing-visual-studio-codespaces/) to for switching. Or start a branch and use git to move code around. Turn your video on, but set up a screen and camera over to the side, so that looking at each other is different from looking at the code. Staring at each other is draining. Working alongside each other is invigorating.

(TODO: take a picture)

Is your team too large for this? It does get ridiculous with 8-12 people in one meeting. That’s a smell: either your application is too big (it takes that much knowledge); can you split it? Or, someone thought adding people would speed the work. This is a classic [Mythical Man-Month](https://en.wikipedia.org/wiki/The_Mythical_Man-Month) problem.

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

coordination problems increase nonlinearly O(n!) with the number of people


When working together eliminates all the coordination work and merge pain, the team can be smaller and more responsive.

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
#### Piles of waiting pull requests are a symptom of disparate goals within the team.

When we divide tasks among people, we can say “we’re working on it” about several things at once. Is that something your organization wants? If so, then it is holding your team back from focus. If this is the organizational API you need to meet, try marking five tasks “in progress” in JIRA, then working one at a time together.

> Why is knowledge work being treated as an individual activity?
> 
> The “output” of knowledge work needs to include shared organizational expertise, and individual work doesn’t get us there.
> 
> — Michael McCliment (@cornazano) [March 18, 2021](https://twitter.com/cornazano/status/1372384282300317698?ref_src=twsrc%5Etfw)


The team works most smoothly as a unit. Production software needs a team behind it because so much knowledge is required: the purpose of the software, its customers, its interfaces, all the tech it runs on and the data it stores and all the changes in the world (such as vulnerabilities) that it needs to respond to. It takes several people to hold all this, with redundancy. To change software safely, combine all that knowledge. We can do this efficiently together, or painfully alone: asynchronous, with a lot of coordination and unpredictably stepping on each other.

#### Pull requests are an improvement on working alone. But not on working together.

We know that code review improves outcomes– compared to coding alone without any review. Don’t do that. Do code together — with constant, live review and growing understanding between the team members and the code, between the team members and each other.

Leave the pull requests for collections of individuals sharing a codebase. Give me direct collaboration on my team.