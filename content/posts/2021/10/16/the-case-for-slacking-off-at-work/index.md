---
title: The case for slacking off at work
date: '2021-10-16T10:25:52-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://jacobsingh.name/the-case-for-slacking-off-at-work/
---

[The case for slacking off at work](https://jacobsingh.name/the-case-for-slacking-off-at-work/)  



![](https://images.unsplash.com/photo-1599640112391-06cf6a9d7c2a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDUxfHxsYXp5fGVufDB8fHx8MTYzMjkzNTkwNA&ixlib=rb-1.2.1&q=80&w=2000)![](https://images.unsplash.com/photo-1599640112391-06cf6a9d7c2a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDUxfHxsYXp5fGVufDB8fHx8MTYzMjkzNTkwNA&ixlib=rb-1.2.1&q=80&w=2000)

The word agile is pretty frustrating. Not because it’s the wrong word, but because it’s been so badly coopted it longer means anything.

At the heart of it, Agile software development is simply the practice of executing work in small batches, measuring the impact quickly, and then starting a new batch with that new information. It is quite simply **optimizing for learning.**

One of the biggest mistakes organizations make as they scale is they try to **optimize for utilization.** That’s a fancy way of saying “keeping everyone busy.”

Why is this a bad thing? Well, if everyone is busy, they cannot absorb any variance – the antithesis of agile.

Imagine a highway with 4 lanes where every car is going exactly 70km/h and all cars are 3m apart. This is optimum efficiency. We are using all the space available and the maximum number of people are going the maximum speed.

What happens when someone needs to change lanes to get to their exit?

What about an accident?

What if someone is driving 50 in one lane?

This is why we need slack. Traffic jams are not because there are too many cars – traffic jams are because there is variance, and not enough slack in the system to account for it.

**This post is an explanation of why slack is crucial for agility and lastly a proposal (the Slacklog) as a way to build meaningful, intentional slack.**

### The Theory of Constraints

While Elon Musk is planning to turn all our cars into robots, and that’s all well and good, it will be a long time before software companies pull off something similar. So we have to deal with the issue of multiple individuals and teams pulling from the same dependencies. Dependencies can be tools like “staging machine” or “database update” but they are more often people like “marketing department” or “QA tester” or “Front end engineer”

This brings up the central problem in manufacturing and in software development: The Theory of Constraints. This post will make no attempt to explain it. Go read “[The Goal](https://en.wikipedia.org/wiki/The_Goal_(novel))” or even “[The Phoenix Project](https://www.goodreads.com/book/show/17255186-the-phoenix-project)” or just “[The wikipedia page](https://en.wikipedia.org/wiki/Theory_of_constraints)” if you want more info.

Basic gist is: Your assembly line only moves as fast as the slowest part. Optimizing anything else just makes things worse.

## Not all projects are created equal

So back to **optimizing for utilization.** The tricky thing here is that in most organizations, there is **one project** which is 10x as important as all the other projects. Not all things are worth optimizing for. I love the google doodle team, but if they had a critical engineer who was required every time the search index needed to be updated, I think we all know what the right call would be.

But people are not fungible resources. You can’t just take them out of one project team and throw them in another. There is a context switch, there is a skill mismatch, there is domain knowledge, there are relationships to rebuild. So we have org structures and resourcing to ensure that **the one most important project** gets all the people it needs.

We assume **the one thing** is perfectly estimated and resourced and nothing will go wrong. But when something invariably does go wrong (merging on the highway or an accident), there is no space. Everyone else is already fully utilized on other stuff. We try to adjust, but we just jam up the whole thing.

## The case for slack

Now, many would say “that’s okay, it will happen less efficiently, but it will happen eventually.” This might be okay for you. But the core tenant of agile is rapid loops of small batch releases and learning. When the organization is running multiple projects in parallel instead of a few key projects serially, we will absolutely hit gridlock.

Add to that cross-incentives between different stakeholders, and it becomes unclear which project is the Google Search Index and which one is the Google Doodle. Even if it is clear, the Google Doodle manager is measured on “awwws per minute” and will obviously resist giving away their key engineer.

Makes sense that we need slack in the system to allow for priorities to shift and mistakes to happen, right? How do we make it happen?

## The basics

You can’t have slack all over the org. So first step is to resource fully dedicated x-functional teams to products and keep those boundaries fairly rigid. There’s a huge cost to “borrowing” engineers between products.

The second step is to correctly visualize and measure the value stream (where delays happen) so that it’s obvious where the constraints are. This could be as simple as a standup, or as complex as a Kanban board.

The third step is to limit specialization. In the Google Search Index team, let’s say we have a database indexing engineer. They may be 25% utilized most of the time, but during a big update, there might be demand for 400% of their time. This slows the entire project while the rest of the team waits on them. They move from being the slack to being the constraint. A forward thinking manager would ensure that another engineering with similar skills (a background in caching or encryption) would x-train so they are able to do some of the indexing engineer’s work.

## But we can’t just pay people to sit around!

Even if we do the above 3 steps, there is still a problem. As a project starts, It’s mostly product and design. So engineers are at very low utilization. They participate in the product and design work a bit, but are usually not even on the team at this point (another problem). QA is zero util.

Next phase we are mostly building out an MVP with a limited backend to test the market. So all 3 front-ends are engaged, but backend work is light. QA is planning a bit, but mostly empty. Then we engage QA at the end of an iteration, but they take 4 days to test the build while others are mostly sitting empty.

If product and other engineers do QA a bit and a front-end engineer learns some python, we can sort of balance this out (see above). But it doesn’t mean everyone is at 100% util.

**So what happens on most teams?** 

They start the next project on the roadmap simultaneously (this is the fatal mistake).

If frontend is 100% utilized in sprint 1, and backend is 50% utilized, they will start the backend parts slated for sprint 2. Sounds good in theory, but in reality, sprint 1 projects will spill over, demand will come from other teams for help, a new person needs onboarding, on on-call shift will turn into an all-nighter, etc. etc. In sprint 2, backend will again be under utilized as front-end catches up.

## The slacklog

In my experience as a product engineering leader and a coach, I think the #1 reason teams fall into this trap is not that they believe doing more things at once is faster or better, it’s because they are afraid of people sitting idle.

So here’s a proposal: Let’s make a Slacklog for every team / function.

### What’s a Slacklog?

A Slacklog is a backlog of things which *can* happen, but don’t *need* to happen.

Slacklog criteria:

1. Not in direct support of any quarterly business targets
2. Broken down to no more than 2 day projects
3. Immediately executable by >1 person on the team (no pet projects)
4. Easily understandable and clearly valuable
5. Uncontroversial (no politics or approvals)

### Building a slacklog:

1. Get the team together
2. Use this set of prompts (or make up your own)

* We could avoid \_\_\_\_\_\_\_\_ on our team if only we had a tool that would \_\_\_\_\_\_\_\_\_.
* If we knew \_\_\_\_\_\_ about , it would help us prioritize.
* We think \_\_\_\_\_\_\_\_\_\_\_ technology could make us do \_\_\_\_\_\_\_\_\_\_\_ in a more \_\_\_\_\_\_\_\_\_\_ way.
* New joiners on our team find it hard to get started because of \_\_\_\_\_\_\_\_\_\_\_\_.
* It would be much easier for people to interact with us if gave them the ability to \_\_\_\_\_\_\_\_\_\_\_\_.
* We could make better prioritization decisions if we could visualize \_\_\_\_\_\_\_\_\_\_\_\_\_\_.
* We would have less downtime if we fixed \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.
* It would be easier to recover from bugs if we knew \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.
* It would be a lot more fun to work here if we had \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.

1. Have everyone fill up minimum 1, max 3 ideas independently.
2. Group / De-duplicate.
3. Use dot voting to make a prioritized list.
4. Choose the top “team size / 2” problems. Have a pair of teammates work on detailing each (ideally put product people on some engineering problems and visa-versa). Note: this is not a commitment to do the work, see slacklog criteria #3 above.
5. If you need to play HiPPO, play a little HiPPO, but otherwise let the team own it.
6. Each pair diverges and creates 1-3 options on how to address the issue with a rough size.

* e.g. New joiners on our team find it hard to get started because of unclear and inconsistent API parameters. We could…
* Check all the inline API docs for correctness and explain inconsistencies (M)
* Build a facade around inconsistent services with Open API compliant methods (L)
* Make a simple training checklist and ensure newbies are run through it (S)

Now you’ve got a slacklog!

### How to use a slacklog:

**Purge:** Ensure the slacklog doesn’t get too long. Consider wiping it out and building fresh every 6 months. If something hasn’t gotten done in 6 months, it’s probably not very important.

**Celebrate:** Even though these are optional tasks, it doesn’t mean they shouldn’t be celebrated and demoed. It’s also important to make sure people doing the primary stream aren’t the only ones being rewarded.

**Handoff:** Don’t let people own tasks. This is another form of constraint. Tasks should be simple enough to transfer easily and should be jointly owned by as many people as possible.

**Increase flow:** Use this as an opportunity to have backend engineers do QA focused Slacklog items or designers do front-end engineering items. They will be slower to execute, but in the future, they will be able to take on other job roles, thereby eliminating the need for slack.

## Now go slack off!

I’ve never done this explicitly, but have tried similar things. Would love to hear if it worked for your organization/team.