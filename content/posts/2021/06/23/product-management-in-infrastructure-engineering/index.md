---
title: Product Management in Infrastructure Engineering
date: '2021-06-23T23:15:46-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/product-management-infra-engineering/
---

[Product Management in Infrastructure Engineering](https://lethain.com/product-management-infra-engineering/)  



![](https://lethain.com/static/blog/2018/prod-mgmt-infra-hero.png)![](https://lethain.com/static/blog/2018/prod-mgmt-infra-hero.png)

Recently a bunch of teams I work with have turned the corner, having paid down technical debt to a long-term sustainable level. The future unfurls with possibility. We can do *anything*. That’s exciting! It can also be pretty disorienting. For me, this is the most inspiring moment of management, and one of the hardest.

When we were completely focused on system reliability or churning tasks, most teams pulled their roadmaps down to a month or two, and we got so focused that we disconnected from our internal users. With less time soaked by maintenance, we’ve scurried to understand our users’ needs and define an optimistic, future-facing roadmap to support them.

In short, we’ve bootstrapped product management.

Many of the infrastructure engineer teams I’ve been a part of have struggled to make the transition from maintenance to innovation, and I wanted to write down some of the ideas that we’re exploring to ease this shift. I’d also love to hear what has worked well for other folks!

## Foundation to Innovation

I believe teams tend to have two distinct modes of operation:

* a foundation mode where the vast majority of tasks are mandatory, driven by non-negotiable needs like compliance, security, reliability and “victim of success” challenges like scaling a very popular product. Kanban is optimized for this mode, and I think [The Phoenix Project](https://www.amazon.com/dp/B00AZRBLHO/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1) is a really helpful resource on executing in this mode.
* an innovation mode where you have a lot of flexibility in which problems to prioritize and how to solve them. This is similar to product development as [described in Inspired](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507/ref=dp_ob_image_bk).

In practice many teams have one foot in both modes, and most teams cycle between the two over time, but for any given team at any given time, they usually have a primary model.

The foundation mode is a game of execution, focus and limiting work-in-progress, whereas the innovation mode is about listening to users, exploring solution spaces and an eternal focus on validating solutions as early and cheaply as possible.

Most infrastructure teams have a lot of experience in foundation, but have much less in innovation, so I won’t belabor managing through scarcity, and will instead dive into how to manage in times of surplus engineering capacity.

## Problem discovery

When you have surplus engineering capacity, folks tend to have a long backlog of stuff they’d like to work on, and many teams immediately jump on those, but I think it’s useful to fight that instinct and to step back and do deliberate discovery.

There are two things that are essential to discovering opportunity: cast a very broad net, and don’t evaluate ideas while discovering them. Try to get as many ideas as possible, and don’t spend a single moment worrying if they’re any good, prioritization is a later step.

I recommend taking a four prong approach, learning about your users’ needs, what peer companies are doing, where industry leaders are going, and brainstorming with your team.

Some of the techniques that I’ve seen work well:

* **SLAs** – sit down with your users to discuss what SLAs they expect from your system, and then turn those into your dashboards. Even if you can’t hit some of those SLAs today, understanding what users want you to be able to offer is powerful.
* **User surveys** – it’s surprisingly hard to write a great survey, and easy to create survey fatigue, but a good survey is an awesome way to get many folks to share input. A good survey is a short, quantifies when possible, and gets proofread by folk with opposing perspectives before it’s sent out! They’re especially good as a first step to identify who to follow up with in detail.
* **Coffee chats** – meet with your users periodically and learn about what they’re doing. Do remember to ask if there is stuff you can improve, but I think it’s most valuable to understand what they’re doing, which is great fodder for thinking about how you can help. A cheaper version of this is a short email with a quick compliment and asking if you could help with anything.
* **Discussion groups** – bringing together a small group of two to four folks and hearing their ideas is a good way to get input. I find these work best when you can bring a specific proposal, or set of proposals, for folks to react against. As a variant, we’ve also experimented with recurring customer advisory groups.
* **Peer-company chats** – in addition to chatting with your users, I’ve found it equally valuable to chat with a wide variety of folks working on similar problems at other companies to understand how they’re thinking about things. I’ve heard some extremely valid concerns around this leads directly to cargo-culting and groupthink, which is why I think it’s so important to decouple discovery from prioritization: listen to what other folks are doing, don’t automatically decide to adopt them.
* **Academic and industry research** – look for papers coming out of the big tech companies (Google, Microsoft, Facebook, etc) and also for academic research on a given area. I did a basic example of this [when I surveyed load generation research](https://lethain.com/braindump-on-load-generation/), and it was helpful to expand my thinking beyond the obvious.
* **Open source** – [along the lines of my exploration of the open source data ecosystem](https://lethain.com/from-lambda-to-kappa-dataflow-paradigms/), I find it useful to spend some time understanding the state of open source for a given area. This gives you an easy sense of trends and how other folks see the space evolving.
* **Cloud vendors** – with [cloud offerings rapidly expanding](https://lethain.com/physics-of-cloud-expansion/), it’s useful to take a look at what new related offerings have popped up on AWS, Azure, GCP and such.

The goal of each of these is to collect a tremendous amount of information. My mental model of this phase is to load as much state into your head as possible, to give you a broad perspective as you move into prioritization.

## Prioritization

Brimming with research and user needs, I try to create three artifacts:

* A **charter** that identifies the unique value your team tries to provide, your competitive advantages and the strategy that you’ll employ.
* An **optimistic three-year vision** of the best possible system you’d like to be providing. Constrain the vision by what is possible, but don’t constraint it by what is reasonable. My rule of thumb is “where could we be if everything went perfectly for three years?”
* A **prioritized list of user pain** that captures your users’ active needs, and in particular buckets the concerns together into things that you might be able to address, eliminate or empower with a single solution.

Your aim is to relieve as much user pain as possible while also making forward progress towards your optimistic vision. I think doing this well is the artistry of product management, and I believe each project can usually make significant progress towards both.

Changing priorities late in a project is expensive, so we try to align on priorities as early as possible, and allow users as much input as possible early to weigh in on which parts will be useful to them, and in particular which parts can be used independently. A great list of priorities allows us to deliver incremental value to our users at each phase, not waiting until the last step to deliver a big bang of utility.

Sometimes current needs don’t align well with the future, or the future is a long ways away, and in that case my rule of thumb is to invest 70% of your effort on solving immediate user needs, and 30% on advancing towards the future. I advocate 70% towards immediate user needs, because I think folks tend to over index on the future, and this helps avoid falling into that trap.  

[In areas where cloud vendors are rapidly expanding](https://lethain.com/physics-of-cloud-expansion/), sometimes it may be reasonable to devote 100% of your efforts to immediate user pain, on the assumption that cloud offerings will be available in the next 2-3 years to absorb the operational load and technical debt of the existing solution. Some areas are not likely to get cloud investment in the near term, but increasingly we should be looking at areas we can strategically underinvest today on the assumption that the clouds will provide an easy solution soon.

## Solution validation

Once you’ve decided what to focus on solving, a many teams immediately go “full waterfall”, designing a twelve month roadmap. Long-term planning is hard to resist, because pretty much every user and every planning process demands it of you, so you’ll probably end up writing an artifact of this nature, but I beg you not to pretend it means something.

This isn’t because estimating is hard–although estimating is hard–but because it assumes that our solutions are actually good solutions. It’s my opinion that most solutions are, in fact, pretty bad. The secret is not to “get brilliant” and pick better solutions, but rather to get skeptical and to design your approach to validate the value and practicality of solutions as cheaply as possible.

I often assume that internal users have a great sense of existing capabilities, but that sometimes isn’t the case. Part of “getting skeptical” is evangelizing your existing solutions and seeing if there is already a reasonable way to solve the problem under discussion that maybe you haven’t documented well or requires some architectural familiarity between both the users and the providers to realize a solution is already available.

It’s a common pattern to do the hardest migration first, and I’m a big fan of that approach, but even then you’ve spent the majority of the time required to build a system by the time you’re validating it. Do experiments, gather data to prove the approach won’t work, validate the approach has worked for others. Try as hard as possible to prove your solution cannot work.

Once you’ve validated a solution, you also want to keep in mind similar needs from other users. The pattern might look like doing one hard integration first, and then doing a staccato burst of easy integrations to smooth the edges and check for broad applicability.

We’ve been experimenting with the pattern of embedding the team building a solution into the team they’re building the solution for, and that feels like a good strategy for quick iteration and avoiding falling in love with awesome things that are not necessarily useful things.

## Closing

There are many infrastructure engineering teams which don’t make the transition from maintenance to innovation, and some which intentionally decide against doing so. It’s an uncomfortable transition, but I’ve found it remarkably rewarding: more direct contribution to your coworkers’ success, more excitement from other leaders within the company, and shrugging off the mantle of cost center to become an acknowledged source of innovation.

While I’m really excited at how this approach has helped us focus on directly supporting our users, it’s still an early approach. Three questions in particular continue to bounce around in my head:

1. User discovery takes up a bunch of time from other teams. How can we be more effective with their time?
2. How do we avoid falling in love with solutions, particularly for those that are difficult to validate early?
3. How do other folks do this!?

If you’re doing something different, or even if you’re doing something similar, I’d love to hear from you!

Thanks to [Amy](https://twitter.com/amyngyn), [Peter](https://twitter.com/peterseibel) and [Ranbir](https://twitter.com/TheRanbirChawla) for shaping this post.