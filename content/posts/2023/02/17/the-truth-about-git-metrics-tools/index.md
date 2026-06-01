---
title: The Truth About Git Metrics Tools
date: '2023-02-17T21:25:00-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://abinoda.com/git-metrics
---

[The Truth About Git Metrics Tools](https://abinoda.com/git-metrics)  



The Truth About Git Metrics Tools
January 24, 2023

There’ve recently been a couple of interesting Twitter discussions about engineering metrics tools, namely whether [people actually use them](https://twitter.com/ericabrescia/status/1619045553710698503) and the [questionable metrics](https://twitter.com/GergelyOrosz/status/1535290809288892418/) that they expose.

There are at least a couple dozen different vendors out there that currently provide this type of a solution. These products primarily provide analytics on top of tools like GitHub and Jira, and some support additional data sources.

I have a unique perspective on these solutions because the company I formerly started, [Pull Panda](https://github.blog/2019-06-17-github-acquires-pull-panda/), provided customers with similar metrics features like pull request throughput and turnaround time. After getting acquired by GitHub, I spent a year continuing to work in this space because GitHub had interest in launching a similar product.

My experience working on Pull Panda was that pull request metrics provided value in creating awareness around inefficient code review processes. But there were no real benefits beyond that. I was dismayed to find leaders frequently using the metrics for inappropriate purposes like performance reviews, or requesting we add metrics like lines of code to the product which [I knew were harmful](https://abinoda.com/flawed-five-metrics).

After getting acquired, I kept an open mind because I thought that my new colleagues at GitHub like Dr. Nicole Forsgren might have good ideas for how to leverage Git data to produce useful metrics. We built an initial product and piloted it, but shut it down after we found that teams didn’t get much true value from it. Our product vision for “data-driven engineering” made for compelling sales pitches, but it turned out there wasn’t real value to back it up.

Today, the sheer number of vendors out there pushing these types of products has made these metrics look like valuable tools even though they’re not. Many of these vendors make bold marketing claims of helping organizations 10x developer productivity, with pricing as high as $400 per year per developer.

I’ve personally yet to come across an example of real benefit gained from these metrics other than shining a light on inefficient code review processes, which is a problem that’s easily solveable without dashboards. Moreover, these tools encourage managers to walk down bad paths such as micro-managing or stack-ranking their developers.

Finding ways to measure and improve software organizations is a [complex problem](https://abinoda.com/three-bucket-framework) to which Git metrics are not the solution. Thankfully, we seem to be on the tail end of the hype cycle with these types of tools, as most leaders I speak to nowadays seem to recognize that they’re of little value. If you’re a leader looking for insights on how to improve developer productivity, steer clear of these types of solutions and instead focus on [developer experience](https://getdx.com).