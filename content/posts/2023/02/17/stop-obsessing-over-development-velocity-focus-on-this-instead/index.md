---
title: Stop Obsessing Over Development Velocity, Focus on This Instead
date: '2023-02-17T11:03:22-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://itamargilad.com/velocity-vs-impact/
---

[Stop Obsessing Over Development Velocity, Focus on This Instead](https://itamargilad.com/velocity-vs-impact/)  



An awful lot of effort is going these days into boosting product teams’ productivity: getting them to burn those story points faster, deliver the planned scope in every sprint and cycle, and generally ship more stuff, faster. The term “development velocity” is often thrown around by executives, but what they’re actually aiming for is upping *launch throughput*—apparently a matter of vital importance for the success of the company.

I’m here to argue that development velocity (whatever that means) and launch throughput are entirely the wrong optimizations. Obsessing over these things will distract you from what’s really important and is likely to do more harm than good.

We’ll use a thought experiment to see why.

Imagine three product groups: A, B, and C. All three have the same “throughput”: they all launch on average 40 new product changes per year—new features, product enhancements,redesigns, pricing/marketing changes, etc (bug fixes and maintenance work are not counted as launches).

Here’s how the experiment will play out:

* Product group A is our control group—nothing about it changes throughout the experiment.
* Product group B is the “Throughput” group. It will optimize for launching more, faster.
* Product group C is the “Impact” group. It’s goal is to improve the ratio of launches that create a positive impact.

Before we continue, it’s worthwhile pausing to talk about group C’s mission.

## **Most of What We Build is a Waste**

It’ll probably not surprise you to hear that not everything we launch is a success, but it is quite alarming to see how bad we really are at creating value. Research of A/B experiments carried out independently by multiple companies suggests that, at best, [1 in 3](https://hbr.org/2017/09/the-surprising-power-of-online-experiments) ideas will have any measurable impact, and the industry average is likely [1](https://vwo.com/blog/cro-industry-insights/) in [7](https://conversionxl.com/ab-tests-fail/) (14%). Everything else either has no impact or creates negative impact (users engage less, customers buy less, etc). It’s hard to believe that what we’re building will have zero or negative results, but looking back at past projects shows that is indeed quite often the case. We can hazard a guess (unscientifically, as companies don’t collect or share this type of data) that that the distribution of impact-per-launch looks something like this:

![](https://lh5.googleusercontent.com/1oQoreqT85QsqXR7qKRoqN-xnifMdZDJYZfUowRVr-z5FPGiIVRTP2SlvV2tRyE2eSJILc8JssZwgqdcVLuoKMaeiVfoBTlX14QiD-HYUlEe9bOEfJLw3vAngTT7g-hVCJwDRQo7)![](https://lh5.googleusercontent.com/1oQoreqT85QsqXR7qKRoqN-xnifMdZDJYZfUowRVr-z5FPGiIVRTP2SlvV2tRyE2eSJILc8JssZwgqdcVLuoKMaeiVfoBTlX14QiD-HYUlEe9bOEfJLw3vAngTT7g-hVCJwDRQo7)

Given that, we need to add an important set of parameter in our experiment:

* All three groups start with the same (better than average) distribution of success: 25% of the ideas they launch create a positive impact, 55% have no impact and 20% create negative impact.
* Let’s also assume that on average, a positive launch creates an improvement of 0.5% in the company’s [top metric](https://itamargilad.com/the-three-true-north-metrics-that-your-product-and-business-need/) (say items sold, or messages sent) and the average negative change causes a drop of 0.5%.

There are obviously a lot of assumptions here, so at the end of the article I’ll show you what happens when we change these values.

Let’s start running the experiment and track the groups year-by-year.

## **Year 1**

Group A launches 40 product changes in year 1, out of which, 10 (25%) create some measurable positive impact, 22 (55%) do nothing, and 8 (20%) deliver an unexpected negative result.

As product group A launched 10 positive-impact changes this year, it created a nice improvement of 5% (10 x 0.5%) in the top metric. However it also launched 8 negative-impact changes, which detract 4%. So the overall contribution to the top metric product group created this year is a mere 1%.

**Product Group A (Control)**Product changes launched per year40Positive impact changes (25%)10No impact changes (55%)22Negative impact changes (20%)8Positive value contribution5.0%Negative value contribution-4.0%Total value contribution**1.0%**

This is our baseline performance. Let’s see if we can improve on it.

#### To receive posts like these by email

Group B has worked hard to up its launch rate. The company hired top-of-the-line consultants and coaches to teach the team and the managers ways to boost “velocity”, “utilization”, “accountability”, and other important-sounding terms. Let’s imagine this works, and the team indeed managed to boost its throughput by 20% (I don’t think this is a realistic scenario, but let’s assume). It ends year 1 with a whopping 48 product launches instead of 40. Success! The executive team is elated and the CTO gets a nice bonus.

How much did this massive boost in productivity help the business?

**Product Group B (Velocity)**Product changes launched48Positive impact changes12No impact changes26Negative impact changes10Positive value contribution6.0%Negative value contribution-4.8%Total value contribution**1.2%**

Out of the 48 launches, 12 created positive impact, which is two more than the control group. However as group B did nothing to improve its success rate, the number of no-impact launches grew from 22 to 26, and the negative-impact subset grew from 8 to 10 (the numbers are rounded, as there are no half-launches).

The total value contribution is therefore 12 \* 0.5% + 10 \* -0.5% = **1.2%**, which is a slight improvement over the to 1.0% of the control group, but in practical terms, it’s almost insignificant.

Group C has worked hard as well in year 1, but with the aim of improving its success ratio. It spent time researching and understanding customers and the market, it set clear, measurable goals, it evaluated multiple ideas per goal, and, perhaps most importantly, tested these ideas repeatedly and used what it learned to improve or discard ideas. If you’re familiar with lean startup, product discovery, design thinking or my own [GIST framework](https://itamargilad.com/gist-framework/), none of this is news to you.

In year 1 group C achieves this impact distribution: 40% positive-impact ideas launched, 50% no-impact ideas, and 10% negative-impact. This may seem like a too-good-to-be-true improvement, but in reality even a small amount of discovery work can make a big difference over none.

However the improvement comes at a cost. Because the group now spends more time researching and testing ideas, and is willing to dump half-built ideas that don’t pan out, the total launch throughput has dropped by 20% — from 40 launches per year to a mere 32 (this doesn’t have to be the case, but let’s say it is). Already, group C’s chances of winning the experiment are looking grim, but just for sport, let’s run the numbers.

**Product Group C (Impact)**RatioYear 1Product changes launched per year32Positive impact changes40%13No impact changes50%16Negative impact changes10%3Positive value contribution6.4%Negative value contribution-1.6%Total value contribution**4.8%**

While group C has reduced it’s launch throughput this year, it was able to launch more positive-impact ideas, and just as important, fewer no-impact and negative-impact ideas. As a consequence it generated a net positive impact of on the top metric of **4.8%**.

In other words, **group C that optimized for impact did** ***4 times better*** **than team B with its higher launch capacity, and 4.8 times better than the control group A.**

![](https://lh3.googleusercontent.com/f75kFiZ0089WTtGukjq17Dj5UpAP0aGUSb17dIlKLrpR67YnHkgeeeJTUVKz40JUcyoahgW9zvUw2pnkbyII072RNfXwlSPrisZeKK-U8z6hib4IMJE0vyOk2nYGu_uLpl-bQog9)![](https://lh3.googleusercontent.com/f75kFiZ0089WTtGukjq17Dj5UpAP0aGUSb17dIlKLrpR67YnHkgeeeJTUVKz40JUcyoahgW9zvUw2pnkbyII072RNfXwlSPrisZeKK-U8z6hib4IMJE0vyOk2nYGu_uLpl-bQog9)

This is a rather unintuitive result. Can a product group that has two-thirds of the output really create four times the impact? The answer is *absolutely yes*. Here’s what Jeff Patton has to say on on this topic:

> *“One of the common misconceptions in software development is that we’re trying to get more output faster. Because it would make sense that if there was too much to do, doing it faster would help, right? But if you get the game right, you will realize that your job is not to build more—it’s to build less. … At the end of the day, your job is to minimize output, and maximize outcome and impact.”* 
> 
> *Jeff Patton,* [*User Story Mapping*](https://www.jpattonassociates.com/read-this-first/)

If you come to grips with the reality that most of what we create is a waste, chasing output is actually creating more waste, faster. The much more important and often lower-hanging achievement is improving the ratio of positive-impact ideas that we launch. Doing this means consistently creating more value for our customers and our business.

But wait, there’s more.

Tired of launching the wrong things slowly? [Check out my workshops](https://itamargilad.com/workshops) to find concrete solution.

## Year 2

Let’s see how things shape up in year 2.

Team A is still our control group, so nothing changes. However some things do naturally change. The more we add things to our product, the more complicated and hard to maintain it becomes. We bloat the codebase, the interfaces, and the test matrices. There are new dependencies, more moving parts and novel ways to break the builds. We have more bugs to fix and customer requests to deal with. Bad or do-nothing features eventually have to be removed or improved on. All this means that our ability to develop product changes and launch them decreases over time. So team A who managed to cram in 40 product changes in year 1, is only able to launch 36 in year 2.

**Product Group A (Control)**Year 1Year 2Product changes launched per year4036Positive impact changes109No impact changes2220Negative impact changes87Positive value contribution5.0%4.5%Negative value contribution-4.0%-3.6%Total value contribution**1.0%****0.9%**

As you can see, everything goes down by 10% year-over-year, so the total value group A is creating is just a 0.9% improvement in the company’s top metric. If nothing changes you can expect this value to drop even further in the coming years.

Group B is facing the same challenge. In fact because it managed to launch so much more stuff on year 1, it’s being hit even harder on year 2. It keeps working on improving throughput, but the results are not as dramatic as in year 1— there’s only so much you can squeeze out of a development team. So in year 2 team B’s throughput goes down from 48 to 45 launches per year.

**Product Group B (Velocity)**Year 1Year 2Product changes launched per year4845Positive impact changes1211No impact changes2625Negative impact changes109Positive value contribution6.0%5.6%Negative value contribution-4.8%-4.5%Total value contribution**1.2%****1.1%**

The total value contribution goes down to 1.1% — better than the control group, but disappointing for a product group that has put two years of hard work into upping its game. If nothing changes team B will keep digging itself into a hole: high development costs, lots of waste, bloated products that are almost impossible to maintain, and low return on investment.

Group C is seeing an opposite change. During year 2 it has become even more proficient at testing ideas quickly and cheaply and its distribution of success goes up to: 55% positive impact, 40% no-impact, 5% negative impact. But there are a number of other interesting side effects as well. As the group is now working on short-ish build-measure-learn projects there’s less room for scope creep, procrastination and over-engineering. These shorter projects require fewer people to run, so more ideas get a chance to be tested and the team is utilized better. Often the group discovers it can launch a smaller-than-planned version of the idea and still deliver value to users and/or the business, which shortens time to launch. With all the evidence created, decision-making is quicker, managers are willing to delegate more, so less time is lost in debate.

All this leads to a significant increase in throutput. The team launches 39 product changes in year 2. These launches will definitely bloat the codebase, but as they are mostly of value that’s a price well worth paying.

**Product Group C (Impact)**Year 1Year 2Success RatioLaunchesSuccess ratioLaunchesTotal3239Positive impact changes40%1355%21No impact changes50%1640%16Negative impact changes10%35%2Positive value contribution6.4%10.7%Negative value contribution-1.6%-1.0%Total value contribution4.8%9.8%

The results at year 2 are even more striking: **the high-impact group did 10x better than an average product group and 9x better than a high-throughput product group.** 

![](https://lh5.googleusercontent.com/C7Gtl0JIK8w9KZvLLEWJvHl2WG2XT-U7LIh_W3i84T3rDQTz6DifuFB_hT7QBSb6SpSXWXgm8T3nJWLffCtTmD2QNP74irHT1Sbd4BP6oTP2Hel5L4nFcmoANhIkH-gdhwdz80XW)![](https://lh5.googleusercontent.com/C7Gtl0JIK8w9KZvLLEWJvHl2WG2XT-U7LIh_W3i84T3rDQTz6DifuFB_hT7QBSb6SpSXWXgm8T3nJWLffCtTmD2QNP74irHT1Sbd4BP6oTP2Hel5L4nFcmoANhIkH-gdhwdz80XW)

We can see why some companies seem to be so much better at creating successful products, while others seem to tread water. Focusing on outcomes and impact pays big dividends.

# **Experiment Variants**

You may argue that I chose parameters that are favorable to my preferred methods of doing stuff. I’m biased, it’s true, but only because I worked in group A and B for so many years. Let’s try a few variants and see how they affect the results.

## Better Impact Distribution

Let’s say that all three groups are already doing some testing of their ideas and the base distribution of launch impact is:

Positive impact33%No impact55%Negative impact12%

Here’s what happens now:

![](https://lh5.googleusercontent.com/r95urEm1FJMfpFFn4I_bExq39Bkr3C3chqyo_YCvSHDw5vqP9dWrlTarQRW-FCr4uD2kNxdxaJRig1YQProxNsUyPsZKaOKO9ulGXh36yGzhFeY1LCeYN8wapCnViffacalUQZj4)![](https://lh5.googleusercontent.com/r95urEm1FJMfpFFn4I_bExq39Bkr3C3chqyo_YCvSHDw5vqP9dWrlTarQRW-FCr4uD2kNxdxaJRig1YQProxNsUyPsZKaOKO9ulGXh36yGzhFeY1LCeYN8wapCnViffacalUQZj4)

Even a little injection of lean/discovery makes all groups better. In year 1 the differences compared to group C are not as pronounced — all groups make good contributions. However group C is still the one creating the biggest boost in impact with the least amount of output. In year 2 group C pulls away from the other groups due to it’s bigger focus on impact.

## Positive Launches Count More

What if we assume that the average positive-impact launch contributes more than the average negative-impact launch detracts?

Average contribution of product change to top metricPositive impact0.8%No impact0Negative impact-0.3%

Here are the results:

![](https://lh4.googleusercontent.com/uvNQFpvtVfjqAIFteZQSxOODbuYPRor37PnKBYyv1wsvHbPoPNJuJqYsuLu1N4Wtx87KJnv2ZPMTcSeKvWgE6m-tMf8ka7iHIsq16Er5a9x3inEsDSCR-MjYiAWyskxK66ur9I8x)![](https://lh4.googleusercontent.com/uvNQFpvtVfjqAIFteZQSxOODbuYPRor37PnKBYyv1wsvHbPoPNJuJqYsuLu1N4Wtx87KJnv2ZPMTcSeKvWgE6m-tMf8ka7iHIsq16Er5a9x3inEsDSCR-MjYiAWyskxK66ur9I8x)

This change makes all teams perform better, but again team C with its better success ratio is doing best, and is absolutely killing it on year 2. Having said that an average impact of 0.8% is pretty optimistic.

Note: if you want to see the spreadsheet I used to run this experiment, and maybe run it with your own numbers, go ahead and grab your [free copy here](https://docs.google.com/spreadsheets/d/188dWZ9hIiPdu4rvQzjULsUQ2MVIljZBG7fhz743hk_A/copy). (you’ll need to first sign into a Google account, then just click Make a Copy).

## **Conclusion: Leave Production-Line Thinking Behind**

To the best of my knowledge, executives at companies like Google, Netflix or Airbnb never talk about upping velocity or boosting launch throughput. There are several reasons for this. First, most of these executives have developed products themselves. They know there’s no magic dust you can sprinkle over the developers that will make them more prolific. Performance issues exist, and sometimes fixing them *is* the top priority, but they usually stem from the complexities and constraints of the organization and the product. Fixing those is important, but slow and ongoing. It’s only the uniformed manager that sees his mission as extracting maximum performance from the product team and believes in magical solutions.

The second reason that good managers don’t obsess over throughput, is that they build teams that take care of it on their own. The people doing the work are in the best position to detect when they’re too slow and to come up with solutions.

Finally, smart leaders realize that the key is not in doing a lot, fast, but in doing the right things, and that’s where they spend most of their energy—helping the organization make good product and business decisions.

Photo credit: [Doenertier82](https://commons.wikimedia.org/wiki/File:Phodopus_sungorus_-_Hamsterkraftwerk.jpg)

**To receive articles like this, as well and tools and templates, in your inbox, [sign up to my newsletter](https://itamargilad.com/newsletter)**.

Share with a friend or colleague