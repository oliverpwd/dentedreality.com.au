---
title: Prioritization Is a Political Problem as Much as an Analytical Problem
date: '2022-06-24T09:13:34-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.mironov.com/pri-politics/
---

[Prioritization Is a Political Problem as Much as an Analytical Problem](https://www.mironov.com/pri-politics/)  



Product and engineering leaders tend to be analytical, and we think of prioritization as an algorithmic problem. Unfortunately, other execs see a different kind of problem…

Most of our tools and processes around product/feature prioritization are heads-down analytical: RICE, opportunity trees, Kano, [count-the-digits](https://www.mironov.com/moneystories/), weighted 16-column spreadsheets, WSJF, Eisenhower, whatever. Our (hidden) assumption is that choosing the objectively best work is hard, but getting organizational buy-in is not so hard. That .

At least in the B2B software product world, **I haven’t found that to be true**. Rather the reverse: regardless of how we rank alternatives or sequence work or match roadmap items to corporate initiatives, no matter what analytical method we apply, we [product managers] get similar reactions from the go-to-market side of the house: *“I only see 1 of my 5 critical items”* and *“we have to do more”* and *“your process gets in the way of the commitments we need to make.”*

At the leadership level, I see a fundamental disconnect between the folks defining/building software products and the folks marketing/selling them:

* The “maker” side of the house defines prioritization as **committing to fewer things in order to finish the most important ones**. That means [turning down the vast majority of requests from every stakeholder](https://www.mironov.com/4laws1/)… and insisting that any new commitment forces us to drop an existing commitment. (Mathematically, EXCLUSIVE OR choices.)
* The “selling” side of the house defines prioritization as **getting commitments for all of the important things we need to do**. Business cases and high-level requirements should be routinely approved. Demands are handled sequentially: having finally gotten the “maker” side to commit to A, we next need commitments for B and C and D and E. (Mathematically: AND rather than EXCLUSIVE OR.)

This back-and-forth happens in so many organizations: a go-to-market team with an inclusive (**expansive**) view of ever more products and features and opportunities – facing a builder team juggling too many commitments and doing [CPR](https://www.mayoclinic.org/first-aid/first-aid-cpr/basics/art-20056600) on existing under-invested products. More than just language, this is IMO a fundamentally different worldview.

Things I frequently hear from B2B field/sales organizations:

* *“Product doesn’t understand how important this is. They aren’t listening!”*
* *“We need to get a lot more done. Engineering/Product lack urgency.”*
* *“Customer X will pay us for this work. We can get an outside development team to do exactly what’s needed.”*
* *“We’ve followed every step of the proposal/deal process, filled out the forms, presented a business case. That should get us to YES.”*
* *“Markets and customers are constantly changing. We need to react quickly, adding new capabilities as each customer asks for them.”*
* *“My item is small. It should easily fit into this week’s sprint.”*

Across the aisle on the development side, I hear:

* *“Just last week, the exec team confirmed our top 3 initiatives for the quarter. We’ve pulled staff away from bug fixes and performance work and security (*again*) to hit committed dates. Which top initiative should we postpone for today’s brand-new item?”*
* *“Here is another one-line ticket written by non-technical users who don’t understand their problem or our system. We’ll need weeks of deep discovery from over-committed product/design/engineering staff to figure out WTF they really need. And there are 25 more cryptic one-liners right behind this one.”*
* *“Engineering has 18 unfilled developer positions. We can’t assign work to people we haven’t hired yet.”*
* *“Field teams engage outside developers (who don’t know our systems) to build quick-and-dirty product extensions. Then Engineering has to support them. Most of our P1 escalations are for code we didn’t write and don’t think is good.”*
* *“No one wants to prioritize maintenance work until something breaks. 10x more expensive (and frustrating) to do quick partial fixes than solve our root issues.”*

One side’s solutions are the other side’s problems.

## Approaches That I Have *Not* Found Helpful:

### [A] Asking exec teams to collectively prioritize long lists of things

It’s understandable that product leaders throw up their hands in frustration, and want to give the prioritization problem back to the rest of the exec team. It seems simpler to bring a list of 32 (or 57 or 133) requests into the weekly E-Staff meeting and let the group vote. IMHO reasons why this doesn’t work:

* **Each functional group actually has different priorities**. Customer Support wants 100%+ effort on bug fixes and workflow improvements. Sales wants 150%+ of engineering on demands from this week’s biggest deals. *(With a fresh set next week.)*  Marketing needs exciting, promotion-worthy new features that will drive top-of-funnel interest. Finance and Operations focus on cost reduction and internal efficiency. Legal has 110 must-do compliance fixes. No department feels like they are getting enough of what they need from Product and Engineering.  *[See [Misaligned Stakeholders](https://www.mironov.com/align/).]*
* **Our brains can’t handle more than 7-ish things at a time**. We never get all the way through 48 items, 6 dimensions, 13 initiatives tied to 5 major strategies. And there’s no one single metric for the whole list: short-term revenue, long-term bets, quality, discovery, customer satisfaction… we exhaust ourselves.
* **Project headlines don’t provide enough information** for informed discussion. Some product manager might know exactly what’s included in “Improved authentication v2.2” or “data migration tool” or “custom report for HSBC,” but the executive team doesn’t. And execs can’t spend 70 hours reviewing 70 sets of product docs. So we each imagine different project scope based on the same headlines.

Eventually, the CEO gives up… and decides that we’ll choose projects with the highest current-quarter-revenue ROI. Sales gets to pick, and we go another quarter without addressing fragile systems or architectural debt or instrumentation or [**product sprawl**](https://www.mironov.com/sprawl/).

### [B] Lectures about algorithms, development processes, and staffing shortages

As product leaders, we can fall into [**explaining philosophies**](https://www.mironov.com/philosophy/) or frameworks. *“That’s not how agile works.” “Let me walk you through my roadmapping algorithm.” “Hiring great engineers is hard.” “This didn’t get a RICE score above 162.”* Go-to-market-side folks find this infuriating. They don’t care about ticketing systems or sprint lengths or test harnesses or hiring challenges. What they (correctly) hear is that they won’t get what they need.

Especially if they’re used to IT Services organizations that do exactly (and only) what’s been spec’d by business stakeholders, they interpret this as **unwillingness**: ***won’t* rather than *can’t*.** Which means that pushing product/engineering harder will get us to YES. Inspecting every developer’s to-do list will uncover massive waste. Finding one-time project money for outside contractors is a solution. Prioritization means we get most of what we need.

### [C] Expecting spreadsheets to prioritize for us

Technologists have an unstated but deeply held belief that better algorithms will solve prioritization issues. More columns, better weightings, finer-grained estimates. Displaying 8 significant digits instead of 2.

But the error bars on our guesstimates are huge. We squint for differences between 4.10835 and 4.10977 when both are +/- 3. I find that numeric sorts are handy for choosing 12 candidates for my 6 open slots – *so that we can ignore items 13 through 972* – but less handy for deciding #1 vs #2 vs #3. Engineering estimates are notoriously inaccurate/optimistic, and revenue estimates are worse. Our semi-arbitrary inputs don’t improve much with ever-deeper analysis.

And items in our backlogs have different criteria/units. Creating revenue estimates for usability or validation experiments or dashboards is mostly IMO wasted effort.  *(Can we really estimate churn reduction from fixing this data export feature? How much incremental sales from a smoother login process?)* So forcing everything into one stack-ranked computation isn’t effective.

## Some Approaches That I’ve Found Helpful

Each of these helps share the pain of hard choices across the organization, rather than bashing Product for unilaterally making unpopular choices.

### [1] Set an explicit top-down allocation of effort across a few broad categories

Technical investments come in a few broad categories, so it’s useful to make some strategic allocation decisions before sorting individual tickets.
![](https://www.mironov.com/content/images/wp-content/uploads/2018/11/a-planned-pie.png)![](https://www.mironov.com/content/images/wp-content/uploads/2018/11/a-planned-pie.png)

Separating new features and customer initiatives from infrastructure and -ilities lets us compare similar items with similar objectives. It reduces our tendency to apply a simple “current quarter revenue-only ROI” metric to a complex mix of short-term and long-term investments.

Then we can ask more nuanced questions like *“which 2 of these 8 short-term revenue proposals are likely to deliver the best short-term ROI?”* separate from *“how will we scale up our platform for 6x volume next year?”* separate from *“have we done enough validation and discovery to confidently bet on International market expansion?”*

And a top-level allocation keeps us from zeroing out any category. We can have heated arguments about revenue boosters relative to each other without accidentally defunding the entire infrastructure budget. IMO, shifting 100% to any single slice is a going-out-of-business approach.

### [2] Push every exec-level stakeholder to provide a very short, **fully ordered** list of their group’s needs

There’s a tendency for execs to cascade down prioritization requests, then merge all responses into a huge set of requests (e.g. top 10 things from NorthEast Sales, top 8 each from SouthEast, 13 from LatinAm Sales and AsiaPac, a dozen from the Alliances team… ). But product leaders with support from the CEO can limit **each exec** to 3 or 4 things rather than 25 or 38 or 92 items. And these must be absolutely force-ranked: only a single #1 priority and a single #2. That lets product/engineering share the pain of real-world scarcity with the selling side of the house.

It also gives much better visibility to those top items. If the head of Customer Success can whittle down that group’s most critical needs to 3, we can discuss that short list in depth. Product/engineering can rough-size 3 projects and match them against strategic objectives. Marketing and Sales may have strong support for one versus another. We can all read 3 product briefs outlining what would be in/out of an implementation. As an executive team, we can start to make hard choices. A manageable set of options lets us understand them.

### [3] Briefly recap top 3-4 products or projects every week

When I get a great new idea, it tends to push everything else out of my head. Similarly, I see organizations constantly proposing new initiatives or opportunities – without remembering what’s already underway. Call it “roadmap amnesia.”

Our excitement and optimism around this minute’s hot new topic reinforces our AND assumption: ***this would be great, so there must be room for it somewhere**. Let’s get started right away! Here’s draft copy for the product announcement and a few slides to show our best customers…*

Quickly reviewing what’s **already committed and underway** (every week) can be tedious or frustrating. *Can’t we do more? Why does building software take so much longer than I want it to? Delayed again?* But it repeatedly frames the right issue: here is what we thought our absolute priorities were last week. Has something changed? There’s no excess time or talent, so we have to pair adds with deletes.

### [4] Use Now/Next/Never to frame upcoming choices

It’s not expensive to change our minds about what’s next in the development queue. (But very expensive to swap projects already underway.) So a [Now/Next/Later/Never](https://medium.com/the-creative-strategist/why-now-next-later-is-one-of-the-best-frameworks-for-roadmapping-4d547a2f2692) structure helps move the discussion from “cancel something partially finished” to “what’s next when we finish X.” Proposing what should be next gives us something real to argue about, and sets a bar for alternatives: *“Is Y more valuable/urgent than Z which is currently up next?”* highlights a specific trade-off (EXCLUSIVE OR instead of AND).

### [5] Define in advance what kinds of work can be realistically outsourced, and actively recruit external partners

Contrary to [50 years of industry experience](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary-ebook/dp/B000OZ0N6M), it’s easy to think that we can rent short-term talent to build long-term product success. If a customer will pay us for some custom work, we can just hire a team in Buenos Aires or Riga… build from their specs, drop it into our codeline, and celebrate. Architecture, ongoing support and product strategy be damned.

But there are some situations where this can work if **we think them through before our enterprise account team urgently escalates a deal to the CEO**. If this is a viable product, we have work to do – and exec-level agreements to make.

* If we do lots of complex integrations with aging enterprise applications, we could define/build/document an API to our data store. And train a few outside development partners in advance to use it. Then customers have a go-to team for their unique [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) needs – which they pay for separately, including annual support fees.
* We might have a white-label HR application that lets customers share videos internally. Building in color palette selectors and logo/branding customization and several video formats lets them (**or an outside marketing/content agency**) make our product look more like a custom solution.
* Product/engineering can recruit and train a few partners in advance, rather than during mid-deal scrambles. This reduces the temptation to hire random outsiders based on low prices and unrealistic delivery promises.

But each of these takes time/money/design/engineering/thought/ongoing work. Infinitely flexible systems are unusable – or never ship. So negotiating a **few** dimensions for “canned” customizations or extensions is essential. Everything else goes back into our infinite backlog, likely deprioritized forever.

Note that each of these **makes our trade-offs more obvious and shares some of the prioritization problem with non-product executives**. We break up the problem, reduce the cognitive load, and get bits of buy-in on partial solutions.

## Sound Byte

Prioritization is more than an analytical/intellectual exercise. It’s an organizational challenge with natural disagreements among stakeholders. Product leaders need to think about motivating the right kinds of participation and addressing the emotional issues that arise. Spreadsheets and models are necessary, but not sufficient.