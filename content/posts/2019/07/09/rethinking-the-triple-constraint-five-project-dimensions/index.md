---
title: 'Rethinking the Triple Constraint: Five Project Dimensions'
date: '2019-07-09T22:09:20-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/swlh/rethinking-the-triple-constraint-five-project-dimensions-b3593c364b11
---

[Rethinking the Triple Constraint: Five Project Dimensions](https://medium.com/swlh/rethinking-the-triple-constraint-five-project-dimensions-b3593c364b11)  



![](https://i2.wp.com/miro.medium.com/fit/c/96/96/0*7tQd-o9lPrOLXofG.jpg?w=607&ssl=1)![](https://i2.wp.com/miro.medium.com/fit/c/96/96/0*7tQd-o9lPrOLXofG.jpg?w=607&ssl=1)
Karl Wiegers in The Startup
Jun 14 · 11 min read



![](https://i0.wp.com/miro.medium.com/max/60/1*cFvJ78tiri8mWC7qSYGZKg.jpeg?w=607&ssl=1)![](https://i0.wp.com/miro.medium.com/max/60/1*cFvJ78tiri8mWC7qSYGZKg.jpeg?w=607&ssl=1)

![](https://i1.wp.com/miro.medium.com/max/1740/1*cFvJ78tiri8mWC7qSYGZKg.jpeg?w=607&ssl=1)![](https://i1.wp.com/miro.medium.com/max/1740/1*cFvJ78tiri8mWC7qSYGZKg.jpeg?w=607&ssl=1)


Perhaps you’ve seen a sign at an auto repair shop that asked, “What do you want: good, fast, or cheap? Pick two.” While humorous, the sign is also wise: it acknowledges the reality of trade-offs. You generally cannot optimize every desired outcome of a given situation.

The notion of such a “triple constraint” or “iron triangle” appears throughout project management. The problem is that I have seen numerous representations of the triangle with various parameters on the triangle’s vertices — size, cost, time, or scope — and various assumptions made about what is being held constant, such as quality or functionality. I’ve also seen diagrams that show four project dimensions. So, in my view, the traditional “triple constraint” is wrong, although the concept of constraints and trade-offs is certainly valid.

# The Five Dimensions

I think in terms of five dimensions we have to manage on a software project (Figure 1, adapted from [*Creating a Software Engineering Culture*](https://www.amazon.com/exec/obidos/ASIN/0932633331/processimpact/102-2637384-1916904)). First, of course, there are the features (aka scope), which itemize the product’s functional capabilities. But it’s important to distinguish quality from scope. I can write software very fast if it doesn’t have to work correctly. The other three dimensions are the time we have available before delivery (schedule), the budget for the project (cost), and the staff available to work on the project.

![](https://i0.wp.com/miro.medium.com/max/60/1*h6CEbznd9f4c8KfrFe3qSQ.jpeg?w=607&ssl=1)![](https://i0.wp.com/miro.medium.com/max/60/1*h6CEbznd9f4c8KfrFe3qSQ.jpeg?w=607&ssl=1)

![](https://i0.wp.com/miro.medium.com/max/906/1*h6CEbznd9f4c8KfrFe3qSQ.jpeg?w=607&ssl=1)![](https://i0.wp.com/miro.medium.com/max/906/1*h6CEbznd9f4c8KfrFe3qSQ.jpeg?w=607&ssl=1)


Figure 1. The five dimensions of a software project.

I don’t lump staff and budget together and call the combination “resources” as is sometimes done. Most of the project cost is indeed staff salaries. I’ve seen situations, though, where a team had adequate funding but were not able to hire additional staff. In this case, perhaps the project manager can use the available money in different ways, such as outsourcing some work, buying automated test tools, or bringing in contractors.

For each project, we need to decide which dimensions are most critical and how to balance the others so we can achieve the key project objectives. The trade-offs among these five dimensions are not simple or linear. For example, if you add staff, the schedule might be shortened (although not necessarily) and the cost could well increase. A common, but unfortunate, trade-off is to shorten the schedule or add features while sacrificing quality. Anyone who has been the victim of buggy software questions these kinds of trade-off decisions, but they do take place.

Each of these five dimensions can take one of three roles on any given project: a *constraint*, a *driver*, or a *degree of freedom*. Constraints define restrictions within which the project manager must operate. The project manager has no flexibility around a constraint dimension. If a team of immutably fixed size is assigned to a project, staff becomes a constraint. Cost is a constraint on a project being done under a fixed-price contract (at least from the client’s perspective). Quality will be a constraint for a project that develops software for a medical device or an airplane’s avionics system. Y2K projects were schedule-constrained.

A driver is a key objective or success criterion for the project. For a product with a desired marketing window of opportunity, schedule is a driver. Commercial desktop applications often have features as a driver. The project manager has a little flexibility around the drivers. A specified feature set might be the primary driver of the project, but features are a constraint if the feature set is not negotiable.

Any project dimension that is neither a driver nor a constraint is a degree of freedom. This is a factor that the project manager can adjust within certain limits. The manager’s challenge, then, is to adjust the degrees of freedom to make the project succeed in meeting its success drivers within the limits imposed by the constraints. Suppose that on some corporate information system project the drivers are features and quality and staff is a constraint, so the degrees of freedom become schedule and cost. The implication for this profile is that the features demanded by the customers will all be included, but the delivery time for the product may be later than desirable and the project might cost more than planned.

Here’s a little safety tip: all five dimensions can’t be constraints and they can’t all be drivers! Something has to give to be able to meet the key objectives. If the project is over-constrained, with no degrees of freedom, then you will almost certainly fail. The first added requirement, the first team member who gets the flu, the first risk that materializes will trash the schedule because the project manager has no flexibility to respond to these changes. A student in a project management class I taught once said, “Our project has a fixed budget, we can’t add any people, all of the features are critical, there can’t be any defects, and we have to finish on time.” That project wasn’t likely to succeed.

# Negotiating Priorities

An important aspect of this model is not which of the five dimensions turn out to be drivers or constraints on any given project, but that the relative priorities of the dimensions be negotiated in advance by the project team, the customers, and management. This negotiation process helps to define the rules and bounds of the project. For instance, schedule is often presented as a constraint when in fact it is a driver. The way to tell the difference is to ask, “Okay, you want this delivered on June 30. What happens if it’s not delivered until, say, July 14?” If the answer is to forget the whole thing because it won’t be useful to us or we’ll be socked with penalties from the government or our client then, yes, schedule truly is a constraint. But if the answer is, “Well, we’d sure like it by June 30, but we’ll live if it’s not available for two more weeks,” then schedule is a driver. If there is some flexibility around a dimension, then it is not a constraint. A little bit of flexibility makes it a driver, and a lot of flexibility makes it a degree of freedom.

Let me illustrate how this five-dimension idea works in practice. Once I heard a discussion between a senior manager and a project manager about a new project. The senior manager asked, “How long will this take?” The project manager replied, “Two years.” “That’s too long,” said the senior manager. “I need it in six months.” So what did the project manager say? He said, “Okay.”

Now what changed in those few seconds? Nothing! The project didn’t shrink by a factor of four, the team didn’t get four times bigger, and the team didn’t magically become four times as productive. The project manager simply said what the senior manager wanted to hear. (The project took more than two years to complete, incidentally.)

What are some other ways the project manager could have responded instead of simply saying okay? Let’s look at the five dimensions. Maybe he could have asked what portion of the product absolutely must be available within six months. That is, can we cut back on the features intended for the initial release? The project manager could question the schedule, asking, “What’s so vital about six months?” Perhaps this system is replacing a legacy system that runs on an antique computer and they’re removing that computer from the building in six months. Okay, that’s a good reason. Or maybe there’s nothing magic about six months, but we understand there’s a strong desire to get the system operational quickly. In that case the target date of six months is a driver, not a constraint.

You can continue this analysis down the list of the five attributes.Can I get more people or more money? Does the software have to work? Some organizations deliver *something* on the scheduled release date, but it is severely crippled in functionality and full of bugs. Nonetheless, they declare victory and claim they shipped on schedule, even if what they shipped wasn’t useful. It’s just a little game they play. Contemplating these five dimensions is a better way to understand your project priorities instead of just assuming that every aspect of the project is both critical and nonnegotiable.

# Flexibility Diagrams

A visual way to depict the degree of flexibility is with a Kiviat diagram, also called a radar chart or a spider chart (Figure 2). In a Kiviat diagram, you show the five dimensions around a circle and draw a separate axis for each dimension coming out from a common origin point in the center. All the axes are the same length and they are normalized to the same scale. Each axis represents how much flexibility the project manager has in the corresponding dimension, so I call these pictures “flexibility diagrams.” I use a relative scale from zero to ten for flexibility. Zero is not shown at the exact center of the origin just for convenience in drawing the plot.

![](https://i0.wp.com/miro.medium.com/max/60/1*a53J8d340b7P4JHWzSdyOQ.jpeg?w=607&ssl=1)![](https://i0.wp.com/miro.medium.com/max/60/1*a53J8d340b7P4JHWzSdyOQ.jpeg?w=607&ssl=1)

![]()


Figure 2. Flexibility diagram for a corporate information system.

Plotting a point at zero indicates that the dimension for that axis is a constraint with no flexibility. If you plot a point fairly low on the axis, between zero and two or thereabouts, that represents a driver. It shows that the project manager has a small amount of flexibility in that dimension. Any dimension plotted at a higher level on its axis represents a degree of freedom having more latitude for adjustment. If you connect the five points for the five dimensions that you plotted, you get an irregularly shaped pentagon that visualizes one profile of the project’s characteristics.

Figure 2 shows the flexibility diagram for an information system my team once developed. This project had a fixed team size, so the value plotted on the staff axis is zero: a constraint. The project was aiming for a desired, but not critical, delivery date, so the point on the schedule axis also has a low value. The project had varying amounts of flexibility around the features that would be incorporated into the initial release, the product quality, and the latitude for cost overruns. Therefore, the values for these degrees of freedom are plotted higher on their axes.

Note that this is not a high-resolution or quantitative tool. We’re not going to calculate the area of the pentagon or anything like that. But the size of the pentagon does provide a rough indication of how much flexibility the project manager has to work with. If the pentagon is small, that means that you have numerous constraints or drivers, which will make it more difficult for the project manager to steer a path to success.

Different types of projects will lead to flexibility diagrams having very different shapes. Figure 3 illustrates a flexibility diagram for a project for which quality is a driver and the schedule shows the greatest latitude. This is what you might see for a product intended for use in a higher-risk environment. Note that this diagram does not show any constraints; none of the axes are plotted at the zero value. That’s fine. In contrast, the profile for a commercial software product in a highly competitive environment might look like Figure 4, in which a specified feature set must be included (a constraint), the schedule is constrained to a specified ship date, and the quality is just whatever it turns out to be.

![](https://i1.wp.com/miro.medium.com/max/60/1*7wiGXbzcGNifwLzG3_9mSA.jpeg?w=607&ssl=1)![](https://i1.wp.com/miro.medium.com/max/60/1*7wiGXbzcGNifwLzG3_9mSA.jpeg?w=607&ssl=1)

![]()


Figure 3. Flexibility diagram for a quality driven application.

![](https://i1.wp.com/miro.medium.com/max/60/1*CqxXI1FkrobqGyNBbandxQ.jpeg?w=607&ssl=1)![](https://i1.wp.com/miro.medium.com/max/60/1*CqxXI1FkrobqGyNBbandxQ.jpeg?w=607&ssl=1)

![]()


Figure 4. Flexibility diagram for a competitive commercial application.

The shapes of the pentagons in these examples visually indicate the important aspects of each project. If you push the point on one of the axes inward to reduce the amount of latitude the project manager has in one dimension, you’ll generally have to adjust the other dimensions to compensate. You can use this sort of analysis to make management aware of the trade-offs and decisions they must make to meet a project’s key objectives, and to negotiate realistically achievable commitments on each project.

# Flexibility Table

You can also document your project priorities in the form of a flexibility table, as illustrated in Figure 5. This example is simplified just to provide a flavor of how this works. For each project constraint, state the limits the project manager must work within. For each success driver, described the goal you’re intending to achieve. For each degree of freedom, describe the tolerance or latitude that the project manager has available.

![](https://i0.wp.com/miro.medium.com/max/60/1*tCCF10dvcr9HBR1VMUK63Q.png?w=607&ssl=1)![](https://i0.wp.com/miro.medium.com/max/60/1*tCCF10dvcr9HBR1VMUK63Q.png?w=607&ssl=1)

![]()


Figure 5. Sample flexibility table.

The table in Figure 5 is for the project whose flexibility diagram appears in Figure 2. Recall that staff was a constraint. We had just five full-time team members available for the duration of this project. Schedule was a driver. We wanted the first release delivered within four to five months, but there was no fixed delivery date. The other three dimensions had more flexibility. Because the project was essential, the project manager could overrun the initial budget by a reasonable margin before anyone would get upset. We did have a core set of high priority features that we needed to have delivered in the first release, but other than that, we could defer some requirements if necessary.

Note that each of the five dimensions takes on only one characteristic. For example, schedule is either a constraint, a driver, or a degree of freedom, not two of these or all three. You wouldn’t have entries for the same dimension in more than one column in a flexibility table.

# Applying the Five Dimensions

The point of this analysis is to help the project manager make decisions as to how to respond to changing conditions or realities on the project. You can use the five-dimension model to renegotiate when the world changes. Suppose staff is constrained. If new requirements come along that simply *must* be included, the only parameters that can change are quality, cost, or schedule. Nothing is free. Ask management which dimensions to adjust to accommodate this request. The specific answer is less important than the discussion that is triggered when project managers react to unexpected changes in any of these five dimensions. Customers and managers have to understand the impact of such changes on the other project dimensions so they can make the right decisions.

One characteristic of a healthy software engineering culture is that project expectations and commitments are established through negotiation. To avoid unpleasant surprises late in a project’s life cycle, the stakeholders all have to understand and agree on their objectives and priorities. Not everyone might be happy with the outcome of the negotiations, but people can commit to realistic schedules and deliverables only if all the parameters are discussed honestly. A group with a culture in which people are afraid to say no or to discuss problem areas openly will always fall short of expectations. Tools like the flexibility diagram can facilitate these frank, and often difficult, negotiations.