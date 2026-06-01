---
title: Measuring output, outcomes and impact in platform teams at Adevinta
date: '2022-01-13T11:25:47-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/adevinta-tech-blog/measuring-output-outcomes-and-impact-in-platform-teams-at-adevinta-6ccf8a148547
---

[Measuring output, outcomes and impact in platform teams at Adevinta](https://medium.com/adevinta-tech-blog/measuring-output-outcomes-and-impact-in-platform-teams-at-adevinta-6ccf8a148547)  



## What we learned from implementing a metrics-based approach to measure results in a platform team

[![](https://miro.medium.com/fit/c/96/96/1*is7oPyJb2RK5oMcxDjNcSw.jpeg)![](https://miro.medium.com/fit/c/96/96/1*is7oPyJb2RK5oMcxDjNcSw.jpeg)](https://medium.com/@adevinta?source=post_page-----6ccf8a148547-----------------------------------)
[Adevinta](https://medium.com/@adevinta?source=post_page-----6ccf8a148547-----------------------------------)
[May 20, 2021](https://medium.com/adevinta-tech-blog/measuring-output-outcomes-and-impact-in-platform-teams-at-adevinta-6ccf8a148547?source=post_page-----6ccf8a148547-----------------------------------) · 8 min read



**By** [**Xavier Gumara Rigol**](mailto:xavier.gumara@adevinta.com) **(**[**Medium**](https://medium.com/@xgumara)**,** [**Twitter**](https://twitter.com/xgumara)**,** [**LinkedIn**](https://www.linkedin.com/in/xgumara/)**), Senior Engineering Manager for Experimentation and Analytics Solutions at Adevinta**

![]()



As a manager of an internal platform team at [**Adevinta**](https://www.adevinta.com/) (that is, a team whose customers are other employees at the company) it has been hard to deliver results in our team by following a metrics-driven approach. This has been accentuated by the fact that our platforms can be used by employees from our marketplaces around the world.

In recent quarters though, **we have taken action and changed our approach to** [**measure the outcomes**](https://blog.crisp.se/2019/10/16/christopheachouiantz/output-vs-outcome-vs-impact) **of our activities rather than the outputs.** As a result, we have clearer goals, more engaged team members and the ability to visualise the impact we are making in the organisation.

In this article we explain a specific example of outcomes, outputs and impact for our Analytics Solutions team (an internal platform team) and detail the steps we followed to move from measuring progress using outputs to measuring progress using outcomes.

![]()


*Continue reading a data story with a successful ending*

# Framing the problem

Our Analytics Solutions team is responsible for a product that allows Data folks (such as Engineers, Analysts and Scientists) to use SQL (Analysts *lingua franca*) on top of big data datasets (datasets with billions of rows that don’t fit in “traditional” data storages).

We know our Analysts prefer running SQL queries on top of big data datasets rather than having to spawn a notebook to inform their decision making, which is why we’ve always delivered the capability of adding SQL metadata on top of every single S3 dataset.

Although we won’t be going into the technical details in this article, you can [read](https://medium.com/albert-franzi/accessing-s3-data-through-sql-with-presto-ddb6d4fbb99c) about or [watch](https://www.datacouncil.ai/talks/iker-martinez-easy-access-to-data-with-presto) a video of when we presented the solution back in 2018. As an update, we are no longer using Presto but AWS Athena.

The problem was that for teams that manage datasets with Personal Identifiable Information (PII), i.e. our central Messaging component, accessing the data via SQL was not possible.

If a dataset contains PII, the size of the dataset can shrink due to user requested data deletions, and these deletions require us to write different generations of the same data. In the end, only the last generation contains the correct information.

Are you lost yet?

If the answer is yes, it might be because we’re talking about outputs for a platform team rather than outcomes or impact. What do we mean by that? Let’s dig deeper in the following example.

# Outputs vs outcomes vs impact

In the example above, “making datasets with PII available using SQL” is an output of the Analytics Solutions team. Broadly speaking, the outputs the platform team produces are all those features our colleagues enjoy: making new datasets available, enabling scheduling capabilities for our notebooks solution, adding backfill support to our internal data wrangling libraries, etc.

Traditionally, outputs have been very easy to measure and visualise at a team level: every user story or epic accomplished is, more or less, a new output delivered. That’s why we have been using outputs for years in our quarterly planning sessions.

When we acknowledged that we wanted to switch to a metrics-driven approach in order to measure the results of our team, we started thinking about the outcomes we achieve thanks to our outputs.

Using the previous example, we can define the following relations:

![]()


In the above diagram you can see that if more datasets are available via SQL, the number of weekly querying users and teams using the service will increase.

In the following chart, you can see the amount of weekly querying users our “SQL on top of big data” service had during the first weeks of 2021:

![]()



And the corresponding number of teams using the service:

![]()



What insights can you extract from the data? Yes, week 17 was our best week so far! The reason? You got it right: it was the week before we made datasets with PII available using SQL. Outcome achieved!

This confirmed that the outcomes we can expect our Analytics Solutions team to achieve are an increase in usage, reduction of cost, generation of new opportunities, increase in customer satisfaction, etc.

Going one step further, what do we mean when we talk about “impact” in platform teams? Let’s look at this Slack message from one of our Data Analysts in the Messaging Center component, [**Pawel Tyszka**](https://www.linkedin.com/in/pawel-tyszka-41378b48/)**:**

*“Hi Analytics Solutions team, I just wanted to share my first use case of accessing a Messaging dataset via SQL that you enabled last week.*

*Coches.net* [one of our marketplaces] *wanted to know the percentage of messages sent by professionals to non-professionals by month (as a % of all messages). Using notebooks I’d need to set up a notebook, read months of data, write some code and wait for the long query to finish. In SQL the query ran in just 11 seconds.”*

This new feature (output) gained us a new user and team (outcome) which accelerated their decision making process (impact). Complete success!

Not to mention the happiness of the team after seeing those charts and the message from our Data Analyst in Slack! Thanks to these charts everyone can see the outcomes of the Analytics Solutions team’s outputs; and believe me, our team is very happy when we can present progress on our weekly [gembas](https://en.wikipedia.org/wiki/Gemba).

We didn’t feel this sense of achievement and recognition when we weren’t measuring outcomes and were just delivering features.

# Managing the lifecycle of your platform-team KPIs

One of the challenges of being a platform team is that impacting the KPIs the business is already tracking is very hard. What do we mean by that?

Because non-platform teams work on “The Main Product” your company offers, some KPIs will be available for them to monitor and use to define goals i.e. number of customers, conversion rates, etc.

In the best case scenario, your company will have an OKR that focuses on increasing the number of users by X or the number of transactions by Y. This OKR will then be cascaded to your product team and you can think of new features (outputs) that will make this metric increase (outcomes). In a similar way, marketing and other teams will be able to think about how they can also impact that KPI.

As a platform team, how can you impact the number of customers who use your “Main Product”? You can’t do it directly.

To put an external example: [Amplitude](https://amplitude.com/) is very open about the metrics they want to move. The north star of Amplitude used to be weekly querying users and then became [weekly learning users](https://blog.amplitude.com/evolving-the-product-north-star-metric). These two metrics serve to measure the outcomes of the new features/outputs they add to the tool. However measuring the impact Amplitude has on its customers beyond that is difficult.

![]()



In summary, the business KPIs your company sets won’t work immediately for your platform team. You’ll therefore need to find your own platform team KPIs (the same way Amplitude or our Analytics Solutions team found weekly querying users as a metric to move). You could run a workshop to come up with the KPIs as a team or impose them (we prefer the first), but either way you’ll need to apply [product thinking to your platform team](https://skamille.medium.com/product-for-internal-platforms-9205c3a08142).

Once you have defined your platform team KPIs, you will need to prioritise making them automatically available for your team to monitor weekly. If your platform team is managed by an Engineer, chances are this won’t get prioritised, so you’ll need to apply product thinking or hire a Product Manager to start breaking the wall.

After you have your KPIs monitored (it should be fine to start with a handful and then iterate), you’ll realise that the numbers are low (we have 10–15 teams using our SQL service) compared to your customer-facing “Main Product” numbers, and this makes them harder to move or experiment with.

Taking into account the above, setting goals on your KPIs is the next step. How many metrics do we have the bandwidth to impact? What is more important this year? How many weekly querying users do we want to have by the end of the year? What is a realistic yet challenging number to keep the team engaged?

We usually do this exercise once or twice a year when we set yearly OKRs for all the teams. We then review and adapt them on a quarterly basis. If a goal is achieved before the end of the period, we focus on other priorities. If we don’t achieve it by the end of the period we retrospect and decide if we want to keep the goal or if we need to modify it.

Finally, it’s important to regularly review the KPIs with the team and celebrate achievements. We usually review them once a week in our gemba walks and have a deeper discussion at a quarterly team meeting.

# Learnings

In general, the more to the right you move on the “outcome → output → impact” spectrum, the more difficult it will be to automatically measure the contribution your team is making.

In our specific example, automating the calculation of the increase in productivity is hard, almost impossible. What worked for us is to focus on the things we can control, such as automatising the measurement of outcomes.

Another learning is that if you do the exercise from right to left (that is, from impact to output), the relations between impact, outcomes and outputs will look like a tree. Most likely you won’t be the only one who can contribute and make an impact. After an expansive exercise, you will need to narrow down the possibilities and prioritise.

![]()


Next we learned that measuring is important. One of the reasons we didn’t use a metrics-driven approach initially was because tracking and reporting on data for our services was never a priority. This could be caused by a lack of product thinking in platform teams or technical complexity in extracting the data (or both).

To finish, let’s focus on time scales and managing expectations. Setting an outcome-based goal (i.e. increase the number of weekly querying users) for a specific quarter and expecting the team to deliver the outputs that can move this metric AND have time for the specific metric to move is unrealistic.

For this year, we’ve set outcome-based targets and so far, we’re very happy with the improvements from this new way of working.