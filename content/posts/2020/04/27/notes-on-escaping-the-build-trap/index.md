---
title: Notes on Escaping the Build Trap
date: '2020-04-27T19:36:20-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/notes-escaping-the-build-trap/
---

[Notes on Escaping the Build Trap](https://lethain.com/notes-escaping-the-build-trap/)  



![](https://lethain.com/static/blog/2019/build-trap.png)![](https://lethain.com/static/blog/2019/build-trap.png)

Last year while thinking about [product management in infrastructure](https://lethain.com/product-management-infra-engineering/)  

I read Cagan’s [Inspired: How to Create Products Customers Love](https://www.amazon.com/Inspired-Create-Products-Customers-Love/dp/0981690408),  

which I thought was a solid book, roughly summarized as “use rapid experimentation to guide product innovation.”

It’s apparently the time of year when I read about product management, and having heard quite a bit of praise for  

[Melissa Perri](https://twitter.com/lissijean)‘s  

[Escaping the Build Trap](https://www.amazon.com/dp/B07K3QBWG1/), I decided  

to give it a read and write up [book notes](https://lethain.com/tags/book/).

These are some core quotes from the book, along with my reflections.

> When companies do not understand their customers’ or users’ problems well, they cannot possibly define value for them. Instead of doing the work to learn this information about cutomers, they create a proxy that is easy to measure. “Value” becomes the quantity of features that are delivered, and, as a result, the number of features shipped becomes the primary metric of success.

Proxy goals are essential for most teams, but strongly agreed that many teams have the wrong proxy goals.  

[Measuring stuff](https://lethain.com/goals-and-baselines/) is [very hard](https://lethain.com/metrics-for-the-unmeasurable/).  

I’ve definitely experienced teams that start measuring before they understand their users needs,  

and that often leads to tears.

The second bit, where teams subjugate critical thinking to goals, is *extremely* dangerous,  

and is a frequent challenge when companies attempt the transition to results oriented management.

> Product managers are rewarded for writing long specification documents or, in an Agile world, creating extensive backlogs. The team is rewarded for shipping massive quantities of features. This way of thinking is detrimental yet pervasive.

This quote describes a common anti-pattern where folks are measured on process outputs  

rather than business outputs. This is very, very common, mostly because (as Perri discusses in many places in this book)  

companies tend to *actually* operate in a waterfall development cycle.

> For example, many companies follow such a rigid development process and cadence that there is no opportunity to experiment. Whenever I start a new training or workshop, I say to product managers, “Raise your hand if you went back and iterated on the last thing you shipped.” Normally, 15–20% of the people raise their hands. My next question is, “How do you know that what you shipped was successful?” The answers here usually revolve around meeting a deadline and finishing with bug-free code.

Evaluation, control and predictability are these fundamental requirements for operating a large company,  

but none of those forces work well with experimentation. This creates a remarkably toxic loop that I’ve  

seen very, very few companies escape.

> Products , as I said before, are vehicles of value. They deliver value repeatedly to customers and users, without requiring the company to build something new every time. These can be hardware, software, consumer packaged goods, or any other artifacts in which human intervention is not needed to achieve value for the user. Microsoft Excel, baby food, Tinder, the iPhone these are all products. Services , unlike products, use human labor to primarily deliver value to the user. Service-based organizations are design agencies that create logos or brands for businesses, or they could be accounting companies where an accountant does your taxes. These services can be “productized,” where they are the same service for the same price for every customer, but they still inherently need people to execute them. They can also be automated for scale, by creating a software product that executes on the service.

This distinction between *products* and *services* is concise and useful. Services depend directly on human labor to deliver value, products do not.

> Companies that optimize their products to achieve value are called product-led organizations. These organizations are characterized by product-driven growth, scaling their organization through software products, and optimizing them until they reach the desired outcomes.

The book then moves into a discussion of different kinds of companies.  

Perri proposes four types of companies: sales-led, visionary-led, technology-led and product-led.

Starting with sales-led, which she describes as:

> They’ll go above and beyond for that client, working closely with them to define the product roadmap, taking all of their requests, and sometimes customizing things especially for them. But this way of working does not scale for long. When you have 50 to 100 customers or more, you cannot build everything uniquely to match the needs of each one, unless you want to be a bespoke agency.

Visionary-led is described as:

> The easiest way to think of a visionary-led company is to consider Apple. Steve Jobs propelled that company forward, creating the product strategy, and got it over the hurdles of failed products to the success it is today. He pushed the boundaries of what was known, and the rest of the company followed.

Technology-led is:

> These companies are driven by the latest and coolest technology. The problem is that they often suffer from a lack of a market-facing, value-led strategy.

Product-led is:

> This brings us back to being a product-led company. Product-led companies optimize for their business outcomes, align their product strategy to these goals, and then prioritize the most effective projects that will help develop those products into sustainable drivers of growth.

Reading these definitions, they all resonated with me, but I do wonder what the  

difference between a “product-led” and “business-led” company is within these definitions.  

Specifically, it seems like “product-led” is equivalent to “valuation-optimizing”, and all  

the others are optimizing irrational things.

For example, this definintion of sales-led optimizes for signed deals, but you can imagine a version  

of sales-driven that optimizes for life-time value and margin, which I think would be a roughly equivalent  

fitness function as described by product-led.

Technology-led is a bit different, and most such companies seem to fall into the trap of being solutions seeking a problem.  

However, reflecting on [Innovator’s Dilemma](https://www.amazon.com/Innovators-Dilemma-Revolutionary-Change-Business/dp/0062060244),  

I suspect many of the most successful companies are the result of exactly that approach.  

(Probably many of the least successful companies as well.)

> Product management is the domain of recognizing and investigating the known unknowns and of reducing the universe around the unknown unknowns.

This is a great definition, particularly the emphasis on *recognizing* “unknown unknowns” and converting them into “known unknowns.”

> Product managers are the key to becoming product-led. Yet so many companies put people without these capabilities into this role.

I’m always wary of any argument which suggests that some approach is the only viable approach.  

In this case, my read is that Perri believes that product management essentially can’t be done  

without product managers, which seems a bit extreme to me. The majority of my work has been in  

environments without product management, although certainly not always, transitioned to being  

product-led in our thinking (even, perhaps especially, on infrastructure teams).

> Product management is a career, not just a role you play on a team.

Sort of same thoughts as above. My experience is that this is a series of skills,  

extraordinarily important skills, but you don’t have to have the title Product Manager  

to develop them.

> If you are lucky enough to be taught product management, what you learn is usually very tactile: writing requirements documents (or user stories in Agile), planning meetings with developers, running check-in meetings, gathering requests from the business team, and testing for acceptance of the developed work and bugs. Many of these steps stem from the work of product managers who operate in a traditional Waterfall environment.

When I wrote the opening of [An Elegant Puzzle](https://lethain.com/elegant-puzzle/), I also wrote about folks not getting much training  

as engineering managers. It’s a shame that our professions are so under-trained.

> Why? Agile does indeed promote a better way of collaboration and a faster method of building software, but it largely ignores how to do effective product management.

Preach! Agile is an project management framework, not a product management framework.

Perri then goes into three archetypes of bad product managers: the mini-ceo, the waiter, and the former project-manager.

The mini-ceo is:

> Product managers are not the mini-CEOs of a product, yet 90% of the job postings I have seen for product managers describe them as being the mini-CEO. CEOs have sole authority over many things. They can fire people. They can change up teams. They can change directions. Product managers, on the other hand, can’t change many of the things a CEO can in an organization.

The waiter is:

> The waiter is a product manager who, at heart, is an order taker. They go to their stakeholders, customers, or managers, ask for what they want, and turn those wants into a list of items to be developed. There is no goal. There is no vision. There is no decision making involved.

The former project-manager:

> Product managers are not project managers, although a little project management is needed to execute on the role correctly. Project managers are responsible for the when . When will a project finish? Is everyone on track? Will we hit our deadline?

Overall, this “bad archetypes” section didn’t quite hit the mark for me,  

at times coming across as slightly dismissive of project management.  

That said, it’s hard to draw distinctions without drawing blood, and I appreciate  

that the goal of the section was to introduce some liveliness.

> The real role of the product manager in the organization is to work with a team to create the right product that balances meeting business needs with solving user problems.

This line resonated quite a bit!

> Great product managers understand that they will get further by taking advantage of the skills and expertise of their team.

I think that most leadership boil down to this definition!

> A frequent question I get is, “What is the difference between UX design and product management?”

This line really surprised me! I never imagined a scenario where it would be ambiguous that these  

are very different functions. Since it’s apparently a common question, it made me appreciate starting  

out at Yahoo! which was large enough to have dismabiguated many such roles.

> This is where people usually become confused between what Agile calls a product owner and a product manager.

I’ve never worked in a formal Agile environment, so I haven’t run into precisely this distinction before,  

but I’ve certainly run into scenarios where a team wasn’t performing their full product management workload  

but in a somewhat subtle way where they felt they were doing the full load and I disagreed but struggled  

to identify the distinction (I’ve started to call the missing bit “problem selection” in my writing).

> Most organizations do not give their people the necessary time to do product vision and research work. They would rather hold them responsible for a steady stream of outputs and measure success based on stacking backlogs and writing stories.

This is, in my opinion, the most important theme of the book, and I’ve found it to be consistently true.  

It makes me wonder what companies actually do this well *at scale* and *while scaling*.

> Scaled Agile Framework (SAFe) teaches this differently, and I think it’s one of the weakest points in the entire framework. In SAFe, product managers are the managers of product owners and are responsible for external-facing interactions and work.

Ah, poor SAFe. I don’t know anyone who likes it.

> I’ve trained dozens of teams who are using SAFe, and I have never seen it work well.

Indeed.

## Career ladder

Perri proposes three kinds of product management work: tactical, strategic and operational.

Tactical:

> Tactical work for a product manager focuses on the shorter-term actions of building features and getting them out the door. It includes the daily activities of breaking down and scoping out work with the developers and designers, in addition to crunching the data to determine what to do next.

Strategic:

> Strategic work is about positioning the product and the company to win in the market and achieve goals. It looks at the future state of the product and the company and what it will take to get there.

Operational:

> Operational work is about tying the strategy back to the tactical work. Here is where product managers create a roadmap that connects the current state of the product to the future state and that aligns the teams around the work.

Then goes in depth into how different points in career progression as a product manager will do different ratios.  

Overall, this section was super reasonable and thoughtful although a bit less relevant to me as someone not focused  

on the product manager ladder specifically.

I did find the section on Chief Product Officers interesting:

> A company should think about adding a CPO when it starts to develop its second product, expands into another geography, or merges with another company. This role is critical to ensure that the entire portfolio is working together to achieve the company goals.

This is an area I’ve been thinking about a lot from the infrastructure perspective,  

where we end up supporting a portfolio of products and platforms built on our platforms,  

and we have to balance investing energy into supporting all of them.

## Organizational structure

The next section goes into structuring teams, which is something I’m quite interested in!

> Companies tend to organize in three main ways: value streams, features, and technical components.

When I [design an org or reorg](https://lethain.com/running-an-engineering-reorg/), I do by best to align  

by value stream, and then bundle technical components into those value streams.  

Working in infrastructure, I think I occupy a different position on the “ensure work is supported long-term versus flexibility to invest” continuum,  

but not *too* far distant from Perri’s.

> When I came in, Marquetly was structured around technical components. “Our Agile coach suggested we put Scrum teams over every area of our product so we have coverage,” said the CTO. Although this makes sense in theory, in practice it helped to promote poor product management.

*Note that Marquetly is the, I think hypothetical, company that the book mentions.*

To the previous quote, I think this is only subtely wrong for infrastructure groups, as I think you should group by value-streams and then  

cluster technology into those value-streams. However, product groups don’t have that luxury, and this is probably  

the right definition between product and infrastructure work:  

*infrastructure engineering consists of areas where technologies can be easily grouped into value-streams*,  

and then product engineering is everything else (with “product infrastructure” being aspects of the former  

that are coupled more heavily to specific products).

> A similar issue happens when teams are organized around specific features. A lot of teams do this to get coverage ownership over every part of the product. Although this is good if you are literally starting from scratch and do not have a product organization set up, but, over time, it promotes a very output-oriented mindset. Instead of working toward a goal and saying no to anything that doesn’t get us there, we tend to look for ways to develop more things related to our little slice of the product.

I don’t feel like I’ve worked anywhere that organized around features,  

but yeah, that sounds very bad.

> One team is focused on retention, another on implementing new currencies, and another on acquiring new users. Each of the teams has ownership of their goal and is judged for success based on their outcomes. They are also allowed to work across all products to do whatever is needed to reach those goals. It takes a huge amount of coordination across the product teams, so everyone is responsible for collaborating intensely with one another. Even though the coordination might seem like a handful, having fewer teams makes them ruthlessly prioritize around the most important initiatives. There’s no useless work.

This sort of approach seems ideal for groups of teams on a single product,  

but I think would require breaking groups of teams into different products and codebases  

to maintain per-developer productivity beyond hundreds of engineers.

> A value stream is all of the activities needed to deliver value to the customer. That includes the processes, from discovering the problem, setting the goals, and conceiving of the idea, to delivering the actual product or service.

Yeah, interesting how product and platforms support different behaviors somewhat.  

That said, also: move responsibilities between teams more!! Teams are so useful when they’re gelled,  

but we keep making the people secondary to the technology or features, which feels like the wrong tradeoff sometimes.

This chapter also goes into designing product organizations, which was eminently reasonable and  

aligns pretty well with [the approach to sizing teams that I’ve written about before](https://lethain.com/sizing-engineering-teams/).

## Strategy

This section reminded me a great deal of [Good Strategy, Bad Strategy](https://lethain.com/good-strategy-bad-strategy/),  

which is one of my favorite books I’ve read in the past few years.

> Gibson Biddle, who was a VP of product at Netflix from 2005 to 2010, talks about aligning his team around a common guideline for evaluating its product strategy. That guideline was to “delight customers, in margin-enhancing, hard-to-copy ways.” He set goals that would accomplish this and would help Netflix execute on the company vision around key initiatives, including personalization, instant access to entertainment, and ease of use.

I love the emphasis on “margin-enhancing, hard-to-copy” as part of the guidelines.  

I think more companies should explicitly emphasize this in their visions/strategy/etc.

> The powerful thing about a strategic framework like the one Netflix uses is that it forces you to think about the whole before zooming in on the details.

This idea of frameworks as forcing you to zoom out is a powerful one that I hadn’t  

really considered before.

> Good strategy isn’t a detailed plan. It’s a framework that helps you make decisions.

Strong agree on usefulness to decision making as the fitness function for strategy.

> Communicating the end state of a product is not inherently wrong. You should be striving toward a vision. However, it becomes dangerous when we commit to these visions and lofty feature sets without validation.

There is an interesting tension between being clear (helping focus) and being wrong (focused on wrong thing),  

that is difficult for strategies to navigate. How do you pick the right company strategy to begin with?

> A good strategy should transcend the iterations of features, focusing more on the higher-level goals and vision. A good strategy should sustain an organization for years. If you are changing strategy yearly or monthly, without good reason from data or the market, you are treating your strategy as a plan rather than as a framework.

Strategy as lasting years is useful recommendation.

> This failure stems from the actions taken to fill the following gaps that exist between outcomes, plans, and actions. These gaps ultimately cause friction within the organization: The Knowledge Gap, The Alignment Gap, The Effects Gap.

Excited to learn about these three ways that management prevents strategy  

from working.

> The Knowledge Gap is the difference between what management would like to know and what the company actually knows.

This is very real. It’s so common (including for me) to reject strategy proposal due to lack of data,  

forcing teams into discovery thrash instead of making progress. Conversely, it’s frequent that I see  

essential data missing from proposals. Aligning early and often on approach has been the most effective  

strategy I’ve found to navigate the Knowledge Gap.

> We also saw this gap surface with the CTO of Marquetly. He demanded that we lay out every single detail of a not-yet-validated product so that he could feel more certain about what we were doing. A deluge of information isn’t always that helpful for upper management. You need to focus on communicating and asking for just enough information to make a decision.

I think the extent of detail to expose upward is very company specific.  

Most places I’ve worked prefer too much detail rather than too little (e.g. “show your work”),  

and elliding data wouldn’t work out well.

> Instead of seeking more detailed information, upper management should be limiting its direction to defining and communicating the strategic intent , or the goals of the business.

This resonates, but again seems inconsistent with all companies I’ve worked at.  

I realize that’s part of Perri’s premise–that most companies are poorly run from a product management perspective–but  

I’ve seen the “wrong” approach work at very rapid scale and at very successful companies.

Maybe the distinction is that I believe most leaders do this not because they want to make the decision themselves,  

but instead because they want to build confidence that the team has been sufficient rigorous in their evaluation.

> The Alignment Gap is the difference between what people do and what management wants them to do, which is to achieve the business goals. Organizations try to fill this gap by providing more detailed instruction; whereas, instead, they should allow each level within the company to define how it will achieve the intent of the next level up.

This is another area where I roughly agree, but disagree a bit in the details.  

My experience is that “failure to delegate” is usually about teams building alignment  

up with their leadership, not about their leadership want to provide instruction.

More thoughts to unpack here at some point, hmm!

> At one company, I walked around asking all of the product managers on the hundred or so teams why they were working on their current project. I then asked their leaders the same question. I got two different answers from these two different levels. They could not connect the activities of the teams back to the outcomes of the companies because leadership had passed down feature requests rather than expected outcomes and goals. As soon as those feature requests were committed, it was nearly impossible to change them because the company expected them to be delivered.

I think many companies get so busy they don’t “have time” to ensure alignment through the layers,  

which leads quite directly to unaligned execution. Likewise, my experience is that few companies can  

distinguish between misalignment due to poor individual performance (by the person being delegated to) and misalignment due to poor direction  

(from the person delegating).

> Instead of sending down mandates, organizations should, instead, turn to aligning every level of the company around the why and should give the next layer down the opportunity to figure out the how and report back.

I do wonder how this works in practice within rapidly changing companies with numerous external stakeholders  

(such as regulators, financial partners, etc). There are certain kinds of companies where the rate of change caused by external  

stakeholders is *extremely high*, and this sort of casual propagation doesn’t seem like it would work in such environments.

> The Effects Gap is the difference between what we expect our actions to achieve and what actually happens. When organizations do not see the results they want, they try to fill this gap by putting more controls in place. However, that is the worst thing you can do in this scenario. Giving individuals and teams the freedom to adjust their actions so that they are in line with their goals is what will truly allow them to achieve results.

Absolutely seen this problem, although still not quite sure how to address in environment with many external stakeholders  

with urgent and frequent change.

> Strategies are interconnecting stories told throughout the organization that explain the objective and outcomes, tailored to a specific time frame. We call this act of communicating and aligning those narratives strategy deployment .

Very few companies are sufficiently deliberate about the stories they tell.  

I’ve been reflecting more recently about how important framing and marketing  

is for successful internal initiatives.

> Strategy deployment is about setting the right level of goals and objectives throughout the organization to narrow the playing field so that teams can act. So, while executives might be looking at a five-year strategy, middle management is thinking in smaller strategies yearly or quarterly bounding the teams in a direction that allows them to make decisions on a monthly or weekly basis.

I’d like to spend some more time this year working on a few experiments with cascading strategies,  

it’s certainly something I’ve spent some time on, but probably not enough.

> In most product organizations, there should be four major levels in strategy deployment: Vision, Strategic intent, Product initiatives, Options.

Roughly this expand as (a) **Vision** is long-term outcome, (b) **Strategic intent** is challenges preventing vision,  

(c) **Product initiative** is the specific approach to those challeneges, and (d) **Options** are initiatives translated to the team level.

In particular, I’ve been thinking about the “Options” category a lot in [recent work to increase program engagement](https://lethain.com/fostering-program-engagement/),  

where initially we sometimes gave folks overly broad goals without guidance on how to accomplish them, and that didn’t work very well.

This goes into the Product Kata which Perri has [written this most excellent post explaining](https://melissaperri.com/blog/2015/07/22/the-product-kata)  

far better than I can repeat here. My only comment is: yes!!!

> If you are a single-product company, like Roku, this is easy because your company vision is very similar, if not the same, as your product vision. If you are a large corporation, like Bank of America, it becomes complex.

I’ve found *very* few good multi-product visions. They seem to fail into abstraction quite quickly.  

Curious if anyone has great examples to the contrary.

> Getting the right level and number of strategic intents is incredibly important. As Marquetly found out before, too many higher-level goals, and you are back to peanut buttering.

Obligatory reference to the Yahoo [Peanut Butter Manifesto](https://www.wsj.com/articles/SB116379821933826657) which is still a gem after all these years.  

[Limiting work-in-progress](https://lethain.com/limiting-wip/) clearly does work, but few companies do it successfully.

## Setting success metrics

This section goes into setting effective goals,  

one of the hardest aspects of shifting from project-orientation to product-orientation.

> Pirate Metrics were created by Dave McClure, founder of 500 Startups, to talk about the life cycle of users through your product. Think of it as a funnel: users finding your product is acquisition ; users having a great first experience is activation ; keeping users returning to your product is called retention ; users recommending others because they love your product is referral ; and, finally, users paying for your product because they see value in it is revenue . Put it all together and you get AARRR Pirate Metrics. Get it?

I haven’t seen this one before, but think it’s quite good.  

Tracking referrals seems like a seriously lagging indicator, but useful.  

(Curious to think about what the internal equivalent of a recommendation is.)

> HEART metrics measure happiness, engagement, adoption, retention, and task success. These are usually used to talk about a specific product or feature. Here, adoption is similar to activation in Pirate Metrics because you are talking about someone using the product for the first time. Retention is the same as in Pirate Metrics.

Likewise, I haven’t seen this one other, but also quite good.

> Whatever your metric, it’s important to have a system of metrics, not just one, to guide product decisions. It’s easy to game one metric when it’s your singular focus.

This is very true, and have the right mesh of metrics is critical, particularly to ensure things  

like security don’t overpower usability and so on.

> I call the system of two metrics that balance out each other mutually destructive pairs , although there can be more than just two.

I’ve mostly heard this described as countervailing metrics, and have likewise found them extremely useful.

## Problem selection and solution exploration

Enjoyed the problem selection and solution exploration chapters a bunch, which aligned a lot with my thoughts [about problem exploration and selection](https://lethain.com/intro-product-management/).

## Product-led organization

> The product-led organization is characterized by a culture that understands and organizes around outcomes over outputs, including a company cadence that revolves around evaluating its strategy in accordance to meeting outcomes. In product-led organizations, people are rewarded for learning and achieving goals.

Yes! Learning and *impact* are huge.

> Management encourages product teams to get close to their customers, and product management is seen as a critical function that furthers the business.

Ah, but still not totally bought into the idea that product management must be its own function  

versus something that many folks in many functions, but agree that teams need to be directly engaging with their users frequently.

## Outcome-Focused Communication

Very good map of how to communicate with stakeholders. Very actionable if this is something you’re currently thinking about.

## Rewards and Incentives

> Rewards and incentives are motivators for the employees of every company. The biggest issue I see with companies trying to transition to becoming product-led is that they don’t evaluate their current reward structures to make sure they incentivize the right behavior.

Incentive design is just so, so hard. I don’t know a single company that  

believes they’ve nailed this. Likewise, I don’t know a single  

good company that isn’t tweaking their approach, so at least the absence of tweaking  

is probably a reliable negative indicator.

## Safety and Learning

> In addition to reward structures that prevent people from innovating, the culture of the organization plays a big part. You might not be judging your teams for success based only on outputs, but they may still not be willing to try new things. Why? There may not be enough safety in the organization to fail and learn.

This is obviously what you want, but how do you measure learning?  

I assume it would be by doing more experiments per time period (e.g. learning to run experiments quickly/cheaply)  

and more successful experiments per time period (not necessarily a higher percentage of successes, but simply more of them,  

I think you’d want to avoid focusing on success rate directly).

## Budgeting

> One of the factors that leads to the output-over-outcome mindset in organizations is the way that they do budgeting. A CTO of a global financial services company once asked me for advice. As he moved up through the ranks in the organization, he realized that many of the issues it faced were a result of the way it was budgeting.

…

> It’s far wiser to look at funding product development like a venture capitalist (VC). Startups must pitch investors on their vision and on the data they collect to prove that the vision will be viable and profitable in the market.

Agreed! The move to regarding my organization’s time as a portfolio to invest  

[has been extremely valuable for me](https://lethain.com/how-to-invest-technical-infrastructure/).

> Product-led companies invest in and budget for work based on their portfolio distribution and the stage of their work. This means allocating the appropriate funds across product lines for things that are known knowns and ready to be built, and it means setting aside money to invest in discovering new opportunities that will propel your business model forward. They then allocate more and more funds to grow the opportunities as they become validated.

I’ve not yet had the chance to work at a company that did *all* of this deliberately,  

but I think most companies have emergent systems for doing parts.  

It’s definitely the correct “rational” way to approach this!

## Final thoughts

Overall, I thought *Escaping the Build Trap* was a strong foundational work on product management,  

and would easily recommend it to someone thinking through their approach to product management.  

I’ve read a handful of similar books, and this was the best overall package so far: clear, actionable and readable.

Even now, pondering if I can kick off a reading circle with folks at work.