---
title: Reducing risks by taking risks
date: '2016-08-02T10:58:15+00:00'
format: link
service: instapaper
tags:
- read
external_url: http://techblog.outbrain.com/2016/07/reducing-risks-by-taking-risks/
---

[Reducing risks by taking risks](http://techblog.outbrain.com/2016/07/reducing-risks-by-taking-risks/)  



You have a hypothesis you wish to prove or refute regarding your behavior in an extreme scenario. For example: after restarting the DB, all services are fully functioning within X seconds. There are at least 3 approaches:

1. **Wait && See** — if you wait long enough this scenario will probably happen by itself in production.
2. **Deep Learning**  — put the DBA, OPS and service owner in a big room, and ask them to analyze what will happen to the services after restarting the DB. They will need to go over network configuration, analyze the connection pool and DB settings, and so on.
3. **Just Do It** — deliberately create this scenario within a controlled environment:

*Timing* — Bases on your knowledge pick the right quarter, month, week, day and hour – so the impact on the business will be minimal.

Monitoring — make sure you have all monitoring and alerts in place. If needed, do “manual monitoring”.

Scale — If applicable do it only on portion of your production: one data center, part of the service, your own laptop, etc.

[![](https://i0.wp.com/techblog.outbrain.com/wp-content/uploads/2016/07/Taking-a-Risk1.jpg?w=921)](https://i0.wp.com/techblog.outbrain.com/wp-content/uploads/2016/07/Taking-a-Risk1.jpg)

The **Wait && See** approach will give you the right answer, but at the wrong time. Knowing how your system behaves only **after** a catastrophe occurs is missing the point and could be expensive, recovery-wise. 

The **Deep Learning** approach seems to be the safer one, but it requires a lot of effort and resources. The answer will not be accurate as it is not an easy task to analyze and predict the behaviour of a complex system. So, in practice, you haven’t resolved your initial hypothesis.

The **Just Do It** approach is super effective – you will get an accurate answer in a very short time, and you’re able to manage the cost of recovery. That why we picked this strategy in order to resolve the hypothesis**.** A few tips if you’re going down this path:

* Internal and External Communication — because you set the date, you can send a heads up to all stakeholder and customers. We use statuspage.io for that.
* Collaboration — set a HipChat / Slack / Hangouts room so all relevant people will be on the same page. Post when the experiment starts, finishes, and ask service owners to update their status.
* Document the process and publish the results within your knowledge management system (wiki / whatever).
* This approach is applicable for organisation that practice proactive risk management, have a healthy culture of learning from mistakes, and maintain a blameless atmosphere.

People that pick **Deep Learning** are often doing so because it is considered a “safer”, more conservative approach, but that is only an illusion. There is high probability that in a real life DB restart event the system would behave differently from your analysis. This effect of surprise and its outcomes are exactly what we wanted to solve by predicting the system’s behaviour. 

The **Just Do It** approach actually reduces this risk and enables you to keep it manageable. It’s a good example of when the bold approach is safer than the conservative one. So don’t hesitate to take risks in order to reduce risk, and **Just Do It**

##### Photo credit: <http://www.jinxiboo.com/blog/tag/risks>