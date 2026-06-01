---
title: A Primer on Engineering Delivery Metrics
date: '2020-09-29T23:45:31-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://leaddev.com/primer-engineering-delivery-metrics
---

[A Primer on Engineering Delivery Metrics](https://leaddev.com/primer-engineering-delivery-metrics)  



Before joining [Stripe](https://stripe.com/), I had the opportunity to build, grow, and lead the [Splice](https://splice.com/) engineering organization for almost four years (yes, still I mix up the names). The most challenging engineering problem I’ve had to tackle so far has been working on accelerating software delivery in an organization that grew from 5 to 55+ engineers in my first 18 months. As the Splice team expanded, our ability to deliver software ground to a halt. The processes that worked when the company was small couldn’t support the explosive growth, and we needed to find a way to get back on track. By focusing on delivery metrics, we were able to increase the rate of software delivery drastically, and you don’t have to take my word for it, let’s look at a graph of cycle time (or delivery lead time) from May 2018 to April 2019.

![](https://lh3.googleusercontent.com/p4BZUo4UtAzkdOV3uqK88jTx34Cy6e_p1OJRC3WeEHBTdY1mobwx17QYg8zZly7NPJ0DACLoAVeP6LIo6APVbnD0wCnAYypKng1eiqT6qkZI3sIWbNfh-RjIvMktsp4FeNZvfxT2)![](https://lh3.googleusercontent.com/p4BZUo4UtAzkdOV3uqK88jTx34Cy6e_p1OJRC3WeEHBTdY1mobwx17QYg8zZly7NPJ0DACLoAVeP6LIo6APVbnD0wCnAYypKng1eiqT6qkZI3sIWbNfh-RjIvMktsp4FeNZvfxT2)

This graph shows how we stabilized **delivery lead time** over a year. This metric’s average also decreased from a few hundred hours to the lower tens, even reaching 20 hours on our best delivery weeks despite frequent organization change. We did this without working longer hours or even weekends, but rather by engineering our processes using metrics to observe and direct the desired change. Today, any team can take control of their ability to deliver production-ready software at an accelerating tempo by understanding and adopting a few simple metrics. Let’s dive in.

## What are engineering delivery metrics?

Engineering delivery metrics are a method of measuring the software delivery phase in software development. We measure delivery, and not the entire development process because the design phase of software varies significantly. In the early stages of software, we don’t know what we’re looking to build, so to make our lives easier, we focus on the portion of the pipeline where we can have more control as engineers. To do this, we can assume that the delivery process begins when we commit code and ends when code is running in production.

![](https://lh5.googleusercontent.com/mwxLQLKwZjLRvwgi31jE-SaioQlO77r0LlyBYghPafBpuojTbBWl_Cz3eWPZZ7n0bquUD1gBKt0-KQyMczOgCRFdBpSNrfhSwB0UrjHs-JVHusrl45ZgrAskb_wII5KjoxpDamKJ)![](https://lh5.googleusercontent.com/mwxLQLKwZjLRvwgi31jE-SaioQlO77r0LlyBYghPafBpuojTbBWl_Cz3eWPZZ7n0bquUD1gBKt0-KQyMczOgCRFdBpSNrfhSwB0UrjHs-JVHusrl45ZgrAskb_wII5KjoxpDamKJ)

**Product design & development**

**Product delivery**

Create new products and services that solve customer problems using hypothesis-driven delivery, modern UX, and design thinking.

Enable fast flow from development to production and reliable releases by standardizing work, and reducing variability and batch sizes.

Feature design and implementation may require work that has never been performed before.

Integration, test, and deployment must be performed continuously as quickly as possible.

Estimates are highly uncertain.

Cycle times should be well-known and predictable.

Outcomes are highly variable.

Outcomes should have low variability.

[[1]](#ipfootnote0)

We can instrument several metrics across the entire delivery process, and their effectiveness depends on the outcomes we’re seeking for our organization. Before we measure, we must ask, ‘what are we trying to achieve with these?’ Metrics are neither good nor bad. They can be useful or harmful, and the results depend on our context and ability to use them.

Some examples of metrics can be:

* Build time
* Code volume
* Code churn
* Time to merge

In the absence of any context, it’s hard to tell if any of these metrics will produce the desired results. For example, would we [get any positive outcomes if we measured lines of code](https://www.infoworld.com/article/2072312/lines-of-code-and-unintended-consequences.html)? Deleting code can sometimes produce better results than adding more.

## Why use delivery metrics?

Knowing why we measure can be more impactful than what we measure. Software delivery is an emergent property of a software engineering team and the processes it adopts. For example, heart rate is an emergent property of the heart and can give us valuable information about its health. In conjunction with useful metrics, well-defined outcomes offer us a window into how our organization delivers software. Metrics help us observe our process and evolve it.

At Splice, the desired results involved eliminating roadblocks that engineers had in shipping software because we wanted to learn fast. Product engineering teams in early-stage companies are learning with every line of code they get in front of users. If we wanted to achieve our mission of ‘enabling Splice to learn faster than the market by delivering production-ready software at an accelerating tempo’, we needed a way to see what was holding us back so that we could change it. If we were a company that supported enterprise customers, our emphasis might have increased our services’ reliability over our iteration speed.

![](https://lh4.googleusercontent.com/6Br30nuJ28xuwlhfxCPSZxaR124VxWkrmrT3HQbETVsnegiB5BYwEsE8nMFwhJFoHyrTnd12wCiJ34-t1jpcx7to5-hIHnxG0NFb2OPN8TgytiACBHtGbkjzsfblLNXGUEzdWOMv)![](https://lh4.googleusercontent.com/6Br30nuJ28xuwlhfxCPSZxaR124VxWkrmrT3HQbETVsnegiB5BYwEsE8nMFwhJFoHyrTnd12wCiJ34-t1jpcx7to5-hIHnxG0NFb2OPN8TgytiACBHtGbkjzsfblLNXGUEzdWOMv)

*One year of code pushes at Splice during our delivery improvement plan, showing how we improved our throughput without growing in size or working longer hours.*

Before you pick what you want to measure, define why you want to measure it. A few examples of outcomes you might be looking for can be:

* Better reliability
* Improved quality
* Lower effort
* Increased throughput
* Cost-effectiveness
* Staffing efficiency
* Faster learning

## Which delivery metrics are useful?

When you search the web for “engineering delivery metrics”, the results are abundant and not always useful or tailored to your outcomes. When we embarked on this journey, the most valuable resources I found were a series of reports compiled by different groups or companies we had to mix-and-match from to get actionable results. Fortunately for us, Dr. Nicole Forsgren and her team have done all the heavy lifting and summarized it in a book called [*Accelerate.*](https://www.oreilly.com/library/view/accelerate/9781457191435/) It sits on my desk, next to [*The Manager’s Path*](https://www.amazon.com/Managers-Path-Leaders-Navigating-Growth-ebook/dp/B06XP3GJ7F) by Camille Fournier. These two books mark the beginning of a new era in engineering leadership, where learning how to be a great leader doesn’t require oral tradition inside an established tech company.

In *Accelerate*, Dr. Forsgren and her team set the foundation of four metrics they found to be good indicators of software delivery performance across thousands of organizations. From there, they also proposed a capabilities framework that can allow software organizations to increase their performance and drive better business outcomes. A fascinating conclusion is how they were able to find a relationship between software delivery and organizational performance. It seems that if we’re good at delivering software, then our company as a whole performs better.

If you’ve read [Smruti’s article on debugging engineering velocity](https://leaddev.com/debugging-engineering-velocity-and-leading-high-performing-teams), you’ve already encountered the four metrics outlined by Dr. Fosgren, and the ones we found to be the most useful as we drove change at Splice.

#### Software Delivery Performance Metrics

⌚️ **Delivery lead time**. How long it takes code from commit to production.   

🚢 **Deployment frequency.** How often we are deploying to production.   

🚒 **Mean time to restore.** How long it takes us to restore service after an incident.   

🔨 **Change failure rate.** The percentage of changes that degrade service or require remediation.

### What about story points and velocity?

[Velocity](https://www.agilealliance.org/glossary/velocity) is not a good measure of the software delivery process because it’s designed to be a capacity planning tool. When we use velocity to measure productivity, our approach is flawed because:

‘*First, velocity is a relative and team-dependent measure, not an absolute one. Teams usually have significantly different contexts which render their velocities incommensurable. Second, when velocity is used as a productivity measure, teams inevitably work to game their velocity. They inflate their estimates and focus on completing as many stories as possible at the expense of collaboration with as many stories as possible at the expense of collaboration with other teams (which might decrease their velocity and increase the other team’s velocity, making them look bad). Not only does this destroy the utility of velocity for its intended purpose, it also inhibits collaboration between teams.’* *[[2]](#ipfootnote1)*

## How should you use delivery metrics?

Without knowing the exact problem you or your team faces, it’s challenging to make a recommendation that can be helpful. Instead, I [asked engineering leaders for their questions](https://twitter.com/buritica/status/1277745668505972736) and found some common patterns.

### How do I convince my team about using metrics?

In the last few years, I’ve advised several companies in the adoption of delivery metrics, and the first hurdle any leader has to cross is to sell their team on the use of these metrics. In my experience, convincing a team to adopt metrics is highly dependent on how well they understand the purpose of measuring, and how much they trust you. Unfortunately, metrics have been used to judge individual performance in ways that have negatively impacted employees beyond their actual performance, such as using lines of code. These poor management practices have eroded the trust between management and collaborators, and it’s normal for engineers to approach metrics with skepticism.

To successfully convince your team to adopt delivery metrics, you must have an obvious purpose for the metrics and solid reasoning for the outcomes you seek. Some questions you should be able to answer to your team members about your intention of measuring the delivery process can be:

* Why do we need metrics?
* What are we going to measure?
* Who will have access to these metrics?
* Why did we pick these metrics, and which others could we have chosen?
* What is our plan to move these metrics forward?
* How will these metrics impact individuals?

Engineering managers should hold their problem-solving abilities and reasoning to the same standards for engineers in their organization. In my case, writing a proposal that outlined my thinking in the form of an RFC helped iron out the details that weren’t clear, and my team helped make it more robust through their questions. You can [read the original version of this document here](https://github.com/buritica/mgt/blob/master/rfcs/up-tempo.md).

The primary lesson I took from deploying delivery metrics was the importance of trust. For metrics to be successful, I needed my team to trust my intentions and embrace the strategy presented to them, especially when I didn’t have too many answers on the actual results we’d get. Not only should you have answers for the questions outlined above, and possibly others depending on your needs, the answers need to give confidence to your team about the approach, even if you don’t know what you’re doing yet.

### How can I, an engineer, prevent metrics from being used against me?

The most common question I get from individual contributors who are directly responsible for delivering software is how to prevent these metrics from negatively impacting them. The best response I’ve found is to focus on the outcomes intended on these metrics and ask questions that derive the purpose of measuring. In the process, you might find that the purpose of measuring is to gauge individual performance. At this stage, you’re likely facing a manager that misunderstands the purpose of delivery metrics and what they measure. Depending on your organization, and the relationship you might have with them, you may want to encourage them to rethink their approach, or you can have them read this article. It’s not an easy problem to solve.

Another possible scenario you can encounter as an engineer is the mismanagement of expectations or promises made on behalf of the team. When this happens, the intended outcome isn’t the improvement of the team, but rather the appeasement of external parties. We don’t set metrics so we can move them to keep others happy, we do it so teams have a way to observe what’s getting in their way. Measuring without a plan of improvement can cause the team to lose motivation and engagement, leading to the opposite results. A management team that adopts metrics is implicitly saying it will be investing in accelerating the software delivery process. Explicitly, they should allocate staff and attention to this plan, otherwise it’s surveillance and not team acceleration. If you find yourself in this scenario as an individual contributor, relying on senior ICs and taking ownership of the plan to drive these metrics forward might help you prevent adverse outcomes.

Metrics aren’t just a tool for management, to the contrary they are tools that give visibility to engineers about how they deliver software collectively. Delivery metrics are also empowering because they give everyone the language to prioritize work that is essential to delivering high-quality software at scale, through data. For example, you can now argue that single-threading engineers in projects leads to lower cycle times because moving past code reviews in teams of one is an obstacle, and you should either increase the size of the team or reduce the amount of parallel work to get on track. Take ownership of your own metrics and use them to get blockers out of the way.

### How can I actually measure what I want to measure?

Finally, the last pattern I’ve found trying to support organizations in the pursuit of measuring their delivery is about the method of measuring. As engineers, we tend to be overly obsessed with tooling. The truth is that delivery processes vary from organization to organization, and even within an organization. Finding teams that use different task tracking tools in the same company is not uncommon. Approaching measuring from a tooling-first approach can make it harder for you to focus on the outcomes you’re trying to drive because you might end up spending more time setting up the tool or adapting your process to it before you discover your needs.

Tools exist, and some are better than others, but just like task tracking software, they’re all different and depend on what you need. Before you procure an expensive SaaS tool that you might not end up using, a simple tool might help you understand what you need. A few months ago, I sat down with Nicole Forsgren, Ph.D., and asked her about three recommendations for leaders who were wondering how to measure their teams, and this is what she had to say.

**A survey is enough.** Surveying your team about their experience delivering software can give you enough signal of where the roadblocks lie. Dr. Forsgren also mentioned you can find the exact survey she used to capture the four software delivery metrics at [devops-research.com](https://www.devops-research.com/). Now it’s available with an interactive Quick Check and baselines.

**Accept where you are, even if it’s bad.** A baseline, even a bad one, can help you get moving forward because you now have a frame of reference. For example, if you target a few daily deployments and find out you’re deploying only once a month – reset expectations, accept your reality, and set a plan to improve. Without a realistic understanding of your performance, you will never know what you need to improve, and just as significantly, what you’ve accomplished when you have put in the hard work.

**Continuous improvement is better than a five-year roadmap.** Pretending that you know all the changes you need to adopt can be problematic. Iterating towards the desired outcomes can produce better results than a multi-year delivery acceleration plan.

Discussing these recommendations with Dr. Forsgren was fascinating because I had experienced them myself (except for the survey, I wish I had surveyed instead of trying to pipe GitHub data into BigQuery and chart it with Data Studio). Early on, I pulled a baseline for cycle time out of nowhere. Thirty-six hours seemed like a good number; we discovered that the number could be much better in the process. We also created a dedicated team focused on driving these metrics forward with other product engineering teams’ support. Engineers were empowered to make changes in the process that improved the delivery process over time.

## How can I manage my team through delivery metrics?

You can’t. Delivery metrics were designed to help you, and your team identify opportunities in your delivery process, fix them, and use more of your energy towards the product problems in front of you. Attempting to manage individuals based on delivery metrics is akin to measuring a single heart cell’s heart rate. I don’t recommend you use deployment frequency or cycle time as proxies of individual delivery. Many software tools are heading in the direction of delivery insights for individuals, and based on my experience, I would caution you against this use. There are better approaches to this challenge, like up-leveling your managers and giving teams the right goals and expectations. Delivery metrics shouldn’t replace management judgment.

## Conclusion

Engineering delivery metrics, coupled with well-defined organizational outcomes, can drastically improve how your organization delivers software. Thanks to research done by people like Dr. Forsgren and her team, we have the tools to communicate with and beyond engineering teams about what it means to be a high-performing organization. For example, we can use cycle time to reason through the impact of single-threading engineers in projects because fewer eyes on code reviews increase the time it takes to deliver software. We can also look at our processes without building complex tools or procuring expensive SaaS. Now that we have them available, it’s our responsibility as leaders to ensure that metrics that can help us sustainably deliver high-quality software are used properly, and in the service of the individuals and organizations, we lead. If you want to dive deeper into the story on why I found and deployed delivery metrics or the results that we drove, you can watch [this talk](https://codeclimate.wistia.com/medias/jcrn6ahlp1) or skim [through these slides.](https://speakerdeck.com/buritica/increasing-engineering-tempo-at-splice)

*Thanks to Silvia, Marc, Coda, Kellan, Marco, André, and Camille for reading an unfinished version of this post. A special thank you to Dr. Nicole Forsgren, for her infinite patience for my questions, and huge shout out to the Splice Engineering team <3 who had to deal with my non-stop Time to Merge reports. They deserve the real credit for this work.*

### Footnotes

PhD, F. N., Humble, J., & Kim, G. (2018, p 15). *Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations* (1st ed.). IT Revolution Press.

PhD, F. N., Humble, J., & Kim, G. (2018, p 13). *Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations* (1st ed.). IT Revolution Press.

1. [1]
2. [2]