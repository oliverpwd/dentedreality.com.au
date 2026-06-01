---
title: Agility ≠ Speed
date: '2021-11-26T15:52:21-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://kevlinhenney.medium.com/agility-speed-96057078fe40
---

[Agility ≠ Speed](https://kevlinhenney.medium.com/agility-speed-96057078fe40)  



## Software development benefits from a sense of direction

[![](https://miro.medium.com/fit/c/56/56/0*0FHiiXZNl75te565.jpg)![](https://miro.medium.com/fit/c/56/56/0*0FHiiXZNl75te565.jpg)](https://kevlinhenney.medium.com/?source=post_page-----96057078fe40-----------------------------------)
[Kevlin Henney](https://kevlinhenney.medium.com/?source=post_page-----96057078fe40-----------------------------------)

10 hours ago·9 min read






![](https://miro.medium.com/max/1400/1*fBRjlac1JsyDHeldjqAlgw.jpeg)![](https://miro.medium.com/max/1400/1*fBRjlac1JsyDHeldjqAlgw.jpeg)

This article first appeared in [**Tips From The agile Trenches**](https://www.hanoulle.be/book/tips-from-the-agile-trenches/)

I was changing a lightbulb this morning and was struck by a shift that has occurred in recent years. Lightbulbs used to be sold according to their power consumption. People were entrained to buy bulbs according to power rating — what the bulb consumed from the electrical grid — rather than brightness — what they, as consumers, actually benefited from.

Filament bulbs are incredibly inefficient, producing more heat than light (which certainly has parallels in many discussions in software development). It is not simply that old bulbs were inefficient, but that this inefficiency was both stable — the brightness of 60 W bulbs changed little over decades — and expected. The expectation reinforced the idea that efficiency would not improve. It was an expectation that masked many assumptions and created secondary industries, such as lava lamps. Delightful as they are, the only reason lava lamps were ever a thing is because incandescent lightbulbs produce so much waste heat.

The problem is clear and, had we been able to look past our assumptions, it was always clear. Brightness is measured in [lumens](https://www.bipm.org/en/measurement-units). A whole industry was built on having people buy according to the wrong measure. For as long as it was stable and widely used, it was unquestioned and acted as a suitable proxy. But in the presence of change people have found they are so accustomed to using the wrong measure that they struggle to know what they actually want using the right measure. It is common for modern energy-saving bulbs to be sold by lumens in conjunction with an old wattage equivalent that accompanies their actual power consumption.

In software development — a discipline built on abstraction — we should be wise to this phenomenon… but all too often we are taken in by it. Marketeers and advertisers talk about ‘engagement’ metrics for websites, but the one thing their metrics do not actually measure is engagement. Product owners are encouraged to ‘prioritise by business value’, when [such an approach is impossible](https://kevlinhenney.medium.com/changing-your-priorities-19202e42546e) within the laws of physics as we currently understand them — by all means prioritise by estimated business value, but don’t fool yourself into thinking that an *estimate* is an *actual*. Teams that aspire to be more agile have created currencies of story points and have ritualised development velocity. They have mistaken a weak proxy measure as a meaningful system of estimation, an indication of progress and a mark of quality. This is not agility.

An obsession with speed often overtakes the core values of agile software development. It’s not just the development of software; it’s the development of working software. And we should be cautious of any language or technique that optimises around project management measures. Software development is better thought of in terms of [*product development* than *project management*](https://kevlinhenney.medium.com/getting-over-the-waterfall-c090c6228ca9), therefore time to market is typically less important than time in market. Sprinting matters less than endurance.

## Sprints are not about sprinting

Our thinking about business and the business of software is framed in terms of the language we use. Sometimes our words and metaphors can hinder just as much as they can help. For example, when Scrum originally adopted the word *sprint* in the early 1990s, it was to contrast it with the word *iteration*. At the time, when people spoke of iterative and incremental development, iterations could be months long — objectives would meander and scopes would drift. By contrast, the word *sprint* suggested an activity that was directed, short and uninterrupted. This was the original sense and, for its time, it had value.

Times change and time changes everything, including our words. The mechanics of software delivery have become fine grained to the point of continuous. The intended distinction between *sprint* and *iteration* is long gone; the residual meaning is that sprint after sprint after sprint sounds exhausting.

The 30-calendar-day sprint of old has dropped to a common default of two weeks for most Scrum teams. Iterations in other development approaches have also experienced deflation from months to weeks, from weeks to week and, in many cases, to nothing — the discrete timebox disappearing into a stream of lean continuity. There is no longer a meaningful time-based distinction between *sprint* and *iteration*. The remaining distinction is one of context — Scrum vocab or not — and implication — sprint overwhelmingly suggests speed.

And ‘overwhelming’ is the problem. Unaware of its origin story and intent, many now favour the word *sprint* over *iteration* because of the implication of raw speed, not because they are necessarily employing Scrum. Rather than being shielded from pressures and interruptions, teams routinely experience them with increased frequency and intensity. Rather than finding better ways of working, teams find themselves micromanaged. Rather than being able to manage their flow, teams become overwhelmed.

Which leads us to the seemingly koan-like paradox: sprints are not about sprinting; sprints are about sustainable pace.

## Measure for measure

Many teams and managers put a great deal of effort into measuring and tracking their velocity. In theory, what they are tracking is progress over time. In practice, however, they are more likely tracking how much work they have put into developing the system over a particular period of time, such as a sprint, or how accurate their estimates are, or what their utilisation is.

User stories are often estimated and tracked according to a measure of relative effort, such as story points or T-shirt sizes. The proposed benefit of not using real time is that estimates are decoupled from targets, thus developers should estimate in terms of the functionality rather than being biased by desired dates. [Giovanni Asproni](https://97-things-every-x-should-know.gitbooks.io/97-things-every-programmer-should-know/content/en/thing_50/) highlights the importance of decoupling these concepts:

> To be able to estimate well it is obviously important to learn some estimation techniques. First of all, however, it is fundamental to learn what estimates are, and what they should be used for — as strange as it may seem, many developers and managers don’t really know this.
> 
> Estimates, targets, and commitments are independent from each other, but targets and commitments should be based on sound estimates.

The intent of story points is to focus on relative sizing independently of other expectations of time. The problem is that, in being numeric, story points become a currency susceptible to arithmetic, especially once they’ve been aggregated. Rather than the approximation an estimate is intended to be, story points invite conversion while offering the illusion of precision. Once a conversion rate is established, the converted value becomes how people think and talk about them, whether tacitly or explicitly. Story points degenerate into a measure of time, albeit one abstracted enough from real time that, like any currency, they become subject to speculation and inflation. Although a looser fit, T-shirt sizes (S, M, L, XL, etc.) can also fall into the same trap.

And what does the conversion rate — sorry, velocity — mean? If we travel 200 km in two hours, that tells us that we are travelling at 100 km/hour. We have a measure of distance against time. What does it mean to say that a team burned through a total of 100 points in two weeks? If points are a proxy measure of time, we can convert from 100 points to a number of hours or days… which means that the rate derived is a measure of… time against time?! We are either measuring utilisation or we are tracking estimated against actual time, i.e., accuracy of estimation. The one thing we are not measuring is progress in the software developed.

If keeping developers busy was the main goal of software development, all would be good… but the goal of software development lies in the development software, not the consumption of development hours.

> If there’s one management platitude that should have been throttled at birth, it’s “what gets measured gets managed”. It’s not that it’s not true — it is — but it is often misunderstood, with disastrous consequences.
> 
> The full proposition is: “What gets measured gets managed — even when it’s pointless to measure and manage it, and even if it harms the purpose of the organisation to do so.”

> Working software is the primary measure of progress.

Of course, measuring such progress can be subtle and non-trivial, which is why we often favour simplifications, sometimes at the expense of meaning. As with any abstraction, the problems arise when we fail to understand the limits and implications of our simplifications, and we end up pursuing our abstractions at the expense of our concrete goals, conflating our indications with our ambitions. As H Thomas Johnson cautions:

> Perhaps what you measure is what you get. More likely, what you measure is all you’ll get. What you don’t (or can’t) measure is lost.

The irony of tracking is that it is all too easy to lose track of what we actually want.

## The physics of velocity

The language of *velocity*, which comes originally from Extreme Programming rather than Scrum, is metaphorically compatible with *sprint*. But there is a subtlety in this word choice that deserves our attention. In everyday language it is common to treat *velocity* as a synonym of *speed*, albeit one that sounds more formal and technical. But if we are being formal and technical — a reasonable expectation in the formal and technical discipline of software development — the more precise meaning is that velocity is the rate of change of position, not just the rate of change of distance. To move from one position to another is not just described by a magnitude: it also entails a direction. It is one thing to state we are travelling at 100 km/hour; it is quite another to observe we are travelling 100 km/hour north… especially when we should be heading south.

The busyness of the development team is not that interesting or useful, but it is easy to measure and report. Essentially, this corresponds to speed. The degree to which the team is building the right thing in the right way at a good pace, however, is harder to assess. Harder to assess, but it is meaningful and useful. If you are going to track velocity, then track velocity. Most velocity metrics are actually speed metrics; most speed metrics are just utilisation or estimation metrics. To track velocity, focus on functionality completed (not functionality worked on), focus on functionality delivered (not functionality requested or promised), focus on functionality used (not estimates of business value), track defects (and time spent on defects), track technical debt (not just having it and repaying it, but [the consequences of having it](https://www.oreilly.com/radar/on-exactitude-in-technical-debt/)) and so on. As in physics, velocity in software development is multidimensional.

If we make speed our focus, we game ourselves to develop faster, which may lead to making ourselves visibly and frantically busy at the expense of meaningful progress. Faster… yet also later and exhausted. Many teams seem to be trapped in a [Red Queen’s race](https://www.gutenberg.org/files/12/12-h/12-h.htm):

> “Well, in our country,” said Alice, still panting a little, “you’d generally get to somewhere else — if you ran very fast for a long time, as we’ve been doing.”
> 
> “A slow sort of country!” said the Queen. “Now, here, you see, it takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!”

Although we may find ourselves nodding along to or advocating the mantra of “deliver better software, faster”, we should pause a moment to realise that what we probably mean is “deliver better software, sooner”. The difference is both subtle and huge.

## The physics of agility

It’s not that agility doesn’t involve speed; it’s more that it involves velocity. But the physics metaphor doesn’t stop there. Even understanding progress in terms of direction stops short of fully appreciating that this is not still not what is meant by *agile development*. Of course, if most teams chasing agility stopped chasing story points and forcing delivery, and focused instead on identifying and removing obstacles from the path of development, that would be a significant improvement on their status quo. This would definitely be leaner, but it would not necessarily be more agile. It would streamline the flow of development, but it would not necessarily improve the ability to respond to change. For all the non-prescriptiveness of the [Agile Manifesto](https://agilemanifesto.org/), that is unambiguously a core value:

> Responding to change over following a plan

That is what the word *agile* entails. It is not simply achieving a sustainable speed in an optimal direction; it is being able to change both speed and direction, and to do so easily. It is the second derivative of position with respect to time, not just the first: agility relates both to velocity and to the ability to change it, revising direction and pace as circumstances demand.

The pipeline metaphor often used in software development, from [waterfall](https://kevlinhenney.medium.com/getting-over-the-waterfall-c090c6228ca9) to CI/CD, can be a helpful starting point, but agility is found not in following the line — or following it at great speed — but in how individuals interact to respond to faults and kinks in the line, to the line veering off, to the line breaking.

Agility is not speed; it’s something far more useful and far more interesting.