---
title: '::..: glen.nu :.: ramblings :.: on code review :.::'
date: '2015-10-20T11:16:34-06:00'
format: link
service: instapaper
tags:
- read
external_url: http://glen.nu/ramblings/oncodereview.php
---

[::..: glen.nu :.: ramblings :.: on code review :.::](http://glen.nu/ramblings/oncodereview.php)  



 *I wrote this in March 2014 when I was managing the User Lookup Service team at Twitter, to codify our theory of and approach to code review, and to try to establish some basic best practices. It’s not intended to tell you or your team how to operate, merely to describe how I think about it, and how important I feel good, timely code review is to both the quality and throughput of a team’s code.*
# TL;DR

1. Code review should probably always be your top priority, and you should figure out the best way to work it into your event loop.
2. Make your review requests a pleasure to read.

I believe that the single most important thing a team can do collectively to improve its throughput is to make code review a (or better yet, the) top priority for all team members. This is the most compelling and concise reason I could come up with, so I’ll call it out as blatantly as I can:

> Pending code reviews represent blocked threads of execution.

In the best case, an engineer blocked on code review is able to make progress on some other change, at the cost of (1) context switching and (2) increased memory allocation. Some engineers are great at this, but the more changes you have in the air, the more total memory is required, and if some of that gets paged out, the context switching gets expensive.

In the worst case, an engineer blocked on code review can’t make any progress at all, because the work allocated to him/her is serialized on the review. I do my best to make sure everybody has a few potential threads of execution available to them, but sometimes this isn’t possible and in this case code reviews amount to synchronous barriers to getting other work done.

As a team, we all depend on one another to get work done so we can efficiently meet our goals, and often this work cannot be completely parallelized. We’re often blocked on infrastructure shortcomings, or work from other teams. If we think in terms of what we ourselves control, when we are blocked from making progress on a given task, we are generally either blocked on someone writing code or on someone reviewing it.

We can’t limit total work in progress unless we also limit total reviews in progress, and the best way to do this is for everyone to review code in as timely and careful a manner as we can.

So assuming I’ve sold you on the premise, how do we make this happen? I believe there are things we can do both as reviewers and submitters to make our code review process as efficient as possible.

# Reviewers

### Make sure you know what reviews you’re on the hook for

Have a simple way to find all the pending reviews that someone (or some automated tool) went to the trouble to put your name on. I haven’t personally found reviewboard to be particularly useful in this regard, and have ended up depending on plain old email. I won’t presume to tell you how to filter your mail or what tools to use, but make sure you have a fast way to find reviews for which you, specifically, owe time.

### Shorten your event loop; When possible, be interrupt-driven

Armed with a method to quickly find out what code you need to review, try to integrate invocation of that method into your event loop, with the platonic ideal of being able to handle code reviews as they arrive. Everybody needs focused time to get their work done, and switching from a tight compile/test/code eval loop into a code review cycle is not free; But weigh the cost of these context switches against the larger switch you have to make when you’re blocked on code review. Do put off a code review for a few minutes while you finish a thought. Don’t put it off for a day or for more than a few hours; If you have time to get up to eat or go to the bathroom, you probably have time to run through your code reviews before paging your code back in.

### Prioritize code review above your other work\*

\*except for outages, and customer service

This is sort of a combination of my previous two points, but I think it bears specific attention: for reasons I hope I made clear in my preamble, threads of execution are blocked and unproductive while code reviews are pending. If you let code go unreviewed, you are explicitly prioritizing your productivity over the productivity of the rest of the team. If everyone on the team is operating at 75% efficiency because they are spending 25% of their time in code review, that is a better outcome than some members of the team operating at 95% and other members idling or thrashing.

If you have nothing to say, then say that! If your name is on a review, you should at least acknowledge it with something like “LGTM, but I don’t really know this code well.” The key point is to minimize the time between outgoing and incoming activity on the review, so nobody’s ever blocked for more time than is strictly necessary.

### Expect to spend time on code review every day, throughout the day

A question that comes up in 1:1s from time to time is “how much time should I be spending on code reviews?” The short answer is “as long as it takes.” Minimally, your day should begin and end with clearing your code-review backlog. Ideally you find time to clear the backlog at least once or twice in between. Inbox zero is the goal here, and I don’t think it’s unreasonable to spend 1-2 total hours a day on getting there.

### Be thorough, each and every time.

The only thing worse than no code review at all is a single good code review broken into many smaller reviews over days. It’s the submitter’s job to publish code reviews that are well-formed and and carefully crafted. It’s the reviewer’s job to be as thorough as possible in the each pass, rather than metering out their feedback in a series of partial reviews on multiple revisions. If a review drags out into many revisions, it’s sometimes because it started out sloppy, but it’s often because reviewers didn’t pay enough attention the first, second, or third time and missed things. This is something I continue to work on, and it’s hard to be consistent about. If you catch something late in a review cycle, own up to it, and apologize.

# Submitters

### Dot your i’s and j’s

In exchange for your reviewers making code review their top priority, make sending out a good code review yours. Carefully review your own code in the reviewboard draft before publishing. Make sure there’s nothing missing from the change, and nothing unnecessary. Make sure you have, to the best of your ability, written code you like and which conforms to the style guidelines (or local examples) of the project you’re working in. Don’t post a review and then immediately post multiple revisions as you find problems; this will confuse and bewilder your reviewers. If you don’t like what you see, discard the draft review before publishing, fix the change, and start over.

### Keep reviews as small as possible

Bias to small, digestible reviews. When possible, try to break down your large refactor into smaller, easier to reason about changes, which can be reviewed in sequence (or better still, orthogonally). When your review leaks out into a second page (or even to more than a few files), ask yourself if it can be compartmentalized. If everyone is efficient at reviewing code as it is published, there’s no advantage to batching small changes together, and there are distinct disadvantages. The most dangerous outcome of a large review is that reviewers are unable to sustain focus over several pages of changes, and the code isn’t reviewed well or at all.

### Write good titles and descriptions

Your title should distinguish your review clearly in a list of other reviews in someone’s inbox. Your review description should tell the story of your change. You should talk about why you’re making the change, what problem you’re solving, what code you changed, what classes you introduced, how you tested it. It should not be a list of checkpoint commits with a vague title. It should tell the reviewers what specific pieces they should take extra care in reviewing. Your reviewers will thank you for making their job easier by explaining to them what they should be looking at, and their reviews will be correspondingly more thorough.​

### Acknowledge comments quickly

A tight event loop is even more important when your code is out for review; Do your best to acknowledge comments as quickly as you can, and particularly to ask for clarification if you don’t understand the comment or want to push back on it. As soon as a reviewer clicks “Publish Review,” the action is back on you. If the change is straightforward and small, post a new review quickly, to keep the ball rolling. The more quickly you are able to respond to comments and defects, the more likely the reviewer is to still have them paged in, and the more quickly you’ll arrive at consensus.

# The End

If you made it to the end of this, I really appreciate your reading it. You probably now have at least one pending review request.