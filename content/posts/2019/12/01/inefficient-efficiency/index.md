---
title: Inefficient Efficiency
date: '2019-12-01T22:49:25-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@kentbeck_7670/inefficient-efficiency-5b3ab5294791
---

[Inefficient Efficiency](https://medium.com/@kentbeck_7670/inefficient-efficiency-5b3ab5294791)  



![](https://miro.medium.com/fit/c/96/96/2*JAaDel4nA2PXn6UpDKQXvA.jpeg)![](https://miro.medium.com/fit/c/96/96/2*JAaDel4nA2PXn6UpDKQXvA.jpeg)

Kent Beck
Nov 26 · 4 min read




![]()


Now I’m Feeling Thirsty

You’re making morning drip coffee. You need to make 2 cups. Do you:

* Put 1 cups worth of water in the boiler so the water boils sooner and the first cup is ready sooner or,
* Put 2 cups worth of water in so both cups are done sooner?

I posted the question above on Twitter and received 50 replies (a lot for one of my tweets). Most of the comments were either snark or thoughtful coffee making advice, so I don’t think I got my point across.

Since my indirect approach didn’t get through, I’ll just out and say it:

* We all make latency/throughput tradeoffs every day.
* We bias these decisions towards throughput (I blame [Taylorism](https://en.wikipedia.org/wiki/Scientific_management)).
* High cost of delay, high chance of learning, and high rate of change all point towards prioritizing latency instead.

The coffee thing is just an illustration.

## Latency/Throughput

Latency [is](https://en.wikipedia.org/wiki/Latency_(engineering)) “the time interval between a stimulus and its response”. I want to get downtown. How long until I arrive? Latency is measured in time units.

Throughput [is](https://en.wikipedia.org/wiki/Throughput_(business)) “the rate at which a system achieves its goal”. People want to get downtown. How many arrive each hour? Throughput is measured in deliveries per time.

Sometimes latency and throughput interfere with each other. Buses might deliver more people per hour than individually hailed cars (higher throughput), but it takes me personally longer to get downtown because I have to walk to a bus stop and wait for the bus (higher latency).

Relationships between latency and throughput are not always so clear. If so many people hail rides that traffic gets bad, then latency and throughput both suffer. If enough people take the bus and traffic clears as a result then both latency and throughput improve.

## Coffee

Here, then, is the coffee example, not as a desperate plea for barista coaching but as an example of a tradeoff you make every day. Here are the activities in sequential coffee making:

![]()


Coffee making for latency

And here we make 2 cups “at the same time” (not really entirely in parallel, but I think you get the picture):

![]()


Coffee making for throughput

Line up the two and you see that the first version has better latency but the second version has higher throughput. Under what conditions does this difference make a difference?

* Optimize for latency when one consumer is desperate for a cup while the other doesn’t much care (e.g. is still asleep). The cost of delay for the first consumer is high.
* Optimize for latency when the maker of the coffee is likely to learn from mistakes. Better to have 1 mediocre cup and 1 great cup than have 2 mediocre cups delivered sooner.
* Optimize for latency when preferences are likely to change. If one consumer is likely to change their preference to tea while the first cup is brewing, then it’s worth delivering one cup at a time instead of wasting a second, “efficiently produced”, cup.

## The Analogy

In software development we face the equivalent of “one cup at a time or two” every day:

* Do we carefully plan all foreseen architectural improvements or do we get started with the first profitable change we find?
* Do we carefully pack specified features into a roadmap or do we implement the next most viable feature and figure it out from there?
* Do we carefully screen a large pool of candidates for a job or do we hire the first viable candidate, expecting to replace them if they don’t work out?

In each case the answer is, “It depends.” Three of the factors are:

* How much does delay cost?
* How likely are we to learn something that will change our approach?
* How likely are external forces to change our approach?

High scores on any (or all) of these measures suggest prioritizing latency over throughput.

You may notice the word “carefully” in all of the descriptions above. I had to accept the limits of my predictive powers. At some point, thinking further doesn’t help, only action followed by reflection helps. However, thinking feels mighty good and (as Bert Meyer said), “Bubbles don’t crash”. I think the illusory safety of thorough thought encourages my bias towards throughput.

## Intuition

Preferring to reduce latency even at a (potential) cost in throughput is one of those intuitions that my generation learned the hard way. I wrote about another when I discussed baskets of options. Both these intuitions seem to have gone out of fashion (he says, feeling like a get off my lawn old fart).

Betting against urgency, learning, and change is the exception, not the rule. I hope you learn this faster than I did.

The title of this piece is a pun. On the one hand, emphasizing throughput seems efficient but is actually inefficient. The [Peter Drucker quote](https://www.brainyquote.com/quotes/peter_drucker_105338) comes to mind, “There is nothing so useless as doing efficiently that which should not be done at all.”

The title can be read the other way. By emphasizing latency we get feedback sooner. Learning and adapting to external changes lead to less waste and therefore greater efficiency. Each piece is inefficient (compared to some theoretical maximum), but the whole is efficient.

In my world, latency dominates. Mostly. But it depends.