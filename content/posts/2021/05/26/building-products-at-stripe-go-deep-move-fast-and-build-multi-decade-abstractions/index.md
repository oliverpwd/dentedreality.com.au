---
title: 'Building Products at Stripe: Go Deep, Move Fast, and Build Multi-Decade Abstractions'
date: '2021-05-26T22:39:37-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://newsletter.bringthedonuts.com/p/building-products-at-stripe
---

[Building Products at Stripe: Go Deep, Move Fast, and Build Multi-Decade Abstractions](https://newsletter.bringthedonuts.com/p/building-products-at-stripe)  



This is the next part of my ongoing series about product culture. If you missed it, check out [my previous piece about Airbnb](https://newsletter.bringthedonuts.com/p/building-products-at-airbnb) and [my article on strong product cultures](https://newsletter.bringthedonuts.com/p/what-makes-a-strong-product-culture) that kicked everything off.

[![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4f31acb6-b5da-4ce4-85da-c979cedc9cc8_4775x3188.jpeg)![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4f31acb6-b5da-4ce4-85da-c979cedc9cc8_4775x3188.jpeg)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4f31acb6-b5da-4ce4-85da-c979cedc9cc8_4775x3188.jpeg)

Stripe co-founders Patrick and John Collison


**This month we’re going deep on Stripe.** As you’re about to learn, “going deep” is a core product principle at Stripe. The company is now the most valuable startup in the United States, raising a round in March at a breathtaking $95 billion valuation. (Disclosure: I am an investor in Stripe and have a relationship with the company dating back to 2015.)[1](#ipfootnote0)

I had the opportunity to interview my friend **Michael Siliski**, who I worked with at Google [Michael’s [LinkedIn](https://www.linkedin.com/in/msiliski/) and [Twitter](https://twitter.com/msiliski)]. Michael joined Stripe in February 2020 after a fabulous twelve-year career at Google, where he led product teams in Google Mobile Maps, Google Play, Android, and Area 120. Michael’s one of the more [thoughtful product writers](https://medium.com/swlh/the-role-of-a-product-manager-e0354b4b6845) I know, so I relished the opportunity to speak to him about Stripe.

**Ken Norton:** What’s your role at Stripe?

**Michael Siliski:** I’m the Business Lead for Payment Experiences & Platforms. I have a team of mostly product managers, but also some strategy and operations, as well as broader responsibility for our core payments business. That’s everything from a merchant integrating Stripe payments, to a user making a payment, the full payment stack with different features, integrations, and whatnot. And then we build a lot of the payment platforms that power all of Stripe’s products. I have both external and internal customers.

**Ken:** What is Stripe’s product culture like?

**Michael:** There’s a lot we have in common with tech broadly, but one thing that distinguishes Stripe is that **it’s an incredibly deep-thinking culture**. It’s a **written culture** really focused on getting to the right answer. Going really deep and getting all the way down into the details around things, then distilling it down to a form that makes the complexity broadly consumable and actionable.

Another thing is a sense of urgency. **The company is especially dedicated to moving very, very fast.** That urgency comes from [Co-founder and CEO] Patrick [Collison] who even has [a page on his website](https://patrickcollison.com/fast) dedicated to fast projects in history, ones that were unreal and unreasonably quick.[2](#ipfootnote1) That has really permeated the Stripe culture.

**That deep thinking and speed are combined with a substantial amount of user focus and user empathy.** That’s something that you see talked about everywhere as being important, but I haven’t ever quite felt it as I have here. And finally, Stripe is a humble and low-entitlement culture. There’s a high degree of kindness between people, and I don’t think you can ever take it for granted.

## Go deep and move fast

**Ken:** I’m struck by the juxtaposition between moving fast but going deep. Is there sometimes tension there?

**Michael:** Those things can sometimes be in tension, and it can be difficult to strike exactly the right balance. But the way that I think about it, if you know where you’re trying to get to, then you can afford to go really deep because your effort is focused in the right direction.

**Stripe runs on written long-form documents in a way that I haven’t seen before.** So that means somebody can go deep, like all the way down, and then distill it back out to everybody else. So you don’t have to do all of that work yourself. It does require a lot of reading for sure, but the benefit is great clarity of thought on complex topics.

Engineers, partnerships, PMs, everybody is producing documents. That’s part of how Stripe has always worked, from a perspective of trying to get to the right answer and make sure the best ideas come through, not just the loudest voices. It helps facilitate the flow of information in a world where we’re increasingly remote.

## Product “shaping”

**Ken:** Walk me through a typical new product or feature. How does it start?

**Michael:** We expect every product manager to be actively talking with customers and really spending a lot of time understanding customers. But it’s not just a product management thing. Engineers are expected to be talking with customers as well.

So a lot of the time, you’re starting from an actual user need that an actual person has expressed to you directly. And then they’ll either tell you what the product is that they need because it’s adjacent to something that we’ve already built, or you understand their problem, and then you go design the right product to solve it. And then you can take that and test it with those same customers. A rapid iterative loop with the right customers solves for a lot of common product development pitfalls.

**At Stripe, we talk about product “shaping,” which is a term I hadn’t encountered before.** Shaping is the process of creating a rough solution to a concrete user problem — it fills the space between the broad strategy and the detailed product specification, or the PRD. This process frontloads a lot of the critical thinking about what you’re planning to build and why. Still, you haven’t necessarily fleshed out the requirements in a way where someone could go and implement them yet.

The product shaping document will come at it from the perspective of a user. And, you know, a lot of the time, those look like a description of a user story, and you’re walking through a story interspersed with code snippets because a lot of our products are APIs. These documents are basically walking through someone’s experience, and there are curl commands here and there showing how everything is done via an API at each step. They play the role that mocks or wireframes might play in a consumer product UI.

[![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc43ab04-4abb-430d-b489-2f00e83d4e77_1182x286.png)![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc43ab04-4abb-430d-b489-2f00e83d4e77_1182x286.png)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc43ab04-4abb-430d-b489-2f00e83d4e77_1182x286.png)

Creating a new ACH charge using Stripe’s Payments API on the command line


**Ken:** A challenge I hear from B2B companies is once you reach this level of maturity, you have big customers who are asking you for something specific. And the mistake that a lot of companies make is to just build whatever the loudest customers are asking for, and you lose your focus. The classic innovator’s dilemma. How does Stripe stay fresh and making sure you’re not just transferring a list of features?

**Michael:** That is definitely a challenge. You obviously want to take care of your customers, and your business is actually running on those customers. But we never want our roadmap to be just the list of things that people have asked for. That’s where the longer-term thinking comes in. You have to balance the short-term, reactive stuff with the long-term. Stripe has a very, very long time horizon. If you know where you’re going over time, you can reason clearly about which specific asks are one-offs vs indicative of emerging trends relevant to many users.

## Multi-decade abstractions

**Ken:** What does long-term mean for Stripe? How far out are you looking?

**Michael: We talk a lot about building multi-decade abstractions.** I personally like to think 10 to 30 years to get out of the three- to five-year mode, but generally here people do say “multi-decade” a lot. Patrick and John and the entire leadership team are clear that this is a long-term bet and that we’re still very early. That long time horizon comes from the top, and it’s in the culture. And my sense is it’s been like that at Stripe since day one.

**Ken:** This is fun to hear because [I’ve argued for 30-year product visions](https://www.bringthedonuts.com/essays/ants-and-aliens-thirty-year-plan.html) before, but not many people have taken me up on it!

**Michael:** It’s always hard to look 30 years in the future and craft a particular product, but I think you can look at long-term trends. Stripe, if nothing else, is a long-term bet on the internet and globalization: commerce moving to the internet. Those are multi-decade trends inherently. It’s a bet on technology and startups. You can pick some of the long-term trends, and say “this is where things are going,” and you can then skate where the puck is headed on that front.

Then you can evaluate your short-term moves in light of which of those are actually taking you in the right direction. And which of them are maybe deviations from that direction. It’s important to know what hill you’re climbing. Then it’s much easier to know if the path you’re taking is optimal, or slightly sub-optimal, or headed off in the absolutely wrong direction.

## Comparing Stripe and Google

**Ken:** How is Stripe different from Google, a company we both know well?

**Michael:** It’s tough for me to compare because it’s such a different stage. I’ve heard from Xooglers at Stripe that it feels like Google in 2005, but I wasn’t at Google then. Google was 20,000 people at the point where I joined [in 2008]. And so a lot of the way it feels different to me is that it’s just so much smaller. Either way, it definitely feels easier to get things done here, with fewer layers to work through and more focus on getting to the right decision and getting there fast. And the amount of focus on really deeply understanding and working backward from users is also quite different.

There’s a lot of similar things, for sure. **Both companies have long-term big visions and optimism about the impact technology can have on people’s lives.** Both companies value technology and are product-focused.

**Ken:** Google’s use of OKRs plays a big role in reinforcing long-term planning and ambition. Does Stripe use something similar?

**Michael:** I would say we’re still settling into the right overall planning structure. We have multi-year plans at a company level, the actual narrative strategy that looks out several years and says, okay, this is the direction we’re going, and here’s how we see things evolving. And we are increasingly using a quarterly and annual goal-setting process similar to OKRs. I am running my team on quarterly goals plus two-page documents per area that frame those goals, and then specific project plans and strategy docs flow from them.

## What Stripe values in a PM

**Ken:** I know Stripe [didn’t have product managers in the beginning](https://www.forbes.com/sites/quora/2012/12/10/does-stripe-have-product-managers-or-do-engineers-manage-the-products-themselves/?sh=45d367a03344),[3](#ipfootnote2) or at least anyone with that title, as surely people across the org were doing the work. I remember meeting with [co-founder] John [Collison] in 2015 when PM was just starting to be formalized, and he wanted to soak up everything we’d learned at Google, especially about growing and mentoring PMs.

**Michael:** I’ve been here for a year and a half, so I wasn’t present for the evolution of it. It was at an inflection point when I joined where it was truly building out PM as a professional function. I joined well past the point where Stripe had decided that it was really important.

But I still didn’t know what I was going to be walking into. I’ve joined teams where you come in, and they’re “Oh, a PM. What am I supposed to do with you? Why are you here?” When I arrived at Stripe, I had one-on-ones with all of the engineering leads on the team and asked them about what they do and what their challenges were, and what they wanted out of product management. To a person, they knew *exactly* what they needed [from PM], and there was a huge amount of demand for help from us on lots of fronts: strategy, identifying target users, prioritization, helping set direction, and communication. That said, I do think we are still playing catch up in building up capacity on the product management side. [Note: Stripe has [tons of open product roles](https://stripe.com/jobs/search?t=product-and-technical.product-management%2Cproduct-and-technical.product-operations)!]

**Ken:** Who do you look for? What kind of PM would thrive at Stripe?

**Michael:** I think way back to 2010 when I first read your hiring essay [[How to Hire a Product Manager](https://www.bringthedonuts.com/essays/productmanager.html)], and it’s still canon and applies super well. We want technical PMs, strong product instincts, lead by influence, channel multiple points of view. At Stripe, we look for not just smart people but *quick* people. You will do well if you’re very, very agile. Being able to ingest a lot of complexity and then find a path of clarity through that. **Quick-thinking, quick-acting people do really well here.** 

We also want people who will not be held back by a lack of somebody handing them a checklist of all the steps to go through. Being able to thrive in ambiguity. You may have something in mind, but you go talk to customers and learn something totally different. People who are fluid with that will do very well. I do think we also look for PMs who are very technical for most roles.

**Ken:** Does that mean a CS degree?

**Michael:** Not a hard and fast rule, but our interview process does test people for their ability to actually think about technical problems. I think we go a step beyond understanding how systems work. Are you comfortable getting into it and thinking not just about how it works but about how it *should* work? It is not just the ability to work with engineers but also empathy for how the developers are using our infrastructure to build their systems.

You also have to have some degree of taste. While “taste” can be hard to define precisely, in some sense, whatever the domain — whether it’s music or something else — if you spend the time and you put a lot of thought into appreciating something, teasing apart what makes it great, and building a thoughtful, opinionated perspective, that’s taste.

[![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5e4c1cdb-b7f5-4897-b41e-62b3fb75fb04_1620x521.jpeg)![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5e4c1cdb-b7f5-4897-b41e-62b3fb75fb04_1620x521.jpeg)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5e4c1cdb-b7f5-4897-b41e-62b3fb75fb04_1620x521.jpeg)

Stripe’s website circa 2011 (from the Stripe Engineering Blog)


## Taste and the role of design

**Ken:** Say more.

**Michael:** It’s something that really does come through when you look around Stripe. One of our operating principles is “really, really care.” And you can tell when you’re talking to somebody just how much time they spent thinking about and caring about whatever it is that you’re discussing.

If they’re talking about an API, have they really deeply considered it? Are they passionate about the details? Those people who do so end up spiking high on taste. **It’s craftsmanship and a huge amount of dedication to getting all of the details right.** Much like a designer who’s putting all the pixels on the screen and getting the colors exactly right. That same degree of care applied to API development.

**Ken:** One of the things I find fascinating about Stripe is the extent to which the company is known for having outstanding design. Obviously, that includes the marketing site and the developer documentation that is cleaner and more beautiful than anything I’ve ever seen. So it’s interesting that a B2B company without a lot of UI is known for centering great design.

**Michael:** Right, people just really, really care about those things. I don’t know how that happened originally. Part of it is just who Patrick, John, and the leadership team are and the kind of people that they attracted. There’s a surprising amount of tastefulness and just caring about every angle of everything. Whether it’s the user experience, support experience, or how the brand presents itself. **There is just the feeling that it should all be exceptional. We should push for an extreme quality bar on all of the fronts.** 

Certain people are attracted to that, and they attract more people like them. And then it becomes part of the culture, right?

***Like what you hear? If so, there are [scores of product management job openings](https://stripe.com/jobs/search?t=product-and-technical.product-management%2Cproduct-and-technical.product-operations) at Stripe in hubs around the world and remote.***

[Share](https://newsletter.bringthedonuts.com/p/building-products-at-stripe?utm_source=substack&utm_medium=email&utm_content=share&action=share)

### Recommend Reading

* [A Quick Guide to Stripe’s Culture](https://stripe.com/jobs/culture)
* [Stripe’s Payment APIs: The First Ten Years](https://stripe.com/blog/payment-api-design)
* [Stripe’s Remote Engineering Hub, One Year In](https://stripe.com/blog/remote-hub-one-year)
* [Inner Workings of Design at Stripe](https://www.youtube.com/watch?v=08TsVjUKH4M)

[![](https://cdn.substack.com/image/twitter_name/w_36/shreyas.jpg)![](https://cdn.substack.com/image/twitter_name/w_36/shreyas.jpg)Shreyas Doshi @shreyas

@Suhail Stripe did not have people with the Product Manager title for several years.

First person with the PM title was hired in 2015 (5 years after founding).

But…. there were people that were performing the PM role before that and were clearly doing that quite well.

Role ≠ Title

September 4th 2020

1 Retweet156 Likes](https://twitter.com/shreyas/status/1301910476570329088)
[![](https://cdn.substack.com/image/twitter_name/w_36/isaach.jpg)![](https://cdn.substack.com/image/twitter_name/w_36/isaach.jpg)Isaac Hepworth @isaach

@seanrose @far33d stripe did not. i was the first PM hired by stripe and joined at ~200 people.

September 8th 2020

6 Likes](https://twitter.com/isaach/status/1303423923179016193?s=20)
[![](https://cdn.substack.com/image/twitter_name/w_36/isaach.jpg)![](https://cdn.substack.com/image/twitter_name/w_36/isaach.jpg)Isaac Hepworth @isaach

@seanrose @far33d by 500 employees there were about half a dozen full-time product managers at stripe.

September 8th 2020

4 Likes](https://twitter.com/isaach/status/1303424342106058752)
[![](https://cdn.substack.com/image/twitter_name/w_36/jeff_weinstein.jpg)![](https://cdn.substack.com/image/twitter_name/w_36/jeff_weinstein.jpg)Jeff Weinstein @jeff\_weinstein

A year in, here are the top 10 things I appreciate about Stripe and I’d suggest mimicking.

June 19th 2019

11 Retweets58 Likes](https://twitter.com/jeff_weinstein/status/1141154177944555520)
## 

1. I’m always careful to note when I have a relationship with a company I write about. That’s the case here with Stripe: I’m an investor through my interest in GV funds, and I provided occasional coaching and advice to the company while employed by GV (formerly Google Ventures). I’m also a customer: I use Stripe to run [my coaching business](https://www.bringthedonuts.com/coaching/).
2. During our conversation, Michael and I wondered if Patrick had added COVID-19 vaccines to [his list](https://patrickcollison.com/fast). Sure enough: it’s the most recent example.
3. Patrick’s Quora answer is from 2012 and no longer representative of the company’s thinking. But it’s an interesting historical artifact. Thanks to Stripe’s first PM, [Isaac Hepworth](https://twitter.com/isaach), for pointing me to the link!