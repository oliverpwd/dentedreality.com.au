---
title: Software planning for skeptics
date: '2022-05-26T22:08:30-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://amontalenti.com/2017/10/27/skeptics/
---

[Software planning for skeptics](https://amontalenti.com/2017/10/27/skeptics/)  



Engineers hate estimating things.

One of the most-often quoted lines about estimation is “Hofstadter’s Law”, which goes:

> Hofstadter’s Law: It always takes longer than you expect, even when you take into account Hofstadter’s Law.

If you want to deliver inaccurate information to your team on a regular basis, give them a 3-month-out product development timeline every week. This is a truism at every company at which I have worked over a varied career in software.

So, estimation is inaccurate. Now what?

Why do we need a product delivery schedule if it’s always wrong?

There is an answer to this question, too:

> Realistic schedules are the key to creating good software. It forces you to do the best features first and allows you to make the right decisions about what to build. [Good schedules] make your product better, delight your customers, and — best of all — let you go home at five o’clock every day.

This quote comes from Joel Spolsky.

So, planning and estimation isn’t so much about accuracy, it’s about constraints.

The inaccuracy comes from the risk of software engineering. As Brooks put it, “the programmer is an optimist.” His shorthand describes an underlying psychological truth, which has actually been studied.

![](https://amontalenti.com/wordpress/wp-content/uploads/2017/10/march.png)![](https://amontalenti.com/wordpress/wp-content/uploads/2017/10/march.png)

During “estimation time”, all programmers exhibit these psychology attributes — and this applies especially to engineering managers!

* **Wishful thinking** — “This one feature will solve everything!”
* **Anchoring** — “We’ve done this before, so it’ll be easy!”
* **Planning fallacy** — “We can get this done in a weekend!”
* **Cognitive dissonance** — “I know I am bad at estimates, but this time will be different!”

A discussion on these and other factors can be found in works in peer-reviewed journals.

The key thing to estimating (and engineering planning, in general) is to split the world into three areas:

* what you know
* what you know you don’t know (**known risks**)
* what you don’t know that you don’t know (aka **unknown unknowns**, or **byzantine risk**)

Then, good engineering managers follow this axiom:

* It’s easy to estimate what you know
* It’s hard to estimate what you know you don’t know
* It’s very hard (maybe impossible) to estimate things you don’t know that you don’t know

Let’s take an example.

If you’ve built web applications using simple web frameworks and SQL databases before, then building another one for a simple business *likely* won’t be hard to estimate. This is something you know, and you know roughly how long it takes to build a database model, test a few web views, put together a design, etc.

But, let’s say that that in addition to the web application, you also need to deliver an iOS mobile application.

And you’ve never built one of these before. Building an iOS mobile app in this context has known risks. Do you have engineers who will be able to pick up the Apple and iOS tooling? Will learning Objective-C or Swift take more time than learning other languages? Does mobile development completely break your ideas about how to test and deliver production apps?

You have studied mobile applications and read about their technologies, so you know what risks are involved, but you also know that your lack of experience will make this hard to estimate.

Finally, let’s say that it turns out, this customer’s application is in the health care space, and anything that the application does will need to be logged and audited. But **you don’t know this**, and the customer fails to mention it.

You don’t know what’s involved in making a piece of software audit-ready. You’ve not only never done it before, but you also aren’t even sure if it’s possible to do, while still building apps the way you’re used to building them. You don’t even know what you don’t know. This is an **unknown unknown**. You can’t estimate this, but you also can be pretty guaranteed that **some** unknown unknowns will happen during the course of development. Unknown unknowns are often the cause of an original estimate being wildly off.

So, your goal, during discovery and planning, is to try to know more about the product you’re delivering, so that you have a lower risk of being taken by surprise by an unknown unknown! Think of it as a “risk discovery” process. What are we forgetting to talk about that will probably bite us later?

## Surviving the tar pit

Brooks said: “Software is like a tar pit: the more you fight it, the deeper you sink.”

Staying out of a software tar pit is all about being realistic about risk and cost/benefit.

He also wrote: “For the human makers of things, the incompletenesses and inconsistencies of our ideas become clear only during implementation.”

So, to tie these ideas together: a meticulous plan to nowhere still leads nowhere. This does not mean, however, that you don’t need a plan. Software teams need to discuss their work before they build it, or they’ll build things that are so bad they aren’t even worth discussing. And once they start building, they should know that it’s **only now** that they are learning what is truly involved in delivering the finished product.

Plans are guides, not constraints. As Dwight D. Eisenhower said, “No battle was ever won according to plan, but no battle was ever won without one.”

## Feeding the feedback beast

Feedback is everyone’s favorite topic — because, everyone’s got an opinion.

They’ve got an opinion about the weather, their favorite ice cream flavor, or the top 3 restaurants in New York City. So, it’s no surprise they also have an opinion about “what customers want” or “what would be cool”.

Let’s start with the most important thing about feedback: any moderately successful company has more feedback than it knows what to do with.

There are people using its products, there are employees invested in its products, and then there are investors, advisors, journalists — the list goes on and on. Opinions about what to do are everywhere — the trick is, separating the wheat from the chaff.

There are quite a few competing opinions about what to do with feedback.

For example, Steve Jobs’ opinion was to ignore basically all feedback from everyone except himself and a trusted, small group of designers. Jobs believed the market doesn’t know what it wants until it has it.

Bill Gates, by contrast, believed that the most important bit of feedback was “market feedback”, mainly in the form of competitors. If you built every feature that the competitors had, you had the winning product. That’s all that mattered to Gates, pretty much. Winning in the competitive matrix. Microsoft mastered this art.

Jack Dorsey (of Twitter and Square) described his role as CEO as “Chief Editorial Officer”. A particularly apt analogy, he thought that his job was to take all these opinions about what Twitter or Square should be doing (from investors, employees, early customers, etc.) and make an editorial judgment about what to keep and what to cut. Product/market fit was not truly achieved, he believed, until you had cut away excess features and honed in on the core idea or vision of your product. For him, feedback led him to *cut* features, not develop new ones.

Des Traynor of Intercom once said that [“Product strategy means saying ‘no’.”](https://www.youtube.com/watch?v=9AM6QQlgLSQ) Upon reflecting on this presentation and this one-liner that went viral, he wrote up a guide called [“Rarely say yes to feature requests”](https://blog.intercom.com/rarely-say-yes-to-feature-requests/), which outlines a rubric for evaluating customer feedback.

1. Does it fit your vision?
2. Will it still matter in 5 years?
3. Will everyone benefit from it?
4. Will it improve, complement, or innovate on an existing workflow?
5. Does it grow the business?
6. Will it generate new, meaningful user engagement?
7. If it succeeds, can we afford to support it?
8. Can we design it so the reward is greater than the effort?
9. Can we do it well?
10. Can we scope it well?

This is a great list, and his point is that if, and only if, you can answer yes to *ALL* of these questions (not just some of them or most of them) should you consider building that feature!

So, as you can see, the end output of most feedback is a null and empty void.

But it’s from this battle that truly great products emerge. I once wrote about the culture of “killing ideas” in [“Why Startups Live”](http://thenextweb.com/entrepreneur/2013/07/02/why-startups-live/). Here is the relevant passage:

> To make sure you don’t grow in the wrong direction, you have to stop thinking your ideas are important.
> 
> Ideas become data points, speculations, lines in the sand. Not things worth pursuing by their mere existence — instead, things only worth pursuing if they are *worth* pursuing. Startups spend a lot of time asking the question, “Is this worth it?”
> 
> Startups have to kill ideas quickly and unceremoniously. If we hold funerals for every idea we kill, our last funeral will be our own.
> 
> Killing ideas becomes such a common startup activity that it can be very disorienting and demoralizing to work at a startup at times. Most of your ideas are killed. Maybe, even, all of them.
> 
> Startups think ideas are a dime a dozen. And they’re right. Ideas are meant to be killed.
> 
> Except for the ones that survive. It’s brutal and it’s harsh. But it’s also fast-paced and exciting. And when an idea perseveres, having survived the harshest treatment possible, the result is truly magical.

## Flowing with teams and projects

Of all the agile hype systems, my favorite management concepts come from the “lean product” movement, and specifically, the “kanban” notion of product flow.

Here is my interpretation thereof, what I might call my “Modified Kanban Manifesto”.

* Iteration plans should fit on a whiteboard. Or, for distributed teams, a single fully-visible Google Spreadsheet at 720p resolution.
* People should be assigned ideally one, sparingly two, and at most three, iteration goals. The capacity in your iteration matters, as do the skills of the people involved.

When planning iterations, there is a difference between goals and tasks. Goals are what we aim to achieve by the end of the iteration. Tasks are how we achieve those goals.

Iterations should only define goals.

Tasks should be defined at the individual and team levels, with people using their own tools and workflows for tracking and completing them. For example, my engineering team uses Github issues, and checklists therein, for tasks. A goal might span several checklists and several issues. The task management is up to them; deciding, at a high level, our product direction is up to me and my fellow product managers and tech leads.

The way to keep an iteration moving is making sure that everyone is on the same page with where we are with our iteration goals.

Assigning people to more than one goal per iteration is dangerous. It is, however, possible. Ideally, we keep every individual “in flow”, working on a single goal. However, there are times when people will need to have their brains “split” on several goals per iteration.

We need to recognize what we are doing here: **harming the delivery of the primary goal**.

In these cases, we should only allow them to advise on one (or, at most, two) other projects beyond their primary iteration goal. Sometimes, this trade-off is worth it. However, it is rarely worth it to assign someone to three goals at once. That person will be over-comitted and not achieve any of their goals.

In my mind, when an engineer is assigned to 1 project, they are in “flow”, if they are assigned to 2 projects, they are “strained”, and if assigned to 3, they are “over-committed”.

Slicing engineers into 4, 5 or 6 projects guarantees nothing gets done. That’s why visualizing engineer queues and work-in-progress is so important.

I also recognize that we have specific skill and affinity bottlenecks in our system. I have over 20 people on my product team, but only 4 UX engineers; they are the only ones who can do iterative improvements to our dashboard from a customer-facing standpoint. Thus pulling one of them off that project and onto something more speculative (e.g. a marketing or partnership project, or even a quick win for a big prospect in sales) does not merely distract 1/20th of my team — it actually destroys 25% of our UX capacity. Distracting just 2 people from this team causes a 50% (or more) delivery delay — guaranteed.

This does not just slow down delivery of their work, but causes an overall product delivery delay that can cost my company hundreds of thousands, even millions, of dollars. Decisions like these matter more than it appears on the surface.

This specific UX bottleneck is dangerous, but what’s even more dangerous is distracting people away from the most important work.

This is in the same way that closing a lane on a four-lane highway during rush hour does not merely reduce average speed of cars by 25%. It actually causes every single car to grind to a dead halt. In a systems world view, you could phrase this thusly: removing capacity from an at-capacity system guarantees the system becomes unstable — and likely breaks down.

### Skeptics should be wary

Skeptics like me should be wary of project management tools that allow people to be assigned to many tasks and items at one time, without visualizing their queue or capacity. This can lead to the feeling that many things are being worked on, even though nothing is being worked on. The lack of priority in the work will not only hurt flow, but also hurt predictability and team-wide communication.

Skeptics should avoid the temptation to pursue many ideas in parallel. It is more dangerous than saying no or punting on specific ideas. The analogy here is the landing strip at JFK airport. If 20 planes land per hour at JFK, it doesn’t help to put more planes in the air. Doing so will just guarantee that a lot of planes fly around in circles until they run out of gas and fall out of the sky, crashing.

Why do we “put more planes in the air” in product, then? Because everyone else — including our customers — demand to know that “we’re working on it”.

We should resist this temptation — we need to manage expectations appropriately. This will prevent our system from becoming unstable and endangering our landing of regularly-scheduled planes. There’s no harm in saying, “Your plane has been re-scheduled for departure in 1 hour.” Or, “we have to spend some time ‘taxi’ing the tarmac’ before taking off.” This way you build some slack into the system and don’t over-commit it.

(This airplane analogy, BTW, comes from an oldie but goody [by Reinertsen](https://amzn.to/2zUr8rp).)

Skeptics understand that software work has high variability. Counter-intuitively, variability is a positive trait of the system we want to preserve, and we want to build in slack so that we can exploit it, rather than suffer at its hands. Often the variability leads to good returns in terms of product innovation.

### Creative technical work is intrinsically different

Why is creative technical work so unlike sales work, and thus so hard to empathize with for salespeople?

Well, I asked a salesperson to imagine what would happen if he was told, to meet his monthly quota, he could only pitch one prospect. He had to pitch that prospect all month. He wasn’t allowed to talk to any other prospects. And, when the 30th came along, it was either he had closed that customer, or he hadn’t.

This is much like working on a product feature. Does that sound fun?

The reason we don’t do this in sales is because of optionality. You can’t possibly schedule more than 2 or 3 meetings with a prospect in a month anyway. It is therefore waste not to speak to other prospects, who could turn into customers. So, may as well talk to many customers in parallel. As many as your calendar will allow and will ensure you don’t distract from high-probability closes. You take a “portfolio theory” approach — aka “spray and pray”. Obviously you prioritize strong leads and de-prioritize weak ones. But ultimately, your sales process is probabilistic and benefits from the variability of buying as many lottery tickets as possible — hopefully ones where you have some inside knowledge on the draw.

Product work is basically the 100% opposite. We wish we could take “spray and pray” approach, but we can’t. We can’t buy a bunch of options; we can only commit to one at a time. Put concretely, we can only decide 1, or at most, 2 things to build. When we decide to build them, we have to spend hours, days, weeks, and even months working through the technical implementation. And only once it’s “done” do we know if we truly have succeeded. Plus, even once proven and code complete, we need intense focus to test (often manually), deploy, and verify our work.

And even after all of that, we have to allow ourselves the ability to get customer feedback to iterate on the initial delivery!

It requires enormous focus. It feels chaotic. But, we love it. Yet, we will learn to hate it if we try to systematize it.

### There’s beauty in chaos

To quote one of my favorite bloggers, Rands: “The growth paradox is that the chaotic means by which you found success may be distasteful to those you hire to maintain & build on that success.” ([source](http://randsinrepose.com/archives/hacking-is-important/))

Creative technical work cannot be systematized. Many other kinds of work can. That’s just a fact of life. We can live with it. In fact, we can grow with it. But if we try to change the fact of life, we’ll die.

The best we can do is learn to make our company thrive from its variability — and the outsize returns that variability can often generate — as has happened time and time again at the world’s most innovative software companies.

Rather than trying to control our product process and turn it into a factory floor for software features, we need to be ruthless about prioritization, ensure we have adequate capacity (through hiring), and **let engineers focus maniacally on single projects while they carry them through delivery**.

To conclude: product distractions aren’t just distractions — they are fatal mistakes! The skeptic’s furrowed eyebrow is actually your savior.