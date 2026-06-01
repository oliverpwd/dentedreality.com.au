---
title: Can You Really Measure Individual Developer Productivity?
date: '2020-11-27T16:53:01-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://blog.pragmaticengineer.com/can-you-measure-developer-productivity/
---

[Can You Really Measure Individual Developer Productivity?](https://blog.pragmaticengineer.com/can-you-measure-developer-productivity/)  



A reader asks a question that comes up at some point in every engineer’s and engineering manager’s career, where their manager, or the one above will pop the question. Can you measure engineering productivity? And if so, how can we measure it right now? They ask:

> I work as an engineering manager for a company whose non-technology leadership insists there has to be a way to measure the individual productivity of a software engineer. I have the opposite belief. I don’t believe you can measure the productivity of “professional” careers, or thought workers (ex: how do measure productivity of a doctor, lawyer, or chemist?). For software engineering in particular, I feel that metrics can be gamed, don’t tell the whole story, or in some cases, are completely arbitrary.
> 
> Do you measure individual developer productivity? If so, what do you measure, and why do you feel it’s valuable? If you don’t and share similar feelings as mine, how would you recommend I justify that position to non-technology leadership?

## It’s Just So Tempting

Imagine you are in the shoes of the CEO. The person who pays for a developer’s time. It would be really nice to be able to measure, wouldn’t it? To know if that developer is doing good work, doing enough work, or just slacking off. If they’re slacking off, we’d fire them and hire someone who works better. And since we could measure it, we’d interview in a way that measures this efficiency. No more problems!

**But if developer productivity can be measured, how is there not a single standard of measuring this in the industry?** Try to measure any one dimension, and you’ll fail. Measuring lines of code is meaningless and leads to busywork. Number of tickets closed? People will get creative opening tickets, or optimize for the easy-to-fix ones. Number of commits per day? It will lead to small and frequent commits, but not more. Any single metric you give to people, it can – and will – be gamed.

## Teams Over Individuals

Even if we had this magic formula to measure individual productivity, it would all go to waste when looking at teams. Productive teams can move faster and produce more value than the individuals themselves. Instagram: 13 a team of 13 building a company [acquired for $1B](https://www.businessinsider.com/instagram-employees-and-investors-2012-4?international=true&r=US&IR=T). Whatsapp: a team of 50 engineers [serving 900M users](https://www.wired.com/2015/09/whatsapp-serves-900-million-users-50-engineers/).

Teams are an interesting thing. Put together three, high-performing developers, and with poor team dynamics and certain projects, that team might work worse than the three average ones combined. Do the same with three average performing developers, with the right dynamics and the right project, and they might do wonderfully well. Team dynamics play a large role in this, as does the team culture.

Teams are where engineering managers come into play. An engineering manager is often just as expensive to hire as a senior developer. In fact, they are often someone who used to be a senior developer. From a purely financial standpoint, it only makes sense to hire one, if adding this manager results in a positive return.

**Taking a team of 8 developers, and adding the one manager, that team should perform better than a team of 9 developers**. It makes little sense from math, but it actually works. [Google tried to prove that managers don’t matter](https://www.inc.com/scott-mautz/google-tried-to-prove-managers-dont-matter-instead-they-discovered-10-traits-of-very-best-ones.html). Instead, they discovered that they make a huge difference that warrants hiring them – assuming they have the right traits. The right traits meaning being a good coach, empowering teams, creating inclusing environments, being results oriented, being good communicators and [five others](https://www.inc.com/scott-mautz/google-tried-to-prove-managers-dont-matter-instead-they-discovered-10-traits-of-very-best-ones.html).

Once you have an engineering manager in place, they need to be accountable for the team’s performance. The team should perform better with an engineering manager, than without one. If there are performance issues, they should spot it. When someone is doing exceptionally well, they should also notice this and help [promote this person to the next level](https://blog.pragmaticengineer.com/software-engineering-promotions/).

## Why Do We Need To Measure?

We went on a tangent with teams, so let’s get back to the original question that management wants to know: how to measure individual developer productivity. But there’s an even more important question behind this ask.

***Why* does management feel they need to measure individual productivity? What problem would this solve?** What is the motivation here? What would happen with developers who score poorly according to the metrics measured? And why?

Digging deeper might bring up completely different strategies. Maybe the company is doing poorly financially, and they need to downsize some parts of engineering. Maybe the leadership team is unhappy with the delivery speed. Maybe they feel that engineering is a black box, and they want finer control. But in all the above cases, getting a metric to measure will not solve the underlying problem. So figure out what that problem is.

## Let’s Talk About Tech Organizational Culture

In the [book Accelerate](https://www.amazon.com/gp/product/1942788339/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=gregdoesit-20&creative=9325&linkCode=as2&creativeASIN=1942788339&linkId=66a3a5483fb43c2bc51ab76dd1cadc2b) by Nicole Forsgren, Jez Humble, and Gene Kim, the authors analyzed three distinct organizational cultures. Pathological (power/fear-oriented), bureaucratic (rule-oriented) and generative (performance-oriented). Here is a neat overview of the three of them:

![](https://blog.pragmaticengineer.com/content/images/size/w600/2020/06/IMG_3789.jpg)![](https://blog.pragmaticengineer.com/content/images/size/w600/2020/06/IMG_3789.jpg)

Westrum’s Typology of Organizational Culture, from the book [Accelerate](https://www.amazon.com/gp/product/1942788339/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=gregdoesit-20&creative=9325&linkCode=as2&creativeASIN=1942788339&linkId=66a3a5483fb43c2bc51ab76dd1cadc2b)

Why is organizational culture important? It’s because it can predict the performance of the organization:

*“We hypothesized that culture would predict both software delivery performance and organizational performance. We also predicted that it would lead to higher levels of satisfaction. Both of these hypotheses proved to be true.”*

**Performance-oriented cultures do better than rule-oriented or power-oriented ones,** according to the research cited in Accelerate. So if your organization wants to measure individual performance just to be able to put some more rules in place based on this, then we are likely talking about a bureaucratic organization. This type of organization will fare worse than a performance-oriented organization that is focused on overall outcomes.

## Things We Can Measure

As a hands-on engineering manager, there a *lot* of things that you can measure to observe on the team. These go from the number of commits, average commit size, time to review, number and frequency of code reviews, time to merge pull requests to the main branch, and so on. None of these metrics are helpful by themselves, but together, they can paint a picture, and draw attention to places that could be problematic. And all of them only make sense in the context of the team.

For example, is one of the developers taking 3x as long to merge their changes, and do they get 3x as many code review comments as others? If they are a new joiner, this is expected. But if they are a veteran on the team, maybe there’s something other going on there? Similarly, looking at these numbers can help identify top performers who are going over and beyond with code reviews, on top of their work. You can spot brewing conflicts by reading through pull requests with lots of back-and-forths.

**There’s a wealth of data to look at: but none of it is useful without context.** Tools like [Velocity](https://codeclimate.com/) and [Pluralisght Flow](https://www.pluralsight.com/product/flow) expose much of this data: but they will never be able to deliver the context. For example, you might see that the number of commits and code reviews has dramatically dropped from an engineer. But when digging in, it might turn out they were pairing with team members, speeding them up, mentoring them, and adding long-term value outside the sprint. You won’t be able to tell any of this until you look behind the curtain.

There are a lot more things we can measure, though, at the team level. Like the output of the team. What has the team shipped? What was the business impact? How was the quality: how much rework was needed afterward? And, of course, let’s not forget about the measurable things about the team. How is morale? What about attrition? How are people growing professionally: are they getting promoted?

## How do Top Tech Companies Do This?

We’ve explored what you can and cannot measure. So how to the likes of Google, Facebook, Stripe, Uber, Airbnb and other large or small, but innovative tech companies and startups measure software engineering performance?

**All tech companies [with good developer](https://blog.pragmaticengineer.com/the-developer-culture-test/) culture give performance feedback based on the competencies and levels they define for engineers.** These companies have a career progression, or competencies framework, that clearly define expectations for each level. Some of these progression frameworks can be browsed [on Progression.fyi](https://www.progression.fyi/).

Engineering managers give feedback on an ongoing basis, and have more formal reviews every 6-12 months. On these [performance review sessions](https://blog.pragmaticengineer.com/performance-reviews-for-software-engineers/), they’ll give clear feedback if the engineer is below, meeting, or above expectations.

So how does this tie to measuring performance? Anything you want to optimize for, should be part of these competencies expectations. Do you expect senior engineers to ship complex projects end to end: meaning planning, estimating, coding, rolling out and listening to customers? Add it in. What about a junior engineer – what is the expectation compared to a senior? Go through the exercise, and take inspiration from the [existing progression frameworks](https://www.progression.fyi/). Define what you want to set as a baseline – and thus, what you’ll be levelling against. If you set out to do this, I recommend reading the Dual Ladders chapter in the [Become an Effective Software Engineering Manager book](https://blog.pragmaticengineer.com/become-and-effective-software-engineering-manager-my-book-review/) by James Stanier.

Getting competencies right is time-consuming and hard. When doing so, the “core” of the tech team should be involved: people who have been around at the company for long enough to understand what should, and should not be encouraged. Once these competencies are crafted, you also need to keep them up to date. If this all sounds like a lot of work: it is. But this can set the focus on what engineers start optimizing for, so you want to get this right.

## Non-technical leadership: fight, convert or flight

When you’re an engineering leader who reports to someone non-technical, and you start being challenged on things like measuring people’s performance, you probably have a trust issue. The non-technical people don’t understand what is happening, and they want more information. Once they have more information, they’ll start making decisions if they don’t trust you. Once they start making the decisions – welcome to being micromanaged by a poorly qualified manager.

You need to resolve this trust issue before it consumes you. I’ve seen this happen with several of my peers, who were managers or senior managers in an organization that wanted to be a tech company but was missing tech leadership. They hired tech leaders, only to report to non-technical people, who failed to give trust upfront. *“Why do the developers come in late, when everyone on accounting starts at 9am on the dot?”* *“Why should we do a hackathon when it takes away time from product development?”* This and similar challenges were common.

**Good engineering teams need autonomy to operate well – as do their engineering leaders.** You either need to get this autonomy or accept that you won’t be in charge: the business will be. And know that in an environment that will be bureaucratic at best, and pathological at worst, you and your team will fail to live up to your true potential.

Fight or flight – and good luck with the good fight.

Note: see another [answer to the exact same question from Charity Majors](https://charity.wtf/2020/07/07/questionable-advice-can-engineering-productivity-be-measured/), cofounder of [Honeycomb](https://www.honeycomb.io/). And see the [piece from Martin Fowler](https://martinfowler.com/bliki/CannotMeasureProductivity.html) on (not) measuring developer productivity.

*This post is part of the [Ask the Engineering Manager series](https://blog.pragmaticengineer.com/ask-the-engineering-manager/). Have a question on career growth, as a developer? [Ask it here](https://blog.pragmaticengineer.com/ask-the-engineering-manager/).*