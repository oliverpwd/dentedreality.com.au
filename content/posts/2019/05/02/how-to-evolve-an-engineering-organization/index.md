---
title: How to evolve an engineering organization
date: '2019-05-02T14:32:22-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/how-to-evolve-eng-org/
---

[How to evolve an engineering organization](https://lethain.com/how-to-evolve-eng-org/)  



![](https://lethain.com/static/blog/2019/evolve-eng-org.png)![](https://lethain.com/static/blog/2019/evolve-eng-org.png)

Recently, I had the opportunity to present to a group of early-stage  

founders about evolving their engineering organizations.  

While preparing, I realized that despite my excitement for this topic,  

I’ve only written about it indirectly.

The most comprehensive, related piece I’ve written is about running reorganizations.  

Reorgs do involve quite a bit of organizational design, but  

they’re a difficult environment to demonstrate best practice.  

They’re typically implemented in short order and  

heavily constrained by business needs, team health and available leaders.

Good organizational design is a directed evolution that balances  

the pursuit of a clear destination with the willingness to repeatedly  

adjust your path towards that destination.

The algorithm I’ve found effective is:

1. **Measure** what you hope to improve *before* you make changes.
2. **Size** your organization against your peers, goals and performance.
3. **Structure** into teams and groups.
4. **Project** your organization’s future growth.
5. **Rest** between changes to develop mastery.

Org design is a topic where solid fundamentals go surprisingly far, and  

that even the most experienced folks sometimes find difficult.  

This framework isn’t a secret formula for organizational design,  

but it will guide you towards all the right questions, as well as the  

standard answers to those questions.

Not the final word, but a good start.

## Measure

Organizational design isn’t defined by approaching an ideological ideal,  

it’s judged by its effectiveness at solving your current needs.  

Measurement is the underpinning of clearly understanding your reality, and  

is the first step towards good organizational design.

This first step is skipped surprisingly often, to unquantifiable results.  

The biggest reason its skipped is that measuring how well your organization works  

is *exceptionally* difficult.

Some of the measurement approaches that I’ve found effective are:

* **Define goals** with a clear timeframe and target,  
  
  and continue measuring your performance against your goals to  
  
  develop confidence in your forecasting.
* **Identify proxy metrics** that correlate with your goals.  
  
  Accelerate’s definition of productivity is  
  
  a great example of using proxy metrics.
* Measure your **organizational health**, looking at metrics like  
  
  employee referral rates, employee attrition, and team health surveys.
* **Instrument your planning processes** to generate productivity metrics  
  
  perhaps using task or story points velocity.  
  
  While this kind of metric is rarely *precise*, they are often very *useful*.
* **Model** behavior using a systems model, and adjust it parameters  
  
  to refine your intuition on how your current organization works.
* **Create synthetic metrics** that package a variety of signals  
  
  into a structure that you can reason about usefully.

You don’t need to do all of these, just focus on one or two  

that work for you. As your organization grows,  

you’ll incorporate more of these, but there’s no need to go overboard:  

pick a couple, remember to use them, and you’re well on the path to good  

organizational design.

## Size

Once you’re measuring how the current organization,  

the next step is to determine your target organizational size.  

How far to look into the future will depend on your stage, and  

might range from three months for a very small company to  

multiple years for a mature one.

The speed of your hiring funnel determines the start of  

your planning horizon, and the predictability of your  

business determines the horizon’s end.

Once you pick a horizon, say six months, the next comes is to  

calculate your organization’s ending size.

Most companies determine their size by merging momentum and hiring velocity  

into a projection, but that can create an investment interia  

that’s initially quite reasonable and slowly slips into efficiency.

Three more useful sizing strategies are:

* **Benchmarking against similar companies.**  
  
  Talk to five slightly larger companies and build a small dataset  
  
  of how they’ve sized their organization. Every company is different:  
  
  faithfully copying another company’s approach is *cargo-culting*.  
  
  but learning from a handful to identify useful upper and lower bounds  
  
  is *benchmarking*. Benchmarking is a remarkably sound technique to cheaply  
  
  determine the range of reasonable solutions,  
  
  and I’d recommend it as *the* initial approach to solving almost any  
  
  organizational problem, including sizing.
* **Project forward through systems model.**  
  
  Use the same systems modeling techniques you used to measure  
  
  your throughput to project future throughput.  
  
  It’s particularly important to factor in your  
  
  hiring capacity,  
  
  as hiring and training more recruiters usually creates  
  
  resistance towards rapidly accelerating hiring,  
  
  and having hired recruiters creates a similar resistance  
  
  to rapidly decelerating hiring.
* **Forecast backwards from goals and roadmap.**  
  
  Benchmarking and modeling both have a tendency to overfit  
  
  on your current organization, but sometimes you’re looking  
  
  to accomplish something far beyond your current organization’s  
  
  capabilities. In that case, take your future targets and  
  
  reason about what you’d need to accomplish those, very  
  
  studiously ignoring your current configuration.  
  
  For example, you might do this purely from a financial projections  
  
  perspective, then reason about the kinds and quantities of products  
  
  or businesses your company would need to met those, and further from  
  
  those products to a company size.

Each approach exposing different gaps in your projections,  

which makes your estimates the most powerful when you apply all three together.  

Once you’ve satisfied the three perspectives, it’s time to convert  

your size into a structure.

## Structure

An organization’s size is just a number, its structure is how  

the pieces fit together and accomplish useful things.

### Organizational atoms

Even the most complex organizations are composed from a handful  

of simple *organizational atoms*.  

The three organizational atoms I build with are:

1. **Teams** are groups of six to eight engineers with one engineering manager,  
   
   with a shared purpose, a shared oncall, and who work together closely.
2. Each team is composed of one or two **workstreams**, which represent their ability  
   
   to parallelize project execution. Generally I’ve found workstreams of three to four engineers work  
   
   best, with smaller workstreams often representing a failure to limit work-in-progress.
3. Every five teams is then collected into a **group**, which are a composition of related teams  
   
   that work on adjacent work. Each group is managed by a group engineering manager, who supports the  
   
   managers on the teams within their group.
4. Beyond this point, recursively collect every five groups into another container,  
   
   the next of which you might call a *pillar*, an *organization* or whatnot.  
   
   Each container has an engineering manager, who supports the managers within their container.

You can mostly ignore workstreams during the organizational design phase,  

as they are more relevant during roadmap and sprint planning.  

I debated if they’re worth mentioning here at all, and decided that they *are* worth introducing  

because they address the primary concerns with establishing such “large” teams of  

six to eight. Namely that you need to focus on more projects than you have properly sized teams,  

which often pulls folks towards smaller teams: just add workstreams to a proper teams instead.

### From atoms to structure

Converting your size into your structure is then a simple process:

```
teams  = size   / 8
groups = teams  / 5
org    = groups / 5
# and so on

```

For example, imagine you have sixty engineers:

```
size   = 60
teams  = 60  / 8 # 7.5 teams
groups = 7.5 / 5 # 1.5 groups
orgs   = 1.5 / 5 # 0.3 orgs

```

Starting with the largest containers first, ususally organizations,  

recursively balance the areas of responsibility across the containers.

You need one organizations, let’s call it the *engineering* organization.  

Then you need two groups, perhaps you’d start with the classic *product* and  

*infrastructure* split. Then each of those groups needs four teams, which you’d  

split according to your needs.

Of course , the tree doesn’t have to be perfectly at all times, and most  

companies start out weighted towards product engineering.

It’s tempting to invest very, very heavily into exactly how these groups  

are defined, but it’s my experience that it’s easy to overoptimize these decisions.  

There is no one *right way* to divide groups, but there are a handful of  

useful rules you can use to identify reasonable structures.

Some rules of thumb to consider while you’re identifying scope for groups and teams are:

1. **[Conway’s law](https://en.wikipedia.org/wiki/Conway%27s_law)** argues that organizations  
   
   create products that reflect their own structure. Use this to your advantage,  
   
   shaping your structure to reflect the products you want to create.
2. **Minimize cross-team coordination**, including the predictability tax,  
   
   by making teams as self-contained as possible.  
   
   Teams should depend on as few other teams as possible to accomplish their goals.  
   
   This is also true recursively for groups, organizations, and so forth.
3. A **short escalation path** allows you to quickly resolve conflict. This is accomplished  
   
   by grouping dependent teams as closely together as possible, and by keeping your org tree  
   
   somewhat balanced, in particular avoiding long, skinny reporting chains.
4. **Structure according to company needs**, not overfitting on individual preference.  
   
   Some companies heavily incoporate senior leaders’ areas of interest into their organizational  
   
   structure, and this approach accumulates organizational design constraints over time.

You can go surprisingly far with the above atoms and rules for structuring organizations.

*More structuring tips in Rules of thumb for org design.*

## Project

Now that you’ve design your organization for the next year or so,  

it’s surprisingly powerful to extend your planning horizon a bit further.  

If you just sized and structured for six months, and  

then take a stab at projecting out to twelve and eighteen months.

The further out you project, the less accurate your projects, so  

the goal for these additional attempts at sizing is to perform  

a rough sort of *sensitivity analysis* to identify breaking points when your  

organization will have to undergo major transitions.

Typically these transitions are adding additional layers of management,  

which in balanced engineering organizations will occur roughly at 40 engineers,  

200 engineers, and further entries in the sequence of `8 * 5^N`.

If your projections cross any of those thresholds, then know that you’ll  

need to invest disproportionally more time during that period on coaching your team,  

redesigning your process and potentially hiring experienced external leaders.

*More on adding practices in Best practices on org best practices.*

## Rest

At this point you’ve finished your organizational design, and there  

is only one commandment left to master: *stop making organizational changes*.  

Although these changes feel useful, productivity always occurs *between*  

organizational change, not during it.

It’s only after you stop making changes that folks begin to practice working  

in the new structure, slowly building mastery in the new paths of production.  

The time to acclimitize increases as an organization grows, with small teams  

tolerating a couple of changes each year, and larger organizations sometimes  

requiring *years* of stability to rebuild momentum.

As a rule of thumb, if you haven’t been able to update your measurements  

before you’ve proposed a new update, then you’re changing too frequently.  

Learning takes time, but it’s the only way to consistently improve an organization.

If there is a core belief in my approach to management, it’s that quality management decisions  

exert a subtle, enduring and ultimately defining influence on company health and  

company outcomes. Following a structured, deliberate approach  

to sizing and structuring your engineering organization doesn’t require  

unique insight, is learnable, and *it works*: give it a try.