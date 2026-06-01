---
title: Notes on Building Evolutionary Architectures.
date: '2019-11-22T19:16:39-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://lethain.com/building-evolutionary-architectures/
---

[Notes on Building Evolutionary Architectures.](https://lethain.com/building-evolutionary-architectures/)  



I recently picked up [Building Evolutionary Architectures](https://www.amazon.com/Building-Evolutionary-Architectures-Support-Constant/dp/1491986360/ref=asc_df_1491986360/?tag=hyprod-20&linkCode=df0&hvadid=266173100564&hvpos=1o1&hvnetw=g&hvrand=6992201456656250307&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061254&hvtargid=pla-380563455104&psc=1) by Ford, Parsons and Kua. It occupies a similar spot in my head as [Accelerate](https://lethain.com/accelerate-developer-productivity/) and [A Philosophy of Software Design](https://lethain.com/notes-philosophy-software-design/), in the category of seasoned software practitioners sharing their generalized approach to software. Altogether, I rather enjoyed it, and it more elegantly explains many of the points I attempted to make in [Reclaim unreasonable software](https://lethain.com/reclaim-unreasonable-software/).

Below are my notes from *Building Evolutionary Architecture*.

## Summary

The book starts by asking a question that I’ve grappled with frequently: “How is long-term planning possible when everything changes all the time?” Their proposal is evolutionary architecture, which is architecture that “supports guided, incremental change across multiple dimensions.”

**Incremental change** is both “how teams build software” and “how they deploy it.” Building software this way requires delivering incremental units of value, moving further away from the tragedy of big bang software development. Deploying software incrementally is using the sort of modern development practices described in [Accelerate](https://lethain.com/accelerate-developer-productivity/).

**Guided change** is identifying “fitness functions” to measure the state of important properties like security, availability, and so on. You then rely on these fitness functions to evaluate each change and ensure they’re heading you towards your intended destination. These fitness functions are run in your deployment pipeline, removing the architect from the gatekeeper role, and instead allowing them to focus on guiding rather than enforcing.

**Multiple dimensions** refers to anything you want to ensure, such as security, data structure, reliability, latency, observability, etc — really any important properties. Each of these dimensions should have one or more fitness functions to support its guided change, or to “project that dimension.”

## Fitness functions

Defines fitness functions as, “An architectural fitness function provides an objective integrity assessment of some architectural characteristic(s).” Fitness is usually assessed in your deployment pipeline, preferably as unit tests that can be run locally for the fastest possible development loop.

### Atomic vs holistic

Two varieties of fitness functions are **atomic** and **holistic**.

Atomic fitness functions “run against a singular context and exercise one particular aspect of the architecture.” [Sorbet](https://sorbet.org/) asserting valid types on a codebase is an example of an atomic fitness function. As would be asserting there are no incompatible dependencies for a codebase.

Holistic fitness functions “run against a shared context and exercise a combination of architectural aspects such as security and scalability.” Ensuring that no personally identifying information (PII) is published into your logging system is a holistic fitness function. Monitoring that latency doesn’t increase with code changes would also be holistic.

### Triggered vs continual

Two additional dimensions of fitness functions are **triggered** and **continual**.

Triggered fitness functions “run based on a particular event, such as a developer executing a unit test.” These are verifications run on demand in your deployment pipeline, during local development and so on: linting, tests, fuzzing, coverage, etc.

Continual tests “don’t run on a schedule, but instead execute constant verification.” This might be alerts on latency or ensuring infrastructure costs are trending towards budget.

### Static vs dynamic

The taxonomy expands further with **static** and **dynamic** fitness functions.

Static fitness functions “have a fixed result, such as the binary pass/fail of a unit test.” Examples here are acceptable latency range, acceptable test coverage, unit tests passing, and so on.

Dynamic fitness functions “rely on a shifting definition based on extra context.” These would embody a tradeoff between say freshness and request volume, tolerating less freshness (and consequently more caching) for high volume infrastructure.

### Automated and manual

The final distinction about fitness functions is between **automated** and **manual** fitness functions, which mean what you’d expect.

### Designing fitness functions

You should identify fitness functions as early in a project’s lifecycle as possible, because they serve as a ratchet on quality degradation. However, you’re going to miss a bunch of potentially useful fitness functions since you don’t understand the system until you run it at scale. To account for that, meet periodically (at least annually, but that seems quite infrequent) to refresh and reevaluate your systems’ fitness.

## Incremental change

When you’re in a service architecture, ensure that clients can upgrade at their own pace rather than assuming all clients will upgrade immediately and synchronously (they won’t). Also automate the deprovisioning of unused services and versions once they stop receiving traffic. (The pattern of ratcheting out adoption of old versions is particularly helpful, in my experience.)

Recommends **versioning services internally** instead of clients passing versions. This fingerprints incoming requests and routes them to the correct implementation, but the endpoint that clients call doesn’t change. “In either case, severely limit the number of supported versions,” and in particular ”strive to support only two versions at a time, and only temporarily.”

**Testability** is essential for incremental change, supporting a rapid development loop. It also moves away from “strict development guidelines (with the attendant bureaucratic scolding).”

They’re going to be tradeoffs between fitness functions over the course of development, and the point is to use them to have a structured conversation as early as possible. They’re also a good safety break to realize you’re heading down an unacceptable path of tradeoffs.

Follow **hypothesis-driven development**, “rather than gathering formal requirements… leverage the scientific method instead.” This is a fascinating idea that reminds me of [Escaping the Build Trap](https://lethain.com/notes-escaping-the-build-trap/)’s vision of product development.

## Architectural coupling

**Modulary** is “a logical grouping of related code” and one of the most important tools to limit architectural coupling. Create modules out of related functionality to maximize *functional cohesion*. Aiming to scope modules as *architectural quantum*, “an independently deployable component with high functional cohesion.”

Small modules are easier to change, so generally prefer smaller, but getting the right boundaries is key to balance between coupling and complexity.

There is a discussion of evolvability of different styles of codebases: big ball of mud, monolith, layered architecture, modular monoliths (e.g. monolith but with enforced modular boundaries), microkernel (“core system with an API that allows plug-in enhancements”), event-driven architectures, mediator pattern, service-oriented architecture, microservices, service-based architectures, and serverless. Which of these to pick is less important than designing the implementation well.

## Evolutionary data

One of the heaviest frictions for evolving architecture is the underlying data, and that friction has inspired the practices of **evolutionary data**. This requires that schemas as (1) test, (2) versioned, and (3) incremental. (I’ve personally found [django-migrations](https://docs.djangoproject.com/en/2.2/topics/migrations/) to have good patterns to learn from here.)

It’s ideal to have shared-nothing architecture where applications don’t directly integrate against the same database. If you do, consider the “expand/contract pattern”, which allows you to support broader functionality, transition incrementally, and then remove the old using a combination of [code rewriting](https://lethain.com/refactoring-programmatically/), code ratchets and so on.

Also introduce the concept of **inappropriate data coupling**, for example transactions force large architectural quanta. Anything within a transaction needs to be deployed with the other pieces contributing to that transaction. Transactions are also often owned by a database administration or infrastructure team, which introduce cross-team coordination aspects as well.

This section also makes a great observation of how weak DBA tooling is, why are IDEs so good and DBA tools so poor? They blame vendors-as-religion behavior from DBAs, but blaming the lack of tools on DBAs being devoted to their vendors feels a bit reductive.

## Building evolvable architectures

Tips for building evolvable architectures:

* **“Remove needless variability”** through adoption of immutable infrastructure, long-lived feature flags, and so on.
* **“Make decisions reversible”** by making it easy to undo deploys and such. Prefer immediately shifting traffic off a broken new version to slowly deploying a previous revision. Prefer flipping flags to disable new features over deployment, etc.
* **“Prefer evolvable over predictable.”** If you optimize for the known challenges for an architecture, you’ll get stuck because there are at least as many unknown challenges as known challenges. It’s better to be able to respond to problems quickly than to cleanly address what you’re currently aware of.
* **“Build anticorruption layers.”** Mostly this means building good interfaces so you can shift out the implementation underneath. The act of adding interfaces can be expensive as well, so balance this with finding the [last responsible moment](https://effectivesoftwaredesign.com/2014/03/27/lean-software-development-before-and-after-the-last-responsible-moment/) to make the decision.
* **“Build sacrificial architectures.”** Assume that you’ll make tradeoffs that won’t last forever, and be okay with occasionally throwing away your implementations. Uses example of Ebray rewriting from Perl to C++ to Java over course of seven years.
* **“Mitigate external change.”** For example, don’t rely on global package repositories, but instead pull in copies of packages you need locally. Then you can manage your upgrade timing in addition to owning your build pipeline reliability.
* **“Libraries versus frameworks.”** Argues against frameworks, since you write code that integrates with frameworks, as opposed to writing code that calls out to libraries. Consequently, there is tighter coupling in frameworks.
* **“Version services internally.”** Discussed earlier in these notes, don’t leak version identifiers to users, instead inspect the incoming requests and handle them appropriately. Easier for service to manage that complexity than all clients to handle it.
* **“Product over project.”** Structure your teams, and consequently your architecture, around long-lived products, not to short-lived projects.
* **“Dealing with external change.”** Your clients (as in, software generating requests to your service) will change their needs over time, define explicit contracts to state these agreements, perhaps as [Service Level Objectives](https://landing.google.com/sre/sre-book/chapters/service-level-objectives/).
* **“Culture of experimentation.”** Evolution is built on structured, measured experimentation, which requires a [structured, thoughtful approach](https://lethain.com/magnitudes-of-exploration/).
* **Start with low-hanging fruit.** Easy wins beget larger wins, start where it’s easy. (I also had a chat earlier this week with [Keith Adams](https://twitter.com/keithmadams) who described a power function for which files/systems are frequently changes, so perhaps start where most changes happen.)

## Books

Books recommended within *Building Evolutionary Architectures*:

* [Continuous Delivery](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley-ebook/dp/B003YMNVC0)
* [Lean Enterprise](https://www.amazon.com/dp/B00QL5MSF8/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
* [Domain-Driven Design](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215/ref=asc_df_0321125215/?tag=hyprod-20&linkCode=df0&hvadid=312118197030&hvpos=1o1&hvnetw=g&hvrand=13507817513197383403&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061254&hvtargid=pla-449269547899&psc=1)
* [Refactoring Databases](https://www.amazon.com/Refactoring-Databases-Evolutionary-paperback-Addison-Wesley/dp/0321774515)

## Final thoughts

This is a fantastic book, easily falling into the same rare category as *Accelerate* and *A Philosophy of Software Design*. I could easily imagine asking a team I was working with to read this book together and reflect on its practices. If you haven’t gotten a chance to spend time with it, it gets a strong recommendation from me.