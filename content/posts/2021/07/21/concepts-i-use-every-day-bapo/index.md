---
title: 'Concepts I Use Every Day: BAPO'
date: '2021-07-21T22:15:33-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/nerd-for-tech/concepts-i-use-every-day-bapo-896d0ba0ccbb
---

[Concepts I Use Every Day: BAPO](https://medium.com/nerd-for-tech/concepts-i-use-every-day-bapo-896d0ba0ccbb)  



[![](https://miro.medium.com/fit/c/96/96/1*KHB2h8mrucKz3utPsZij4w.png)![](https://miro.medium.com/fit/c/96/96/1*KHB2h8mrucKz3utPsZij4w.png)](https://jchyip.medium.com/?source=post_page-----896d0ba0ccbb--------------------------------)
[Jason Yip](https://jchyip.medium.com/?source=post_page-----896d0ba0ccbb--------------------------------)
[Jul 4](https://medium.com/nerd-for-tech/concepts-i-use-every-day-bapo-896d0ba0ccbb?source=post_page-----896d0ba0ccbb--------------------------------) · 3 min read



# Because org structure change can get messy, there’s a tendency to have structure drive strategy

## Changing org structure can be messy

![]()


There are several reasons why org structure changes can get messy:

* **Changing org structure can mean changing managers.** Given “people leave managers, not companies”, the org structure change can trigger problems including departures;
* **Changing org structure typically means responsibilities are re-allocated.** People are no longer responsible for work they used to be responsible for and/or they are now responsible for work that they might not want to do. This can lead to disengagement or even departures;
* **From the manager side, changing org structure can mean more or less direct reports.** This can mean overwork with too many reports and contexts to stay on top of. This can mean status threat and political jockeying with too few reports;

## Organisation constrains architecture; architecture constrains strategy

> “Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization’s communication structure.”
> 
> Melvin E. Conway

Conway’s law is an observation that technical architectures tend to mirror the organisation structure.

Architecture constrains strategy. You can’t pretend that teams are operating autonomously on distinct goals when all their activities require modifying the same coupled technical architecture.

![]()

“Autonomous” teams working on a shared monolith

## Therefore structure drives architecture which drives strategy?

So typically, org structure drives the appropriate technical architecture, and the technical architecture constrains what’s considered for product strategy.

There is a logic to this… and it relies on an assumption that the larger business/product context should care about your internal organisational problems.

![]()

It’s the wrong problem but it’s what our technology and org is designed for

“Structure drives strategy” is an inside-out way of thinking.

# BAPO: Business → Architecture → Process → Organisation

> “Unless structure follows strategy, inefficiency results.”
> 
> Alfred D. Chandler Jr.

“Strategy drives structure” is an outside-in way of thinking. [BAPO is Jan Bosch’s expression of “strategy drives structure”](https://janbosch.com/blog/index.php/2017/11/25/structure-eats-strategy/).

![]()


[Structure Eats Strategy — Software Driven World (janbosch.com)](https://janbosch.com/blog/index.php/2017/11/25/structure-eats-strategy/)

**Business** (or product) strategy drives technical **Architecture** which drives **Process** (aka ways of working) which drives **Organisation** structure.

Reality is messier and more iterative but this general direction of “what drives what” makes sense.

*NOTE: I typically use Product Strategy → Technical Architecture → Ways of Working → Org Structure but it doesn’t have a pronounceable acronym.*

## BAPO step-by-step

*(Again, reality is messier and more iterative)*

1. **Categorise product capabilities according to where they are in the** [**product lifecycle**](https://hbr.org/1965/11/exploit-the-product-life-cycle)**.** In other words, what capabilities are commodity versus differentiating versus innovation;
2. **Adjust architectural service boundaries and dependencies** to remove coupling across lifecycle stages and create one-way dependency from more volatile to more stable (and never vice versa);
3. **Set up appropriate ways of working (and KPIs) depending on the product lifecycle stage.** For example, we want to minimise effort and cost for commodity capabilities, we want to iteratively and incrementally improve performance for differentiating capabilities, and we want to run a lot of experiments to find new opportunities for innovation capabilities;
4. **Design the org structure to group related capabilities.** You generally want to avoid mixing working styles which means generally avoiding mixing capabilities in different lifecycle stages.

# References

# See also

* [ESAO](https://publications.lib.chalmers.se/records/fulltext/198701/local_198701.pdf) (Ecosystem, Strategy, Architecture, Organising);
* [Pioneers, Settlers, and Town Planners](https://blog.gardeviance.org/2012/06/pioneers-settlers-and-town-planners.html)