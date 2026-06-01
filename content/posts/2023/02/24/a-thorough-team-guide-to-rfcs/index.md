---
title: A Thorough Team Guide to RFCs
date: '2023-02-24T09:37:19-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://buriti.ca/a-thorough-team-guide-to-rfcs-8aa14f8e757c
---

[A Thorough Team Guide to RFCs](https://buriti.ca/a-thorough-team-guide-to-rfcs-8aa14f8e757c)  



![]()

Maximum Sensation by mounir fatmi, on display at the Brooklyn Museum

Early in my management days, I found myself in an unforeseen situation. A new and unexpected frontend framework was added to our early-stage startup stack from one week to another. We were not in production yet, so the thought of maintaining two utterly different parallel client-side stacks this early wasn’t a problem I was anticipating. Opinions about technical decisions replicate almost as fast as frontend frameworks, so as the news spread, so did the backchannel feelings.

A few months later, we introduced the Request for Comments (RFCs) practice as a team’s decision-making tool. Over time, we became more aligned, better informed, and technical decision-making became less painful. Since then, [RFCs have become one of my favorite tools](https://buriti.ca/6-lessons-i-learned-while-implementing-technical-rfcs-as-a-management-tool-34687dbf46cb), and with this guide, you may be able to pilot them with your team as well. Let’s dig in.

# An introduction to RFCs

RFCs are older than the World Wide Web and they also helped build it. RFCs originated as documents meant to facilitate technical decision-making related to the Internet and its infrastructure. To put it simply, RFCs are written proposals that seek feedback and encourage discussion about technical decisions, their tradeoffs, and implications. The IETF (Internet Engineering Task Force maintains [an index of all the RFCs](https://www.rfc-editor.org/rfc-index.html) that have been submitted and discussed since 1969.

Since then, the practice of submitting proposals for discussion has expanded to different open source software projects like [Rust](https://github.com/rust-lang/rfcs), [Ember](https://github.com/emberjs/rfcs), and [React](https://github.com/reactjs/rfcs) as a way to make decisions. Since I have led and built primarily distributed engineering teams, most of my practices are heavily inspired by open source processes like RFCs. If they work for groups of volunteers who have never met each other and help bridge cultural, physical, and temporal gaps, then they may work for my team too.

**Why would you want to consider RFCs?**

Before I tell you the wonders of this process, I’ll highlight that what has worked for me and my teams may not work for you. I’ve tried this process at a few companies and have helped a few more implement it themselves. *There be dragons*, so instead of leading with *the process,* we’ll start with *the outcomes we seek.*

When I build engineering teams that make products, I like giving them autonomy and pushing down decision-making as much as I can. When teams are exposed to the problems and get to own their solutions, we can build an organization that focuses on impact over inputs. I’ve also learned the hard way; for this autonomy to work, the organization needs a technical strategy that guides these decisions, coupled with technical principles that serve as the foundation for tradeoffs. The technical strategy or roadmap depends on your context, so I don’t have any pointers for you. One of my favorite ones is to [choose boring technology](http://boringtechnology.club/) when it comes to principles.

The outcomes we seek with RFCs are better technical decisions. While programming is primarily an individual act, building software is a social exercise, so facilitating decisions between groups has helped me build more effective engineering organizations. When we work as teams, every line of code is a decision we make on behalf of someone else, and keeping different perspectives helps us inform ourselves and ideally make better decisions. For example, code reviews can be a way of asking for feedback on decisions you’ve made on behalf of the group. When this process works well, your peers give you feedback and perspective, you incorporate the relevant parts, and move on. Code reviews can also go terribly wrong, so it’s essential to keep in mind that more input doesn’t necessarily lead to better decisions.

Additionally, the cost of incorporating feedback into technical decisions increases over time. Choosing to migrate to language X when you’re already running Y in production takes more effort than evaluating tradeoffs over a shared document. Writing is a thinking process, and ‘paper’ is less rigid than written code, so technical proposals as a means of drafting technical implementations can lead to better decisions and better outcomes. You can read more about the possible benefits of using RFCs with your [teams in this post.](https://buriti.ca/6-lessons-i-learned-while-implementing-technical-rfcs-as-a-management-tool-34687dbf46cb)

**Why RFCs have worked for me**

It’s important to highlight that RFCs are not a magic bullet, and they won’t solve deep collaborative problems if there is dysfunction. They’re a tool, and like most tools, the way you use them will determine their effectiveness. I believe RFCs have worked for me because of the kind of organizations I like building. These are places where individual contributors of all levels are empowered and encouraged to make impactful decisions while seeking input from across the org. In this environment, balance is critical. RFCs aren’t requests for permission, but they’re also not an invitation to rewrite the world or change someone else’s system. They should follow a product or technology roadmap and enable participation and visibility across the company. If you are building an organization where hierarchy dictates or directs decision-making, RFCs, as described below, may not work for you.

# The lifecycle of an RFC

Like most processes, RFCs are phased and evolve as they move along the way. We’ve mentioned that the key to a successful deployment of this practice is to focus on the outcomes you seek over the process or the tooling. Just remember that your local context will have a considerable impact on RFCs’ effectiveness. By keeping the outcomes insight, you can modify the life cycle accordingly and iterate towards success.

# 🧐 Proposing

The proposal stage is where it all begins. To make your life easier, I’ve open-sourced some templates that you can use and adapt to your own needs.

* [Google Docs RFC Template](https://docs.google.com/document/d/1EM5ORZ8sO-g678jNc2nHMAkGjX5-6DuB6EkhjsNcOXo/edit#)
* [Dropbox Paper RFC Template](https://paper.dropbox.com/doc/RFC-Template-Title--BJJD6B25kkYC_zRXc2q5BxB0Ag-dYS7Oe0SKA0wjqzvuaxsO)
* [Notion RFC Template](https://www.notion.so/buritica/RFC-Template-Title-8df1bd0d24b0440486fe133eecdf4a5e)
* [Markdown RFC Template](https://github.com/buritica/mgt/blob/master/rfc_template.md)

Some considerations on the proposal stage:

* If you’re in a psychologically safe environment, proposals can be drafted in the open without fear of people piling on when potentially risky ideas are being born.
* If you’re not in such an environment, drafting the proposal with a small trusted group and expanding their reach can make it easier to evolve a risky proposal or to shut it down before it cascades into organizational drama.
* Proposals should not be a requirement for prototyping or getting started with an approach, but any code that’s written should consider that feedback may surface unforeseen risks, leading to wasted time.
* Proposals shouldn’t be seen as a request for permission but rather understood as, ‘Here’s the direction we want to go, are we missing something?’
* The sooner proposals get feedback, the faster they can evolve. If you expect very polished documents before they’re open for feedback, you may be adding an unnecessary burden on the software design process.
* There should be a straightforward way of submitting a document as a proposal to keep documents moving forward. It may continue to evolve, but ideally, documents shouldn’t remain as drafts in perpetuity, or it will be unclear when they’re ready for comments beyond the draft phase.
* Consider pairing less-experienced folks with senior or staff level engineers as ‘backers’ so they can provide early feedback and lend their organizational clout.
* You may want to skim or talk through the first few proposals so you can provide ‘air-cover’ and minimize surprises.

# 🤔Commenting or suggesting

As stated in their name, commenting is the entire purpose of Requests For Comments. We write documents so that our peers and team members can provide input from their different perspectives and expertise to drive our collective towards a better decision. Given the poor internet experience with the comment section, I’m tempted to rename RFCs to Request For Suggestions to better communicate this step of the process’s intent.

Comments may be one of the deciding factors when you consider tooling for RFCs. If you use something like Github and send proposals as RFCs, you can have inline threaded discussions. On the other hand, using collaborative documents like Google Docs allow you to suggest changes directly. We discuss tooling in detail later on in the article.

Elements to consider during the commenting phase:

* The commenting period should have limits so that proposals don’t linger forever waiting for comments. RFCs are meant to drive decision-making, not halt it.
* Consider active moderation during the first few RFCs if your teams frequently find themselves in heated discussions. Giving and receiving feedback requires a certain degree of psychological safety, especially when new or risky ideas are being discussed.
* If you want to get ahead of active moderation, encourage your team to read through Amy Ciavolino’s excellent guide to [Mindful Communication in Code Reviews](https://kickstarter.engineering/a-guide-to-mindful-communication-in-code-reviews-48aab5282e5e).
* Comments work best when individuals understand that they’re giving perspective rather than arguments.
* Expect a proposal that will get piled-on and have strategies to reduce its blast radius.
* The first few proposals may be quiet; consider seeding comments or designating people you trust to provide feedback.
* Recognize and highlight excellent commenters and comments so you can steer the culture of RFCs in a positive direction.
* Technical proposals usually have product and business implications; consider inviting people from other functions to provide cross-functional collaboration. On one end, engineers learn to communicate in terms of business impact while the rest of the organization gets access to technical decision-making. If you do this, keep an eye out for the Dunning-Kruger running amuck.
* Comments may be further discussed in a meeting, especially those that need more context. Async communication is good, but the tone doesn’t carry well.

# 🤝Deciding

Effective RFCs are those that facilitate decision-making. Since writing an RFC can be seen as prototyping with prose and code to inform a decision, the document in itself is the decision. Some open source projects implement an approval decision, and I had incorporated these into my original deployment. Since then, I’ve learned that rather than empowering, I was creating a culture where people perceived they had no agency because their decisions had to be approved. While today I consider RFC approvals to be bureaucratic, ownership over the business and technical domain must be clear. I can’t just send an RFC that rewrites someone else’s system just because. If you have a centralized architecture function, you may want to consider approvals, but most of this guide may not apply to you if that’s the case.

Other considerations when it comes to decision making are:

* Instead of an approval step, you may want to consider a stage that resembles ‘merging’ a pull request so that the commenting period concludes and the team understands this proposal has concluded, and the path forward is clear.
* There will come a time where you, or other people with authority, oppose a decision because of increased risk or other factors. For example, when picking a language that isn’t part of the stack yet. Ideally, these discussions happen before a proposal gets to the decision step, but we’re all quite busy these days. Architecture reviews may be a good step to move before rejecting someone’s recommendation, and they’re also an extensive topic worthy of an entire guide themselves.
* Communicating decisions in a digestible format can help keep the rest of the organization informed. Consider an RFC newsletter or digest calling out the key points of each proposal and their state.

# 🗄 Archiving and updating

Once a proposal has lived through its cycle, the natural step is to follow through with the proposed approach. Archiving submissions helps keep a handy record of previous decisions and discussions. Depending on how prolific your team is, you may eventually need a document taxonomy, functional full-text search, or both. Archived documents can be excellent reference material and onboarding literature, as long as they’re well summarized and organized. Another tooling consideration is the ability to archive the body of the comments.

I used to think that previous RFCs should be kept up to date when decisions evolved, but that turned documents into software and created two homes for technical debt. Not the outcome I sought. People should still feel comfortable using archived documents as the foundations for new ones or expanding them through brief extensions. You probably want to consider discussing proposals for significant system changes, but production software and its documentation should be where you concentrate the attention of your updates. Updating proposals is something I haven’t been entirely successful with, so [I’d love to learn](https://twitter.com/buritica) about any approaches that have been successful in this space.

# 🔬Tooling

I left tooling for last because it’s the first thing people always ask about and the one I have the flimsiest responses for. Tooling is relative, flawed, and controversial. In this space, I’m a fan of done over perfect as long as it doesn’t get in the team’s way and the life cycle of RFCs. I won’t tell you what tool to use, but I’ll pose some questions to ponder in your decision-making journey.

* Can you use an existing tool?
* Outside of engineering, who else needs to get access to proposals?
* Are writing and formatting easy?
* Is access management possible?
* Can authorized people comment easily?
* Are comments threaded?
* Can suggestions be resolved when they’re addressed?
* Can edits be suggested directly?
* Are there moderation tools available?
* Can the life cycle be automated?
* Can documents be classified and searched?
* Is archiving simple?
* Is cross-document linking possible?
* What kind of rich-media support is available?

Deciding on tools is full of tradeoffs, and I don’t have your context, so I won’t give you a recommendation. I’ve used many tools for RFCs, so here’s an unranked list of possibilities without comment.

* Collaborative documents like Google Docs, Dropbox Paper, Notion, Coda, or Quip
* A markdown document sourced in a git repo in Github, Gitlab, Bitbucket, or self-hosted
* A presentation using Slides or Keynote
* Contract management software
* [Other RFC tools](https://www.rfc-editor.org/pubprocess/tools/)

# Managing change

The success of any process is [highly dependent on how you manage its](https://hbr.org/2005/10/the-hard-side-of-change-management) deployment, and there’s enough written about it for you to [reduce your chance of failing](https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2) at it. Nonetheless, below are additional thoughts to reflect upon before you get your team onboarded onto RFCs.

# 👩‍✈️ Pilot and measure

Adopting RFCs should be considered a collective experiment because their success isn’t guaranteed. Approach its implementation as a pilot, and explore ways of measuring your success, which will vary depending on your local context. Remember, you’re adding friction, so keeping an eye on whether your team feels held back is essential.

Some example questions to ask in surveys or 1:1s:

* Have RFCs led to better decisions?
* Is your team making decisions faster?
* Is your team better informed?
* Are individuals commenting productively?
* Are people from different groups equally represented in the comments?
* Are experienced people using proposals as opportunities to mentor?
* Do early-career folks feel comfortable sharing their ideas?
* Is leadership engaging at the right level?
* Can the process be lighter while achieving similar outcomes?

*💡 Pro-tip: Write your first RFC on implementing RFCs. It’s a great way to kick the tires of your tooling, experience your own process, and lead by example. I got into the habit of ‘RFC-ing’ most of* [*my process changes*](https://github.com/buritica/mgt/blob/master/rfcs/up-tempo.md) *and even re-organizations.*

# 📈 Scaling decision making

Depending on your team, there are a few breakpoints where a light RFC process will start breaking. If your team is decently sized or grows too quickly, you’ll be faced with information overload and should think about defining guidelines on who must read what. Another side effect of larger-sized teams is visibility into decision-making. Building a cadence into your process or adding steps like architecture reviews and team office hours can improve your ability to observe the system. Eventually, you may run into the problem of having too many proposals or where information is no longer discoverable, and you’ll have to invest in knowledge management for your RFCs. Give people space to not have to read all proposals and the freedom from commenting on all of them. When you scale a decision-making process, you’re also scaling trust or lack thereof.

# 🚲 Iterating

Process is what I ship, so I’ve adopted product development practices that have helped me maximize the success of my ‘products’. Piloting (beta testing) is one. Another one is to iterate on the process as I gather feedback. We measured in our pilot phase, and we can use the same framework to adjust our approach, accelerate our decision-making, and improve our outcomes. Better yet, once your process has been adopted, you can shift the ownership to the team so they can evolve it in a way that serves them best. At Splice, most of the evolutions of our RFC process and SWARCH (software architecture reviews) came from the team itself through RFCs.

Variations of the previously posed questions can be:

* Can we adjust RFCs to lead to even better decisions?
* Which decision bottlenecks can we eliminate?
* How can we improve information flow?
* Are there ways we can encourage better discussions?
* How can we make it safer to contribute or comment?
* Can we build on our existing tooling to improve the RFC experience?

# 🐉 RFC Dragons

No process is perfect, so before you consider adopting RFCs with your team, there are some tradeoffs to consider.

**👀 When to RFC**

Knowing when to write an RFC is almost as important as the content of the RFC. If your team is effective, you probably don’t need long-form documents for decisions that are best lived through code. But not all groups are effective, so you may need a very prescriptive guide when writing before coding is necessary. For example, you may want to prevent a package-manager change over the weekend as an outcome of an engineer’s free time.

Developing criteria for when to use different processes as an individual comes with time and experience. [Here’s an old example](https://github.com/buritica/mgt/blob/master/rfcs/rfc-proposal.md) I used when I first adopted RFCs with one of my teams. It’s out-dated, so you should only consider it a reference as you build your own.

**🙋‍♀️ Domain ownership**

Sometimes the ability to propose change can be understood as an invitation to drive change. It’s great when individuals take the initiative and make things better, but I’ve found myself reading some RFCs that were beyond the reasonable scope of change without a heads up of them coming. A hypothetical example could be a newly onboarded engineer proposing the rewrite of someone else’s system. Unlike pull requests, RFCs should be scoped to those responsible for the systems or products that will be impacted. This doesn’t mean cross-domain collaboration can’t happen, but it should follow the lead of those accountable for their decisions’ outcomes. If your domain’s ownership isn’t explicitly outlined, you may have additional challenges beyond out-of-scope system proposals.

**✋ Friction**

First, when you implement RFCs, you will be introducing friction to your team. Instead of going straight to building, we are required to think *and write* about what we’ll build. Friction brings frustration. Our industry has convinced us that programmers are supposed to be writing code as much time as possible, leading to negative sentiments to practices that keep programmers away from their editors. If you ask your team to write ahead of building, you should be ready to approach the frustration associated with ‘time not writing code’ and its possible impact on morale.

If your team is in the forming stage or balanced towards less experienced, friction may be a good thing because you can complement the lack of experience with collaborative problem-solving. Balancing friction is a delicate act that you’ll have to learn as you incorporate RFCs into your software delivery process. Some considerations that may help you balance friction:

* Enable people to move their implementation forward in parallel to their proposal if the risk is low.
* Encourage people to talk through recommendations with their managers or senior ICs before they invest in writing.
* Allow for submissions to be considered work in progress to gather early feedback until the ‘official’ commenting period.
* Have clear guidelines for when RFCs should be written.

**👍 Who decides**

We briefly discussed this matter during the life cycle, but clarifying who will be responsible for deciding whether to move forward or not on a proposal prevents difficult conversations. I’ve shared that my preference is to push down decision-making rather than building a hierarchical or authoritative model. No matter your leadership philosophy, all of the above options are better than consensus-driven decision-making through RFCs or design by committee. The few times I had to unblock proposals were mostly because people expected consensus from the entire group before moving forward.

In open source software projects, most decisions are made by volunteers and have a broad impact that may require some consensus level. Most companies aren’t open source projects, so even though proposals should consider user feedback, the criteria and vision of those responsible for the decision should be allowed to drive momentum. If a poor decision was made, it is a new lesson, and it can be fixed. And, in the eventuality of a trapdoor decision, you may want to consider alternative ways of deciding or [avoiding them if possible](https://www.youtube.com/watch?v=oqWoFrRM8sA).

**🧰 Tooling**

Deciding what tool to use is always a trap, and we covered it above, but I take this opportunity to remind you that you’ll never find a perfect tool unless you build it yourself. I’m not going to encourage you to do so, but share it with the world if you do.

# Conclusion

By defining a process for decision-making, you can give your team the space to own the outcome of the choices they make. RFCs are one of the ways that you can do this, and this guide may help you manage the change. If you have adopted a similar process, I invite you to write about it and [share it with me](https://twitter.com/buritica?lang=en) so we can all learn together about team decision-making.

*A special thanks to Michael Gorsuch who proofread this post, and to all my former colleagues who contributed to this guide by helping me sharpen the process.*

*This article was originally written* [*for LeadDev*](https://leaddev.com/technical-decision-making/thorough-team-guide-rfcs)*, and cross-posted here.*