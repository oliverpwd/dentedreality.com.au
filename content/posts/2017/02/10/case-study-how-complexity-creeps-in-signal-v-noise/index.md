---
title: 'Case study: How complexity creeps in – Signal v. Noise'
date: '2017-02-10T14:38:32+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://m.signalvnoise.com/case-study-how-complexity-creeps-in-cba48023e6a1#.vptdtioy6
---

[Case study: How complexity creeps in – Signal v. Noise](https://m.signalvnoise.com/case-study-how-complexity-creeps-in-cba48023e6a1#.vptdtioy6)  



## Seemingly inconsequential decisions can open the door to significant organizational and operational complexity

Lately we’ve been on a bit of a tear internally working to eliminate operational complexity from our business.

Complexity is like addiction… It comes on slowly, forming weak bonds that you can barely feel. But as it continues, the bonds strengthen quietly until they calcify and become hard to break.

Removing operational complexity involves eliminating manual busy work, bottlenecks, dependencies, promises to placate, and a whole host of other things.

I want to share an actual example in our business of how a couple small design decisions lead to significant operational complexity.

### Basecamp Enterprise

In [Basecamp 3](http://basecamp.com), we used to offer a *Basecamp Enterprise* plan. Basically it’s a higher priced, annual-only offering with a few extras tossed in. The red flag here is “with a few extras tossed in”.

In order to differentiate and justify the value of a higher priced offering, we added a few line items to the pricing chart. We did this for two reasons: 1. To add more perceived $ value (more stuff = worth more), and 2. to visually distinguish enterprise from the other plans (longer list of benefits).

Here’s what the plan chart looked like (arrows added to highlight points for this article — they weren’t in the actual customer-facing chart):

![](https://i2.wp.com/cdn-images-1.medium.com/freeze/max/30/1*K81-c_5WPtc4HtTHNb1JBw.png?w=921&ssl=1)![](https://i0.wp.com/cdn-images-1.medium.com/max/800/1*K81-c_5WPtc4HtTHNb1JBw.png?w=921&ssl=1)

Those four little lines on the right lead to four big flash points internally

Seems innocent enough. No big deal, right?

#### Complexity creeps in

Let’s explore what each of the lines marked with an arrow in the chart about *really* means inside our company:

1. **Pay by check.** Larger organizations often prefer to pay for things by check since an accounts payable department handles large invoices. So we figured we might as well accept checks on the Enterprise plan. Simple process: Someone sends in a check and we process it. No biggie, right? But it turns out it was quite a bit of *extra* work for Andrea, our office manager, who was tasked with processing the checks and updating the accounts to make sure they were marked paid. As anyone who’s processed receivables knows, checks can come in without the proper identifying information. This turns what should be a simple deposit into a challenge for even the best detective.
2. **Dedicated account manager.** If a customer pays us a lot, it seems reasonable and fair that they’re entitled to have direct contact with someone on our end. But we don’t have dedicated account managers. So that means we have to assign customers to someone on our support team who already has other things to do. Now that person is tied to a specific customer. And what if that person’s out of town? Now they have to coordinate with someone else to take over while they’re out. We’re just shifting the burden and expectations around and creating dependencies that tangle people together. And what are the expectations for an account manager anyway? We never really laid this out, so there’s a lot of assumptions baked in on both sides. That’s a recipe for a potentially complex relationship.
3. **A 60-minute personal tour for your whole team.** Also seems reasonable if you’re paying $5000 a year for Basecamp. But who’s going to do it on our end? Who’s job is it to coordinate, to schedule, to reschedule if someone can’t make it? The account manager? Now that person’s schedule is chunked up further, and they’re unavailable to help with other tickets, etc. Yes, we already offer to give people tours on request, but an *option* is different than an *obligation*. We’re tying ourselves tighter and tighter to a specific customer’s schedule and needs — simply because they’re paying us more.
4. **SLA uptime guarantee.** What does this even mean? We hadn’t fully nailed down the specifics by the time we popped it on the pricing chart. We figured we could just figure it out later. So we started a discussion thread in Basecamp. Who was involved in this conversation? David, Mercedes, Kristin, Chase, Noah, Merissa, Will, Jonas, and Taylor. So this involved ownership, our COO, multiple people on the support team, ops, copywriting, and design. It’s hard to remember other “simple”, inconsequential things that involved so many different people across the company. All to hammer out a promise that we thought would be a good idea, but almost certainly didn’t have to promise. I think the SLA uptime guarantee was originally my *bad* idea.

Now… Could we have handled some of the above different? Of course. We could have automated check payment, or at least significantly cut down on the manual labor. Could we tie downtime into automatic discounts? Could we have automatically fired off a “schedule a tour” email with a link to a shared calendaring system so the customer could jut pick a time and the whole thing would be automated? Yes and yes and yes and yes. But that would been a significant chunk of work for something that a small fraction of our customers were buying anyway.

But more importantly, let’s pull it all back to: Did we even need to offer *any* of this to justify a higher price? Or could we just charge a higher price. Big companies are used to paying more for basically the same thing — maybe they just wanted to pay more. Maybe they would have just paid more regardless. It’s likely pay by check swayed some who absolutely couldn’t pay by credit card, but the other benefits are a lot less obvious.

And pulling back even further… Why do we even want to charge some customers significantly more than others? Do we even want those customers? Does our business depend on a tiny fraction of customers paying significantly more? No.

We’re not an enterprise software company. We don’t want to be an enterprise software company. We have no interest in solving big company problems. Our interest — our love — is helping small companies run better businesses and *grow in control*. We know [Basecamp 3](http://basecamp.com) is better suited for this than any other product of it’s kind. Why take any attention away from helping the small guy just to make a few extra bucks off the big guy?

So why did we try to fish for the whales? Mostly because it seemed easy to do. And that, my friends, is where complexity hides.

#### The solution

So what did we do? We’ve stopped offering the Enterprise plan. Problem solved. Existing customers who are on it can continue on it, we’re just not offering it to new customers any more.

### A few rules of thumb

How can you spot situations where you’re creating complexity? Here are a few rules of thumb, things to step back and consider when you do what you do:

1. **Am I creating work for someone else?** It’s very easy to just add a line to the pricing chart and say “Oh, support will take care of that”. I know — I’ve done that. It’s *very* easy to do. And a shitty thing to do.
2. **“We’ll figure it out later”**. This one isn’t always bad, but it’s a red flag. When you bury a bunch of unanswered questions so you can dig them up later, you’re probably avoiding them in the first place because you know finding the answer is going to be challenging.
3. **“If it becomes a pain in the ass we’ll automate it later.”** Also not always a bad option, but recognize that historically we don’t often come back to automate things unless they are causing programmers/designers significant personal pain. If other people are experiencing the pain, it’s easy to just let it continue. Since automation requires understanding the problem deeply, and programmer and designer resources, it’s easy to say “it’s not important enough to push off more important customer-facing product work”.

I’m sure there are other rules of thumb. If you have some you’d like to add please post them as comments below.

Hopefully this post served to highlight how a few words in a few places can create significant organization and operational complexity. This is very much [a butterfly flaps it’s wings](https://en.wikipedia.org/wiki/Butterfly_effect) kind of stuff stuff. Small moves, big waves.