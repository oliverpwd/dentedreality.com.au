---
title: How Big Technical Changes Happen at Slack
date: '2021-02-07T11:51:35-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://slack.engineering/how-big-technical-changes-happen-at-slack/
---

[How Big Technical Changes Happen at Slack](https://slack.engineering/how-big-technical-changes-happen-at-slack/)  



Most new things in technology turn out to be fads: patterns of talking and doing that come and go without leaving a permanent mark. Microkernels; EPIC architectures like IA-64; object request brokers; and 1990s’-style neural nets are gone, and will not return. Sorry for the deep throwbacks; only time proves which things are fads, so for uncontroversial examples we have to reach pretty far back.

While it is hard to imagine today — at their height — all of these defunct technologies were wildly popular, with charismatic, sincere, and smart advocates. They were supported by plausible first-principles arguments that showed why their chosen tech would inevitably triumph. The fads spawned movements, manifestos, conferences, and companies. To be clear, these fads are not to be confused with deliberate frauds, which are much more rare. The motivations behind these technologies were heartfelt. Things just turned out differently, despite all available appearances at the time.

On the other hand, a crucial few new techniques are revolutions: potent, enduring changes that confer long-term advantages to their adopters. Object-oriented programming, hardware virtualization, the world wide web, public cloud, CI/CD, and 2010s-style neural nets (reborn as deep learning) are now permanent parts of the world of computing that were once indistinguishable from fads. We are, already, surrounded by concrete technical successes that we did not know how to achieve before these things came along.

Like all technology companies, **Slack wants to make sure we catch revolutions at the right time, while limiting the energy we spend chasing fads**. What strategy can we follow to ensure this? This post outlines our approach to this problem, which we continue to refine and apply through our practice at Slack.

## Telling Fads and Revolutions Apart

We can’t rely on individual leaders’ intuitions to pick winners; both [precision and recall](https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c) will be too low. Instead we strive to actively **invest in exploring new things**, knowing that most of these investments will return nothing. To bias our investment towards useful new things and away from fads, **we are ruthless in killing experiments early** that do not prove valuable. We hope to try a little bit of everything, accepting that this means dabbling with a lot of fads; and we hope to end up riding some waves all the way to shore because our experiences with them keep providing positive returns.

## The Adoption Curve

This is enough philosophy to build a minimal, descriptive model of our adoption of new technology.

![](https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/7/0_P2aekLXnaC1BU2rD.png)![](https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/7/0_P2aekLXnaC1BU2rD.png)

This curve is a typical [sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) describing technology adoption over time. The S shape comes from changes in the rate of adoption. At first, when only a few experimenters are playing around, we have no choice but to adopt it **slowly**; later on, as it becomes clear what the benefits are, more hands pitch in to capture those benefits, and we **quickly** adopt the new technology into production use cases during the steeply upward-sloping section in the middle. As the majority of fruitful use cases get eaten up, fewer cases are left, and the ones that remain are the tough ones, so adoption **slows down** again towards the end of the cycle.

Let’s demarcate these three phases:

![](https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/7/0_mEs4AGmX4A0Mp3sW.png)![](https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/7/0_mEs4AGmX4A0Mp3sW.png)

We’re not the first to observe that technology adoption follows this sigmoid pattern. Everett Rogers proposed this model in his “[diffusion of innovation](https://books.google.ca/books?id=9U1K5LjUOwEC&redir_esc=y)” theory in 1962. Rogers wasn’t describing Erlang or MongoDB; he was a rural sociologist observing patterns in the adoption of farming techniques. It turns out computing practice is not so different from other fields of human activity.

To ground this abstract view in something more concrete, let’s consider some of the technologies that have traversed the phases of Exploration, Expansion, and Migration at Slack.

### React

The [React library](https://reactjs.org/) has swept frontend development since its first stable release in 2015. Its utilization of the virtual DOM for rendering elements and its approach to unidirectional data flow made it a compelling technology for Slack’s desktop UI.

* In 2016, React was an alien technology to Slack’s frontend codebase. In **Phase 1,** engineers who were curious about React started playing around with it, initially on pilot projects. When they were convinced there was something important for Slack, they constructed a more persuasive demo, [rebuilding our emoji picker](https://slack.engineering/rebuilding-slacks-emoji-picker-in-react) in React. This very familiar (and formerly sluggish) piece of Slack UI was clearly much better in React. The functional prototype did much more to win converts than any first principles argument or whiteboard sketch could have done.
* As our team grappled with the fact that React was going to have a major impact on our codebase, it became clear that doing piecemeal, view-by-view work would leave much of the developer ergonomics and performance benefits of React unrealized. However, a big-bang rewrite was out of the question–the risk vs. reward calculus didn’t favor it and the timeline commitment was too great. As React entered **Phase 2,** a real migration project with a plan and significant staffing began to roll. As views were created and modified, many teams opted into the new style. However, during this intermediate phase many older views still persisted, and needed maintenance.
* In **Phase 3**, we finished the job, mopping up the long tail of legacy views in the client codebase. We finally [shipped a React-only version of Slack on desktop](https://slack.engineering/rebuilding-slack-on-the-desktop) in July of 2019.

![](https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/7/0_k73Ju9ied__bPj4C.png)![](https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/7/0_k73Ju9ied__bPj4C.png)

### Hacklang

Server-side, we’ve been [migrating from PHP to Hack since 2016](https://slack.engineering/taking-php-seriously). A key part of that migration has been a gradual introduction of [types](https://docs.hhvm.com/hack/types/introduction) to our PHP code:

* In 2017 we entered **Phase 1,** when some local Typing Enthusiasts began dusting the codebase with obvious-and-easy types.
* Some folks saw bugs caught by these early types before hitting production, and started using types as well. This plunged Hacklang types, somewhat unintentionally, into **Phase 2** (other people are affected). The new type annotations also caused some problems along with the bugs they were catching, and [a canonical static vs. dynamic typing debate](https://martinfowler.com/bliki/DynamicTyping.html) unfolded and ran its course. Through debates and accumulating experience, a rough consensus emerged that increasing type coverage would do more good than harm, and a majority of teams elected to use types**.** After an initial wave of easy type coverage, later on in Phase 2, we made more ambitious efforts to migrate to typed code; began putting systems in place to make it more likely for new code to be statically typed; and did a lot of communicating and evangelizing types to the backend community at large.
* This left the Hard Parts of the codebase for **Phase 3**. Rationalizing Slack’s own internal object variants (for varieties of channels) and converting some complex core modules has proven time-consuming.

### Vitess

[Vitess](https://vitess.io/) is a database clustering system for horizontal scaling of MySQL that we have [turned to as we evolve our data sharding strategy](https://www.cncf.io/case-study/slack/).

* **Phase 1** began when we started critically examining the capabilities of Vitess. We spent a lot of time manually managing our homegrown sharding solution, and Vitess seemed to automate most of our pain points. The nascent Vitess team eventually became convinced that this technology was a winner.
* The initial work to move some low-risk production workloads, like RSS feeds, to Vitess began **Phase 2.** This early Phase 2 work involved very few people outside the Vitess team, but required operational support and situational awareness of the presence of a new data storage system. As we moved more and more tables over, slowly at first, we slowly de-risked and debugged Vitess for our intended use case; developed tools for doing backfills; came to share a vocabulary for doing migrations (like “dark-reads” of duplicated data) and the kinds of problems that can emerge; and all of these practices made each new table a little easier than the ones before…
* …until they weren’t. Today, we’ve migrated hundreds of tables totaling more than 50% of our query workload, but are still working through some “Hard Tables”, and the “Long Tail of Weird Tables” in **Phase 3**. Some of the most critical tables to the application have also evolved complicated dependencies and query patterns that make them harder to move than the ones we got good at migrating in Phase 2. Separately, we have a long tail of tables that are just not worth manual table-by-table engineering and so we are developing other tools for faster bulk migrations.

### LibSlack

In contrast to these technologies that have graduated through the phases of adoption, [our cross-platform C++ client library](https://slack.engineering/libslack-the-c-library-at-the-foundation-of-our-client-application-architecture) did not move beyond Phase 2, and was eventually discontinued.

* In **Phase 1**, LibSlack engineers proved out the concept of a shared client library for business logic and data caching by building User and Presence implementations. Additionally, the logistics of compiling and shipping a cross-platform library were fleshed out in depth.
* However, the project did not gain traction in **Phase 2**. Technical and strategic incompatibilities between the library and our Desktop client became evident. The re-implementation of existing logic and caches in our iOS and Android client with the LibSlack library proved cumbersome. Simultaneously, Slack had one fewer client codebase to maintain as Windows phone was discontinued.

In the end, the runway to a full migration never appeared. [We took what we learned from the LibSlack effort](https://slack.engineering/client-consistency-at-slack-beyond-libslack) and applied it to our mobile and desktop clients in various valuable ways. The code artifact did not achieve enduring adoption but the project informed how we build our clients and organize our engineering teams.

## Navigating This Curve

**Note that these phases are a descriptive model, not prescriptive.** We’re not forcing adoption to follow this sigmoid curve; it just naturally must, no matter how we wish things were. There is no way for early exploration to proceed as quickly as midlife adoption, and there is no way for the final push to get to full adoption to go as quickly as the middle phase went. The three phases are not consequences of any milestones, processes, tools, or people at Slack. They are part of the fabric of technical change, and they would be there whether we noticed them or not.

But now we’ve noticed them, and we can use them to make our efforts more successful. The tactics and strategy for each phase are different.

### Phase 1: Exploration

Phase 1 is frictionless to enter. When an engineer first starts messing around with a technology they’re excited about, **no permission-granting process or ceremony is needed**. It probably happens dozens of times a day at Slack: someone reads about or invents something new, and commences fiddling around with it. Perhaps they have read a blog post about [Elixir](https://elixir-lang.org/getting-started/introduction.html), or [Cassandra](http://cassandra.apache.org/), or [WebAssembly](https://webassembly.org/), or [TCR](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864). They download some software, build it, poke around a little, work through some introductory material, and maybe take a stab at applying it to their day job.

**Most exploration efforts sputter out here**. This is good! Giving up here is one of the important ways we resist spending too much energy on fads. However, some things do make it out into our real workflows and codebases. Sometimes, an engineer can just apply this solution in place, because it solves a problem local to their team’s work. Sometimes, though, the situation is even more exciting: this new widget is useful for an entire class of problems that other teams face. Our intrepid engineer now believes they know something consequential that the rest of us in Slack Engineering do not: that there is a better way for us to do things. **Once work starts to affect others’ work**, you’ve entered Phase 2.

### Phase 2: Expansion

Let’s take a moment to pity the poor engineer entering Phase 2! For they are now trying to modify other engineers’ behavior. This is going to involve communication, persuasion, and — if it is going at all right — substantial technical work. For most projects, Phase 2 is the most difficult, time-consuming, and discouraging phase. It is the “[product-market fit](https://link.medium.com/cdlBfnncc1)” phase of the technology cycle, and many of the projects that enter it will not successfully complete it.

**At Slack, client teams are free to choose not to depend on your system,** with few exceptions. This may surprise you if you have a lot of experience at an “infrastructure-driven” engineering company. At some companies, leaders pick winners and losers before the product-market fit negotiation at Phase 2 has reached its conclusion. The goal of having a winner selected before it has been widely deployed is to provide clarity (“What does the future hold? Which system should I build on?”) and to economize on the expensive period in Phase 2 where more than one way of doing things needs to be supported.

While those are reasonable goals, it is not how Slack chooses to approach the adoption of new systems. We prioritize fad-resilience over speed of adoption. And so, we (intentionally) place the burden of getting other teams to adopt new technology mostly on the change agent. While this can be frustrating for the advocate of a new system, we know of no better substitute. Clearing this hurdle forces selection of Stuff that Works. If the new thing really is as wonderful as we hope it is, it should help the teams that depend on it get things done; this success can move them to adopt it and advocate it.

Some of the work of Phase 2 is fundamentally more like product work than like what-you-might-think-is-engineering. You need to do **user research** to figure out what problems matter. You need to **communicate** the value of your solution relative to previous practices, in ways your users are prepared to hear. You need to **build** things that close the gap between current practice and the change you’re making, to grease the skids for your busy and distracted clients.

Successful execution in Phase 2 eventually leads to some **self-propelled adoption**, where people you did not explicitly sell on the new tech are freely choosing to use it. The end of Phase 2 is close at hand when the new system is a de facto standard, the default practice for new projects. It is unusual to accidentally achieve this kind of adoption. **It’s really hard**, and draws on skills that are not part of every engineer’s professional experience.

### Phase 3: Migration

The self-propelled adoption phase eventually starts to taper off. We are left with a residue of holdouts: use cases that seem especially resistant to the new way of doing things. Some systems that have been quietly working in the background are especially unmotivated to change just because they are not being actively developed. In some cases we are discovering late in the game some ways in which the previous system really worked better. Finally, there are always a few stubborn users who are overly invested in their muscle memory of the old way.

While we’ve been talking about “the” technology adoption curve, there is actually a fork in the road at Phase 3. **Even very successful projects might not migrate every last use case** to the new way of doing things. For instance, at Slack we have very widely adopted gRPC as an internal API technology. It is solidly in late Phase 3. However, we are unlikely to build a new version of memcached that uses gRPC; memcached’s custom protocol works well, and is well-supported in the clients we care about. The existence of exceptions like this doesn’t make gRPC adoption a failure.

In other cases, the costs of having More Than One Way (cognitive burden on engineers; operational burden from running the Olde Systeme) are high enough that we will migrate everything to the new way. For such projects, we need a plan to tackle the hold-outs. [Different tactics are appropriate for different obstacles](https://lethain.com/migrations/). The systems that just haven’t changed in a long time might need the change agent to adopt them and start moving them into the future. If the holdouts are functionally motivated, by real capabilities the new system lacks, you may need to enhance the new system, or wrap it in code that emulates the old system’s capabilities.

In the occasional case of emotional attachment to the old system, person-to-person outreach is usually a lot more effective than public, high-stakes debate. And please be gentle; your beautiful, new system will be the Old Way some day, too — if it is successful enough to live that long.

## Expectations of Technologists

OK, that is a lot of description. What about prescriptions? What do we expect of one another as engineers and engineering leaders at Slack to smooth our progress?

1. First, **we should explore some**. It is a big world out there. We must occasionally poke our heads up and see what is going on. Obviously no one can explore everything, and no one can explore all the time. We have our external commitments and internal roadmaps and so forth. Those things still come first in an industrial setting. But some non-trivial portion of our energy should take the form of exploring new things.
2. We need to **be a reasonable customer** of other teams’ technology. The teams that support us in lower layers of the stack need to move their systems into the future, too, and this will sometimes impose costs on the above layers. When the costs are unreasonable, or when it moves in a direction that is contrary to your team’s needs, you need to communicate this in a way that the teams supporting you can understand.
3. We sometimes need to **break dependencies** on downstack technologies that are not suited to our needs. This is part of the responsibility to set technical direction for our team. This does not necessarily mean the downstack team is doing anything wrong, and we need to handle this dependency-breaking in a mature and professional way.
4. When we are trying to drive change, we do so with a **customer-centric attitude** towards the teams trying to understand and use a new system. Their happiness is the only real barometer of your success. This involves outreach, requirements gathering, feedback, iteration, and purposeful education and skill-sharing.

When in doubt, remember: you’re accountable for your team’s technical success, and your team’s technical success is–in the long run–judged by the people using your stuff.

Want to help us catch the next revolution and eliminate some fads along the way? [We’re hiring](https://slack.com/careers/location/all-locations/dept/engineering).