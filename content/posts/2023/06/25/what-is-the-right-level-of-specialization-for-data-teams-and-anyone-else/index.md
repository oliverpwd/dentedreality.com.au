---
title: What Is the Right Level of Specialization? For Data Teams and Anyone Else
date: '2023-06-25T00:48:08-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://erikbern.com/2021/07/23/what-is-the-right-level-of-specialization.html
---

[What Is the Right Level of Specialization? For Data Teams and Anyone Else](https://erikbern.com/2021/07/23/what-is-the-right-level-of-specialization.html)  



2021-07-23

This isn’t as much of a blog post as an elaboration of a tweet I posted the other day:

> I think this specialization of data teams into 99 different roles (data scientist, data engineer, analytics engineer, ML engineer etc) is generally a bad thing driven by the fact that tools are bad and too hard to use
> 
> — Erik Bernhardsson (@bernhardsson) [July 21, 2021](https://twitter.com/bernhardsson/status/1417664482776690692?ref_src=twsrc%5Etfw)

This seem to have resonated with a lot of people, but for whatever reason, it ended up being a lot more polarizing than I thought! There was a fair amount of misunderstanding of what I meant, so I just wanted to expand this into a slightly longer argument:

## Specialization is a good thing

I’m all for specialization! The society has come a long way from [subsistence agriculture](https://en.wikipedia.org/wiki/Subsistence_agriculture) and that’s almost objectively a good thing. The economy organizes people into different trades and different professions and lets people benefit from their [comparative advantage](https://en.wikipedia.org/wiki/Comparative_advantage).

There were a few replies (and [subtweets](https://twitter.com/tunguz/status/1417827377376202757)) misunderstanding my tweet as an argument against specialization. Which is a bit frustrating, because I think it’s pretty useless to argue against for or against specialization. Clearly, neither extreme is good? Like, subsistance agriculture isn’t great, but you could imagine going in the other extreme and organizing the society around people doing exactly one thing well and nothing else.

A restaurant could have one chef who only chops onions, another one who only souffles things, another one who only makes apple tarts. If this sounds dumb, then it’s because it’s intentionally hyperbolic! My point is, neither extreme is good, so the question is: what’s the *right level* of specialization?

## What are some drawbacks of specialization?

Not an exhaustive list:

* Resource allocation. If you have a chef who only chops onions, they are probably idle most of the time. That sounds bad! If they are more versatile, they can jump around and do a larger set of things, depending on what’s needed at the moment.
* Reduction of transaction cost. If every project involves coordinating 1,000 specialists, and each of those specialists have their own backlog with their own prioritization, then (a) cycle time would shoot up, with a lot of cost in terms of inventory cost and lost learning potential (b) you would need a ton more project management and administration to get anything done.

## Specialization is probably driven a lot by bad tools

So I think the question is, what is the right level of specialization? A bunch of people replied to me saying you need different roles because (I’m just picking one example) some people are better at training models, while some people are really good at all figuring out how to wrangle with Kubernetes and all of that stuff to get models deployed. *Which is exactly the point I was trying to make*. It seems fair that, if tools didn’t require so much knowledge to use (I’m looking at you, Kubernetes), then on the margin, the need for specialization would be less.

I’m super interested in this because I spent about 12 hours every day thinking about tools in the data science space. People are spending way too much time working on things that have nothing to do with their business. We have come a long way, but I still see people wasting *way* too much time debugging YAML, waiting for deployments, or begging the SRE team for help.

## It’s dangerous when people lose sight of the goal

I often think of people as (and this is an unfair crude generalization etc) roughly on a spectrum between *tools-oriented* and *goal-oriented*. Some people have their favorite tools, and that’s what they like to use. They make their whole career about honing a craft with those skills. Other people are more entrepreneurial, and don’t care about what tools they use: they care about the ultimate goal.

I think tools-oriented people can be valuable in certain contexts, like if you need some super deep expertise on some topic. If you’re trying to build a lithium mine in Angola, you might want to find experts in lithium mining and Angolan mineral rights.

But a lot of the time, experts can also be a huge liability, because they are overly biased towards picking tools that they have deep skills in. If you hire the world’s foremost expert in functional data structures for your e-commerce startup, you probably shouldn’t be surprised if that person wants to use functional data structures? And maybe that’s fine, if you are convinced that 100% of your problem can be expressed as operations on functional data structures, but more likely that’s not a pragmatic perspective, and you end up picking suboptimal tools for the job.

When this ends up segmenting different life cycles of a product, I think it gets even more sketchy. So much of the total cost of building tech products is post lauch. But also the opportunity to start iterating on it and learning from it! Adding hand-off points because of specialization feels like putting up a [Chinese Wall](https://www.investopedia.com/terms/c/chinesewall.asp) (in the business sense) between two functions that constrains the information flow and obstructs the value.

And what I also see to some extent is a bit of an entitlement attitude in some developers. They aren’t interested in doing the last 10% of the work that you need to get 100% of the value. Which frankly, I don’t really understand, because here’s the opportunity to shine. Let’s say you built a model that can save a gazillion trillion dollars for your company. If there was a tool to press a button to put it into production, why wouldn’t you want that? You can do it yourself without having to coordinate with other teams, and you can be the hero of the day!

(I’m writing this about deploying ML models, but that’s really just one example… there’s a lot more going on in the data world: pipelines, reporting, monitoring, …).

I mean, I think we’re very far from this, tools-wise, but we should aspire to get there! Let’s not argue against this world on arbitrary grounds of the benefit of specialization. Let’s instead think about what that world would look like, and what tools we would need to get there, and then *let’s build those tools*. This is basically what I’m obsessed with and I think it’s a somewhat ambitious perspective, but I think there’s an incredible opportunity!