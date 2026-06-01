---
title: Metrics-Driven Development
date: '2017-09-21T23:19:16-06:00'
format: link
service: instapaper
tags:
- mdd
- metrics
- read
external_url: https://sookocheff.com/post/mdd/mdd//
---

[Metrics-Driven Development](https://sookocheff.com/post/mdd/mdd)  



Metrics-Driven Development is an emerging term developing from the  

practices of continuous integration, continuous delivery, dev ops, and  

agile software methodologies. This article serves to define what  

metrics-driven development is, why it is useful, and how to use it to  

drive software changes.Let’s start with a definition of [metrics-driven  

development](http://blog.librato.com/posts/2014/7/16/metrics-driven-development).
Metrics-Driven Development (MDD)
The use of real-time metrics to drive rapid, precise,  

and granular software iterations.

This definition is simple and straightforward, but does leave room for  

interpretation. Let’s dive deeper and break the definition down,  

bit-by-bit.

Real-time
To be effective, metrics must be viewable by developers and  

operations staff in close to real-time. Why? Real-time metrics provide an  

immediate view of the effect of software changes to production systems  

— and understanding the effects of software changes in production is one  

of the key benefits for employing metrics-driven development.
Rapid
Changes to production software can be made rapidly to affect changes in  

one or more metrics. Combining rapid deployment with real-time metrics  

provides a powerful force for iterating production software towards  

performance and stability goals.
Precise
Changes to production software can precisely change a given metric in  

a target direction. By being able to make precise changes to a metric,  

the development team can focus on targeting a particular metric of  

interest with each software change.
Granular
Changes to production software can target metrics at a granular level.  

Individual development teams should be able to deploy changes to production  

software that target individual metrics.

This definition and its individual components emphasizes the need for  

combining real-time metric collection and reporting with the ability to  

make small, rapid software changes. These capabilities provide two  

benefits. First, they allow you to make software development decisions  

based on real-world production data. Second, they provide a means of  

affecting measurably beneficial changes to the software with each  

deployment. Together, metrics-driven development helps developers and  

businesses make better decisions by including metrics as an integral part  

of the development process.

## Prerequisites

MDD is a fundamentally iterative process. Although the principles and  

practices outlined in this article can be applied directly, they are  

especially powerful when used with the enabling technologies described in  

this section.

Taken as a whole, these prerequisites allow developers to quickly and  

safely deploy changes to production and control the set of users exposed  

to software changes. In this environment, MDD allows you to use metric  

data to drive each individual software iteration.

### Metrics architecture

Foremost, you need an architecture for collecting metrics from running  

application data and transmitting it to a data collection point. You also  

need a user interface for querying and visualizing data.

In practice today, this typically means deploying a data collection  

library like Coda Hale’s [Metrics](http://metrics.dropwizard.io/3.1.0/) with your application, and using  

an aggregation system like [fluentd](http://www.fluentd.org/) to push data to collection  

points. At collection points, data is ingested into a time-series  

database like [graphite](https://graphiteapp.org/) or [InfluxDB](https://influxdata.com/). A user  

interface like [Grafana](http://grafana.org/) is used to visualize metrics and provide  

dashboards.

Ultimately, your team or organizations requirements will dictate the  

specific technologies used. Providing specific guidance is outside the  

scope of this document.

### Continuous integration

[Continuous integration](http://martinfowler.com/articles/continuousIntegration.html) (CI) is the practice of frequently  

integrating changes from multiple members of each team. Each integration  

is verified automatically and errors are detected as quickly as possible.  

CI makes it possible to easily deploy cohesive working software.

### Continuous delivery

[Continuous delivery](http://martinfowler.com/bliki/ContinuousDelivery.html) (CD) is the practice of building software  

that can be deployed at any time. The priority is in keeping software  

working and deployable at all times. This allows teams to ship code to  

production at any moment, adding and removing metrics as necessary.

### Feature flagging

[Feature flagging](http://martinfowler.com/articles/feature-toggles.html) is a powerful technique allowing teams to  

modify system behaviour at runtime without changing code. The toggle can  

be turned “on” or “off” to expose users to new functionality. These users  

act as a test-bed for new code and by observing the metrics from these new  

users, the development team can make better decisions about the code being  

released.

A principle is a fundamental truth that serves as the foundation for  

a system of belief. What follows are the fundamental truths according to  

metrics-driven development. These truths guide the metrics-driven  

development process and help to frame the discussion of metrics as they  

apply to software development.

### Production is unique

The first principle guiding metrics-driven development is that your  

production environment is unique. This is necessarily true; you cannot  

exactly replicate your production environment for local development,  

testing, or staging. You *must* accept that production is different.

Why is production different? Foremost, the data. The amount and variety of  

data in production typically dwarves that of any testing environment.  

Also, as is typical in production workloads, some data may have been  

changed (either accidentally or intentionally during crisis management)  

and that change has not been accurately replicated in any testing  

environment; your development process needs to account for this  

possibility. Second, the scale. Typically, testing software changes works  

by deploying a single instance of your software to a single virtual  

machine or container. Then, on production that change is deployed to  

multiple virtual machines or containers and interacts with clusters of  

other services. The book [Release  

It!](https://www.amazon.ca/Release-Design-Deploy-Production-Ready-Software/dp/0978739213/)  

describes this problem as *Unbalanced Capacities* and these imbalances in  

production typically cannot be replicated locally.

More generally, there will *always* be edge cases in production data,  

hardware, or environment that cannot feasibly be replicated during  

testing. Production *is* unique.

### Tests are not enough

Testing is not enough to uncover potential production bugs. You need to do  

more than ensure that software changes pass tests, you need to verify that  

software changes correctly affect production behaviour. By using metrics  

and monitoring your team can accurately verify that a software change is  

working as expected.

Note that this does not mean tests are not valuable — they are absolutely  

essential for preventing regressions and validating your assumptions. Just  

be aware that unit tests can only capture the scenarios that you are  

already aware or that surface in QA. Since production is unique, you *will  

not* be able to imagine every possible scenario that should go into your  

unit tests.

### Your mental model is not complete

In production software systems, there is a gap between perception and  

reality. Our perception is the code that we write and how we expect it to  

behave, our reality is what happens when that code is actually run on  

production. For example, we may have a perception about why a certain  

operation is a bottleneck in the credit card processing workflow, but  

reality requires profiling and measuring the current workflow to determine  

the exact location of the bottleneck.

[Coda Hale](https://www.youtube.com/watch?v=czes-oa0yik) calls this the “gap” between  

perception and reality, cautioning us to “mind the gap”.

### Code has no value

Your job is not to write code; your job is to create value. Think about  

it. No sane employer will pay a software engineer to write code, print it  

out, and frame it to hang on a wall. That same code only has value when it  

is running *on production* and being used by *real users*.

So what provides business value? A new feature, improving an existing  

feature, fixing bugs, improving performance, or reducing cost, to name  

a few. All of these things only provide value when the code that  

implements them is *run*, not when they are *written*. It follows that to  

provide the most value to the business, an engineer needs to know as much  

as possible about how the code behaves *while it is running*. Metrics are  

typically the only way this is possible.

### If you can’t measure it, you can’t manage it (or improve it)

Originally attributed to Dr. Edwards Deming, for managing people and  

business processes, the quote “If you can’t measure it, you can’t manage  

it” applies equally well to managing software systems. If users start to  

complain about your site being “slow”, as an engineer you will need to  

have some sort of understanding of what “slow” actually means. This  

implies measuring it, so that you can improve it. If you have a metric  

tracking the latency of user requests, you can make targeted improvements  

to this metric through iterative software changes.

### You can’t measure everything

This article is about metrics and metrics-driven development. So  

naturally, I am bullish about adding metrics to the software development  

process. However, be mindful that quantity of metrics does not equal  

quality — you will need to strike the right balance of metrics in your  

system.

Unneeded metrics place additional resource constraints on the metrics  

pipeline itself, and can make relevant metrics more difficult to locate  

and interact with. This typically means purging and deleting metrics that  

are no longer valuable to you. Treat metrics curation as requirement of  

metrics-driven development.

Practices are the applications of principles stated in a context-dependent  

way. In our case, we apply the principles of metrics-driven development to  

the task of software development. To that end, we treat measurement and  

instrumentation as a software development practice integrated within the  

regular software development life cycle and apply the metrics-driven  

development principles to that context.

### Instrumentation as code

Developers typically have the best mental model of how an application is  

meant to behave in production. It therefore makes sense to make  

instrumentation an integral part of the software development process.

Given that developers can create targeted instrumentation in the  

application code itself, instrumentation becomes a required deliverable  

for every new feature or fix. When writing new code, the developer is able  

to form a hypothesis about its behavior in production; the measurements  

placed in the code are a means for the developer to prove or disprove  

their hypothesis.

### Single source of truth

Metrics collected during operations should be stored in a common  

repository, in a common format, and with a common interface for  

visualization, alerting, and analysis. This allows developers or  

operations staff to easily correlate metrics between systems and across  

all layers of the application stack.

The metrics platform must be timely, comprehensive, and intuitive so that  

everyone instinctively relies on it as their preferred resource to reason  

about the production environment.

### Alert on observations

An effective metrics-driven development process allows for alerts to  

trigger based on metric values. This allows developers and operations  

staff to effectively target affected systems by honing in on metrics  

showing signs of problems. Once isolated, the same set of metrics can  

confirm that any response has successfully resolved the issue.

It’s critical that alerts are triggered off of the same dataset used for  

visualization since disparate systems introduce the potential confusion  

and error. Any lack of certainty during incident response adds additional  

stress and increases the likelihood of human error.

### Use the scientific method

By deploying a change and measuring its effects, developers and operations  

gain confidence that any software change is reliable, performant, and  

affects the metric of interest, confirming any hypothesis.

Now, how do we follow the principles and practices outlined here? By using  

the Metrics-Driven Development Process using the [OODA  

loop](https://en.wikipedia.org/wiki/OODA_loop), devised by [John  

Boyd](https://en.wikipedia.org/wiki/John_Boyd_(military_strategist)).

> The phrase OODA loop refers to the decision cycle of observe, orient,  
> 
> decide, and act, developed by military strategist and United States Air  
> 
> Force Colonel John Boyd. Boyd applied the concept to the combat operations  
> 
> process, often at the strategic level in military operations. It is now  
> 
> also often applied to understand commercial operations and learning  
> 
> processes. The approach favors agility over raw power in dealing with  
> 
> human opponents in any endeavor.

The following example of the OODA loop is adapted from Coda Hale’s  

[Metrics, Metrics Everywhere talk](https://codahale.com/codeconf-2011-04-09-metrics-metrics-everywhere.pdf).

### Observe

All decisions are based on observations of an evolving situation.

You have a question:

> What is the 99% latency of our autocomplete service right now?

You look at current measurements:

> ~500ms

### Orient

During the orientation phase, we examine how an observation relates to our  

previous experiences.

You have a question:

> How does this compare to other parts of our system, both currently and historically?

You look at historical metrics:

> It’s way slower.

### Decide

Given the observation and our experience, we can decide on the next action  

to take.

You have a question:

> Should we make the autocomplete service faster? Or should we add a new  
> 
> feature?

You now have the knowledge to make an informed decision:

> Let’s make it faster.

### Act

You’ve made a decision, now act. Write some code, deploy it, and measure  

the results.

Repeat the loop.

By using the metrics-driven development process you improve the mental  

model of the code so that you can make better decisions. Adopting MDD  

allows you to monitor metrics for current problems, aggregate them for  

historical perspective, and ultimately use our improved mental model to  

generate more business value.