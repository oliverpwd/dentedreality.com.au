---
title: A domain-based structure for software engineering teams | by Ryan Fox | Snapcommerce
  | May, 2022 | Medium
date: '2022-07-11T09:22:10-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/snaptravel/a-domain-based-structure-for-software-engineering-teams-faab1b3428fb
---

[A domain-based structure for software engineering teams | by Ryan Fox | Snapcommerce | May, 2022 | Medium](https://medium.com/snaptravel/a-domain-based-structure-for-software-engineering-teams-faab1b3428fb)  



## How we’re structuring squads to grow individual contributors into tech leads


![](https://miro.medium.com/max/1400/1*dA8DQsK_cjnog-w2VWQ5Zg.jpeg)![](https://miro.medium.com/max/1400/1*dA8DQsK_cjnog-w2VWQ5Zg.jpeg)

In early 2021 at [Snapcommerce](http://www.snapcommerce.com), we had 25 engineers working in squads. Each squad had an engineering manager (EM) acting as the people and tech lead (TL) for all projects, a product manager (PM), a designer, a QA team member, and up to 7 individual contributor (IC) engineers. For engineers, growing as an IC into a TL could be a challenging or unclear path. Having one TL per squad wasn’t creating a natural growth opportunity for ICs to develop their technical leadership and ownership skills.

Some of the other challenges our squads had with the structure included:

* **Lack of focus:** Our sprints were more of a blended mix of high-priority tasks as opposed to working towards well-defined sprint goals
* **Too much time spent in meetings:** Everyone was present for all squad agile meetings (standups, sprint planning, and backlog grooming) but only a portion of the meetings were relevant to their work and expertise
* **Shared OKR ownership:** Responsibility for delivering on the squad’s OKRs was shared among the squad, which often led to a missing sense of accountability
* **Single points of failure:** There was not a conscious effort to ensure single points of failure did not naturally develop
* **Flow of value being blocked:** The structure of implications grew beyond the point where the EM or any one person could hold it all in their head; there was a clear need for more distributed expertise

Our solution was to organize our squads into a domain-based structure that we’ll discuss below.It has helped with the squad and organization’s overall success, while also structuring and increasing our IC growth opportunities.

Since rolling out the domain-based structure, we’ve doubled our team size to more than 50 engineers and we crossed $1 billion in sales in Q1 2022. Here’s how we’re using a domain-based squad structure to scale our software engineering team:


# The function and structure of domains

A **domain** is a squad focus area or specialization. By having multiple domains per squad, squads can subdivide their efforts to focus on different business, product, or technical focus areas. Each domain typically encompassed one or more OKRs or epics.

![](https://miro.medium.com/max/1400/1*Mv8woyiOyugbIt7UDIpKNA.jpeg)![](https://miro.medium.com/max/1400/1*Mv8woyiOyugbIt7UDIpKNA.jpeg)

Each domain consists of the following roles:

* **Domain Lead** (DL)  
  The engineer responsible for the success of the domain. They work alongside the PM to lead planning meetings, rituals, and implementation. It’s a technical leadership opportunity, in that they function as a domain TL, helping assign work within the domain. It’s not a formal mentorship or leadership position, and it’s usually filled by an intermediate or senior engineer on the squad.
* **Domain Contributors** (DC)  
  The engineers that contribute to the domain when it comes to planning meetings, rituals, and implementation. There will be at least one per domain, and an engineer can simultaneously be the DL for one domain and a DC for another, or be a DC in more than one domain.

I developed domains from first principles by looking at our frustrations with traditional squads and seeing an opportunity for improvement. There is literature coming out about similar structures, such as [Team Topologies](https://teamtopologies.com/key-concepts). Domains relate to stream-aligned topology, which is where a work stream aligns with a business domain. They both drive simplified, fast flow communication within a domain.


# Domain structure benefits

Dividing our squads into domains has led to the following benefits:

* **Multiple ICs can grow their TL skills**In contrast to just one TL per squad, there are as many DL positions as there are domains (typically 3–4 per squad). The DLs get exposure to leading agile ceremonies, and engineers have a greater sense of ownership and grow more quickly within the structure. We’ve seen engineers grow into senior engineers, and senior engineers become managers.
* **Reduced meeting time**   
  With domains, not only are we meeting less (because agile ceremonies are organized at the domain level), but meetings are more focused and relevant to individual work. The meeting time per engineer is reduced to M / N, where M is the number of domains they are in and N is the total number of domains on the team. For example, if the squad has 4 domains (N=4) and each engineer is part of at most 2 domains (M=2), then they should spend approximately 50% less time in meetings compared to the traditional squad model.
* **Reduced single points of failure**In our previous squads, ICs would tend to develop into single points of failure / knowledge silos, since many would end up working on projects by themselves. With more than one engineer in a domain, no one should be working alone. We’ve increased collaboration and knowledge sharing, and we’ve lowered the bus factor.
* **Avoid overloading a single manager**Expecting a single EM/TL to know everything for an entire squad can overwhelm them or lead to oversights. With domains, there’s multiple DLs in the squad who are each responsible for leading their domain and distributing work within it. The EM supports the DLs.
* **Greater sense of ownership**  
  As squads, there is shared ownership of team OKRs. Domains create a dedicated group of engineers with the greatest context, ownership, and continuity for that area. At Snapcommerce, it added clarity for the business teams as far as who to reach out to, and many teams were happy to have a domain focused on their initiative.
* **Balances sustainability and productivity**Knowledge sharing helps us grow sustainably and avoid silos, but end-to-end ownership drives productivity. With domains, we tweak this balance based on how many domains an engineer is in. Not every person needs context on everything we have oversight on; instead they can be deep in a subset of the oversight, but not as a single point of failure.
* **Sense of close collaboration and goal-oriented delivery**  
  Now we have smaller units of engineers with a stronger sense of shared ownership and collaboration, rather than a big team where some people end up working alone in order to distribute our efforts across business needs. Our best practice for squad sprint goals is that each domain gets its own highly focused goal with clear ownership.

# Domain challenges

Our first experience with domains was finding success rolling them out in our [data & analytics organization](https://medium.com/snaptravel/how-should-our-company-structure-our-data-team-e71f6846024d). This gave us some experience with the challenges of establishing domains, such as:

## Defining the domains well

Domains tend to be organized in line with OKRs, however it’s preferable for domains to outlive quarter boundaries to have more tech leadership continuity and build up of expertise.

It’s also necessary to think critically about defining domains, whether based on product lines, objective lines, or technical/architecture lines. A highly technical organization that has infrastructure or architecture as a competitive advantage will likely need to define domains on technical lines, because it needs deep expertise in a narrower area. Startups and business-delivery organizations are more likely to define domains on product or objective lines.

## Formalizing documentation for team structure

Naturally, domains create a slightly more complex structure at the squad level, which requires clear documentation of the domains, as well as their DLs and DCs. The key is to create a team charter or similar document that clearly states what the domains are and who is a part of each of them. Luckily, all the engineers still report to the EM, so the reporting structure remains simple.


# Conclusion

We’ve structured our engineering squads with domains for more than a year now, as our engineering org has doubled in size. We’ve seen ICs develop in ways the old structure didn’t allow. Our squads have improved their productivity, sustainability, collaboration, focus, resiliency, and ownership.

Domains also bring flexibility to our organization. There’s more mobility in the individual engineer’s career path, as they can move between domains as their interests change and develop. For organizations using [Spotify’s tribes and squads](https://www.atlassian.com/agile/agile-at-scale/spotify) model like we do, domains also increase flexibility at the squad level. If the organization wants to devote more resources and work to a domain, that domain can naturally bifurcate into a new squad with further specific domains.

As engineering teams continue to look for topological or systems approaches to organizational design, we’re pleased to be able to share our experience developing this simple way that our teams can operate in our complex technical environment. It’s been a worthwhile investment at Snapcommerce and we hope to see more organizations adopt it.

Interested in leading your own domain? We’re hiring.

[Snapcommerce Careers](https://www.snapcommerce.com/careers)

If you want to read more — check out and follow our [Snapcommerce publication](https://medium.com/snaptravel) here on Medium.


# Acknowledgements

Thank you to **Matt Culver** for reviewing this article and offering great suggestions for improving it.