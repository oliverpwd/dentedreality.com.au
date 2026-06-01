---
title: The Alternative to Performance Reviews for Software Engineers
date: '2023-02-23T19:47:15-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://maruz.medium.com/the-alternative-to-performance-reviews-for-software-engineers-7b6d1c9537dd
---

[The Alternative to Performance Reviews for Software Engineers](https://maruz.medium.com/the-alternative-to-performance-reviews-for-software-engineers-7b6d1c9537dd)  



## Learning and development reviews


![]()

Photo by [Glenn Carstens-Peters](https://unsplash.com/@glenncarstenspeters?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

```
Table of Contents  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```
# Introduction

With the increasing reliance on software in every aspect of our lives, using management techniques from traditional industries in software engineering teams has gained momentum.

One practice that has recently seen widespread adoption is using performance measurements. Despite the promises made by such methodologies, many leaders are still struggling in their quest to measure the performance of their engineering teams: at the beginning, the adoption of such systems seems to bring a performance improvement, but shortly after, it becomes clear these improvements don’t translate into increased customer value.

One particular use of performance measurements is to assess and evaluate the performance of individual engineers. Many engineers are now familiar with the concept of performance reviews, but in case you want to refresh your knowledge, Gergely Orosz has published an excellent piece on how the [performance review process](https://newsletter.pragmaticengineer.com/p/performance-calibrations) works at large tech companies.

Performance reviews are so widespread that a world without them seems inconceivable. Nonetheless, many people are familiar with or have experienced the shortcomings of traditional performance measurement systems, yet they bear with it, either because it seems no alternative exists or because they think things will get better if the current system is improved.

But as with anything in business and management, performance reviews are just a tool introduced to solve a problem. We should look for alternatives when the tool is not only not beneficial but harmful.

In this article, I would like to show that:

* In software engineering, performance measurement systems are naturally bound to introduce dysfunctions due to the inability to observe performance across all critical dimensions
* Any organization that uses measurement-driven performance assessments is at a greater risk of destroying customer value
* An alternative, optimal system can be built based on intrinsic motivation

# Why Do We Measure Performance?

Companies that use performance assessments usually do it to incentivise engineers to spend more effort in achieving the company’s goals. The basic assumption of this model is that if the increased effort can be directed towards predetermined targets, more value will be produced.

Companies try to introduce explicit measures of performance to objectively assess the performance of engineers, reduce bias, and increase consistency. In a measurement-based performance assessment system, the performance of a software engineer is assessed against a finite set of dimensions, each with its own set of measurements. Based on the output of the measurements, the engineer is given a rank, which typically corresponds to a bonus.

While this looks like a good system on paper — the more value you produce, the better the reward — the reality is that such a system introduces distortions that can subvert the goal of the system itself: the organisation ends up performing worse than it would without the system being in place.

Before looking into why this happens, it is worth providing a brief summary of the typical dysfunctions we observe when introducing performance measurement systems.

# The Dysfunctions of Measuring Performance

Anyone who has been part of companies with measurement-based performance assessments is familiar with the following dysfunctions introduced by the system:

* undermining teamwork
* attention to individual performance rather than the system performance
* focus on quantity more than quality
* outdated performance standards
* inaccuracy of measurements
* play-it-safe mindset
* constant dissatisfaction
* limiting pride in the work

Let’s look at each of them.

**Undermining teamwork.** When assessing the performance of an individual contributor, we need to extract the individual’s specific contributions from the team’s total outcome, while making sure we don’t attribute to them something to which they did not contribute. This is easier said than done for two reasons:

1. This assumes all effort is observable and the manager has perfect knowledge of which factors contribute to which outcomes. In practice, a lot of the production activity is mostly mental, or it happens in the interactions between people, both of which are difficult to observe and measure. Moreover, most of the time, it’s difficult to be certain about the link between inputs (such as effort) and outputs (such as outcomes)
2. The number of people contributing to an outcome is bigger than we think. In many cases, when someone is making an extraordinary contribution to a project, they neglect some other aspects of the job that someone else is picking up. How do we evaluate the second person’s contributions to the project? For example, imagine the case where an individual contributor A needs to focus on a project, and coworker B decides to pick their on-call duties so A can focus on the project. A’s project becomes very successful, but B’s effort made it possible. How much should B be rewarded?

Since performance assessments are based on individual performance, individuals are often faced with the choice of doing what is best for their own salary or rewards versus attending to the team’s needs. In most cases, what will happen is that the needs of the team get sacrificed.

**Attention to individual performance rather than the system performance.** The system in which work happens plays a bigger role in the performance of an individual contributor than the individual contributor themselves. To improve their own performance, the individual contributor is faced with three potential options:

a. Improve the system

b. Make the numbers look better

c. Game the system

Improving the system is the best option from a customer’s point of view since it improves not only the individual’s performance but also the performance of everybody else. But it is also a daunting task, often requiring cross-functional collaboration and work across several layers of management.

The other two options are cheaper, and while they don’t deliver any value to the customer — on the contrary, they can destroy value — they can result in a better performance assessment.

It is easy to understand why, most of the time, people will go with one of the last two options.

**Focus on quantity more than quality.** Quantity and quality are usually two of the most common aspects of work that companies try to measure. But while quantity is easier to measure — there is always something that you can count at any stage of your production process — quality is more difficult to assess, as in knowledge work, the production activity is largely mental, hence difficult to observe. This difference usually pushes people to maximise their efforts in the dimension that can be easily measured and lower their focus on the dimension that can’t be easily measured.

**Outdated performance standards.** To assess individuals, an organisation must first set the standards against which people will be evaluated. These standards can be explicitly set. For example, there is a document describing what the employee is expected to achieve by the end of the performance cycle — or implicitly set — individuals learn what the company expects them to do by looking at what gets rewarded.

In both cases, these standards are deeply rooted in the past: they describe what the company thinks it will need in the upcoming cycle or what has been rewarded in the past. As such, they limit the ability of individuals to react to opportunities and do what is best for the customer when new circumstances arise. We know that conditions constantly change in today’s business climate, and the ability to catch up with changing conditions is a competitive advantage.

**Inaccuracy of measurements.** In classical engineering control theory, one can design a controller that monitors the controlled process, compares it with a specific set point, and implements an algorithm that, through the application of system inputs, can drive the system to a desired state, achieving some degrees of optimality. While it is tempting to think we can apply the same theory to control an engineering team, a small difference makes it impossible to guarantee the accuracy of a measurement system.

When we apply measurement systems to a system that consists of people, we must consider that the control system’s components have a self-interested behaviour. In other terms, people tend to react to a measurement system when they know about it.

The purpose of a measurement system is to close the gap between the measured performance and the desired target. If the people who are under the measurement system know about that, it is a rational behaviour to subvert the system to ensure the system measures no gap. In complex systems like product development, individuals can control the flow of information, and it is easy to conceal measures that will put their own or their team’s performance under the spotlight. It is also easy to make the numbers look better without this corresponding to increased customer value.

**Play-it-safe mindset.** If people’s pay depends on meeting or achieving some standards, it is a corollary that people will try to set these standards to make them achievable in the context of the system they work within and their current capabilities.

There is a lot of rhetoric on setting ambitious goals, or things like “if you are achieving more than 70% of your OKRs, you have not been ambitious enough,” but the truth is that it’s very difficult to ascertain how much ambitious a goal is, and people setting the goals can always find a way to depict their goals as more challenging or more ambitious than what they really are. The cumulative result is that the whole organisation starts to target easy or achievable goals, and the hard targets that would likely result in a miss are seldom set.

**Constant dissatisfaction.** Because of human nature, the majority of people who go through performance assessments experience a state of dissatisfaction with the system. Consider, for example, the following scenarios:

* You are rated in the top 50% of the company, but someone else is rated in the top 20%
* You are rated in the top 20%, but someone else is rated in the top 10%
* You are rated in the top 20%, but last year you were rated in the top 5%

When this happens, people can react in several different ways that can destroy the value of the organisation. For example, they can become cynical and distrust the system. Or they can start having doubts about themselves and start lowering their own expectations. Even the people who get the best ratings are not immune from these effects and might develop imposter syndrome. For example, they can start attributing their good results to luck and start developing a fear that their “true” incompetence will be revealed at some point in the future.

**Limiting pride in the work.** When people are measured and rewarded according to an external system, performance control is removed from the individual contributor to the organisation. This means that the individual contributor is not working anymore according to their own standards and expectations, but they are following someone else’s standards. This, in turn, creates a separation between the individual contributor and their work — it is not theirs anymore; it is not work crafted according to their skills and experience.

Having described the most common dysfunctions, we can now look into why they arise.

# Why Dysfunctions Arise

Robert D. Austin has developed a useful model to describe how motivational measurements affect performance. For anyone interested in a deep dive into his theories, I suggest reading his book “*Measuring and Managing Performance in Organisations*.”

In Austin’s model, the customer and the company would like employees to allocate their effort in a way that maximises the customer value at a cost that allows the company to make a profit. The employee has only a limited capacity for effort, and the employee needs to spend this effort across several activities — for simplicity, we will assume two activities.

The customer will derive some value for each combination of effort spent in each activity. If we connect all the combinations that deliver the same value, we obtain a set of curves called “same-value curves.” Similarly, we can connect all the points where the employee spends the same amount of effort into a set of lines called effort capacity.

The point at which the effort capacity line is tangent to the same value curve represents the preferred allocation: it is the point at which the choice of effort distribution by the employee maximises the customer value. We obtain the best-mix path if we connect all the preferred allocation points. The best-mix path is the set of allocations that, for any given level of effort, maximises the return to the customer.

![]()

Example of a best-mix path based on effort capacity and customer value

The goal of an incentive system is to increase the level of effort spent by the employee and align the effort distribution in a way that maximises value for the customer.

When a company adopts a performance measurement system, its goal is to implement an incentive system defined as Full Supervision.

Full Supervision happens when measuring every dimension critical to the employee’s performance is possible. When this can be done, the employee knows exactly how to allocate their efforts because that combination will give them the highest reward. But while full supervision is very attractive, it is not always possible, and in practice, it’s much rarer than one would think.

When a critical dimension of performance can’t be measured, using a measurement-based performance assessment system will cause the individual to optimise their effort according to the dimensions that can be measured — to the detriment of the dimensions that can’t. This situation is called Partial Supervision.

In the Partial-Supervision scenario, since only some dimensions are observable, the employee is free to decide how much effort to spend on the non-measurable dimensions, while trying to maximise their reward by spending effort on the measured dimensions. The resulting effort allocation is not optimal since the employee can set a target for the non-measurable dimensions that provide less value to the customer.

Dysfunctions arise when a company thinks they are applying full supervision, but in reality, they are in a partial supervision situation.

![]()

Partial-supervision scenario

Let’s look at what happens in the picture above, where the horizontal axis represents an activity that is measured, and the vertical axis one that can’t. Initially, the employee might allocate their effort while staying on the best-mix path (Point P1). But under the pressure of the measurement system, the employee will start to spend more time on Activity 1. Initially, this is still advantageous for the company, as the employee will increase their total effort in both activities (P2), but at some point, the employee realises that they can get better rewards by focusing only on Activity 1 (P3).

The company is still getting some value from the employee’s work, but not as much as they could. But if left unchecked, the pressure of the performance measurement system can lead to a situation when the employee is optimising completely for their own reward (P4) and not delivering any value. In this situation, the choices made by the employee — the choice path — is not aligned with the best-mix path.

Many people have seen this happening. Let’s say the company adopts a performance assessment system where engineers are evaluated according to lines of code (LOC) written, number of tasks closed, and production incidents caused. Everybody who has been doing this job for a couple of years knows that these are hardly the right things to measure, but they are among the easiest.

Let’s suppose that the company recognises the importance of other activities but chooses not to measure them because the cost would be too high — for example, time spent helping other engineers ramp up.

Under these assumptions, the system predicts that the engineer will keep increasing their level of effort in those dimensions that can be measured and will spend less on those that can’t be measured. By the end of the performance cycle, we can expect that:

* individuals will write lots of Lines of Code without any guarantee about their quality or whether those lines are needed
* a lot of tasks will be created and closed
* there will be a tendency to hide production incidents for fear of impacting the individual’s metrics
* spending time helping others is going to be discouraged

If the current way we do performance reviews introduces such distortions, how can we do better?

# Moving Beyond Measurement-Based Performance Reviews

To answer this question, we need to remind ourselves what the true purpose of a performance assessment system is. The true purpose of a performance assessment system is to align the effort spent by employees in a direction that achieves the goals of the organisation, which in turn translates to improving one of the key measures of organisational performance — most of the time, profit.

Full Supervision and Partial Supervision are two control mechanisms that an organisation can implement based on the ability to observe performance in all or part of the critical dimensions. Dysfunctions arise when we believe we have achieved Full Supervision, but in reality, we can only achieve Partial Supervision because some aspects of performance are not easily measured.

If Full Supervision is not achievable, we must ask ourselves a simple question: what happens if we remove all kinds of measurements? This scenario is called No Supervision.

## What happens when there is no supervision?

In a No-Supervision scenario, the employee decides how to spend their effort based on their total effort capacity and the mix that optimise customer’s value.

If we make the following assumptions:

1. The employee knows what the customer wants. In other terms, it is possible to know the value that the customer places on each allocation of efforts by the employee
2. The employee gains utility from satisfying the customer’s needs

Then it is possible to demonstrate that the resulting effort allocation lies on the best-mix path, which means that for a given level of effort, the choice delivers maximum value to the customer.

![]()

No-Supervision Scenario

Initially, the employee will start spending some effort and benefit from satisfying the customer’s needs (point P0). If the utility gained is greater than the disutility gained by spending effort, the employee will accept that the move is good.

But shortly after, the employee recognises that by spending the same effort, they can achieve more customer value by rebalancing their effort allocation (point P1). At this point, the employee can keep increasing their effort and the utility they gain from satisfying the customer’s needs until they reach a point (P5). At this point, further increasing effort would create more disutility from the total effort expenditure than utility from satisfying customers’ needs. This is the optimal allocation in the No-Supervision scenario.

If we compare these results with the ones achieved by partial supervision, it’s easy to see that no supervision can achieve the same results as full supervision, and it actually produces better results than partial supervision. As the employee increases their effort capacity, they reach a higher same-value line in a no-supervision scenario than in a partial-supervision scenario.

![]()

Comparing No Supervision and Partial Supervision

It is becoming clear now that we can build an alternative to measuring-driven approaches based on the No-Supervision scenario. But before proceeding, we must look again at this model’s assumptions.

## The assumptions underlying the no-supervision scenario

The model we have just described is predicated on two assumptions:

1. The employee knows what the customer wants. In other terms, it is possible to know the value that the customer places on each allocation of efforts by the employee
2. The employee gains utility from satisfying the customer’s needs

In a system based on No Supervision, the employee is motivated by the desire to do a good job, learn and grow as an individual, and do something that matters. This is what we call intrinsic motivation. Intrinsic motivation is defined as motivation that is driven by internal rewards.

On the contrary, supervised systems like the ones discussed in the previous paragraph rely on the use of extrinsic motivation: employees are rewarded for achieving and exceeding targets of organisational performance. Extrinsic motivation is defined as motivation that occurs when external influences drive an individual.

This means that it is possible to build a high-performing organisation by not having any measurements at all if we build an environment where employees are motivated by the desire to do a good job, and know what a good job looks like from a customer’s point of view. How can we build such an environment, and what do performance reviews look like in it?

## Building an environment that fosters intrinsic motivation

There are many excellent books you can have a look at to learn how to build such a system. The top three books I would suggest are:

* *Turning the Ship Around* by David L. Marquet
* *Drive: The Surprising Truth About What Motivates* *Us* by Daniel H. Pink
* *Empowered* by Marty Cagan

The key principles of building a system based on intrinsic motivation are the following:

* Hire for intrinsic motivation
* Focus on excellence
* Develop customer empathy
* Promote trust

**Hire for intrinsic motivation**. Not everybody is motivated by the desire to do a good job, grow in the process, and work well with others, which is fine. But for the success of this system, the people you hire must be driven by intrinsic motivation. If your interview process already has a behavioural interview step, it is possible to enhance it with some questions that probe for examples from the candidate’s experience of the following:

* Achieving results through collaboration with other people on the team
* Recognising gaps in their own performance and making improvements
* Taking action based on feedback
* Going the extra mile to make a customer happy

Based on the type of answers the candidate provides, you can assess whether they are internally or externally motivated and only move to the next step, candidates you believe will be successful in this environment.

Focus on Excellence. It is important that the team is proud of what they are delivering and they feel encouraged to aim higher. To do this, you need to create a culture where the team continually pursues excellence in what they do. There are many ways a team can manifest excellence, but the important thing is that every time you see it, you should recognise it and celebrate it.

**Develop Customer Empathy**. To align the intrinsic motivation of the individual contributor with what the customer needs, it is important to ensure that engineers are connected with customers, understand their needs and wants, and know the impact of their decisions on customer satisfaction. One way to do this is by fostering customer empathy. Many techniques can be used to develop customer empathy. Some of my favourites include the [Follow Me Home](https://blogs.intuit.com/2021/01/21/why-every-company-should-be-doing-a-follow-me-home/) technique developed by Intuit or [Everyone on Support](https://basecamp.com/handbook/10-our-rituals#everyone-on-support-eos) by 37 Signals.

**Promote trust**. Trust is a sort of buzzword, and especially in the current economic climate, it is difficult to foster a trusted relationship between companies and employees. From my point of view, trust means respect. You can demonstrate respect and build trust in many ways, and you need to pay attention to all these key moments to ensure you are increasing trust instead of diminishing it. For example, one way to show trust is to accept that people will make mistakes from time to time and convey the message that it’s OK as long as we learn from them.

# The Alternative to Performance Reviews: Learning and Development Reviews

So far, we have described how you can create an environment based on fostering intrinsic motivation, but we haven’t addressed the role that performance reviews play in it. If you want to build a performance management system based on intrinsic motivation, you can replace traditional performance reviews with a learning and development review.

A learning and development review focuses on helping the individual on their path to mastery. It is not tied to any incentives or bonuses but provides feedback to help the individual improve and grow. What does it look like?

Let’s take a step back and look at product development as a learning problem.

A product’s job is to satisfy a customer’s needs in a way that works for the business. If we look at this problem through the lenses of continuous learning, achieving this objective requires us to answer two fundamental questions:

1. How well are we serving the needs of the customer?
2. Which capabilities do we need to build or improve at the individual and system levels to keep serving their needs?

This means that we can redesign performance reviews around these two questions with the addition of a third one:

3. How well are we cooperating between ourselves in serving the needs of the customer?

Following these principles, a learning and development review can be structured around these five sections:

* Summary of impact: this is a description of the main contributions that the person has made in the past period
* Feedback related to the core competencies: actionable and specific examples related to specific competencies or a rubric
* Contributions to the success of others: how well the individual has contributed to the success of others in the company
* Top strengths: a summary of the top three strengths that the individual has demonstrated in the past period
* Areas of growth: top three areas where the individual can improve and do better
* Looking forward: what the priorities for the individual should be in terms of keeping growing and developing as an engineer

If you are looking for a template, I have put together one [here](https://docs.google.com/document/d/11J8oiCW5Z8kqw5j-oGt1oiUGpMoxQjYJN3R0-0rZ1yE/edit?usp=sharing) that you can use as a starting point.

## What should you watch out for when implementing a system based on intrinsic motivation?

As with traditional measurement-based performance reviews, implementing a system based on intrinsic motivation does not come free or without any risks. Here are the things you should watch out for:

Building an environment where individual contributors feel they can be driven by their skills and experience takes time. While it takes a lot of time to build, it can take a surprisingly short amount of time to destroy it.

This happens because such an environment is based on trust. Every interaction between employees and the organization contributes to that trust, but interactions are not created equal. Initially, it takes a while for a group of people to reach the state of psychological safety that allows trust to be established. Once that state is reached, the team keeps looking for signals that confirm that they are in an environment where they feel safe to take risks and be vulnerable with each other.

As long as the signals keep coming, the team will be in a state of trusting each other. But even a single misstep by a management team member might cause the team to take many steps back. This happens because of the negativity bias, which is the propensity of humans to learn from and use negative information far more than positive information.

Building an environment based on intrinsic motivation requires a high bar for anyone occupying a leadership position, so it is particularly susceptible to the effects of ineffective leadership and people management.

# Common Questions

*Q: How do you do X?*

One of the common questions that people ask when considering moving beyond performance reviews is how the company would achieve X without them, where X can be pay increases, bonuses, promotions, and performance management. The fact that X can take so many values points to the fact that performance reviews are a tool that is overloaded: many different outcomes are driven through it. The generic answer to this question is that you can still do all these things even without doing performance reviews.

*Q: How do you manage performance?*

One of the biggest fear of moving beyond performance reviews is how a company would manage the performance of employees. But in reality, performance reviews are not the best place to address performance issues: addressing performance issues during performance reviews is delegating or postponing a manager’s job.

The fact that something can’t be measured does not mean it can’t be managed. Managers are still accountable for managing the performance of the individuals they support, helping them when there are gaps, and taking action when they can’t be addressed. In this new model, performance management becomes a continuous alignment process between the manager and the individual.

*Q: How do you pay bonuses?*

Many companies that do performance reviews tie bonuses to achieving a specific performance rating: for example, someone meeting expectations gets the standard bonus for their level, while someone exceeding them gets a 15% increase on the standard bonus. Since learning and development reviews don’t assign ratings, how can a company keep paying bonuses?

The short answer is that you don’t need to pay bonuses. Bonuses are part of a system that relies on extrinsic motivation, but if you build your system on intrinsic motivation, bonuses can harm motivation because you are paying a reward to employees for something they could have done just because of internal motivation. If you are not paying bonuses, there are two things you can do instead:

1. Modify your base compensation to match what your peer group is doing in terms of base salary + target bonus. Basically, you consider the bonus already part of the base salary
2. Provide incentives that are not linked to individual performance, but they are the same for every employee. For example:

* You can have a profit-sharing mechanism where employees get a share of profits based on tenure
* You can provide an Employee Stock Purchase Plan where employees can buy shares in the company at a discount

One of the common objections to any incentive system based on tenure is that it encourages people to stick with a company just to reap the benefits of the reward. This behavior is called coasting.

I see two main problems when someone designs a system to discourage coasting:

* You are basically abdicating from your responsibility as a manager. Instead of fostering an environment where people can be driven by their internal motivation and do performance management when goals are not aligned anymore, we create an environment where we make it difficult for people to stay around.   
  Some companies, for example, are known to engineer their compensation package in a way where there is a total compensation cliff after three or four years that forces people to leave unless they have got a promotion
* You are optimizing your system for the small number of people who might coast instead of the majority who want to come to work to do a good job

There is also another aspect to consider — promoting tenure can actually increase the quality of knowledge work. Software engineering takes time: developing domain knowledge, building healthy teams, and understanding the customers’ needs.

# Conclusion

Companies that adopt a high-performance culture mindset have traditionally been employing a pay-for-performance approach to management, which works under the belief that employees can obtain more performance by rewarding them for the extra effort.

In software engineering, this approach will backfire, and instead, it will deteriorate performance. This happens because many dimensions of a software engineer’s job are not observable, and introducing a performance measurement system will force engineers to optimise for the dimensions which can be easily measured, to the detriment of the overall delivery of customer value.

The alternative is to move away from measurement-based performance approaches and build a workplace where employees’ intrinsic motivation can prevail. In such an environment, performance reviews are replaced by learning and development reviews, which focus on helping the employee builds the strengths the company requires to be successful.