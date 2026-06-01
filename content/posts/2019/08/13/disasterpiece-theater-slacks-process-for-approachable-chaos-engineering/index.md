---
title: 'Disasterpiece Theater: Slack’s process for approachable Chaos Engineering'
date: '2019-08-13T19:58:20-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://slack.engineering/disasterpiece-theater-slacks-process-for-approachable-chaos-engineering-3434422afb54
---

[Disasterpiece Theater: Slack’s process for approachable Chaos Engineering](https://slack.engineering/disasterpiece-theater-slacks-process-for-approachable-chaos-engineering-3434422afb54)  



![](https://i1.wp.com/miro.medium.com/fit/c/96/96/0*0SQZk5LBDEdz7Zqa.jpg?w=607&ssl=1)![](https://i1.wp.com/miro.medium.com/fit/c/96/96/0*0SQZk5LBDEdz7Zqa.jpg?w=607&ssl=1)

Richard Crowley
Aug 1 · 8 min read


Slack is a large and complex piece of software that’s been added to and changed many times over the last five years. We added features, grew to 10,000,000 DAUs, and made major architectural changes. We made assumptions and tested them with processes that often resembled science.

Whenever we launch features or make changes, we test the fault tolerance of that new code. Unfortunately, we seldom get to repeat these tests as the environment continues to change around that no-longer-new code. As the sands shift, those initial test results lose value. We remain confident in the resilience and robustness of our most critical systems but that confidence is less well-founded as time progresses. And luck is not an availability strategy, so something must be done.

If we were starting from scratch, we’d probably be practicing Chaos Engineering. After all, [“the best way to test the failure path is never to shut the service down normally.”](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton_html/index.html) But we’re not starting from scratch — we operate a large-scale, business-critical service. So what do we need, right now? We need to make Slack as reliable as possible. We need our development environment to be a more confidence-inspiring place to test for fault tolerance, and we believe that testing the fault tolerance of *all* our systems — not just new systems — will help us meet these needs. We don’t want to cause user-impacting incidents, so whatever we do needs to be safe as well. We also don’t need false confidence, so whatever we do needs to be in production.

In January of 2018, we started a rigorous process of identifying failures that are likely to happen and that we must be able to tolerate, and then purposely causing them to happen in production. This isn’t (yet) Chaos Engineering as practiced and evangelized by Netflix. It’s the first step; we call it Disasterpiece Theater.

# Preparing for an exercise

The process each Disasterpiece Theater exercise follows is designed to maximize learning while minimizing risk of a production incident. Each exercise takes place at a well-publicized time and place with all of the relevant experts in the same room or on the same video conference — we’re not (yet) trying to test our monitoring during these exercises. Before the exercise, one or two hosts write a detailed plan and share it widely. The plan is critical to the safety of the exercise but the plan on its own doesn’t teach us much about our fault tolerance.

The hosts are responsible for doing a “tabletop” exercise in which they think through the entire operation. They document precisely how they’re going to incite the failure, right down to the commands they’re going to run and how they’re going to select which EC2 instances are involved (we’ve taken to calling them “tributes”). We ask the hosts to go on the record for how confident they are that fault tolerance in the dev environment predicts fault tolerance in the prod environment for this exercise. They also document all the logs, metrics, and alerts that should be monitored, as well as runbooks that may be necessary during this exercise. Most importantly, they make a specific hypothesis explaining how the failure will be experienced by upstream and downstream systems and by Slack clients. An example of this might be, “Termination of a MySQL master will result in 20 seconds of increased latency for requests that depend on that database but no increase in latency for other requests and less than 1,000 failed API requests, all of which are retried by clients.”

# Disaster strikes: the exercise in motion

We start each exercise by reviewing the plan and projecting/sharing dashboards in Grafana and searches in Kibana. Now we’re ready to incite failure.

We announce the exercise in our **#ops** channel where more than 700 people hang out. We don’t stop deploys or any other normal activities during the exercise but we do make those folks aware of our plans. We broadcast a few coarse status updates in **#ops** throughout the exercise and keep our play-by-play in **#disasterpiece-theater**.

Exercises always begin by inciting the failure in dev. Then we inspect logs and metrics to confirm the failure is visible in all the ways we expect it to be and not visible in others. It’s a common instinct to want to *go fix something* but we control ourselves and watch the system take care of itself. We look for load balancers and other traffic management to route around the failure or for capacity to be replaced. Occasionally we have to follow runbooks to restore service.

Once the failure has been dealt with in the development environment, we pause to make a go or no-go decision about proceeding to production. The exercise isn’t considered a failure or a waste of time if we don’t proceed to production; in fact, some of our most valuable lessons have come from the development environment. We seriously consider aborting if automated remediations didn’t work, didn’t work *perfectly*, took too long or, most importantly, if the failure would result in more disruption than a short and minor increase in latency for customers. If we’re aborting, we announce the abort in **#ops**.

![](https://miro.medium.com/max/60/0*clR6h7WJovYPH8XC?q=20)![](https://miro.medium.com/max/60/0*clR6h7WJovYPH8XC?q=20)

![]()



Hopefully, though, we’re encouraged by the results in development and are ready to incite failure in the production environment. We project/share the production dashboards in Grafana and searches in Kibana. We announce in **#ops** that we’re moving on to production.

![](https://miro.medium.com/max/60/0*q7q9Sgn77BYhwFz9?q=20)![](https://miro.medium.com/max/60/0*q7q9Sgn77BYhwFz9?q=20)

![]()



Finally, the moment of truth arrives. We incite failure in production. Just like we did in development, we inspect logs and metrics, looking to confirm our hypothesis. We give automated remediation time to do its work. Usually, this moment that’s theoretically terrifying is actually quite calm. When we’re finished, we announce the all-clear in **#ops**.

Then, we debrief: What was the time to detect and time to resolve? Did any users notice? Did any humans have to intervene? What was terrifying? Was any of our documentation wrong? Were any dashboards in Grafana out of date?

# Our results to date

We’ve run dozens of Disasterpiece Theater exercises at Slack. The majority of them have gone roughly according to plan, expanding our confidence in existing systems and proving the correct functioning of new ones. Some, however, have identified serious vulnerabilities to the availability or correctness of Slack and given us the opportunity to fix them before impacting customers. Here are summaries of three particularly successful exercises:

## Avoid cache inconsistency

The first time Disasterpiece Theater turned its attention to memcached it was to demonstrate in production that automatic instance replacement worked properly. The exercise was simple, opting to disconnect a memcached instance from the network to observe a spare take its place. Next, we restored its network connectivity and terminated the replacement instance.

During our review of the plan we recognized a vulnerability in the instance replacement algorithm and soon confirmed its existence in the development environment. As it was originally implemented, if an instance loses its lease on a range of cache keys and then gets that same lease back, it does not flush its cache entries. However, in this case, another instance had served that range of cache keys in the interim, meaning the data in the original instance had become stale and possibly incorrect.

We addressed this in the exercise by manually flushing the cache at the appropriate moment and then, immediately after the exercise, changed the algorithm and tested it again. Without this result, we may have lived unknowingly with a small risk of cache corruption for quite a while.

## Try, try again (for safety)

In early 2019 we planned a series of ten exercises to demonstrate Slack’s tolerance of zonal failures and network partitions in AWS. One of these exercises concerned Channel Server, a system responsible for broadcasting newly sent messages and metadata to all connected Slack client WebSockets. The goal was simply to partition 25% of the Channel Servers from the network to observe that the failures were detected and the instances were replaced by spares.

The first attempt to create this network partition failed to fully account for the overlay network that provides transparent transit encryption. In effect, we isolated each Channel Server *far more* than anticipated, creating a situation closer to disconnecting them from the network than a network partition. We stopped early to regroup and get the network partition just right.

The second attempt showed promise but was also ended before reaching production. This exercise did offer a positive result, though: It showed Consul was quite adept at routing around network partitions. This inspired confidence but doomed this exercise as we ended up doing a lot of work to not even cause any Channel Servers to fail.

The third and final attempt finally brought along a complete arsenal of iptables(8) rules and succeeded in partitioning 25% of the Channel Servers from the network. Consul detected the failures quickly and replacements were thrown into action. Most importantly, the load this massive automated reconfiguration brought on the Slack API was well within that system’s capacity. At the end of a long road, it was positive results all around!

## Impossibility result

There have also been negative results. Incident response often involves making configuration changes using an internally developed system called Confabulator. During one particularly bad incident, Confabulator didn’t operate as expected and we had to make and deploy the configuration change manually. I thought this was worthy of further investigation. The maintainers and I planned an exercise to directly mimic the situation we encountered. Confabulator would be partitioned from the Slack service but otherwise left completely intact. Then we would try to make a no-op configuration change.

We reproduced the error without any trouble and started tracing through our code. It didn’t take long to find the problem. The system’s authors anticipated the situation in which Slack itself was down and thus was unable to validate the proposed configuration change; they offered an emergency mode that skipped that validation. However, both normal and emergency modes attempted to post a notice of the configuration change to a Slack channel. There was no timeout on this action but there was a timeout on the overall configuration API action. As a result, even in emergency mode, the request could never make it as far as making the requested configuration change if Slack itself was down. Since then, we’ve made many improvements to code and configuration deploy and have audited timeout and retry policies in these critical systems.

# Into the future

Disasterpiece Theater has made the regular, safe testing of the fault tolerance of Slack’s most critical systems approachable and non-terrifying. It helps us understand and improve Slack’s basic reliability, one of the most important factors in earning and keeping our customers’ trust, even as we expand and evolve the product.

Exercises like the three highlighted above helped us to improve Slack’s reliability and built (or corrected) our confidence in our systems’ fault tolerance. Our Resilience Engineering team continues to expand and evolve this process all the time and, of course, is planning to run many more Disasterpiece Theater exercises. If you find this interesting and want to be a part of the next exercise, [come join us](https://slack.com/careers/)!