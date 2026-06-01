---
title: Refactor → Organisation
date: '2022-03-25T18:12:37-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/bbc-design-engineering/refactor-organisation-80e4e171d922
---

[Refactor → Organisation](https://medium.com/bbc-design-engineering/refactor-organisation-80e4e171d922)  



In this blog post, rather than focus just on the technical challenges, I want to share:

* *Some of the organisational history that led to WebCore*
* *How we went about re-organising for success*
* *How we viewed the team topologies and interaction modes between teams*
* *How we view the role of the platform (and the Core teams who build it) in enabling many teams to interact with one another*

# First — some history…

The BBC website is made up of several digital services, including [iPlayer](https://www.bbc.co.uk/iplayer), [Sounds](https://www.bbc.co.uk/sounds), [News](https://www.bbc.co.uk/news) and [Sport](https://www.bbc.co.uk/sport). Each is a major service in its own right — with millions of visits every week — and they have grown independently of one another over several years. This was reflected in the way the organisation was shaped — with separate departments owning each digital service.

![](https://miro.medium.com/max/1400/1*ElbJ6bfWemGXTHT0bjnKyg.png)![](https://miro.medium.com/max/1400/1*ElbJ6bfWemGXTHT0bjnKyg.png)

This shape meant each individual product achieved its own aims well, but it also meant the user experience across multiple services wasn’t as seamless and consistent as it could have been. There were mismatched technologies and duplication between the services. Lots of features, despite being conceptually similar, were implemented multiple times — with the total cost of maintenance also paid multiple times. Cross-cutting capabilities — e.g., personalisation and analytics — were major tasks that each product development team had to tackle themselves.

WebCore is part of a strategy to re-imagine BBC Online and create a single website for all the digital services. Standardising onto a single technology set, building shared ‘horizontal’ capabilities, and sharing commodity components between teams — will allow the BBC to better leverage the technology and build more innovative features for the audience.

![](https://miro.medium.com/max/1400/1*l0XJSr1OOo8tFqbknlBEeA.png)![](https://miro.medium.com/max/1400/1*l0XJSr1OOo8tFqbknlBEeA.png)

There are real-world implications to the autonomy and empowerment of individuals and teams. The reality is that WebCore was as much a refactor of the organisation as it was a reimplementation of technology.

High autonomy is vital to high-performing product development teams. The previously decoupled technology stacks made autonomy easier to achieve, so the WebCore strategy forced us to think about how we could balance autonomy with standardised technology.

# Organise for success

Humans will rally behind a common cause and form close-knit relationships within their group. Cohesion is a powerful thing — the sense of belonging brings people together to achieve something greater than the sum of the parts. We leverage this within any organisation to significant effect.

Missions are typically multi-team initiatives within larger organisations, such as the BBC. We can group teams together very deliberately with our organisation shape (i.e., departments) or through more fluid constructs that cross departmental boundaries. Departments are important as a primary way to create purpose and alignment amongst teams, and there are multiple ways they can be shaped. Interactions will inevitably be stronger between teams within the same department as opposed to ones that cross departmental boundaries

![](https://miro.medium.com/max/1400/1*Fo5vNwhiSKZ1SI9gYUaBzg.png)![](https://miro.medium.com/max/1400/1*Fo5vNwhiSKZ1SI9gYUaBzg.png)

The evolution of the BBC’s digital products was reflected in the internal department structures, which were aligned with digital service ownership. Operating across these traditional departmental boundaries — e.g., improvements to the time it takes for newly published content to be rendered to the audience — was more difficult.

![](https://miro.medium.com/max/1400/1*X2lyyTfJKlw-mgj0reYvYw.png)![](https://miro.medium.com/max/1400/1*X2lyyTfJKlw-mgj0reYvYw.png)

One early WebCore decision was to create a new internal department called Core Services — a department that is not orientated towards delivering one of the audience-facing services.

Instead, this is a set of teams with a mission centred around platforming and enablement for all the services. Rather than each department owning and running their own platform services, there is a specialised department for this.

![](https://miro.medium.com/max/1400/1*VcYx_3hVfHX_EmI0XNCrgA.png)![](https://miro.medium.com/max/1400/1*VcYx_3hVfHX_EmI0XNCrgA.png)

The WebCore platform is an internal product, made of a generic set of components (systems, services, and frameworks) and the customers are the internal product development teams. Rather than basing their success on audience engagement, these teams strive to elevate across the organisation and enable the tenant teams who depend on the platform.

# Optimise rather than maximise

In the first stages of migrating content onto the WebCore platform, there were a handful of teams interacting with one another — the core platform teams along with the first tenant teams to contribute components. This meant it was workable for teams to be aware of the components other teams were creating. There was a desire to maximise re-use and avoid any duplication; after all, this was the fundamental premise of WebCore.

Over time, the number of teams using the platform grew. Before long, over 100 engineers were creating components — and keeping track of what was being made became much harder. The early high-bar of ‘zero duplication’ was creating friction — how could teams move fast, iterate, and be inquisitive without causing duplication?

![](https://miro.medium.com/max/1400/1*lwKTKHKLlN3bK7v7r23fLA.png)![](https://miro.medium.com/max/1400/1*lwKTKHKLlN3bK7v7r23fLA.png)

The answer has been to develop a more pragmatic mindset towards technical debt — developing tools to manage it while accepting that aiming for zero debt is not cost-effective. Just like financial debt, technical debt is not always a bad thing. Debt becomes a problem if it is not tracked, becomes too large or if debtors cannot be held accountable.

For example, Component Health tooling allowed us to create a sense of ownership of various parts of the codebase. By instrumenting various key health metrics, teams were allowed some latitude to make their own decisions and be accountable for them over the component’s lifecycle.

This highlights an important principle — inverting control back towards tenant teams.

# Inversion of Control

Using shared technology can create a sense of disempowerment within teams. When a product development team is used to owning and controlling its entire technology stack, moving to a situation where they are dependent on others can be uncomfortable. However, from operating systems to frameworks, no team writes everything from scratch.

Bringing back the sense of control is important — and this is where maturing the platform to provide tenants with self-service interfaces and tooling is central. While earlier phases had focussed on building the systems that can handle traffic (scale, resilience, performance, observability etc.), we have increasingly looked at how we scale up the enablement of engineers and teams. To do this, we looked at [team topologies](https://teamtopologies.com/), and especially interaction modes between teams.

# Team Topologies — interaction modes

In the early phases, we tended to view enablement as “collaboration between core teams and contributing teams”. This was the right fit in those early days — everything was new to everyone, and the number of interacting teams was manageable. However, as the number of teams contributing components has scaled up, we now have a more nuanced view of a spectrum of interaction modes between teams that are available to us.

![](https://miro.medium.com/max/1400/1*3zQf60PjFa_gGKOj7-SoeQ.jpeg)![](https://miro.medium.com/max/1400/1*3zQf60PjFa_gGKOj7-SoeQ.jpeg)

Collaboration

**Collaboration** — this is when a group shares the same mission. When multiple teams interact in this mode, it might look like a cross-team squad who work all day, every day, for an extended period on the same mission. Perfect for [pioneering](https://wardleypedia.org/mediawiki/index.php/Pioneers_settlers_town_planners#Pioneers).

![](https://miro.medium.com/max/1400/1*nfFr5w400RySU0b83WbXZA.jpeg)![](https://miro.medium.com/max/1400/1*nfFr5w400RySU0b83WbXZA.jpeg)

Co-operation/Facilitation

**Co-operation/Facilitation** — This can look like a support model; we have mechanisms where teams can ask for help when they need it. It can also be about encouraging cross-community support, either from subject matter experts or from the wider product development community. Perfect for [settling](https://wardleypedia.org/mediawiki/index.php/Pioneers_settlers_town_planners#Settlers).

![](https://miro.medium.com/max/1400/1*2AoxxaEZ6DsL29Pr3REWIg.jpeg)![](https://miro.medium.com/max/1400/1*2AoxxaEZ6DsL29Pr3REWIg.jpeg)

Systemisation

**Systemisation** — this is about removing manual intervention. It could be documentation, processes, tools, or user interfaces. Perfect for [town planning](https://wardleypedia.org/mediawiki/index.php/Pioneers_settlers_town_planners#Town_Planners).

Collaboration is expensive but is ideal when new ground is being broken. It accelerates the feedback between the tenant and core platform teams, allowing gaps in the platform to be addressed quickly. However, it is essentially a manual intervention and does not scale.

Systemisation is about removing manual intervention and is the horizon goal for the platform. When the patterns are proven then the teams that follow can tread the beaten path. [Golden path tooling](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/) can be used to accelerate teams and keep them within the guardrails of the known-good path. Within the limits of these guardrails, the tenant teams have a high degree of autonomy and can deliver to their audience-facing services with minimal impediments.

Co-operation and facilitation are the grey middle ground between the two. While tools and processes can alleviate some of the burden, this is always likely to be needed. Individual people looking for help, staff turnover etc. will always create a need for this.

# Lessons learned

It’s not always been pretty — but it’s been a fascinating journey and one which I think a lot of organisations will tread.

**Organise around the right mission —** whether it’s the team or department structure, this is the primary way to create alignment and group cohesion. If it’s not right, the result won’t be either.

**Optimise, don’t idealise** — with lots of humans sharing and contributing to the same codebases, there will need to be some rules to keep everyone on the straight-and-narrow. Between humans, try to keep these as rules-of-thumb. Over time, use dashboards and tools to guide the humans and let the robots create enforcement.

**Work together but be deliberate about it** — sharing technology will require engineers working with other engineers across traditional organisational boundaries. It can easily become overwhelming, so pick the right interaction mode for the situation. There may not be one single optimal interaction mode, so a blended approach will be needed.

The key from a platform perspective is to try and get out of the way and let the tenant teams deliver unimpeded. This means relentlessly finding and removing any parts of the development lifecycle where the platform is an obstacle. This may mean providing tenant teams with controls — configuration, tooling, user interfaces etc. — but it may also mean agreeing and enforcing certain standards.

Autonomy is not a silver bullet — without alignment between teams, autonomy can breed inefficiency and low-value variation. Alignment can be created by organising humans and teams with a clear purpose. It can also be created with an opinionated platform — one which makes it easier to do the right thing, and harder to do the wrong thing. Within these constraints, there is plenty of scope of high team autonomy.

The ultimate success of WebCore will be measured over time — in excellent and innovative digital products that will inform, educate and entertain the BBC’s audiences for the next decade. This organisational refactor is a trade-off between optimising for standardised commodity components and the autonomy needed for innovative features.

Change is hard. Substantial change especially so — and where humans are involved in an endeavour that is as complex, creative, and technical as product development it can be challenging to keep sight of the big picture. But by realising that an organisation is a system — albeit a hugely complex one — then we can apply leverage to steer effective change.