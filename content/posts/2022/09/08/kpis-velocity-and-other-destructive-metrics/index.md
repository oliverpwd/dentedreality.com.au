---
title: KPIs, Velocity, and Other Destructive Metrics
date: '2022-09-08T14:31:46-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://holub.com/kpis-velocity-and-other-destructive-metrics/
---

[KPIs, Velocity, and Other Destructive Metrics](https://holub.com/kpis-velocity-and-other-destructive-metrics/)  



[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fholub.com%2Fkpis-velocity-and-other-destructive-metrics%2F)
[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fholub.com%2Fkpis-velocity-and-other-destructive-metrics%2F)
[Email](mailto:?subject=KPIs%2C%20Velocity%2C%20and%20Other%20Destructive%20Metrics&body=%26quot%3BIt%20is%20wrong%20to%20suppose%20that%20if%20you%20can%E2%80%99t%20measure%20it%2C%20you%20can%E2%80%99t%20manage%20it%26mdash%3Ba%20costly%20myth.%26quot%3B%20%26ndash%3BW.%20Edwards%20Deming%20The%20Deming%20quote%20at%20the%20top%20of%20this%20post%20is%20often%20twisted%20into%20something%20worthy%20of%20Frederick%20Taylor%3A%20%26quot%3Bif%20you%20can%26%2339%3Bt%20measure%20it%2C%20you%20can%26%2339%3Bt%20manage%20it.%26quot%3B%20Deming%20would%20disagree.%20You%20can%26mdash%3Bin%20fact%2C%20must%26mdash%3Bmanage%20things%20you%20can%26%2339%3Bt%20measure%2C%20because%20in%20software%2C%20there%20are%20virtually%20no%20measurements%20that%20have%20any%20value.%20Wasting%20time%20collecting%20measurements%20that%20don%26%2339%3Bt%20lead%20to%20improvement%20is%20not%20only%20costly%2C%20it%26%2339%3Bs%20actively%20destructive.%20KPI%20%28Key%20Performance%20Indicator%29%20metrics%20and%20Agile%20just%20don%26%2339%3Bt%20mix.%20They%20are%20the%20software%0D%0A%0D%0ARead%20More%20Here:%20%20https%3A%2F%2Fholub.com%2Fkpis-velocity-and-other-destructive-metrics%2F)
### “It is wrong to suppose that if you can’t measure it, you can’t manage it—a costly myth.”

The Deming quote at the top of this post is often twisted into something worthy of [Frederick Taylor](https://en.wikipedia.org/wiki/Scientific_management): “if you can’t measure it, you can’t manage it.” Deming would disagree. You can—in fact, must—manage things you can’t measure, because in software, there are virtually no measurements that have any value. Wasting time collecting measurements that don’t lead to improvement is not only costly, it’s actively destructive.

KPI (Key Performance Indicator) metrics and Agile just don’t mix. They are the software version of Taylorism. One of my LinkedIn compatriots (Steve Gordon) said it pretty well: “The only reason for KPIs is if you do not trust your developers to deliver working software to the best of their ability and continuously learn to do it better.” Trust and respect are central to agility.

KPI thinking, though, is central to the way many shops work, even so-called *Agile* ones. They take the so-called *Chrysler* management model as their guide. Chrysler collected lots of data into a central place, chewed on it, then spit out directives forcing production changes that they hoped would improve the data. By the time this process went full circle, however, the actual reality on the factory floor had changed. Since the management decisions were based on obsolete data, the resulting changes ranged from ineffective to destructive. The data crunching and the real world of the production floor were far separated, both physically and in time.

Focus on continuous process improvement, and productivity takes care of itself.

Toyota, from which Lean thinking emerged, had a different idea: Focus on continuous process improvement, and productivity takes care of itself. The people doing the work are responsible for the improvements. If anybody measures anything, it’s the actual workers, who act on those measurements immediately. Like all agile thinking, short feedback loops and immediate change made for effectivity. Toyota believes that the most important factor in productivity is a pervasive continuous-improvement culture, and I agree strongly. (For more on that, check out Mike Rother’s [Toyota Kata](http://amzn.to/2BBWX8d)).

So, are metrics never useful? Of course not, provided that the metrics are based on real things and are actionable. Whether you can use them to measure “performance” is another matter. Even defining “performance” in a software context is difficult to impossible. We recognize it when we see it, but we can’t really measure it.

For example, *velocity* (average points per sprint) is not a *performance* metric. If anything at all, it’s a measure of output that tells you nothing about the value of whatever you’re producing, and it’s not even a good measure of output. For one thing, the basic unit (a point) is not a measurable quantity. It’s a judgment. You can’t derive a quantitative measure from qualitative input.

More importantly, velocity is a gauge, not a control (to quote my friend Tim Ottinger). You observe the amount of work you actually complete in a sprint. The average of that number is your velocity. It changes all the time. If the work you complete is always below your velocity, that tells me that you’re making up a number rather than using observations.

Individual velocity as a KPI is particularly abhorrent. (The fact that Jira provides this metric is a good reason to get rid of Jira. It’s just pandering to dysfunction and promoting micro-mismanagement.) You estimate a story at 2 points based on incomplete information—and all estimates in the Agile world are based on incomplete information. You discover something as you’re programming, and as a result spend all week working on that story. You do a spectacular job. You are nonetheless reprimanded by a Jira-obsessed manager because your velocity is so low. That’s just abuse, plain and simple.

Then there’s the Goldratt factor. Elihu Goldratt said: “Tell me how you measure me, and I will tell you how I will behave.” Given that a point is an arbitrary number, I can make my velocity whatever I want. You need to see 200 points/sprint for me to get that bonus. Sure! Whatever you want! I can push out vast quantites of low value easy stories that nobody wants if that’s what I need to do to get that bounus!

Similarly, meeting your estimates tells me nothing except that you can create estimates that you can meet. I’ll happily multiply my guesses by 100 if that’s what it takes! Using velocity as a KPI really says: “we don’t care how good your work is or how valuable you are to the company—all that matters is how well you can estimate.”

As I said, destructive.

Velocity is equally useless as a KPI at the team level. First, every team has a different notion of what a “point” is. Comparing velocity between teams is like saying that basketball teams are “more productive” than baseball teams because they rack up more points during the game. Velocity is also a moving target. It’s something that you measure so that you can guess what you can accomplish in the next sprint (and it’s not even a particularly good metric for that). It’s an average: the number is adjusted after every sprint. And there’s nothing actionable about velocity—it tells you nothing about *how* to improve.

Another problem with velocity as a KPI (or any KPI applied to a team as compared to the entire organization) is that it gets you focused on *local optimization*. It’s the speed of the entire organization that matters—the time it takes for an idea that’s a gleam in somebody’s eye to get into your customer’s hands. An individual team’s pace within that system is usually irrelevant. Imagine three hikers walking along a narrow trail. If the people at the two ends are walking at a fixed pace, it doesn’t matter how fast the guy in the middle goes. Eventually, he’ll catch up with the guy in front. What matters, however, is the speed at which the *last* hiker is walking. The product doesn’t ship until he arrives. As long as the work is inside the production system, it’s a liability—it costs you money and doesn’t make a profit. Working on too many things is just wasting money, in the same way that our middle hiker bouncing around in the space available to him is wasting energy. It’s better to work/walk at the *right* pace. Measuring the velocity of a single team is like measuring the speed of that middle hiker. It doesn’t tell you anything useful. (The hiker analogy comes from Eliyahu Goldratt’s [*The Goal*](http://amzn.to/2DKcbd2), by the way. If you haven’t, read it.)

Even if local optimization did work, you typically cannot “improve” velocity locally because many of the impediments are institutional. Pushing a team to improve when the means to do that is out of their control is another form of abuse. And even if your team does improve its processes dramatically, the velocity will remain unchanged because the definition of a “point” will necessarily shift. You can do more in one point than you used to, but it’s still one point.

Here are some examples of other worthless metrics that are often treated as KPIs. A real KPI measures outcomes. None of these do. (Feel free to add more in the comments):

* **anything that compares what you deliver against an up-front specification**. Specifications change. They change because both we and our customers learn based on what we deliver. We *never* deliver what we think we will up front.
* **anything to do with tasks**. We don’t plan tasks. We plan stories and the developers figure out the tasks. The list of tasks changes as you work.
* **anything to do with milestones**. You can’t set milestones without that soon-to-be obsolete up-front plan.
* **anything to do with commitments**. The notion of a “Sprint commitment” was removed from the [Scrum Guide](http://scrumguides.org) years ago because it was so destructive. The ratio of the number of stories you thought you’d deliver to the number you actually delivered is just measuring how much you learned during development. The things you learned rendered your estimates incorrect. So what? The more discrepency the better! Agile organizations are learning organizations.
* **anything to do with estimates**. Metrics focused on estimates do nothing but measure your ability to estimate (or fudge an estimate). They don’t measure work.
* **variation from a schedule**. Again, long term schedules require up-front plans. We do not do fixed-scope work, in a specific time, set by up-front guesswork, formed from an inaccurate plan.
* **defect density**. If this number is > 0, you’re in deep trouble. There should be nothing to measure. Do [TDD](https://en.wikipedia.org/wiki/Test-driven_development).
* **the amount of code or number of features** (including function-point analysis). We deliver value, not features. We want to write the least code possible (with the fewest features) that provides the most value. Feature counts are irrelevant if we haven’t delivered value. If we could measure it, one of the best metrics would be the amount of code we *didn’t* write.
* **ROI**. It’s too fuzzy a number, often based on wishful thinking.

Collecting a metric that doesn’t show you how to improve is waste.

![](https://holub.com/wp/wp-content/uploads/2021/12/Screen-Shot-2021-12-05-at-3.18.39-PM.png)![](https://holub.com/wp/wp-content/uploads/2021/12/Screen-Shot-2021-12-05-at-3.18.39-PM.png)

So, what internal performance-related things might be worth measuring? (None of these are KPIs, either, but please add any real agile KPIs—measured outcomes in an Agile organization that track actual performance—to the comments if you know of any):

* **the number of improvements you’ve made to your process over time.** Make this into a game that encourages everybody to improve continuously. Every time you make an improvement, tack a descriptive sticky note to the wall. Everybody uses a different color, and whoever has the most notes wins!
* **the number of tests you write before you code**
* **the number of experiments you’ve performed**
* **the number of process and institutional changes instigated by those experiments**
* **the number of things you’ve learned in the past month**
* **the number of validated business-level hypotheses you’ve developed**
* **the number of times a week you talk to an actual customer**
* **the number of changes to your backlog** (if it’s not changing, why not?)
* **the ratio of implemented to non-implemented customer-driven changes requested mid-iteration** (Why are you not changing the plan when the need arises?)
* **the time that elapses between learning that you need some training and actually getting it.** This metric applies to any physical resource as well, of course. Training seems particularly indicative of problems, however, because it’s discounted by people who don’t “get” agile.
* **the stability of your teams**
* **the employee turnover rate**
* **team hapiness/satisfaction levels** I’m reluctant to add this one because I don’t know how to measure it directly. Turnover rate is related, of course, but we’d like to catch problems before people start quitting. I don’t believe in the accuracy of surveys. Maybe you can add some ideas to the comments.

Look at the quality of your continuous-improvement culture, not at time. In the earlier hiker analogy, the only way to become more productive is for *everybody* to move faster. The only way to do that is to have a continuous-improvement culture that infuses the *entire* organization. Focus on improvement, and productivity takes care of itself.

In addition to organization-level metrics, Lean metrics like throughput, cycle time, etc., can be worthwhile to the teams because they can identify areas for improvement. I’m a [#NoEstimates](https://holub.com/videos/#noestimates) guy, so I keep a rolling average of the number of stories completed per week so that I can make business projections.

The most useful production metric is the rate at which you get *valuable* software into your customer’s hands. That’s central to Agile thinking: “Working software is the primary measure of progress.” You could simplify that notion to the number of stories you deliver to your customer every week. If you don’t deliver, you’ve accomplished nothing. Also note that word, *valuable*. The rate of delivery is meaningless if the software isn’t valuable to the users.

And that notion brings us to the final and only performance metric that really matters: customer satisfaction, the only true indicator of value. That’s a notoriously hard thing to measure, but there are indirect indicators. The easiest one is *profit*. If people are buying your product, then you’ve built something worthwhile. There are dicy metrics, too. NPS ([Net Promoter Score](https://en.wikipedia.org/wiki/Net_Promoter))—would you recommend our product to your friends—falls into that category. No, I will not recommend your production monitoring system to my friends—the subject just doesn’t come up in normal conversation. Of course, you could (gasp) actually talk to your customers. Host a convention. Sponsor user groups and go to the meetings. Embed yourself in a corporate client for a few days.

A organization that’s focusing on KPIs typically does none of this, and in fact, the whole notion of a KPI flies in the face of agile thinking. It’s management’s job to facilitate the work. The teams decide how the work is done, and how to improve it. You don’t need KPIs for that, and I believe Deming would say that their absence doesn’t matter because the teams can effectively manage the work without them.

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fholub.com%2Fkpis-velocity-and-other-destructive-metrics%2F)
[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fholub.com%2Fkpis-velocity-and-other-destructive-metrics%2F)
[Email](mailto:?subject=KPIs%2C%20Velocity%2C%20and%20Other%20Destructive%20Metrics&body=%26quot%3BIt%20is%20wrong%20to%20suppose%20that%20if%20you%20can%E2%80%99t%20measure%20it%2C%20you%20can%E2%80%99t%20manage%20it%26mdash%3Ba%20costly%20myth.%26quot%3B%20%26ndash%3BW.%20Edwards%20Deming%20The%20Deming%20quote%20at%20the%20top%20of%20this%20post%20is%20often%20twisted%20into%20something%20worthy%20of%20Frederick%20Taylor%3A%20%26quot%3Bif%20you%20can%26%2339%3Bt%20measure%20it%2C%20you%20can%26%2339%3Bt%20manage%20it.%26quot%3B%20Deming%20would%20disagree.%20You%20can%26mdash%3Bin%20fact%2C%20must%26mdash%3Bmanage%20things%20you%20can%26%2339%3Bt%20measure%2C%20because%20in%20software%2C%20there%20are%20virtually%20no%20measurements%20that%20have%20any%20value.%20Wasting%20time%20collecting%20measurements%20that%20don%26%2339%3Bt%20lead%20to%20improvement%20is%20not%20only%20costly%2C%20it%26%2339%3Bs%20actively%20destructive.%20KPI%20%28Key%20Performance%20Indicator%29%20metrics%20and%20Agile%20just%20don%26%2339%3Bt%20mix.%20They%20are%20the%20software%0D%0A%0D%0ARead%20More%20Here:%20%20https%3A%2F%2Fholub.com%2Fkpis-velocity-and-other-destructive-metrics%2F)