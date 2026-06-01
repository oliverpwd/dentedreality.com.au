---
title: 'Shifting Modes: Creating a Program to Support Sustained Resilience'
date: '2021-08-14T12:03:21-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.infoq.com/articles/series-enhancing-resilience-2/
---

[Shifting Modes: Creating a Program to Support Sustained Resilience](https://www.infoq.com/articles/series-enhancing-resilience-2/)  



### Key Takeaways

* Incidents cannot be prevented because incidents are the inevitable result of success.
* Organizations must shift from a “prevent and fix” safety mode to a “learn and adapt” (Learn & Adapt) safety mode to manage reliability and resilience. This shift helps to more effectively cope with increasing complexity and scale.
* Finding advocates to help socialize the movement and communicating broadly are key aspects of creating a sustained shift to a Learn & Adapt mode.
* Normalizing behaviors — such as stating assumptions, asking more questions, increasing cooperation between diverse roles, and broadly sharing incident write-ups across the organization — help with the mode shift by increasing the flow of information.
* Developing the cultural traits of opportunity creation, flexibility, agility, and trust are necessary for an organization poised to shift to Learn & Adapt.

*To most software organizations,Covid-19 represents a fundamental surprise- a dramatic surprise that challenges basic assumptions and forces a revising of one’s beliefs (Lanir, 1986).*

*While many view this surprise as an outlier event to be endured, [this series](https://www.infoq.com/covid-resilience-article-series/) uses the lens of Resilience Engineering to explore how software companies adapted (and continue to adapt), enhancing their resilience. By emphasizing strategies to sustain the capacity to adapt, this collection of articles seeks to more broadly inform how organizations cope with unexpected events. Drawing from the resilience literature and using case studies from their own organizations, engineers and engineering managers from across the industry will explore what resilience has meant to them and their organizations, and share the lessons they’ve taken away.* 

*The first article starts by laying a foundation for thinking about organizational resilience, followed by a second article that looks at how to sustain resilience with a case study of how one service provider operating at scale has introduced programs to support learning and continual adaptation. Next, continuing with case examples, we will explore how to support frontline adaptation through socio-technical systems analysis before shifting gears to look more broadly at designing and resourcing for resilience. The capstone article will reflect on the themes generated across the series and provide guidance on lessons learned from sustained resilience.*


#### Related Sponsored Content

* ##### [Git Branching Strategies vs. Trunk-Based Development](https://www.infoq.com/infoq/url.action?i=6efaf1f1-146b-4083-887b-db8cd65089fc&t=f)

#### Related Sponsor

 [![](https://imgopt.infoq.com//fit-in/290x500/filters:quality(100)/filters:no_upscale()/sponsorship/topic/c4ab781f-986c-49a1-bce4-377892d31a2a/LaunchDaklyLogoRSB2021-1632130420725.png)![](https://imgopt.infoq.com//fit-in/290x500/filters:quality(100)/filters:no_upscale()/sponsorship/topic/c4ab781f-986c-49a1-bce4-377892d31a2a/LaunchDaklyLogoRSB2021-1632130420725.png)](https://www.infoq.com/infoq/url.action?i=187de8a8-27bd-4d77-8447-2111295486e3&t=f)

Get total control of your code to ship fast, reduce risk, and reclaim your nights and weekends. [**Book a demo today**](https://www.infoq.com/infoq/url.action?i=22a42045-cb32-45a2-b471-27ec78ba7871&t=f)!



Imagine for a moment that you work at a company that continuously ships customer-facing software. Say that your organization has managed to do the impossible and stopped having any serious incidents — you’ve achieved 100% reliability. Your product is successful. It’s fast, useful, usable, and reliable. Adoption increases, users desire new features, and they become accustomed to this success. As this happens, various pressures are continuously exerted on your organization — such as the pressure to ship features more quickly, the pressure to increase revenue, and the pressure to do more with less. Concurrently, there are additional constraints. Employees cannot be asked to work longer hours because work-life balance is a stated corporate priority. Given both this short-term success coupled with the constraints, what would happen over time?

Since employees are not spending time responding to incidents, engaging with retrospective activities, and delivering on action times in this highly reliable future, they’ll have more time to respond to those business pressures for greater efficiency. The tradeoff with having no incidents is that existing employees will fall out of practice on how to collaboratively work to respond to and understand their products in Production (aka [operational underload](https://sre.google/sre-book/being-on-call/#xref_oncall_underload).) Work will continue to increase in tempo, pace, and complexity. New employees will be hired and trained to account for the increase in workload. Unforeseen threats will act upon the system. Inevitably, there will be more incidents.

Incidents are a signal from the system that change is happening too quickly and that there are mismatches between people’s models of the system versus the actual system. Incidents are a buffer that stabilizes the pace of change. Success is the reason that you will never be able to truly prevent incidents according to the Law of Stretched Systems [[1](https://www.researchgate.net/publication/334267822_Steering_the_Reverberations_of_Technology_Change_on_Fields_of_Practice_Laws_that_Govern_Cognitive_Work)]. Embracing this inevitability will be the key to continued success in a climate of increasing complexity and interconnectedness.

What I’m witnessing in the software industry is that we’re getting stuck in a local maxima. We’ve plateaued in our approach to safety. I predict that if we don’t level up how we cope with increases in complexity and scale soon, we’ll be in big trouble.

At Indeed, we’ve recognized that we need to drive organizational change to maintain the success we’ve had and keep pace with changing complexity and greater scales. Over the last 16 years, Indeed has grown quickly and the pace of change has accelerated. Because we recognize the importance of getting this right, we are implementing a shift to a Learn & Adapt safety mode within our resilience engineering department.

In this article I will advocate that this mode shift is necessary in order to contend with the direction that the software industry is being pushed. I’ll describe the work necessary to enact this shift. Finally, I’ll compare the traits of an organization that is well poised for successfully persisting this mode shift. This shift won’t just make your organization safer, but also as Allspaw (2020) notes, “changing the primary focus from [fixing to learning](https://www.adaptivecapacitylabs.com/blog/2020/05/06/how-learning-is-different-than-fixing/) will result in a significant competitive advantage.”

## Different approaches to safety

Facing down this increase in complexity in scale requires escaping the local maxima. A change in how an organization works is necessary. The shift is away from the traditional “prevent and fix” mode that’s popular in software today. A prevent and fix safety mode is defined by a preoccupation with accident avoidance, strict controls, and a focus on what breaks.

![](https://www.infoq.com/articles/series-enhancing-resilience-2/articles/series-enhancing-resilience-2/en/resources/41image001-1610042325755.jpg)![](https://www.infoq.com/articles/series-enhancing-resilience-2/articles/series-enhancing-resilience-2/en/resources/41image001-1610042325755.jpg)

**Figure 1**

An organization preoccupied with this type of safety mode is not spending time focusing on how to adapt to surprise. The organization might also be spending a lot of time fixing things that don’t need the most attention. Sometimes preventative work can actually hinder opportunities for adaptations. For example, turning on [MySQL safe mode](https://dev.mysql.com/doc/refman/8.0/en/mysql-tips.html#safe-updates) in Production to prevent UPDATE statements without a WHERE clause might prevent a recurrence of this type of mistake. Safe mode can also stymie a DBA jumping onto the MySQL command line to make a critical repair during an incident.

By contrast, practicing a “learn and adapt” (Learn & Adapt) approach to safety means that encounters with incidents lead to an enhanced understanding of how normal, everyday work creates safety. Organizations that prioritize learning and adapting over preventing and fixing will also improve their ability to prevent and fix. I describe in more detail how that can lead to [safer operations](https://youtu.be/iED_PQhMJ7o) in a recent talk I gave at SREcon20 Americas.

![](https://www.infoq.com/articles/series-enhancing-resilience-2/articles/series-enhancing-resilience-2/en/resources/34image003-1610042326279.jpg)![](https://www.infoq.com/articles/series-enhancing-resilience-2/articles/series-enhancing-resilience-2/en/resources/34image003-1610042326279.jpg)

**Figure 2**

There appears to be a broad consensus from the [Resilience Engineering research literature](https://github.com/lorin/resilience-engineering) that the Learn & Adapt approach is superior to approaches aimed at accident avoidance and local fixes. A set of traits make some organizations more successful at this than others. [As article 1 in this series mentioned](https://www.infoq.com/articles/series-enhancing-resilience-1/), it’s unreasonable to expect anyone in an organization to have predicted the coronavirus pandemic, but it’s perfectly reasonable to anticipate and prepare for future encounters with surprise. It’s something that an organization can get better at over time with continuous focus and investment.

One example of achieving this mode shift is in how an organization approaches its incidents. In the prevent and fix safety mode, incidents are seen as evidence of poor team performance, poor product quality, or avoidable losses. One primary cause is uncovered through causal analysis techniques like The Five Whys. The analysis typically ends there. By contrast, Learn & Adapt promotes using incidents as a lens through which an organization casts a light on processes, decision making, collaboration, and how work gets done. This is accomplished using an incident analysis loop that focuses on at least 50% of the human factors.

This mode shift isn’t achieved by creating a new team, changing people’s titles, hiring the “right” person, or buying the “right” vendor product. It’s also not something that happens overnight. This mode shift requires the organization to change from within. It begins by sowing the seed of organizational change. Once the seed becomes a sapling, the organization can begin to achieve a continuous reinforcing loop of learning and adapting. This reinforcing loop requires constant nurturing and attention, much like caring for a delicate plant. The caveat is that the sapling can only emerge from the soil and thrive with the right mix of nutrients and the right environmental conditions. Many of those nutrients and conditions are related to organizational culture.

## Driving organizational change

My intense focus in this area was inspired by an experience I had years ago when I participated in a string of hour-long retrospective meetings. I was invited to these meetings because I was an SRE and a recognized subject matter expert in RabbitMQ — a factor in several of those incidents. What I noticed struck me as a missed opportunity.

In each of those meetings, over a dozen people were present in the conference room. In some cases, it was standing room only. It was a very expensive meeting. The facilitator went through the agenda, going over the timeline, the action items, and the contributing factors. It was a rote presentation rehashing what had happened, driven by the template document produced a priori. There was a call for questions, and the meeting ran to the end of the agenda within 25 to 30 minutes. We wrapped early. This was an opportunity where we had a lot of eager people in a room to discuss the incident, but I left the meeting without an improved or enhanced understanding about what happened. The facilitator followed the process faithfully, so I identified a problem with the process itself. I wanted to learn how to make this process more effective. And in pursuing this research, I found that there was so much more to learning from incidents than what I originally assumed.

Once I recognized that process change was necessary, I solicited viewpoints from co-workers on why we conduct retrospectives at Indeed. Reasons I heard are likely familiar to most software organizations:

* Find out what caused the outage
* Measure the impact
* Ensure that the outage never happens again
* Create remediation items and assign owners

While these answers reflect Indeed’s strong sense of ownership, it’s important to use these opportunities to direct efforts toward a deeper analysis into our systems (both people and technical) and the assumptions that we’ve made about them. When someone’s service is involved in an incident, there’s a concern that we were closer to the edge of failure than we thought we were. Priorities temporarily change and people are more willing to critically examine process and design choices.

These approaches to a different organizational culture at Indeed are still relatively new and are evolving toward widespread adoption, but early indications are promising. After a recent learning review where we discussed an incident write-up, I received this piece of feedback: “The write-up had interesting and varied content, effectively summarized crucial Indeed context, and demonstrably served as the basis for a rich dialogue. Participants revealed thoughtful self-reflection, openly shared new information about their perspective, refined their mental models, became closer as colleagues, and just plain learned cool things.”

I have made headway, but there is still a lot to do. While my efforts have benefitted from my tenure in the company, experience participating in hundreds of incidents, and connection to the research literature, I can also attribute some of my progress so far to three key organizational elements:

1. Finding other advocates in the company
2. Communicating broadly, and
3. Normalizing certain critical behaviors

### Find advocates

Advocates are colleagues who align closely with the goals, acknowledge where we could be doing better, and share a vision of what could be. They are instrumental to drive organizational change. Having multiple colleagues model new behaviors can help spur social change and create a movement. It’s very difficult to engage in this work alone. I’ve found these advocates and I wager they exist within your company as well. They are colleagues who keep an open mind and have the curiosity to consider multiple perspectives.

I found one such advocate during an incident in 2020 that I analyzed. In a 1:1 debrief interview with a responder who had only peripherally been involved, I asked why they had participated in a group remediation session. Their answer demonstrates that advocates aren’t created; they’re discovered: “I like to join just about every event [Slack] channel I can even when I’m not directly related. I find that these kinds of things are one of the best ways to learn our infrastructure, how things work, who to go to when things are on fire. Who [are] the people that will be fixing stuff? I learn a lot from these things. Like I said, even when it’s not my stuff that’s broken.”

Incident debrief interviewing is not the only place to locate advocates. I hold numerous 1:1s with leaders and stakeholders across the organization. I find opportunities to bring these topics up during meetings. I give internal tech talks and reach out to potential advocates whenever I visit one of our global engineering offices. Internal tech talks have the effect of drawing people out who have aligned interests or stories to share. They will make themselves known, perhaps by approaching you after the talk. You may find them to be advocates who can help socialize the movement within your organization. Indeed has offices all over the world, across different time zones. Advocates in each of those offices bring uniformity to the campaign.

### Communicating broadly

The second key component of driving organizational change is ensuring the messages are heard across the entire organization — not just within a single team or function. Organization size is an important influence when engaging in broad communication. A 10,000 person org poses different challenges than a 1,000 or 100 person org.

As much as I might think that I am sufficiently communicating the details of a new program, it’s rarely enough. I find that I have to constantly over-communicate. As I over-communicate and leverage multiple channels, I may sound repetitive to anyone in close proximity to my message. This is the only way to reach the far edges of the organization that might not otherwise hear me.

The same communication challenges present themselves in the aftermath of an incident when a team discovers and applies corrective actions. These are often “local-only” fixes, interventions, and lessons that only benefit the part of the organization that experiences the incident. The global organization fails to learn this (sometimes costly) lesson.

Ron Westrum, a researcher in organizational behavior, notes that, “One of the most important features of a culture of conscious inquiry is that what is known in one part of the system is communicated to the rest. This communication, necessary for a global fix, aids learning from experience, very important in systems safety. The communication occurs because those in the system consider it their duty to inform the others of the potential danger or the potential improvement.” [[2](https://qualitysafety.bmj.com/content/13/suppl_2/ii22.short)]

It’s not enough for a team to capture and address important technical fixes and lessons learned in their retrospective materials. Allspaw (2020) spent two years observing how software organizations engage with incidents and found that “hands-on practitioners do not typically capture the post-incident write-up for readers beyond their local team” and “do not read post-incident review write-ups from other teams.” [[3](https://www.adaptivecapacitylabs.com/blog/2020/07/16/presentation-findings-from-the-field/)]

The organization doesn’t truly benefit until those lessons are scaled far and wide. For the write-ups to be useful, they have to teach the reader something new and help draw out the complexities of the incident.

### Normalize new behaviors

Organizational change involves new modes and behaviors. Some of those modes and behaviors might be at odds with how things used to be done. Or they are just non-intuitive. This places a barrier on reaching a critical mass in these desired behaviors. A good place to get started is by modeling the changes yourself. Normalizing these modes and behaviors will help them spread to early adopters and then spawn a social movement. I’ve found there are four main areas to focus on to successfully promote a Learn & Adapt mode to safety.

#### 1) Normalize stating your assumptions as much as possible

Assumptions are beliefs you hold that are sometimes so obvious or (seemingly) self-evident that stating them explicitly doesn’t seem necessary. It’s very likely that what you think is obvious might be surprising to others. For example, you might believe that the fact that the MySQL primary can’t safely fail over to another datacenter automatically is so obvious as to not be worth explicitly stating often. In reality, your colleague might believe the exact opposite.

Stating your assumptions gives others an opportunity to recalibrate their model if there’s a mismatch or vice-versa. The conversations between a group of people recalibrating their models of the system are some of the most insightful conversations I’ve experienced. Great places to state your assumptions are in design review materials and in merge requests. What do you assume will happen in the presence of 10% packet loss? What about 50% packet loss? Do you assume that system clocks are always monotonically increasing? Do you assume that your consumer services will never encounter duplicate messages? What do you assume might happen if they do encounter duplicates? Stating these assumptions explicitly will elicit important conversations because participants in these reviews will come with their own assumptions about what you assumed about your design. There’s no impetus for participants to challenge your assumptions if they assume yours matches theirs.

#### 2) Normalize asking a lot of questions

This is another approach that can help surface mismatched models of the system. Curiosity is an important cultural trait that nurtures Learn & Adapt. You might worry that asking questions betrays a surprising gap in your knowledge, but if everybody asks a lot of questions, it takes the sting out of asking them.

Asking questions can also help promote a more psychologically safe workplace. Discussing technical topics in front of an audience of peers can be stressful. Everybody has errors somewhere in their mental models and you’re bound to surface those through discussions. The way that those errors are revealed to you are reflected by the cultural norms of your organization. Telling a colleague, “Well actually there are several problems with what you just said…” has a chilling effect on their willingness to state their assumptions in the future. Even if you’re certain that somebody is wrong, be curious instead of corrective.

Ask follow-up questions to reveal more of their mental model: “Did you notice any deprecation warnings at compile time?” Posing the mismatch as a question instead of a correction will lead to a more productive and psychologically safe exploration of the problem space. It also makes room for you, the corrector, to be incorrect, which also promotes an aspect of psychological safety.

#### 3) Normalize increased cooperation between roles that traditionally don’t directly work together

A great example of this is product/engineering, and client-facing roles (like customer support or client success). Invite members of those teams to design reviews. Invite them to retrospective meetings or group learning reviews. Sometimes the client-facing support teams are the very first people in an organization to learn about a serious problem. The time between client-facing teams discovering the issue and the product teams learning about them is critical. The work needed to shorten that delay has to happen before the incident occurs, not during.

There was an incident in 2019 that was first detected by the client success team. During the interview phase of the incident analysis, I asked a product manager about how their team directly engages with the client success team. Their response was dismissive of the idea at first: “I don’t think that a sufficient solution for [this incident] should be relying on [customer] feedback to let us know of an issue. It’s too slow of a mechanism to help us identify a high impact issue.”

The corrective action for this incident was to add automated detection. While that corrective action will help detect a recurrence of the same impact, it misses an opportunity to work on better engagement and cooperation with the customer-facing teams. Incidents with impact that evade the existing detection in the future will take longer to resolve.

#### 4) Normalize sharing incident analysis deliverables with everyone in the company

Sharing and discussing incident write-ups is arguably the most important aftermath activity. The [STELLA report](http://stella.report/) delivered by the first cycle of the SNAFUcatchers Workshop on coping with complexity highlights this value: “Postmortems can point out unrecognized dependencies, mismatches between capacity and demand, mis-calibrations about how components will work together, and the brittleness of technical and organizational processes. They can also lead to deeper insights into the technical, organizational, economic, and even political factors that promote those conditions. Postmortems bring together and focus significant expertise on a specific problem for a short period. People attending them learn about the way that their systems work and don’t work. Postmortems do not, in and of themselves, make change happen; instead, they direct a group’s attention to areas of concern that they might not otherwise pay attention to.”

## Cultural traits

Moving from a prevent and fix safety mode to Learn & Adapt involves changing the very nature of how organizations get work done. If your organization is already relatively successful at delivering products to customers, then making changes to the organization can be risky or even ill advised. Change must be deliberate, incremental, and continuously monitored if it is to result in a net benefit.

While the idea of a “safety culture” is problematic, there exists a connection between an organization’s culture and its ability to successfully prepare for surprise, navigate complexity, and learn from incidents. Culture is, as defined by Westrum (2004), “…the organisation’s pattern of response to the problems and opportunities it encounters.” [[2](https://qualitysafety.bmj.com/content/13/suppl_2/ii22.short)] These patterns are informed by the shared set of behaviors, beliefs, and actions promoted and encouraged in an organization. A cultural norm might be obligating people to “own” their mistakes by expecting a set of follow-up behaviors in the aftermath of an incident.

In reflecting on the cultural norms within my own organization, I’ve identified some tradeoffs we’ve made that have helped cultivate and promote this shift toward Learn & Adapt.

### Opportunity over obligation

How accountability and responsibility are handled in an organization is one aspect of the cultural norms. After a costly incident, a lot of attention is cast upon the parts of the system seen as broken or faulty. If there are considerable losses involved, a common reaction is to isolate a person or team to take responsibility and show accountability for the recovery and prevention activities.

People engage with a task differently when they feel it’s an obligation versus an opportunity. Opportunity is taken whereas obligation is assigned (whether explicitly or implicitly.) It is leadership’s role to highlight opportunities by making them attractive, clearly defined, and actionable.

One way to make opportunities more attractive is to change the incentive structures. Ryn Daniels, a software infrastructure engineer, describes a leverage point for [crafting a resilient culture](https://www.infoq.com/articles/crafting-resilient-culture/): “While there is a lot that goes into psychological safety in the workplace, one way to design for a culture of learning and blamelessness is to look at the incentive structures within your organization.” Instead of expecting people to own their post-incident activities, strive to make the opportunity attractive enough for anyone to select. Ryn suggests a strategy: “If your skills matrices for promotions include things like community contributions, post-mortem facilitation, or incident writeups, that can also provide incentive for people to take part in learning-focused activities. The behaviors that get rewarded and promoted within your organization will have a great deal of impact on its culture.”

Creating opportunities instead of assigning ownership not only helps ensure more thorough results, but fosters psychological safety.

### Flexibility over rigidity

Placing rigid constraints on decision-making, new technologies, access, and what people are allowed to do in delivering their work can hinder opportunities for adaptation by undermining sources of resilience. These constraints accumulate over time as scar tissue from previous encounters with costly outages.

Rigid constraints can help an organization navigate legal risk, security risk, and financial risk, but they can limit flexibility. More flexibility can prove useful for adaptation because it gives people space to be curious and exercise their interests in other roles. How does the organization respond to a database administrator giving unsolicited help to the security team? What about a data scientist participating in a code review when it’s unrelated to their work or product? Being told to “stay in your lane” can be a manifestation of cultural norms that bias toward rigidity and could be a reflection of people’s insecurities, previous encounters with failure, or fear there is more work to do than available bandwidth. Fostering this flexibility can pay immense dividends when expertise emerges during an incident in an unexpected way.

### Agility over speed

One of the most important engineering priorities at Indeed is velocity, which is the shortening of the development cycle from idea to delivery. While speed is important in the delivery of software, speed isn’t sufficient to adapt to unanticipated challenges. “Turning the ship” is a common metaphor to highlight the challenges of quickly changing direction as a function of organization size and speed. Agility is a trait that is useful in helping recognize when to change course and accept the sunk costs. In an incident, agility could mean recognizing and escaping cognitive fixation during diagnosis. After an incident, agility could result in the local participants sharing what they’ve learned so that the global organization can take heed and quickly recruit resources by pulling them from less important projects. Agility is a necessary (but not sufficient) aspect of promoting a Learn & Adapt approach to safety.

### Trust over suspicion

Trust is fundamental to an organizational culture that learns and adapts. Trust colors our interpretations when we witness the actions of others when we don’t have the benefit of context. Trust means that we can assume that others are acting in good faith. Sometimes it can be easy to jump to anger or disgust with our colleagues when we are armed with hindsight in the aftermath of an incident. Trust means that we allow that they may have encountered substantial challenges. In a low-trust environment, fear, judgement, sanction, rigidity, and blame are common coping mechanisms.

## Making the shift

In the course of introducing these new approaches in my own organization, I sometimes encounter pushback about how engaging in incident analysis distracts from getting “real” work done. I remind them that this is the real work. Engineering is knowledge work and requires continual learning.

Not only does engaging in incident analysis help people get better at their job as they learn more, but incident analysis is a form of knowledge creation. Ralph D. Stacey, an organizational theorist, helped me make the profound observation that simply filing away an incident report is not new knowledge: “From mainstream perspectives, knowledge is thought to be stored in individual heads, largely in tacit form, and it can only become the asset of an organization when it is extracted from those individual heads and stored in some artifact as explicit knowledge.” Incident write-ups do not become organizational knowledge until they are actually used: “Knowledge is the act of conversing and new knowledge is created when ways of talking, and therefore patterns of relationship, change. Knowledge, in this sense, cannot be stored.” [[4](https://www.researchgate.net/publication/232992375_The_Emergence_of_Knowledge_in_Organization)] Knowledge is created when a group of people meet to discuss a well-crafted incident write-up. Knowledge is created when it is communicated broadly and reinforced through normalized behaviours.

Incidents cannot be prevented, because incidents are the inevitable result of success. Organizations that have the cultural elements to foster a Learn & Adapt mode to safety will embrace the desirable aspects of incidents. Incidents can lead to bridging new connections, engaging with fresh perspectives, surfacing risks, and creating new training material.

If you’re part of an organization that considers incidents avoidable, detestable, or disruptive, it’s likely that you’ll need to change more than just the retrospective process. Start small, mirror the behaviors that cultivate Learn & Adapt, and be patient. Before long, a sapling will emerge.

## References

1. Allspaw, J. (2020). [How learning is different than fixing](http://%C2%A0https://bit.ly/learning-not-fixing). (Adaptive Capacity Labs blog.) (video). Accessed Oct. 20, 2020.
2. Daniels, R. (2019). [Crafting a Resilient Culture: Or, How to Survive an Accidental Mid-Day Production Incident](https://www.infoq.com/articles/crafting-resilient-culture/). (InfoQ: DevOps.). Accessed Dec 28, 2020.
3. Elman, A. (2019). [Improving Incident Retrospectives at Indeed](https://www.learningfromincidents.io/blog/improving-incident-retrospectives-at-indeed). (Learning from Incidents in Software blog.). Accessed Oct. 20, 2020.
4. Elman, A. (2020). Are We Getting Better Yet? Progress Toward Safer Operations. In USENIX Association SREcon Conference, USA.
5. Schemmel, M. (2019). Obligation vs Opportunity. (Internal Indeed Engineering blog.) Unavailable. Accessed Oct. 20, 2020.
6. Spadaccini, A. (2016). Being On-Call. In Site Reliability Engineering: How Google Runs Production Systems. Sebastopol, CA, USA: O’Reilly Media, Inc. First Edition, ch. 11, pp. 125-132.
7. Stacey, R. D. (2001). Mainstream Thinking about Knowledge Creation in Organizations. In Complex Responsive Processes in Organizations: Learning and knowledge creation. London, England, UK: Routledge.
8. Westrum, R. (2004). A typology of organisational cultures. In Quality & Safety in Health Care, 13, ii22-ii27. 10.1136/qshc.2003.009522
9. Woods, D. D. (2002). Steering the Reverberations of Technology Change on Fields of Practice: Laws that Govern Cognitive Work. In Proceedings of the Twenty-Fourth Annual Conference of the Cognitive Science Society. pp.14-16 10.4324/9781315782379-10.
10. Woods, D. D. (2017). [STELLA: Report from the SNAFUcatchers Workshop on Coping With Complexity](http://stella.report/). Columbus, OH: The Ohio State University.

## About the Author

**![](https://www.infoq.com/articles/series-enhancing-resilience-2/articles/series-enhancing-resilience-2/en/resources/1alex-elman-1610042325375.jpg)![](https://www.infoq.com/articles/series-enhancing-resilience-2/articles/series-enhancing-resilience-2/en/resources/1alex-elman-1610042325375.jpg)Alex Elman** has been helping Indeed cope with ever-increasing complexity and scale for the past nine years. He is a founding member of the Site Reliability Engineering team. Elman leads the Resilience Engineering team focused on learning from incidents, chaos engineering, and fault-tolerant design patterns.

*To most software organizations,Covid-19 represents a fundamental surprise- a dramatic surprise that challenges basic assumptions and forces a revising of one’s beliefs (Lanir, 1986).*

*While many view this surprise as an outlier event to be endured, [this series](https://www.infoq.com/covid-resilience-article-series/) uses the lens of Resilience Engineering to explore how software companies adapted (and continue to adapt), enhancing their resilience. By emphasizing strategies to sustain the capacity to adapt, this collection of articles seeks to more broadly inform how organizations cope with unexpected events. Drawing from the resilience literature and using case studies from their own organizations, engineers and engineering managers from across the industry will explore what resilience has meant to them and their organizations, and share the lessons they’ve taken away.* 

*The first article starts by laying a foundation for thinking about organizational resilience, followed by a second article that looks at how to sustain resilience with a case study of how one service provider operating at scale has introduced programs to support learning and continual adaptation. Next, continuing with case examples, we will explore how to support frontline adaptation through socio-technical systems analysis before shifting gears to look more broadly at designing and resourcing for resilience. The capstone article will reflect on the themes generated across the series and provide guidance on lessons learned from sustained resilience.*