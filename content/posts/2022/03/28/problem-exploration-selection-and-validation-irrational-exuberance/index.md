---
title: Problem exploration, selection and validation. | Irrational Exuberance
date: '2022-03-28T11:59:13-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/intro-product-management/
---

[Problem exploration, selection and validation. | Irrational Exuberance](https://lethain.com/intro-product-management/)  



![](https://lethain.com/static/blog/2018/prod-mgmt-hero.png)![](https://lethain.com/static/blog/2018/prod-mgmt-hero.png)

Most engineering organizations separate engineering and product leadership into distinct roles. This is usually ideal, not only because these roles benefit on distinct skills, but also because they thrive from different perspectives and priorities. It’s quite hard to do both well at the same time.

I’ve met many product managers who are excellent operators, but few product managers who can operate at a high degree while also getting deep with their users’ needs. Likewise, I’ve worked with many engineering managers who ground their work in their users needs, but few who can affix their attention on those users when things start getting rocky within their team.

Reality isn’t always accommodating of this ideal setup. Maybe your team’s product manager leaves or a [new team is being formed](https://lethain.com/durably-excellent-teams/), and you, as an engineering leader, need to cover both roles for a few months. This can be exciting, and yes, this can be a time when “exciting” rhymes with “terrifying.”

Product management is a deep profession, and mastery requires years of practice, but I’ve developed a simple framework for product management to use when I’ve found [myself fulfilling product management](https://lethain.com/product-management-infra-engineering/) responsibilities for a team. It’s not perfect, but hopefully it’ll be useful for you as well.

Product management is an iterative elimination tournament, with each round consisting of *problem discovery*, *problem selection* and *solution validation*. *Problem discovery* is uncovering possible problems to work on, *problem selection* is filtering those problems down to a viable subset, and *solution validation* is ensuring your approach to solving those problems work as cheaply as possible.

If you do a good job at all three phases, you win the luxury of doing it all again; this time with more complexity and scope. If you don’t do well, you end up forfeiting or being asked to leave [the game](https://www.amazon.com/dp/B004W3FM4A/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1).

## Problem discovery

The first phase of a planning cycle is exploring the different problems you could pick to solve. It’s surprisingly common to skip this phase, but that unsurprisingly leads to inertia-driven local optimization. Taking the time to evaluate which problem to solve is one of the best predictors I’ve found of a team’s long-term performance.

The themes I’ve found useful for populating the problem space are:

* **Users’ pain**. What are the problems that your users experience? It’s useful to both go broad via survey mechanisms as well as to go deep by interviewing a smaller set of interesting folks across different user segments.
* **Users’ purpose**. What motivates your users to engage with your systems? How can you better enable them to accomplish their goals?
* **Benchmark**. Look at how your company compares to competitors in the same and similar industries. Are there areas that you are quite weak? Those are areas to *consider* investment. Sometimes folks keep to a narrow lense when benchmarking, but I’ve found that you learn the most interesting things by considering both fairly similar and rather different companies.
* **Cohorts**. What is hiding behind your clean distributions? Exploring your data for the cohorts hidden behind top-level analysis is an effective way to discover new kinds of users with surprising needs.
* **Competitive advantages.** By understanding the areas you’re exceptionally strong in, you can identify opportunities that you’re better positioned to fulfill than other companies.
* **Competitive moats**. Moats are a more extreme version of a competitive advantage. Moats represent a sustaining competitive advantage, which make it possible for you to pursue offerings that others simply cannot. It’s useful to consider moats in three different ways:
  + What your existing moats enable you to do today?
  + What are the potential moats you could build for the future?
  + What moats are your competitors luxuriating behind?
* **Compounding leverage**. What are the composable blocks that you could start building today that will compound into major product or [technical leverage](https://lethain.com/building-technical-leverage/) over time? I think of this category of work as finding ways to get the benefit (at least) twice. This are potentially tasks that initially don’t seem important enough to prioritize, but whose compounding value makes it possible.
  + A design example might be introducing a application new navigation scheme that better supports the expanded set of actions and modes you have today, and that will support future proliferation as well. (Bonus points if it manages to prevent future arguments about positioning of new actions relative to existing ones!)
  + An infrastructure example might be moving a failing piece of technology to a new standard, this addresses a reliability issue, reduces maintenance costs, and also [reduces the costs of future migrations](https://lethain.com/migrations/).

## Problem selection

Once you’ve identified enough possible problems, the next challenge is to narrow down to a specific problem portfolio. Some of the aspects I’ve found useful to consider during this phase are:

* **Surviving the round**. Thinking back to the iterative elimination tournament, what do you need to do to survive the current round? This might be the revenue the product will need to generate to avoid getting canceled, adoption, etc.
* **Surviving the next round**. Where do you need to be when the next round starts, to avoid getting eliminated then? There are a number of ways, many of them revolving around quality tradeoffs, to reduce long-term throughput in favor of short term velocity. (Conversely, winning leads to significantly more resources later, so that tradeoff is appropriate sometimes!)
* **Winning rounds**. It’s important to survive every round, but it’s also important to eventually win a round! What work would ensure you’re trending towards winning a round?
* **Consider different time frames.** When folks disagree which problems to work on, I find it’s most frequently rooted in different assumptions about the correct time frame to optimize for. What would you do if your company was going to run out of money in six months? What if there were no external factors forcing you to show results until two years out? Five years out?
* **Industry trends**. Where do you think the industry is moving towards, and what work will position you to take advantage of those friends, or at least avoid having to redo the work in near future?
* **Return on investment**. Personally, I think folks often under prioritize quick, easy wins. If you’re in the uncommon position of understanding both the impact and costs of doing small projects, then take time to try ordering problems by expected return on investment. At this phase you’re unlikely to know the exact solution, so figuring out cost is tricky, but for categories of problems you’ve seen before you can probably make a solid guess (if you don’t personally have relevant experience, ask around). Particular in cases where wins are compounding, these are be surprisingly valuable over the medium and long term.
* **Experiments to learn**. What could you learn now that would make problem selection in the future much easier?

## Solution validation

Once you’ve narrowed down the problem you want to solve, it’s easy to jump directly into execution, but that can make it easy to fall in love with a difficult approach. Instead, I’ve found it well worth it to derisk your approach with an explicit solution validation phase.

The elements I’ve found effective for solution validation are:

* **Write a customer letter.** Write the launch announcement that you would send after finishing the solution. Are you able to write something exciting, useful and real? It’s much more useful to test it against your actual users rather than relying on your intuition.
* **Identify prior art**. How do peers across the industry approach this problem? The fact that others have solved a problem in a certain way doesn’t mean it’s a great way, but it does at least mean it’s possible. A mild caveat that it’s better to rely on folks you have some connection to instead of conference talks and such; there is a surprisingly large amount of misinformation out there.
* **Find reference users**. Can you find users who are willing to be the first users for the solution? If you can’t, you should be skeptical whether what you’re building is worthwhile.
* **Prefer experimentation over analysis**. It’s far more reliable to get good at cheap validation than it is to get great at consistently picking the right solution. Even if you’re brilliant, you are almost always missing essential information when you begin designing. Analysis can often uncover missing information, but it depends on knowing where to look, whereas experimentation allows you to find problems you didn’t anticipate.
* **Find the path more quickly traveled**. The most expensive way to validate a solution is to build it in its entirety. The upside of that approach is that you’ve lost no time if you picked a good solution, the downside is that you’ve sacrificed a huge amount of time if it’s not. Try to find the cheapest way to validate.
* **Justify switching costs**. What will the switching costs be for users who move to your solution? Even if folks want to use it, if the switching costs are too high then they simply won’t be able to. Test with your potential users if they’d be willing to pay the full cost of migrating to your solution instead of their existing planned work.

As an aside, I’ve found that most aspects of [running a successful technology migration](http://lethain.com/migrations) overlap with good solution validation! This is a very general skill that will repay the time you invest into learning it many times over.

Putting these three elements today–exploration, selection and validation–won’t make you an exceptional product manager overnight,  

but they will provide a solid starting place to develop those skills and perspective for the  

next time you find yourself donning the product manager hat.

Published on August 20, 2018.