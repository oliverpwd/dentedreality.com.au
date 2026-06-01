---
title: On Workplace Productivity – Future
date: '2021-06-25T23:09:14-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://future.a16z.com/on-workplace-productivity/
---

[On Workplace Productivity – Future](https://future.a16z.com/on-workplace-productivity/)  



What does it mean to be productive? At the beginning of the pandemic, when many workers went remote, some managers were tempted to start counting things — whether hours, objects, or other things. But they’re about 100 years and two industrial revolutions too late: In the mechanical and electrical revolutions, productivity was indeed a measure of output, and it helped drive the economy. We created cars, machines, widgets by successfully [measuring things](https://www.oecd.org/sdd/productivity-stats/40526851.pdf) this way. 

But most economies are well beyond that type of measurement mindset now, with companies and even national economies (measured by GDP) relying on knowledge work and efficiencies from digital technologies to power all our systems, whether healthcare and banking or retail. It’s not just a mindset of efficiency, though, but one of abundance. Consider taking pictures: Doing so used to be relatively expensive and more scarce (film, not bits), so the number of pictures taken and printed could be considered a measure of productivity. But when everyone can take pro-grade pictures on their phones, immediately view them, and store them for practically free, improved productivity is not about taking more pictures. It’s more about the opportunities that are unlocked from having the huge amount of pictures — for example, the field of medicine using photos to diagnose cancer earlier (via machine learning).

And yet, if we were to measure that productivity of cameras by output, it wouldn’t tell us anything about consumer well-being let alone GDP. The economist Hal Varian has been trumpeting the horn about this so-called “[productivity paradox](https://www.aei.org/economics/googlenomics-a-long-read-qa-with-chief-economist-hal-varian/)” for years, [as have others](https://www.wsj.com/articles/silicon-valley-doesnt-believe-u-s-productivity-is-down-1437100700) who are at the forefront of modern economic research and value creation. But now that our baselines for remote, cloud-based, distributed work have accelerated, the question of how we *value* work (and the systems powering this work) means we must shift how we measure and think about productivity, finally going beyond the relics of the past. 

If leaders and managers want to be able to make decisions or understand what is happening in their systems (or among their workers), they have to use better measures. Measures matter: they change our focus and our behavior. But when you use only one or even a few activity-based metrics about what workers do — lines of code, number of commits, number of private repositories — you don’t actually know what’s happening; it’s not enough to make an informed decision or move the needle. 

To understand, reason about, and improve complex multidimensional work and systems, we must have multidimensional measures. 

## A framework for measuring workplace productivity

Even the most advanced AI systems require humans in the loop, drawing on their creativity, ingenuity, or just their willingness to classify pictures for hours (so we can have better search results or predictive algorithms). If we ignore the well-being of the people running these systems, fatigue and burnout result. An overly simplistic or reductionist take — where leaders measure only one dimension — will break the system. And when things fail in complex systems, they often fail in messy, difficult, spectacular ways. 

Workplace surveys or assessments aren’t enough; they don’t tell us *how* to improve. The same is true for telemetry: Recording or transmitting from the tools we use can tell us how fast teams are submitting code, or how fast (or slow) a test suite is running. But in isolation, this data can’t tell us what is actually slowing down our teams, help us understand our development environment, or what factors would allow us to improve test execution and run times. 

A more holistic framework for productivity — one that reveals a fuller picture — must include several dimensions, including satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. It can be summarized by the acronym [SPACE](https://queue.acm.org/detail.cfm?id=3454124). And while I focus on developer and IT productivity here (something I’ve spent over a decade [measuring across organizations](https://a16z.com/2018/03/28/devops-org-change-software-performance/) of all types), the reality is that developer work [is creative](https://a16z.com/2021/01/12/rise-of-developers-creative-class-company-innovation-ask-a-developer-book/) work, so much of this framework can also be applied beyond developers. 

**Satisfaction and well-being** captures how fulfilled and happy people are with their work or the systems they use to do their work, and how that work affects them. These signals are intrinsically tied into how we typically think of productivity, with several studies showing that satisfaction is correlated with output, and may be a leading indicator for increases in work — such as output and innovation — and for decreases, such as burnout and its impacts on work. But these measures are about much more than how happy a person is; satisfaction and well-being are about how people and teams work together to create value. It’s also about how well we can work with our systems, in the context of technology. For example, creating a superior developer experience allows companies to develop and deliver software faster, whether that’s new features to customers and end users, critical digital infrastructure, or patching security vulnerabilities in systems.

**Performance** measures outcomes — how well a system or process performs — and includes metrics like quality, speed, and impact. These measures are often excluded from how we think about productivity. But if we want to use data to make decisions or improve, performance is essential to understanding if our work efforts had the desired, intended effect. 

**Activity** measures a count of things that are done. These are the most common productivity measures, because they’re the most familiar due to their historical familiarity, and are also the most easily automated. However, it’s almost impossible to fully capture the multidimensional and complex nature of work based on the number of things submitted/done/clicked. Our systems are rife with blind spots and inconsistencies, and therefore not even that good at these easy, automated counts. 

**Communication and collaboration** is about how people and teams work together, and it may be the most overlooked dimension in the framework. (Relatedly, pioneering workplace anthropologist Lucy Suchman’s early studies of “[invisible work](https://dl.acm.org/doi/10.1145/223248.223263)” also highlighted the importance of unearthing underlying work practice, because the ways people work and how that work supports team productivity are not always apparent.) Talking and connections are often not “counted” in traditional measures of productivity. Communication and collaboration also needs to include system documentation that allows for easy use and sharing, as well as modular system design and searchability, which enables developers to find, share, and reuse code. 

**Efficiency and flow** capture progress in work; this can include measures of time or speed through a system, number of handoffs, interruptions, and one’s ability to stay “in the flow”. Efficiency is also very related to all the other dimensions outlined above: Better flow is correlated with increased satisfaction, for instance. Balancing efficiency becomes critical when we consider the other factors. For example, optimizing for individual flow by reducing interruptions and maximizing coding time can block others’ work and interrupt overall team flow by making others wait for code or design reviews. Or, maximizing flow through a system could be taken to an extreme, with teams opting to push all code to production by default, regardless of testing or defects found, increasing the number of errors and bugs found by customers. 

All of the above metrics should be customized and changed based on shifting team/ organizational priorities or needs. Simply adopting the same standard set of metrics may be handy for a baseline, but if your data doesn’t help you make critical decisions — or if it focuses your developers’ attention on the wrong things, shifting their behavior the wrong way — these measures, just like any others, can work against you. 

## Remote development, collaboration, and productivity

How did knowledge workers (again, primarily developers) do on these measures during the pandemic? COVID-19 and work-from-home lockdowns provided an unprecedented opportunity to measure how people work in highly uncertain conditions, as well as remote ones. For instance, research I led [with GitHub](https://octoverse.github.com/) last year [showed that](https://octoverse.github.com/static/github-octoverse-2020-productivity-report.pdf) teams worked longer hours and pushed more code compared to the year before, across four time zones around the world: UK Time Zone, US Eastern Time Zone, US Pacific Time Zone, and Japan Standard Time Zone. 

Using “push window” — the time between first and last push to a developer’s main branch or repository — as a rough approximation of time spent working, we saw developers across all time zones working longer compared to the previous year when lockdown started, with many developers working 10-20 minutes more per day, and then jumping to 60-80 minutes more per day during June and July 2020.

[![](https://future.a16z.com/wp-content/uploads/2021/06/Forsgren_Workplace_Productivity_Push_Window_Work_Volume-1024x474.jpg)![](https://future.a16z.com/wp-content/uploads/2021/06/Forsgren_Workplace_Productivity_Push_Window_Work_Volume-1024x474.jpg)](https://future.a16z.com/wp-content/uploads/2021/06/Forsgren_Workplace_Productivity_Push_Window_Work_Volume.jpg)

In other words: people were working more as the pandemic went on.

To see if this was just developers spreading their work out while they adjusted to new work routines and schedules, we looked at how much work they did, using the number of pushes as a rough proxy. Again, we saw largely consistent work compared to the previous year across the time zones we studied, with some showing jumps until it leveled out — but we didn’t observe any notable decreases. 

But this work doesn’t happen in isolation; development is about collaboration. And even in a year with our routines upended, developers collaborated more, and faster. One of the major ways that developers collaborate is through pull requests. Merging a pull request involves a group of developers on a project reviewing changes, discussing the code, and sometimes following up with additional commits; finally, the pull request is merged. To proxy this collaborative process, we measured how long it took teams to merge pull requests and compared it to the previous year.

Open source teams, who have been used to working and collaborating remotely, started merging code 3.5 hours faster in April as lockdowns started happening, and throughout the rest of 2020 ranged from 1-7 hours faster compared to the year before. Even teams working in more traditional workplace settings saw faster collaboration, with initial improvements to merge time in April jumping about one hour, then ranging from two hours slower to five hours faster, with most time periods showing improvement compared to the year before.

[![](https://future.a16z.com/wp-content/uploads/2021/06/Forsgren_Workplace_Productivity_Pull_Requests_For_Open_Source_Projects-1024x410.jpg)![](https://future.a16z.com/wp-content/uploads/2021/06/Forsgren_Workplace_Productivity_Pull_Requests_For_Open_Source_Projects-1024x410.jpg)](https://future.a16z.com/wp-content/uploads/2021/06/Forsgren_Workplace_Productivity_Pull_Requests_For_Open_Source_Projects.jpg)

At a quick glance, one could walk away from this data and declare “productivity is up!” 

However, we also know that continued work under pressure isn’t sustainable. Recent findings [from the 2021 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/hybrid-work) — based on a Microsoft study of more than 30000 people in 31 countries and on an analysis of trillions of productivity and labor signals across Microsoft 365 and LinkedIn — highlighted that “high productivity is masking an exhausted workforce”. The report also noted that over 40% of the global workforce is considering leaving their employer this year. 

If we don’t seriously consider reevaluating how we measure — and therefore better target fixes to — our productivity problem, we won’t have a productivity problem to think about.

Remote work has taught us some things. On one hand, we learned how to support entirely new ways of working (many companies doing so practically overnight): We can create teams with people from anywhere, using technology to support flexible solutions. Organizations are borrowing playbooks from open source — the original playground of distributed development, where collaborators are not in the same organization let alone location — and repurposing those for fast, high-trust, collaborative work. We can push to the cloud and optimize for clean, fast tooling and intuitive developer experiences that enable them to create solutions — even if they don’t realize they’re “developers”, because the emergence of low-code and no-code tools are making it possible for everyone to use technology to build. 

On the other hand, we need to account for this in our measures. Doing the complex work that goes into our knowledge and digital economy is more than just sitting in a chair, dialing into a Zoom meeting, or pushing more lines of code. It involves creativity and problem solving; a mix of collaboration plus focus time; and balancing both individual and team needs to deliver the best outcomes. Most of our measurement systems aren’t ready for complete telemetry, and some things are best measured [by asking people](https://queue.acm.org/detail.cfm?id=3182626), not the tooling — because only people can tell you what it’s like to build systems, and only people can reveal the blind spots in your systems. 

Remote work has also really highlighted that [productivity is personal](https://arxiv.org/abs/2008.11147) — some people thrived in the shift to working from home, while others really struggled. 

## Productivity is personal

So far, I’ve been focusing on the manager/ organizational lens into the question of how best to measure productivity. But there’s a personal lens, too. In a [recent study](https://github.blog/2021-05-25-octoverse-spotlight-good-day-project/) (published just a few weeks ago) Eirini Kalliamvakou and I conducted, we asked if developers care about productivity and how we can help them improve it. 

We found that they distrust the word “productivity”, and wanted reassurance that the project and data would be private, after a year of being watched and tracked. But they all loved the idea of having better insight into their work, and a way to have “good days” more often. Since the two-week study invited GitHub developers to take a quick survey at the end of their day to ask about their work (based on the SPACE framework), and matched it to their engineering data, we showed them patterns and hints to improve their days. Some things we found:

* **Finding flow is key, and interruptions are a drag.** Minimal or no interruptions give developers an 82% chance of having a good day, but interruptions throughout the day decrease the chance of a good day to just 7%.
* **Meetings are both awesome and terrible.** Collaboration improves our work, but too many meetings can be a blocker; going from two to three meetings per day lowered the chances of making progress toward their goals by 60%.
* **A two-minute daily reflection can help improve your days**. Developers reported that daily reflection was a great new habit, and seeing patterns gave them clear ideas for what to change in their days.

Other research has found that developers who [use reflections](https://www.zora.uzh.ch/id/eprint/174225/1/2019-goalsetting-prePrint-TSE19.pdf) improve their productivity and well-being, and reflections towards the end of the day tend to be less stressful compared to setting goals at the beginning of the day. Quick, daily surveys and reflections offer high-fidelity data while minimizing disruptions. This shows us the power of personal metrics, assuming we get privacy and trust right as well. 

\* \* \*

Once the knowledge workforce went home — out of sight, but definitely not out of mind — many managers who had used physical presence in the office to reassure themselves that their teams were working now struggled to find ways to communicate that work and progress. Their prior methods of “monitoring” were gone. 

But were those methods really any good to begin with? Tracking hours or widgets isn’t what signals an individual’s or a team’s productivity — and in fact, studies have shown that these naive metrics can be gamed and used to [trick](https://hbr.org/2015/04/why-some-men-pretend-to-work-80-hour-weeks) management. We may have fancy tech, but we need better measures to use it right. 

Our technology has changed; now it’s time to change the game for measuring workplace productivity. Finally. 

* ![](https://future.a16z.com/wp-content/uploads/2021/05/nicole1024.jpeg)![](https://future.a16z.com/wp-content/uploads/2021/05/nicole1024.jpeg) 
  
  **Nicole Forsgren** is the VP, Research & Strategy at GitHub. Author of the award-winning book “Accelerate: The Science of Lean Software and DevOps”, she was also lead investigator on the largest DevOps studies to date.
  
  
  **Follow**  
  
  [Twitter](https://twitter.com/nicolefv)  
  
  [Website](https://nicolefv.com/)

Posted June 15, 2021

### Join the Newsletter


Technology, innovation, and the future, as told by those building it.



#### Thanks for signing up.

Check your inbox for a welcome note.




Views expressed in “posts” (including articles, podcasts, videos, and social media) are those of the individuals quoted therein and are not necessarily the views of AH Capital Management, L.L.C. (“a16z”) or its respective affiliates. Certain information contained in here has been obtained from third-party sources, including from portfolio companies of funds managed by a16z. While taken from sources believed to be reliable, a16z has not independently verified such information and makes no representations about the enduring accuracy of the information or its appropriateness for a given situation.

This content is provided for informational purposes only, and should not be relied upon as legal, business, investment, or tax advice. You should consult your own advisers as to those matters. References to any securities or digital assets are for illustrative purposes only, and do not constitute an investment recommendation or offer to provide investment advisory services. Furthermore, this content is not directed at nor intended for use by any investors or prospective investors, and may not under any circumstances be relied upon when making a decision to invest in any fund managed by a16z. (An offering to invest in an a16z fund will be made only by the private placement memorandum, subscription agreement, and other relevant documentation of any such fund and should be read in their entirety.) Any investments or portfolio companies mentioned, referred to, or described are not representative of all investments in vehicles managed by a16z, and there can be no assurance that the investments will be profitable or that other investments made in the future will have similar characteristics or results. A list of investments made by funds managed by Andreessen Horowitz (excluding investments for which the issuer has not provided permission for a16z to disclose publicly as well as unannounced investments in publicly traded digital assets) is available at <https://a16z.com/investments/>.

Charts and graphs provided within are for informational purposes solely and should not be relied upon when making any investment decision. Past performance is not indicative of future results. The content speaks only as of the date indicated. Any projections, estimates, forecasts, targets, prospects, and/or opinions expressed in these materials are subject to change without notice and may differ or be contrary to opinions expressed by others. Please see <https://a16z.com/disclosures> for additional important information.