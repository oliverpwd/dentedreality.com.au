---
title: Independence, Autonomy, and Too Many Small Teams
date: '2020-09-04T17:55:32-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://kislayverma.com/organizations/independence-autonomy-and-too-many-small-teams/
---

[Independence, Autonomy, and Too Many Small Teams](https://kislayverma.com/organizations/independence-autonomy-and-too-many-small-teams/)  



“The two pizza team” paradigm has become really popular in the context of organizing software teams. The idea is to have small, self-reliant teams working independently to solve problems. The “two-pizza” refers to the guidance to keep the team small enough that we need not order more than two pizzas to feed them.

![](https://kislayverma.com/wp-content/uploads/2020/07/dev-prod-with-team-size-1024x701.jpg)![](https://kislayverma.com/wp-content/uploads/2020/07/dev-prod-with-team-size-1024x701.jpg)

These teams are all around us today, but we are not seeing the kind of productivity or shipping velocity that we expected to see. Most developers, especially in larger organizations, complain about meetings, the burden of communication, the slow pace of change etc. Startups often sell themselves to potential candidates by touting their agility. But why should larger companies be slow if everyone is using the same “empowered team”/”autonomous team” model for organizing themselves?

I argue that **we have lost the original intent of the “two pizza teams”** (aka autonomous teams). The way we are organizing and scaling teams as companies grow larger is exactly opposite to the spirit of the idea, and this is making the already difficult problem of keeping teams motivated and agile even more difficult.

### **Why two pizza teams**

The concept of the “two pizza”/”autonomous” team arose from attempts to minimize communication between multiple teams and empowering a single team to be in complete control of delivering customer value.

Before this idea gained popularity, the most common way of organizing teams was in terms of Backend, UI, DBA, Ops etc.. Building any feature required a lot of communication, collaboration, and alignment between all these groups.

The notion of a small team which had all the skills required to solve a single specific problem was intended to solve this problem. A single team would be given the entirety of the problem statement and the tools it needed to solve it. This would ideally remove the problem of aligning multiple teams around shared roadmaps and delivery schedules and allow the team to own the problem solving process end-to-end.

There are two core concepts underlying the two-pizza team – **mission** and **independence**. Ideally, end-to-end means all the way to the customer or the business. Hence, **every autonomous team is expected to generate direct business value all by itself**, without a lot of overlap with other teams. Additionally, **the team should be able to meets its goals independently** (i.e. without reliance on or interference from other teams) This reduces the cross team communication overhead because its members have all the skills needed to solve the problem.

### What went wrong

Somewhere along the line, we forgot about “reducing communication” just started fixating on assigning independent teams to problem statements that were essentially tiny slices of business problems. As the problem space gets more finely sliced in hopes of achieving scale at each step, so does the number of teams. e.g. What might have been a “Data Delivery Team” charged with delivering fresh data to customers unfortunately becomes “Data ingestion Team”, “Data processing Team” and “Data Release Team” (real world example).

This causes problems with both the core tenets of the autonomous team philosophy.

![](https://kislayverma.com/wp-content/uploads/2020/07/narrow-missions-1024x809.jpg)![](https://kislayverma.com/wp-content/uploads/2020/07/narrow-missions-1024x809.jpg)

The **mission is diluted because most of the teams are now working on problems which are subsets of the original problem and as such not valuable in themselves**. The success of a team can no longer guarantee the improvement of at least one business metric. The team’s work is not tied to a business objective any longer, so it gets tied to tightly defined execution scopes.”Data ingestion team” is supposed to pull in data, that’s it. While the team is still allowed to do this however it wants, succeeding in its objective will not mean that fresh data is being delivered to the customer.

Autonomy is diluted as a direct fallout. **Where a single team could have come together to solve problems of data delivery, now multiple teams with different managers and different roadmaps must come together to deliver anything to the customer**. This creates exactly the kind of coordination overhead that these small teams were created to solve in the first place.

**Coordination, also known as alignment, communication, shared roadmap, Gantt chart and many other positive sounding names, is the arch-enemy of the autonomous team**.

We have lots of small teams with lots of independence and no direct impact that keeping everyone pointed in one direction has become a nightmare. Program Managers paper over the ever-increasing complexity involved in coordinating priorities, efforts, and timelines, with developers and managers increasingly wash their hands of the whole business of communicating with other teams.

We took a good idea too far. The current “small” team is certainly small, but we forgot the part about reducing communication. Instead we are now offered “small, highly collaborative” teams as some sort of new ideal, as if high collaboration is something to be desired during execution.

This is a huge blind spot for organizations. The implicit goodness of small teams (devoid of any of the original context) is now internalized to such an extent that deep collaboration between small teams is considered a good thing in the organization. Team productivity and motivation keeps falling even as their sizes increase. And somehow we still believe this way of organizing work among teams is efficient, and something else must be causing the diminishing productivity.

### Collaboration is not good

Collaboration is a great idea during ideation and brainstorming. It helps in getting a lot of input from lots of different people and can help us discover new aspects which we may not consider ourselves. It can expose other approaches to solving the problem, or even some versions of this problem that have already been solved by others. **Broad stroked collaboration between people and systems is how we build something that is greater than the sum of its parts.**

However, **once we reach the execution phase, collaboration is extremely costly.** Collaboration means that two people or teams cannot just focus on doing their jobs, they also have to worry about when the other person is going to finish theirs and how they are going to synchronize with each other to hit the finish line.

![](https://kislayverma.com/wp-content/uploads/2020/07/org-prod-with-team-count-1024x801.jpg)![](https://kislayverma.com/wp-content/uploads/2020/07/org-prod-with-team-count-1024x801.jpg)

I can quote any number of engineering principles to refute the deification of collaborative teams which seems to be the norm today.

In general, it is assumed that multithreading improves the performance of a system. This is completely true if each thread can execute completely independently on its own core without talking to any other thread or sharing any data. However, the moment we end with some shared state or more threads than CPUs, the synchronization overhead can quickly outstrip all the performance gains from using the technique.

[Amdahl’s law](https://en.wikipedia.org/wiki/Amdahl%27s_law) puts a finite upper limit on the increased output when an extra worker is added into the mix. The well-known problem is that every extra worker imposes non-parallelizable, exponentially increasing communication overhead. At some point, adding another worker makes things worse rather than better.

“*9 developers cannot finish a 9 month project in one month*” is a well-known idea in software management. And yet we see managers trying to grow and manage their teams in isolation. Why is that?

My hypothesis is that we see individual teams delivering quickly and we interpret this to mean that adding more members to these teams will further scale the output. In a world where we examine teams by isolating them from the overall system context, it is very easy to confuse independent with autonomous.

### Independence is not Autonomy

In a highly collaborative setup, the correct way of looking at the organization is like a factory floor. **[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints#:~:text=The%20theory%20of%20constraints%20(TOC)%20is%20an%20overall%20management%20philosophy,Critical%20Chain%2C%20published%20in%201997.)** tells us that the only way to increase output in this situation is to broaden the bottlenecks and widen the entire “flow of work” from conception to final delivery to the customer.

![](https://kislayverma.com/wp-content/uploads/2020/07/sequential-teams-1024x349.jpg)![](https://kislayverma.com/wp-content/uploads/2020/07/sequential-teams-1024x349.jpg)

But when we look at each step individually and out of context of the rest of the “pipeline”, “delivery” takes on a very different meaning. It just means “out of my door”. Any attempts to improve output with such a perspective will only create local maxima which means nothing for the final output – it might even be detrimental.

This is where we end up with too many small teams which are only looking at their little slice of work. That is what they are incentivised to do. If the outputs of our teams are arranged sequentially, they are not autonomous in delivery, no matter how independent they might be in their day to day work.

Anyone who has managed a supply chain can tell, independent teams organized in a sequential manner MANDATE a lot of communication and feedback. The lines of communication have not been removed by the creating small teams – they have been multiplied manifold. What’s worse, communication is happening at team boundaries where it is actually the weakest (the [communication overhead in microservices](https://kislayverma.com/programming/overcoming-io-overhead-in-micro-services/) springs to mind readily).

![](https://kislayverma.com/wp-content/uploads/2020/07/too-many-small-teams-1024x742.jpg)![](https://kislayverma.com/wp-content/uploads/2020/07/too-many-small-teams-1024x742.jpg)

Without an autonomous mission, independent teams are forever shackled by the communication overhead.

### **Autonom****y** **is a customer facing construct**

What happens if we organize our independent teams by problem statement rather than function? A team that is authorized to solve a customer problem using any means at its disposal in essence owns the entire “pipeline” of tasks that need to be done. There is no cross-team collaboration and communication required for this team to do its job. This team not only operates independently, it also delivers value to the customer independently.

**A team is autonomous when it “delivers value to the customer” independently**. In his novel “[Goal](https://www.amazon.in/gp/product/8185984565?ie=UTF8&tag=kislayverma-21&camp=3638&linkCode=xm2&creativeASIN=8185984565)“, Eliyahu M. Goldratt highlights this beautifully by having his protagonist (who is plant manager) define his success to mean increased sales. Sales is usually not the problem of the manufacturing team, but the novel highlights how defining a customer facing “global” goal transforms the poorly performing plant.

Scaling this team will directly add more business value because the new resources will be (should be?) deployed in the most optimum way within the team’s pipeline. This is no different from the previous situation of task owners creating local maxima, but because the team owns the final customer problem, even a local maximum is a win for the customer.

This is what the original “two-pizza” team was intended to do. Not merely to execute independently, but to deliver customer value independently. **The core idea behind autonomy is not arranging teams to maximize outputs of steps in the value chain, but defining value chains in such a way that a single, tight-knit team can be unleashed upon it**. Every team has to define its output in terms of customer success because that’s how the organizational boundary is drawn.

### Scaling an autonomous team

The problem of scaling teams applies recursively, no matter the paradigm we choose to apply. Let’s say we have autonomous teams and all that, now how do we scale their output to achieve ever larger objectives?

This is a central problem faced by large organizations. In the early days of a company, domain experts emerge and lead small teams that solve specific customer problems. Since the size of the company is small, having direct customer impact is typically not difficult.

However, as the organization grows large in scope, size and ambition, each little team is now expected to deliver more and more. This typically means growing team sizes by adding more members. Then each team starts internally splitting into separate sub-teams, and we are back to independent teams rather than autonomous teams.

How can we scale our teams to deliver on more and more ambitious goals while retaining their autonomous nature? I will offer some opinions on this in the next post.

Read Next : How to use [Agile for more than just great execution](https://kislayverma.com/agile/agile-for-innovation-going-beyond-execution-excellence/)