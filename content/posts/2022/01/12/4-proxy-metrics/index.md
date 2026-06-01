---
title: '#4 Proxy Metrics'
date: '2022-01-12T16:53:44-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://gibsonbiddle.medium.com/4-proxy-metrics-a82dd30ca810
---

[#4 Proxy Metrics](https://gibsonbiddle.medium.com/4-proxy-metrics-a82dd30ca810)  



## How to define a metric to prove or disprove your hypotheses and measure progress

[![](https://miro.medium.com/fit/c/56/56/2*qI0tii-lp4ULwF_Xs56FNw.jpeg)![](https://miro.medium.com/fit/c/56/56/2*qI0tii-lp4ULwF_Xs56FNw.jpeg)](https://gibsonbiddle.medium.com/?source=post_page-----a82dd30ca810-----------------------------------)
[Gibson Biddle](https://gibsonbiddle.medium.com/?source=post_page-----a82dd30ca810-----------------------------------)

Jul 11, 2019·6 min read





At Netflix, the metric we used to evaluate overall product quality was monthly retention. This high-level product engagement metric improved significantly over twenty years. In the early days, about 10% of members canceled each month. In 2005 the monthly cancel rate was around 4.5%. Today, it’s close to 2%.

Using retention as a metric for all projects isn’t feasible, however. It’s a hard metric to move, and proving a retention improvement requires large-scale A/B tests. Lower-level metrics — proxy metrics — are easier and faster to move than a high-level engagement metric. Ideally, moving a proxy will improve the high-level metric (e.g., retention for Netflix), demonstrating a correlation between the two. Later, you can prove causation via an A/B test.

![](https://miro.medium.com/max/60/1*PfzQa7wY_3PjQAaXebAuLg.png?q=20)![](https://miro.medium.com/max/60/1*PfzQa7wY_3PjQAaXebAuLg.png?q=20)

![](https://miro.medium.com/max/1656/1*PfzQa7wY_3PjQAaXebAuLg.png)![](https://miro.medium.com/max/1656/1*PfzQa7wY_3PjQAaXebAuLg.png)




Today’s “Movie Display Page” is very simple. Start playing, or add “Badlands” to your list. It’s all about the movie or TV show — the interface doesn’t stand in the way of the film.

# How do you measure “simple?”

One of our hypotheses was that a simpler member experience would improve retention. But how do you measure “simple?” And how to do you demonstrate that it improves retention?

We began by exploring customer service data. Why do members call or email Netflix with questions or complaints? What links do they click on when they visit the help pages? Where do customers get confused? Over time, we focused our efforts on new members as a large number of potential customers at the top of the sign-up funnel provided a substantial business opportunity.

We talked to new members in one-on-one sessions and focus groups. We asked a small group of customers to write a journal describing their weekly activity with Netflix. Last, we looked at existing data for the new member sign-up flow, as well as their first few weeks with the service.

One point of confusion among new members: our early DVD-by-mail service required customers to create an ordered list of movies that we would send to them. But some new members failed to add any videos to their Netflix “Queue.” Some new members chose a plan, entered their credit card information, then asked, “Now what?” The notion of adding at least three titles to their Queue confused many new members.

It was clear we needed to simplify the sign-up process and make it easier for customers to create a list of movies. Eventually, we executed a series of “day one” projects focused on eliminating steps, reducing cognitive overhead, and providing clarity about how the service worked.

The proxy metric we devised was “the percentage of new members who add at least three titles to their queue during their first session.” When we first looked at the data, 70% of new members added at least three titles to their queue during their first session. By the end of the year, after a series of fast-paced experiments, we increased this percentage to 90%.

Over the same period, we drove month one retention from 88% to 90% — both retention and our “simple” metric moved together. We chose not to take the time, however, to execute a large-scale A/B test because we were confident that the more straightforward experience improved retention.

# The right proxy metric

Proxy metrics are a stand-in for your high-level engagement metric — the metric that defines your product’s overall quality. First, you seek a correlation between your high-level metric and the proxy metric. Later you work to prove causation.

Here’s a simple model to define proxy metrics:

* Percentage of (members/new customers/returning customers) who do at least (the minimum threshold for user action) by (X period in time).

Some examples of proxies for retention at Netflix:

* Percent of members who add at least one member to their “Friends” list within six months. The Netflix Friends feature launched with one percent of members using the feature, grew to 5% over three years, then Netflix killed the feature. The assumption was that the Friends proxy metric needed to surpass twenty percent to achieve a meaningful retention improvement.
* Percent of members who stream at least 15 minutes of video in a month. At the launch of streaming in 2007, this metric was 5%. Today, it’s north of 90%. We chose fifteen minutes because this was the smallest increment of value — the shortest TV episode was fifteen minutes. ( I’m sure Netflix measures a similar proxy today but at a variety of much higher “hurdles” — likely the percent of members who watch at least 10/20/30/40 hours a month.)
* Percent of members who add at least six DVDs to their queue in a month. The merchandising team’s job was to make it easy for members to find and add movies to their list. Initially, the metric was 70%. Over time, we moved it to 90%.
* Percent of new members who rate at least 50 movies in their first six weeks with the service. This metric was our proxy for our personalization efforts. The theory was that if customers were willing to rate movies, they valued the movie recommendations Netflix provided. We drove this metric from the low single digits into the high twenties over a few years.
* Percent of first choice DVDs delivered to members the next day in the mail. One of the early insights about our DVD-by-mail service was that delivering the first choice DVD the next day was critical. At first measurement, the metric was seventy percent. We drove this metric to ninety percent by standing up fifty automated DVD delivery hubs throughout the US. We also integrated the inventory data from each delivery hub with the merchandising system. We only merchandised titles that were available in a member’s local shipping center.

As you evaluate potential metrics, make sure the proxy:

* **Is measurable.** You can find, collect, and measure the data. Ideally, you can assess the metric in an A/B test, and the metric helps answer the question, “should we launch this feature, or not?” In evaluating a new product strategy, ask yourself, “In an A/B test, what metric would we use to make a go/no-go decision?”
* **Is moveable.** You can affect the metric through changes to the product experience.
* **Is not an average.** The danger of averages is you may move the metric by inspiring a small subset of customers to do a lot more of something. But this may not affect enough members to improve the overall product experience.
* **Correlates to your high-level engagement metric.** For Netflix, successful proxy metrics and retention moved together. Long-term, you hope to prove causation via a large-scale A/B test.
* **Specifies new v. existing customers.** As Netflix grew, we learned to focus our effort on new members. We believed that to become a sizeable worldwide service, we needed to optimize for new members. We would test features with new members, then roll out to all members based on positive results. Existing members sometimes noticed the change, complained about it, but rarely canceled. (Occasionally, if we believed there was a real risk of hurting retention, we ran an A/B test with existing members, too.)
* **Is not gameable.** One product manager focused on customer service. His job was to make it easy for members to help themselves so they did not call our customer service team via our 800 number. The metric that defined his role was “contacts per 1,000 customers,” and the goal was to lower this metric below 20 contacts per 1,000 customers. But the product manager quickly discovered he could game the metric by hiding the 800 number. Consequently, we revised the proxy: “Contacts/1,000 members with the 800 number available within two clicks.”

A big surprise at Netflix: we made decisions quickly, but isolating the right proxy metric sometimes took six months. It took time to capture the data, to discover if we could move the metric, and to see if there was causation between the proxy and retention. Given a trade-off of speed, and finding the right metric, we focused on the latter. It’s costly to have a team focused on the wrong metric.

Eventually, each of the product managers on my team could measure their performance through one or two proxy metrics that contributed to improving monthly retention.

# Product Strategy Exercise (#6)

Identify your high-level engagement metric — the equivalent of Netflix’s monthly retention. Now re-look at your work from the last essay (The Strategy/Metric/Tactic Lockup) and re-evaluate your proxy metric for each high-level strategy against “The Right Proxy Metric” outline above.

This next essay outlines an alternative approach to defining your product strategy:

[Essay #5: Working Top-down and Bottom-up](https://medium.com/@gibsonbiddle/5-working-top-down-bottom-up-426447b2b876)

Enjoy!

Gib

Gibson Biddle

[www.gibsonbiddle.com](http://www.gibsonbiddle.com)

PS. Here’s an index of all the articles in this series: