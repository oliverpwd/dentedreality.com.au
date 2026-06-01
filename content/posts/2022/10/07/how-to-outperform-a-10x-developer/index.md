---
title: How to Outperform a 10x Developer
date: '2022-10-07T15:12:20-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://betterprogramming.pub/how-to-outperform-a-10x-developer-fa1132807934
---

[How to Outperform a 10x Developer](https://betterprogramming.pub/how-to-outperform-a-10x-developer-fa1132807934)  



## First awareness. Then productivity.


![]()

From a software developer’s perspective, the complexity of a production system makes it abstract and distant, so we tend to shut it out and focus on the immediate work of writing code.

[Jeff Foster](https://medium.com/@jeff-foster) wrote a [great story](https://medium.com/ingeniouslysimple/the-origins-of-the-10x-developer-2e0177ecef60) on the origins of the expression “10x developer,” contrasting the value of [outsized code-writing skills against the ability to focus on the product](https://medium.com/ingeniouslysimple/project-vs-product-thinking-b4971163f3dd).

From a DevOps perspective, its all-inclusive reach from development to operations demands collaboration. Focusing on the product trumps coding skills every time, not the least because sometimes not writing new code is the best decision for the product.

This story offers concrete examples where a better understanding of a production system can change how we see our roles as software developers and significantly improve how we design systems and write code.

# **When quality is not enough**

Quality code and honed skills still matter, of course. Software developers should [observe good practices](https://opensource.com/article/17/5/30-best-practices-software-development-and-testing) such as automated linters, code reviews, unit testing, and many others. Still, writing great quality code fast is a small fraction of all the tasks required to bring a system to production and keep it alive.

In that sense, organizations should not spend too many resources finding and nurturing 10x developers. Firstly, they [may not be actual 10x developers](https://www.simplethread.com/the-10x-programmer-myth/). Secondly, and most importantly: *sustained* software development must include supporting material, such as design documentation and operating procedures. Those documents must be constantly reviewed and updated in collaboration with people using them. You can streamline the coordination activities, but the underlying human interactions and workflows will hardly happen 10x faster.

**Update on 9/22:** [Hajime Vukelic](https://medium.com/@hayavuk) added a comment to the story, pointing out that I made it sound like outsized individual performance is impossible or undesirable. I still think it is difficult in a DevOps practice, but his thoughtful reasoning stands on its own and also led me to read one of his personal stories, titled [“What’s a high-differential developer”](https://medium.com/@hayavuk/whats-a-high-differential-developer-2fc42e2ee6a3). I think it is an excellent addition to this general topic.

You want the developers who perform at a higher, yet attainable, level (1.2x developer?) so that other team members can understand and assimilate more productive techniques and behaviors.

![]()

Growing talent is the better path toward productivity. The characters on the right are too unique and rare to make a significant impact across multiple teams.



# Lesson 1 — Greatness takes time: 27 times more.

I don’t mean “time” as in “decades of experience” — that helps too — but rather “time” as the actual time it takes to do great work.

Even the most talented developers sabotage themselves with poor estimations of how long it takes to go from a prototype to a sustainable system in production. I must emphasize the word “sustainable,” where on-call shifts produce few page-outs that [even people who did not write the code](http://sourcepatch.blogspot.com/2021/09/asking-wrong-question-should-developers.html?view=magazine) can resolve.

My favorite technique to estimate the total cost of a feature in production is to create a working prototype and then *multiply the time spent on the prototype by 27*. That is right; if it takes me two days to develop a prototype, it may take nearly three months (2×27=54 business days) of combined effort across the whole team to have it humming along in production.

**Update on 9:22**: User [Liquid Analytics](https://medium.com/@liquidanalytics) made an excellent point in the comment section about the 27x multiplier becoming a possible inhibitor to meaningful progress. I should have mentioned that the idea is to deploy the prototype using modern “test in production” approaches, such as [trunk-based development](https://trunkbaseddevelopment.com/) behind [dark launches](https://www.split.io/glossary/dark-launch) or [feature flags](https://www.atlassian.com/continuous-delivery/principles/feature-flags).

## ***Why 27x?***

Frederick Brooks Jr. explained the first “9x” in [“The Mythical Man-Month,”](https://archive.org/details/MythicalManMonth) his landmark set of essays on software development in book form.

The first 3x multiplier is the cost of going from running code (the book uses the term “program,” characteristic of the time) to a reliable application (the book used the term “program product.”)

The second 3x multiplier comes from the additional testing needed to turn that reliable application into a system (a “system product.”)

Brooks covered the aspects of creating software to be handed to customers for on-premise deployment — characteristic of IBM’s business model at the time. As such, it excludes the costs associated with operational aspects, where I add the final 3x factor — based on my experience in operations engineering, so your multiplier may vary — to turn a system into an operable Cloud-based service.

![]()

Brooks explained why something ready to be deployed at a customer site takes nine times the effort of creating a prototype. I added the extra 3x factor for deploying and maintaining the system.

That final multiplier includes development activities such as:

* Instrumenting the system for observability
* Documenting operational procedures based on the system design
* Development and upkeep of the continuous deployment pipeline
* Integration testing with other cloud provider services.

Combining all multipliers (3x3x3) gives us the 27x additional cost to take a prototype to production.

**Why it matters:** While a seasoned developer may not undershoot the sizing of a new feature by the entire 27x multiplier, anything beyond a [2x or 3x factor](https://fibery.io/blog/software-development-time-estimation/) is guaranteed to create intractable surprises across the team and, more importantly, deprive you of the time needed to add and validate everything you need to avoid handing a nightmare to the operations team.


# Lesson 2 — Operations engineering trumps art

By all means, art has its place, and some corners of the system may look clever or exquisite, but ultimately [form follows function](https://en.wikipedia.org/wiki/Form_follows_function), and the function of a production system is to run software that meets requirements and cost objectives.

This section covers lessons learned in operations and how they should affect design and coding activities, accounting for a portion of that 27x multiple.

The section does not cover the entire spectrum outside code development, which would make this story too long for now.

**More components. More cost. Check everyone’s budget.** Taking operational costs into account during design and architecture is the most important lesson I have ever learned in my time in operations. Any *new* component in the system alters the cost structure of operating that system, so you need to ask yourself whether that component is removing more cost than it is adding and be ready to forego adding something that looks *really* fun into the system.

After all, the same world where CFOs (rightfully) tell you that [bringing in more revenue trumps cutting expenses](https://twitter.com/KurtisHanni/status/1560986912613072899) is inhabited by developers who will abstract a 50ms SQL query into a microservice-wrapped series of paginated RESTful calls (true story.)

I don’t mean to take a reactionary approach to change, but this is an area where one needs to find ways to collaborate or, at a minimum, consult with the operations team.

**World-class status and health endpoints.** No one can afford to fumble after the system status during an outage, especially in micro-service architectures with hundreds of components.

A production system needs an overall health point aggregating the health from various dependencies. The idea is that an operator can quickly assess (1) which parts of the system are not working and (2) which dependencies are not working. The “why” part comes later.

I listed my suggestions for designing health endpoints in my article on [readiness and liveness for Kubernetes containers](http://sourcepatch.blogspot.com/2021/12/the-art-and-science-of-probing.html) — most of the recommendations in that article also apply to non-Kubernetes systems.

**Log errors from the reader’s perspective.** Once an operator realizes that the system is not entirely healthy, the next step is understanding what is causing it and how to fix it.

At an elementary level, something should be happening, and it is not. From the perspective of the person reading a log message, the most helpful log messages follow a template like this:

```
[ERROR|WARNING|INFO]: [Component X] attempted to [take action Y], which returned [response Z].
```

That format may seem evident at first — it looks like a regular subject-verb-object construct — but it is the terminology that matters the most:

* Is *“component X”* something that exists in the system documentation?
* Is that *“action Y”* something accessible to the reader?
* Is *“response Z”* mentioned somewhere in a troubleshooting section?

![]()

Log messages can help explain the system behavior, but only if the message contents match the contents of the official documentation, even if forums unaffiliated with the product fill some gaps.

I have read my fair share of error messages that made me thankful that someone spent the time adding them to the code but gave me pause about referencing file names and library calls that only meant something to their authors. Those internal references should be in dedicated trace files or marked with a “debug” prefix for easy filtering.

Ultimately, every log message must lead to a clear resolution step that does not involve contacting the message’s author or reading the source code.

**Write system documentation:** Writing documentation forces you to structure your understanding of the system into a new medium. The activity brings many benefits to the system besides the imperative of telling people how to install, monitor, secure, or troubleshoot the system.

The act of writing requires authors to *think through aspects of the system* that may be difficult to explain.

Often, that difficulty may indicate potential design flaws, such as struggling to explain the correct order of installation of all components. Other times, the struggle may be due to “underdeveloped” areas of the product requiring long stretches of pseudo-code instructions for the reader (*“…then click here, type this, wait a few seconds, then a panel will pop up, find a button named…”*)

When done correctly, documentation also acts as a gathering point for collaborators that may have the willingness to donate their knowledge but not the time to figure out how to do it. These types of contributions are a huge productivity boost for the entire ecosystem (developers and users) and tend to get otherwise lost in team channels and private conversations.

**Timebox calls to remote components**. In distributed systems, we know better than depend on remote agents always to respond quickly and reliably. Still, we often go with default timeout settings in client libraries and utilities without giving it a second thought because we assume their developers already figured out the magic settings that work for everybody.

That is a common oversight in a world of libraries and utilities shipped with sensible defaults and systems adopting the latest design and operational techniques for maximum availability. The misplaced confidence in the resulting system works out until one of those systems fails, leaving your component unconditionally stuck on a [2-hour wait](https://man7.org/linux/man-pages/man7/tcp.7.html) for a TCP timeout.

Always look for remote calls in the code and make sure you know their limits and how your code will handle those limits:

* Maximum connection response time
* Maximum request response time
* Maximum number of retries

![]()

Remote systems or the network paths between your system and the remote system may be so reliable that we start treating them as function calls in local memory. Scrutinize all libraries and network stacks to find their tolerance for connectivity problems and error codes in case of problems.

Creating an effective retry policy for remote calls is a welcome improvement to any system. Still, it has the potential of obscuring the visibility into looming problems, such as masking a steady worsening of response times until they finally exceed the maximum limits, leading me to the next point.

**Telemetry, observability, and distributed tracing**: There is more to handling outages than looking at system status and log entries. There is also more to operations than handling outages, such as proactively looking at the system’s telemetry of internal metrics, traces, and log entries.

Many platforms already generate a wealth of telemetry data with [minimum instrumentation in the source code](https://opentelemetry.io/docs/instrumentation/). However, one still needs quite a bit of telemetry-specific code mixed with the source code, especially for metrics.

![]()

Each system component may not tell you whether it is meeting its goals. Making the code generate metrics takes extra effort, aggregating them into an actionable dashboard for the operations team.

Also, ensure you (and other developers) have regular access to a local setup of the telemetry framework used in the system’s operations. Many frameworks support local execution in your workstation or a free trial cloud-based account. A uniform setup that allows a seamless transition from local to remote environments takes development, validation, documentation, and upkeep. Creating such environments can be a lot of fun, but it costs time and money too.

I can’t emphasize enough how *even the most experienced and self-confident developers always learn something new or surprising when looking at the telemetry of their code*.

Taking it to the next level, *work with your operations team to ensure a data-sharing arrangement with the operations team*, dedicating special attention and effort to aspects such as data anonymization and access.

**Beware of queueing systems.** Writing queuing systems is fun, and designing the architectural diagrams can be exciting (and enticing), but most people seriously misjudge the cost of adding queuing patterns into a system.

I know there are legitimate use cases for queueing systems, like high-volume transactions — as in millions of messages per day — where the calling component cannot wait for the response and only cares that the transaction eventually gets processed within a reasonable time.

However, if you are not dealing with those use cases, you may want to seriously reconsider the inclusion of asynchronous message processing into the system. That communication pattern adds costs that stretch across the entire length of a business transaction between a message producer “A” and a message consumer “B.” Here are just a few examples of that extra complexity:

* Operational procedures for system administrators to deal with queue sizes exceeding certain limits
* Extra design and code to deal with expiring messages.
* Operational procedures for handling messages sent to dead-letter queues after expiration.
* Extending the system to manage dead-letter queues
* Handling [distributed tracing](https://microservices.io/patterns/observability/distributed-tracing.html) for business transactions spanning over a message delivery.

# Lesson 3 — Thread the quad: code, build, support, operate

While a long career may gradually teach you about different areas of a DevOps practice, you can expedite your growth by intentionally rotating across development, integration, support, and operations. The idea is to learn how things work and how to build software that works well in each significant area of the engineering cycle.

And once you get to know the people and workflows in those areas, it becomes easier to contribute outside your core expertise with less technical and social friction.

Mid-career and senior developers may not be as inclined to change job roles, but their experience allows them to learn faster. A temporary rotation of a few weeks, a shared project, or even access to customer support tickets and incident reports may work just as well.

![]()

A DevOps practice encourages more access and insight into different areas. Take a step further and rotate into those areas, even briefly, to understand how various software characteristics affect their work.

## **Case study 1 (build)**.

We had a team primarily responsible for evolving and maintaining the build system in a previous project. Building (compiling and packaging) the entire code base in a local workstation took about two minutes. In contrast, the same operation in the build cycle took a seemingly eternal fifteen minutes.

One of the developers outside the build team spent an afternoon adding various log entries to the build scripts to isolate the problem, narrowing the likely cause to the steps where the build wrote compiled binaries to disk. Somehow, disk write operations seemed to take orders of magnitude longer in the build system than in a local workstation (and yes, the build machine had SDD storage 🙂

The build team analyzed those findings and attempted different alternatives (some of those outside the Unix skillset from the original developer,) landing on the final solution of increasing the memory allocation on the VMs and moving the temporary directories for each build to an in-memory filesystem ([tmpfs](https://en.wikipedia.org/wiki/Tmpfs).)

## **Case study 2 (operations)**.

I once co-managed the PagerDuty escalation policies and alerting rules for our entire organization — a few hundred people — for a few months. Sometimes, depending on vacation schedules and local holidays, that meant receiving urgent direct messages requesting that I enable alerting triggers in portions of the system outside my immediate scope.

I would always ask a few questions before pushing the buttons, such as:

* “When will the components generating these new alerts be deployed?”
* “I don’t see a playbook link in the description. Does the ops team know where to look for one?”

Without going into the occasional mix of bewildering answers, that (part-time) assignment taught me valuable lessons about the importance of managing the total number of types of alerts in a system, the cost-benefit of adding new components to a production system, and the absolute imperative of involving operations teams in architectural decisions.

# Lesson #4 — Intentional learning: Learn with every task.

At this point, you know how to secure the time to write code that is ready for production and the things you need to include in that code.

That is a long list of things; you don’t want to wait decades to acquire those skills organically, [the “10000-hour” rule](https://www.edsurge.com/news/2020-05-05-researcher-behind-10-000-hour-rule-says-good-teaching-matters-not-just-practice) notwithstanding.

We always learn something while performing a task, but [intentional learning](https://learntechasia.com/intentional-learning-global-reskilling-emergency/) means going beyond getting the work done and figuring out why something works and how to improve it.

A web search may give you a precise answer to a specific problem, and one can learn a lot that way, but with intentional learning, the idea is to go beyond ready-made solutions:

1. **Browse**. If the solution involves a patterned solution for a framework, such as a specific set of resources for Terraform, go back to [browse the complete definition for those resources](https://registry.terraform.io/browse/providers) and maybe browse adjacent resources from the same provider.
2. If the solution involves a utility with specific parameters, go back to the utility’s manual to study those parameters and also skim over the other parameters. The idea is not to memorize but to **index them in your mind**, especially in the case of tools such as “[awk](https://www.gnu.org/software/gawk/manual/gawk.html),” where the manual can be an entire book.
3. **Explain** what you learned. For source code, pull out the “[rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging)” and explain the source code to an inanimate object. For concepts, you may even skip finding someone else and use the [Feynman technique](https://en.wikipedia.org/wiki/Learning_by_teaching), pretending you are presenting that concept to a child.
4. **Write** about the subject. Writing is a more intentional form of learning, helping you consolidate and expand your knowledge of a concept (maybe writing an article,) interrelated concepts (using something like a technical paper,) or an entire domain (for example, writing a book.) Writing goes far beyond learning so that it may be more helpful in organizing adjacent bits of knowledge in your head. If you do decide to take on this exciting activity, make sure to read [“Writing for Engineers”](https://www.heinrichhartmann.com/posts/writing/), by Heinrich Hartmann.

![]()

*“Read the product guides? Who has time for that?”*

I realize this is the age of googling “how-to-make-this-error-message-go-away,” which makes a lot of sense during a time crunch. Still, you don’t learn much from those kinds of shortcuts.

Here I must quote Stephen King, one of the most successful fiction authors of all time, who offered this bit of tough-love advice for [aspiring writers](https://stephenking.com/works/nonfiction/on-writing-a-memoir-of-the-craft.html):

> “If you don’t have time to read, you don’t have the time (or the tools) to write. Simple as that.”

If you do not carve out time from the schedule to explore the technology used in your projects and expand upon it, you restrict yourself to learning just enough to complete your immediate tasks. That dynamic becomes self-reinforcing when people around you assume you are only capable of those same tasks. And it doesn’t take long for those assumptions to become justified.

That “carving out” of time may be more or less challenging depending on different situations, but awareness is a starting point. Sometimes you may constantly be doubling down on taking on repetitive (yet valuable) tasks because it is more comfortable. At other times your organization may become comfortable with someone doing a repetitive chore more efficiently than anyone else. Regardless of the situation, *recognizing that you are no longer learning something new in every task is the first step.*

# Conclusion

A DevOps practice covers many distinct and extensive disciplines, which leads people to specialize in a given field, such as software development, continuous delivery, or operations.

Sometimes that narrowing of interests and purpose happens before people get a chance to explore other areas, so resist the urge and pressure to specialize early in your career. As an organization, balance the productivity that comes from people possibly overstaying in a role with the benefits of a [Japanese-style approach of yearly rotations](https://wa-shoku.info/jinji-ido-the-notorious-system-of-annual-rotations/) — perhaps not on a fixed schedule.

Early in your career, work with your management team to “intern” in coding, delivery, and operations. That kind of rounded experience is precious and exceedingly rare. It will help you multiply your potential in any area you choose to contribute, whether as a programmer, system architect, UX designer, technical account manager, infrastructure engineer, or any other role you may favor.

The willingness to understand what makes a product better from different angles and blend those lessons into your daily routine is a superpower far beyond anything even an actual 10x developer can muster in a niche area.

Ultimately, these lessons come from personal experience, and every path is different. I welcome feedback in the comment section and promise to incorporate them appropriately into the main story.