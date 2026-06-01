---
title: Diving Into Engineering Metrics
date: '2023-10-15T22:00:31-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://hybridhacker.email/p/diving-into-engineering-metrics
---

[Diving Into Engineering Metrics](https://hybridhacker.email/p/diving-into-engineering-metrics)  



In today’s engineering world, you often hear about something called “Engineering Metrics.” Whether you’re a new engineering manager or have been in the field for a long time, you’ve probably come across this term.

But what exactly are engineering metrics, and how can they help you and your team?

In this essay, we’ll dive into the world of engineering metrics and specifically:

* **🔍 What Engineering Metrics are and what’s their purpose**
* **🏭 See how they relate to Productivity**
* 🚀 **How to make the most from them**

*Before we begin, let me introduce our first sponsor. Since this is the first time I’ve included a sponsor here, please let me know if this bothers you in any way!*

*Typo is a Software delivery intelligence platform that enables modern software teams with visibility, insights & tools to code better, deploy faster & stay aligned with business goals.*

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90214e9f-7961-4bdc-9bca-ad62f721755a_1452x596.jpeg)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90214e9f-7961-4bdc-9bca-ad62f721755a_1452x596.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90214e9f-7961-4bdc-9bca-ad62f721755a_1452x596.jpeg)

*Typo is sponsoring this newsletter issue and is offering The Hybrid Hacker readers a **20% discount** on their paid plan (just contact them and say you are coming from The Hybrid Hacker newsletter). I tried Typo first-hand and was impressed by the amount of data they gather and how they aggregate it. Also, you’ll find many of the metrics I’ll mention today in this newsletter there.*

[Learn More about Typo](https://typoapp.io/?utm_source=newsletter&utm_medium=banner&utm_campaign=hybrid_hacker&utm_id=23)

## **🔍** Understanding Engineering Metrics

Engineering metrics are a fascinating topic because they attempt to quantify elements of the software engineering process which can sometimes, due to its nature, feel intangible.

### What are Engineering Metrics

In their wider sense, Engineering Metrics are quantitative measures that provide insights into various aspects of the software development process.

They can cover a wide range of areas, like:

* 📊 **Quality:** metrics like bug rate, test coverage, and escaped defects
* 🚀 **Efficiency:** metrics like velocity, lead time and cycle time
* 🔄 **Operational Efficiency:** deployment-related metrics like deployment frequency or commit-to-deploy time
* 👥 **Collaboration and Team Dynamics:** insights from code review turnaround time or the number of comments per pull request
* 🔒 **Reliability:** measures such as Mean Time to Recovery (MTTR) or Change Failure Rate
* 🛠️ **Technical Health:** metrics related to technical debt and code maintainability
* ⚡ **Performance:** metrics such as response times, server downtimes, and latency figures
* 💡 **Developer Experience:** metrics like DevEx and developer satisfaction surveys

### Purpose of Engineering Metrics

The goals of using Engineering Metrics can be multiple. At a high level, their aim is to provide clarity, drive improvement, and ensure alignment in the engineering process.

Here’s a deeper look at their primary objectives:

* **Understand Performance:** they help teams and managers understand how well the engineering process is working.
* **Improve Over Time:** by tracking trends, teams can identify areas that need improvement and take action.
* **Support Decision-Making:** metrics provide data for making informed decisions, like allocating resources to fix code defects.
* **Align with Business Goals:** metrics ensure that engineering efforts contribute to broader business objectives.
* **Set and Track Goals:** teams can set specific goals and measure progress toward them using metrics.
* **Communicate Progress:** metrics provide a common language for reporting project status to stakeholders.
* **Boost Morale:** seeing improvements in metrics can motivate and boost team morale.
* **Optimize Resources:** metrics help allocate resources efficiently, addressing areas that need more attention.
* **Ensure Quality:** metrics related to code quality and testing ensure that the software meets high standards.

Alongside these goals, Engineering Metrics over the years served another purpose: attempting to measure productivity.

## **🏭** Engineering Metrics and Productivity

In recent months, [an article](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity) published by McKinsey has generated significant buzz in the engineering community and sparked a lively discussion regarding the measurement of developer productivity. 

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dd9ab92-311b-43ef-a8f3-f8a32071d885_3000x1688.png)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dd9ab92-311b-43ef-a8f3-f8a32071d885_3000x1688.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dd9ab92-311b-43ef-a8f3-f8a32071d885_3000x1688.png)

History of Productivity Metrics


Measuring engineering productivity is likely one of the biggest challenges for every engineering manager, and perhaps **even more so for C-level executives**, who often lack a clear understanding of the development process. Engineering metrics have often been identified as the way to achieve this goal.

Let’s look at the history.

### SLOC (early 50′)

It all started with [Source Lines of Code](https://en.wikipedia.org/wiki/Source_lines_of_code) (SLOC). It was initially introduced as a metric when programming languages like FORTRAN and ASM were prevalent. These languages were line-oriented and tied to punched card input, where one card equaled one line of code. This made it easy to count and equated to a visible measure of a programmer’s productivity, often referred to as “[card images](https://en.wikipedia.org/wiki/Card_image).”

### Velocity (early 90′)

In the early 90’, agile development movement started to raise and so the first agile frameworks. [Scrum](https://www.scrum.org/learning-series/what-is-scrum), probably the most famous agile framework, incorporated velocity as a metric used to **measure the amount of work a development team can complete** in a given time frame, typically during a sprint or an iteration. Velocity is often expressed in story points, which are a relative measure of the effort required to complete a user story or a task. 

### Cycle Time (late 90′)

In software development, cycle time typically refers to the time it takes for a development team to complete one iteration or cycle of work from start to finish.

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d73a89d-7b0f-4f37-aed5-9ccf125c13fa_3000x1688.png)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d73a89d-7b0f-4f37-aed5-9ccf125c13fa_3000x1688.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d73a89d-7b0f-4f37-aed5-9ccf125c13fa_3000x1688.png)

Velocity vs Cycle Time


While it could seem similar to velocity, cycle time provides insights into the speed at which tasks/features are completed, while velocity is a metric that measures the overall team’s capacity and productivity over a fixed time frame.

### DORA (2014-2022)

[DORA](https://dora.dev/) (DevOps Research and Assessment), authored by Nicole Forsgren, Jez Humble, and Gene Kim, comprises a set of performance indicators known as the Four Key Metrics. These metrics assist organizations in evaluating and quantifying the effectiveness of their DevOps practices, and they were developed through extensive research in the DevOps and software delivery domain.

The Four Key Metrics include:

1. **Lead Time for Changes:**
   
   * **What it is:** this measures how long it takes to turn an idea or request into a working feature in a live system.
   * **Why it matters:** shorter lead times mean faster responses to customer needs and market demands.
2. **Deployment Frequency:**
   
   * **What it is:** this tracks how often new code changes or features are added to a live system.
   * **Why it matters:** higher deployment frequency shows the ability to release changes quickly and reliably.
3. **Change Failure Rate:**
   
   * **What it is:** it calculates the percentage of code changes that cause problems or need to be undone.
   * **Why it matters:** a low failure rate means solid testing and less risk of issues for customers.
4. **Mean Time to Recovery (MTTR):**
   
   * **What it is:** it measures how quickly a team can fix and recover from unexpected problems.
   * **Why it matters:** a low MTTR shows efficient incident response and less impact on customers.

Based on their research, high-performing organizations typically exhibit shorter lead times, higher deployment frequencies, lower change failure rates, and shorter mean times to recovery.

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F015ff989-f90b-45f7-9c38-ea93572a530f_2000x1295.jpeg)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F015ff989-f90b-45f7-9c38-ea93572a530f_2000x1295.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F015ff989-f90b-45f7-9c38-ea93572a530f_2000x1295.jpeg)

The four metrics and how they score


The introduction of DORA metrics marked a significant paradigm shift. Previously, productivity metrics were subjectively used, with each organization primarily referencing itself. The concept behind DORA metrics was to collect data from numerous organizations and create an empirical measure to evaluate performance and productivity.

In 2018 DORA [was acquired](https://dora.dev/news/dora-joins-google-cloud/) by Google and their research is still ongoing with fresh data being released every year. 

### SPACE (2021)

While DORA gave an empirical way of measuring engineering productivity between organizations, in 2021 the same authors published the [SPACE framework,](https://queue.acm.org/detail.cfm?id=3454124) with the idea of giving a more holistic view of engineering productivity.

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe89dca21-c18f-4510-b470-627c938e29be_770x842.webp)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe89dca21-c18f-4510-b470-627c938e29be_770x842.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe89dca21-c18f-4510-b470-627c938e29be_770x842.webp)

SPACE provides 5 dimensions of metrics:

1. **Satisfaction:** reflects developers’ feelings about their code review workload and opportunities for learning.
2. **Performance:** measures review speed at both individual and team levels, considering team policies.
3. **Activity:** counts the total code reviews an individual completes in a set time frame.
4. **Communication and collaboration:** evaluates the depth and quality of reviews as a measure of team interaction.
5. **Efficiency and flow:** assesses the impact of review timing on workflow and system throughput, balancing interruptions and overall delivery speed.

### DevEx (2023)

Recently (April 2023), another interesting paper was released by some of the authors of DORA and SPACE, introducing what they refer to as the [DevEx](https://queue.acm.org/detail.cfm?id=3595878) [Framework](https://queue.acm.org/detail.cfm?id=3595878). 

While DORA aimed to provide an empirical way to measure the performance, and consequently productivity, of a development team, and SPACE aimed to make it more holistic, DevEx somehow recognizes that measuring productivity is not an easy task.

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10f0ecbb-3866-4b05-9f25-a43d7490eb60_805x507.png)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10f0ecbb-3866-4b05-9f25-a43d7490eb60_805x507.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10f0ecbb-3866-4b05-9f25-a43d7490eb60_805x507.png)

DevEx, as the name says, focus on Developer Experience and explores the three dimensions of how it’s affected.

* **Feedback loops** are crucial for efficient development, as they determine how quickly and effectively responses follow actions. Fast feedback loops are essential for smooth workflows, while slow ones can cause disruptions and delays. Organizations should work on shortening feedback loops by optimizing tools and processes.
* **Cognitive load** refers to the mental effort developers need to complete tasks. High cognitive load, often caused by poorly documented code or complex systems, can slow down developers and increase the risk of errors. To enhance the developer experience, teams should reduce unnecessary hurdles.
* **Flow state** is a state of deep concentration and enjoyment. Encouraging flow at work can boost productivity, innovation, and job satisfaction among developers. Organizations should prioritize creating conditions that facilitate this state for better employee performance and well-being

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcee7a1e3-fe72-453f-8c73-dfae3b15ce36_1153x818.png)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcee7a1e3-fe72-453f-8c73-dfae3b15ce36_1153x818.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcee7a1e3-fe72-453f-8c73-dfae3b15ce36_1153x818.png)

The framework also provides ideas on what to measure and how to measure it.

## 🚀 How to Make the Most of Engineering Metrics

As we saw, the world of Engineering Metrics can be a bit tricky, especially when it comes to measuring things like productivity.

During my early career, I was a big fan of engineering metrics, but nowadays**, I prefer to prioritize people’s well-being** because I believe it ultimately leads to higher performance, even if it means not measuring performance at all.

So, if you’re an Engineering Manager wondering if you should use metrics, the answer is: it depends!

But the real question is: how to use them?

While I don’t have the right answer, here are some tips coming directly from my experience:

* 🔍 **Stick with System Metrics**: some metrics, like downtime, response time, latency, are easy to understand and fair. Every engineer likes these metrics because they’re straightforward and everyone agrees on them. You can compare them without causing any problems.
* 🤝 **Team Metrics are better than Individual Metrics**: when it comes to measuring how productive your team is, it’s best to look at how the whole team is doing, rather than looking at the individual.
* 🚫 **Don’t use metrics to blame**: metrics are supposed to help, not cause fights. Instead of using them to prove someone wrong, use them to find out how to make things better. They’re tools for improving, not for blaming.
* 🔄 **Regularly review and adjust**: metrics aren’t set in stone and as you saw they are continuously evolving. Over time, things may change, and what you measure might need to change too. Regularly review the metrics you’re using and be ready to adjust them to stay aligned with your goals.
* 📚 **Educate your team**: make sure your team understands why you’re using metrics and how they can contribute to improving them. Everyone should be on the same page about why metrics are important and how they can help the team succeed.
* 🎯 **Keep it simple**: don’t get lost in the sea of metrics. Focus on a few key metrics that matter most to your team’s success. Too many metrics can become confusing and overwhelming.

In conclusion remember, **metrics aren’t everything**. 

Engineering Management and productivity are about more than just numbers. While we’re used to using numbers and data to measure things, people are different. You can’t measure everything about people with metrics because they’re not machines. So, don’t rely solely on metrics to understand how well your team is doing.

Use your instinct and listen to what your team have to say as well.

## ✌️ That’s all folks

That’s all for today! As always, I would love to hear from my readers (and if you’ve made it this far, you’re definitely one of the bravest). Please don’t hesitate to connect with me on [LinkedIn](https://www.linkedin.com/in/nicolaballotta) and send a message. I always respond to everyone!