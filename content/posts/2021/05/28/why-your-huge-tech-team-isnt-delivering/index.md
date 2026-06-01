---
title: Why Your Huge Tech Team Isn’t Delivering
date: '2021-05-28T22:47:13-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://blog.usejournal.com/why-your-huge-tech-team-isnt-delivering-3851be27712c
---

[Why Your Huge Tech Team Isn’t Delivering](https://blog.usejournal.com/why-your-huge-tech-team-isnt-delivering-3851be27712c)  



[![](https://miro.medium.com/fit/c/96/96/1*eIpNMHKV0scFSAtahO0QyA.jpeg)![](https://miro.medium.com/fit/c/96/96/1*eIpNMHKV0scFSAtahO0QyA.jpeg)](https://mogest.medium.com/?source=post_page-----3851be27712c--------------------------------)
[Roger Nesbitt](https://mogest.medium.com/?source=post_page-----3851be27712c--------------------------------)
[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28463633d0c7&operation=register&redirect=https%3A%2F%2Fblog.usejournal.com%2Fwhy-your-huge-tech-team-isnt-delivering-3851be27712c&user=Roger%20Nesbitt&userId=28463633d0c7&source=post_page-28463633d0c7----3851be27712c---------------------follow_byline-----------)

[Sep 10, 2018](https://blog.usejournal.com/why-your-huge-tech-team-isnt-delivering-3851be27712c?source=post_page-----3851be27712c--------------------------------) · 10 min read



“Our team used to go fast when it was small. Now we have ten times as many people and less work gets done. What happened?!”

*Short answer:*

Your workstream is controlled by people whose job it is to ship more features, and your software engineers think their job is to write code.

*Long answer:*

It’s complicated and of course there’s no magic bullet to make everything go fast again, otherwise you would have already done it by now.

Below are five reasons I’ve seen time and time again, though. Many companies that have a technology team of over 30 struggle with all five.

![](https://miro.medium.com/max/3840/1*v-wzjbhLp9S6NQlVQz5b_g.jpeg)![](https://miro.medium.com/max/3840/1*v-wzjbhLp9S6NQlVQz5b_g.jpeg)

Most things are hard to pick up and easy to put down. Strangely, software is the opposite.

# Reason 1: Software is easy to write, hard to maintain

I was visiting an old workplace a few weeks ago, and someone stopped me in the hallway and asked, “Are you the person that wrote [an integration with another market] in only two months?”

“Yeah, that’s me. Sorry about that,” I said.

Rewind the clock a decade ago: our company was New Zealand-based, and we were just about to move into another country. That would entail a huge amount of work, rewriting most of the system to deal with the different regulations and systems. My boss sent me away on a “working holiday” to bash it out, which I dutifully did as fast as I could.

I handed it back to the team two months later, 80% done. The team then spent the next year doing the next 80%. And now a large team continues to work on it ten years later, finishing off that last 80%.

Was it the right thing for the company to expand into another country? Maybe, I don’t know. But I tell this story for two reasons:

1. **It added a huge amount of complexity to the system**. What used to be a system built for a single market was now an order of magnitude more complicated so it could handle the different market requirements and different preferences of the countries. Work on any part of the system immediately became harder. Due to the added complexity, people could hold less of it in their heads at any one time. Certainly no-one knew the whole system anymore. There was a noticeable drop-off in productivity.
2. **It continues to cost an extraordinary amount**. There’s the obvious cost of the team that maintains the market-specific code, but what’s not as easy to account for is the cost of every developer and designer who works on the system and has to contend with that added complexity in their day-to-day work.

Every time you add a feature to your product, everything gets harder. Everything gets slower. And everything gets more expensive, from that point and forever more.

As a core business strategy, shared on all levels of the organisation, it is crucial that you are ruthless with the feature set of your application.

“But our customers are asking for more functionality!” I hear you cry. “We have to stay competitive in the market!”

It’s too easy to add a feature; get a bunch of people around a table for a few hours and issue an edict to make it so. It’s almost impossible to take a feature away.

Adding features means adding more developers and designers and testers for the lifetime of your product, which means adding line managers to manage them and ultimately senior managers to manage the line managers, which means needing a bigger floor plate and having bigger meetings and exponentially more connections between people, and higher levels of specialisation so people don’t step on each other’s toes, which means a less holistic view of your product.

My advice is to implement systems to make it as hard to add a feature as it is to take one away. Make sure your executive team down understand the ongoing consequences of asking for a new feature.

![](https://miro.medium.com/max/60/1*SFuEf8ohwML8ShMgJ375NA.jpeg?q=20)![](https://miro.medium.com/max/60/1*SFuEf8ohwML8ShMgJ375NA.jpeg?q=20)

![]()




The product owner’s job is to go forwards. That’s not always the right direction to go.

# Reason 2: Product owners control the backlog

We hire product owners to be the voice of the customer inside our teams. Customers want the product to better match how they want to use it. The product owner’s role is to make customers satisfied.

Then we put them in charge of deciding which work gets done and when.

If you were at all swayed by the idea that we should be minimising our product feature set, you can see the trouble here.

In a perfect world, we’d be able to consider all the consequences of work to be scheduled, and then pick the most important not just for our customer but the success of our business.

I present to you a system of seven pillars that needed to be considered for every (non-trivial) piece of work:

1. **Strategy.** Does it comfortably fit into our stated strategic goals as a company? Does it advance us towards our vision? Does it comply with our mission and values? Does it allow us to meet our short-term objectives?
2. **Product.** Does it meet the needs of our existing customers — the people who pay the bills for our product? Does it grow their loyalty to our product?
3. **Design.** Does it meet the needs of our users, allowing them to do something that improves their experience at home or work? Is it enjoyable to use? Does it thrill them?
4. **Technology.** Does it positively impact on the long-term health of our systems? Does it increase the stability and reliability of the systems? Does it decrease our operations and maintenance burden?
5. **Market.** Will it be attractive to the markets we compete in? Will it gain us attention and more customers? Is it competitive?
6. **Financial**. Will it make us more money than it costs us, including implementation, maintenance and opportunity costs?
7. **Internal.** Will the team be energised to do it? Will we have a physically and psychologically happy team post-implementation? Will the team want to continue working with us?

These seven are equally as important as each other, and therefore don’t come in any particular order.

A product owner is paid to care about one, and sometimes two of these. They are an indispensable person to have in your team, but they are the wrong person to have final say over what comes next.

So who is the right person? It’s a team responsibility. But give a team that mostly consists of developers that responsibility, and they’ll choose the most technically interesting thing. Which leads me to the next reason your team isn’t delivering…

![](https://miro.medium.com/max/60/1*PMBwoU5bWkso8M2A1ocS9Q.png?q=20)![](https://miro.medium.com/max/60/1*PMBwoU5bWkso8M2A1ocS9Q.png?q=20)

![]()



# Reason 3: Implementers are not responsible for business success

First, a definition. In the part of your organisation that delivers software, roles can be neatly split into two types: **specialists** and **implementers**.

Specialists have a responsibility for a single facet of the business. Practice leads may aim to increase the reliability of the system, or the consistency of the user experience, or build processes around quality assurance. At higher levels, specialists are responsible for the financial outcome of the company, or lead the product team.

Implementers are the people who produce the system. We call them after their primary skill, such as Software Engineer and Interface Designer, but they’re all ultimately responsible for shipping a system that works.

There is a growing trend of wanting to give autonomy to the implementers; to get decisions happening amongst the people who intimately understand the system. But all too often bad decisions are made, so management winds back the autonomy.

I think delegated team autonomy is the right way to make good decisions, but only when implementers have a complete understanding of the seven pillars detailed above.

But how can a Software Engineer understand the financial and market implications of a new feature?

This is the system I believe will get your team delivering:

1. **Implementers are responsible for the business success of their work.** From design to technical to financial. Yes, this is going to freak out your dev who only cares about which latest hotness tech they get to use.
2. **Implementers use specialists as expert resources.** It’s the implementer’s job to go find the specialist in each pillar and, with them, determine the implications of the feature. They pull all the expert opinions together into a cohesive picture.
3. **Each team schedules their own backlog.** Because they understand what’s important, and they’re in close communication with specialists and other management, they can weigh up what the most valuable thing is for them to do next. They communicate their decision-making process in a lightweight way so any interested parties can see what’s going on.
4. **Management has veto powers.** If management don’t think the team has correctly considered the seven pillars, they can veto their decision. The team goes back to collecting more information to decide the right path.

![](https://miro.medium.com/max/60/1*C0CxuUgoNlB2DEBagCn-FA.jpeg?q=20)![](https://miro.medium.com/max/60/1*C0CxuUgoNlB2DEBagCn-FA.jpeg?q=20)

![]()




Eating your burger by ingredient has just an unsatisfying end result as grouping your teams by capability.

# Reason 4: Teams are split by technical capability

You’ve got 15 people in a team that’s building a product. Meetings are too long, work is getting missed due to communication complexity. “Let’s split into two teams,” you say. Good idea. Small autonomous teams work best.

Unfortunately the way most people do it is split along capability. A common one in web software is having a front-end team and a back-end team. Immediately there is a problem: neither team is responsible for an product experience, because their team only looks after half of it. Extremely strong bonds have to be created between the two teams to make sure the front- and back-end work is deliverable at the same time, and that each serves the needs of the other.

Instead, split your teams into standalone products and give them ownership of the success of their product. A good first split is “customer experience” and “administrator experience”.

As your administration section grows, maybe it could then split into “call centre administrator experience” and “billing administrator experience”. Your “customer experience” team could split into “pre-signup and signup experience” and “signed in experience”.

Every team does their own front- and back-end development, design and user research. This doesn’t mean the teams don’t have to work with each other; to make a cohesive and attractive product, the entire company needs to work together. But it does mean that day-to-day decisions can be made intelligently at the team level, with only the greater strategic questions needing to be handled in a larger group.

# Reason 5: No-one knows what the company needs them to achieve

It is extremely difficult to develop an excellent company strategy. It is even more difficult to communicate your excellent strategy in a way such that all the company’s staff understand it and buy into it.

Most of the companies I’ve known have had a strategy that essentially boils down to “let’s get more customers to make more money.” The problem with this kind of strategy is that it doesn’t allow people to make decisions. Faced with a choice between path A and path B, both which could potentially get more customers, which one do you pick?

A great strategy focuses and culls. It allows people to say “no, we won’t do that because it’s not in alignment with our mission/vision/values” without waiting for someone from the top to make the judgement for them. It allows people to excel at the one thing the company has decided is its priority. A focused, empowered team is a team that delivers.

Going into developing and communicating company strategies would make this already-long article double the length, so let’s park that for another day.

# Yes, this is hard to pull off.

Taking an existing team with an culture of product-led workstreams requires a cultural shift that will not happen overnight. It might mean hiring a different type of person; people who are willing to make business success part of their job rather than leave it up to someone else to decide what they should next work on. People who are willing to use pragmatic software technology, who are interested in what their customers and users want out of the software, who are concerned about the profitability and long-term viability of their company.

I’d suggest these are the kind of people you want no matter what system you end up using, but after a career of being told what they should work on next and how they should do it, give them plenty of support and encouragement as you hand over the responsibility.

# In short

1. Minimise your product feature set. The size and complexity of your application makes your teams struggle to deliver.
2. Allow your delivery teams (implementers) to control their own backlogs, on the proviso they are responsible for understanding the business success factors for the work by drawing from the specialists’ expertise.
3. When a team becomes too large to be efficient, split it into two standalone products and give the new teams autonomy over their product.
4. Build a focused, clear company strategy, and make sure every single person in the company lives and breathes it.