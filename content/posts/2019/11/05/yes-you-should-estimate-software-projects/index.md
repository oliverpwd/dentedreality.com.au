---
title: Yes, You Should Estimate Software Projects
date: '2019-11-05T10:21:53-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://blog.pragmaticengineer.com/yes-you-should-estimate/
---

[Yes, You Should Estimate Software Projects](https://blog.pragmaticengineer.com/yes-you-should-estimate/)  



I hear more voices [saying](https://hackernoon.com/the-myth-of-software-time-estimations-576a7466d91a) there is little point in doing time-based estimations on how long building software will take, and thus we should just stop doing it. *“Let’s just use story points and estimate complexity, but not the time”* and *“Let’s just try #noestimates”* are suggestions people around me recently brought up. I’m personally skeptical of both approaches. While I do think that doing time-based estimates is *really* hard, it comes with so many benefits for those who keep doing it.

## Time is of essence

**I attribute much of my success in engineering to giving estimates on software complex projects – then also delivering on those timelines.** When I was working on Skype, I was part of the Xbox One launch team. Microsoft finalized the Xbox One launch date based on estimates from the 100+ teams working on Xbox One, including ours. A year later, [we launched](https://thenextweb.com/microsoft/2013/11/20/skype-works-doesnt-work-xbox-one/) on the pre-announced day without significant hiccups and major fanfare. After Xbox One, I worked on launching Skype for Web. Here, we ended up beating our original estimates, leaving more time for experimentation before [the worldwide launch](https://blogs.skype.com/news/2015/06/05/skype-for-web-beta-is-now-available-to-everyone-in-the-us-and-uk/).

When I joined Uber, we had an internal deadline to rewrite and launch the new Uber rider app by the end of 2016. We also pulled this off after a few months of development, hitting our [previously set launch date](https://www.uber.com/newsroom/newriderapp/). Since working at Uber, my team has committed to launches with several external partners, based on the time estimates we provided. Launching [paying with Venmo](https://www.uber.com/us/en/u/venmo/) or [Google Pay on Uber](https://www.medianama.com/2018/10/223-uber-india-google-pay/) were examples of these – and these projects had plenty of complexity that is [hard to appreciate from the outside](https://blog.pragmaticengineer.com/talks/#paymentsintegrationatuberashortcasestudy).

**Estimates matter because most people and businesses are date-driven.** Have you noticed how Apple ships most of their big bang projects at WWDC, a date they commit to far ahead? How Facebook unveils many new features at F8? How Google launches new products at I/O? All of those launches are date driven because that’s a great way to grab people’s attention and to get extensive press coverage.

Publicly traded companies plan and budget based on quarters. They also decide how much to invest in projects and people after asking, *“how long does it take to launch?”* Private, venture-funded companies try to get new features out in time to help with the next fundraising round. Yes, some businesses are not very date driven: but they are rare. Private, profitable lifestyle-businesses and some governments are perhaps the best examples of entities that don’t care *as much* about dates.

## Good communication is more important than good estimation

**I have missed many of my estimates, and it was rarely a big deal.** While people and businesses are date-driven, delays are common in any part of a company. If you think delays only happen in tech parts of a business, talk with people on operations, marketing, recruiting, and other functions. Regardless of the org and function, people tend to be overly optimistic in their estimates for work they’ve not done before. Ever heard of a building construction project overrun? A government initiative be late? Brexit being delayed, [again](https://www.thesun.co.uk/news/brexit/8642205/why-is-brexit-delayed-what-next-leave/)? Where there are people, there are delays.

**How and when the delay is communicated matters far more than the delay itself**. In my case, the projects where the delay was not a big deal were ones where we communicated well ahead of time. We worked with the business to decide what to do. Cut a feature and make the launch? Bring in more people, risking other projects? Or push out the date, informing everyone else involved? When done like this, a delay is just business as usual. However, when a delay is communicated only in the eleventh hour, that’s what leads to frustration, escalations, and unpleasant conversations.

## Estimate and commit – the way to get things done faster

**Pushing back on estimates also misses the bigger point about engineers staying focused on delivering the largest business value**. Remember how I said how I’m pretty good at estimating, then delivering on them? I was not telling the truth about delivering. **For every major project, we shipped something different on the launch date**, than what we agreed to originally. For Skype on Xbox One, we didn’t ship group video calling on launch day. While playing games, the platform turned out to not leave enough CPU processing to decode more than two streams, reliably. And we did not have time to optimise our stream decoding further, so we cut this feature. In the end, it made little to no difference for the success of the launch.

Similarly, for every project with a fixed deadline, we shipped different functionality to what we planned, when we gave the estimates. But the stakeholders were never surprised. We had continuous conversations with the business, as we kept hitting our milestones. Should we keep this feature, that is turning out to be complex to build? Does it add enough business value? If we keep it, do we move the timeline, or do we pull in more people to help ship it? Can we ship a simpler version that would result in a similar business impact?

We would not have had these tradeoff and prioritization conversations without the time pressure our estimates created. We shipped more business value in the same span of time. Because as we got squeezed by deadlines, we had to confirm again and again where we put our focus on and what we throw aside.

**Estimates and deadlines are great for getting things done. They heavily incentivize teams to focus.** We built Skype for Xbox one in 16 months. We knew the final launch date a year before it was due and had a full team working by then. It seemed like a walk in the park.

However, Murphy’s Law caught up with us. We spent most of the 16 months in a way similar to what the #noestimates philosophy promoted – even though this was not a thing back then. We worked on sprints, tracked our velocity, followed the usual Scrum rituals. Looking back, we were doing light jogging at a leisurely pace, making cases for unimportant, but fun work. We spent weeks building a sandbox app that we played on, but never really used later. We did week-long performance optimizations on things that turned out to be pointless, following the launch. We built Easter eggs that never made it into the app. Looking back, we were the too-much-time-on-their-hands type of team.

Our pace picked from jogging to the running pace in the last four months. Two months to the launch, we realized we were behind and started sprinting. We were more productive and produced about the same value in those last four months than we did the previous 12, combined. **Why the sudden productivity change? We had a big deadline coming up, and there was no option of not shipping**. Suddenly, the whole team became focused, distractions were all gone, and we moved at a faster pace than I’ve ever felt the team do so.

## Learning to estimate different types of unknowns

**Giving estimates, than missing them forces deeper reflection and faster learning about the types of unknowns in the software world.** When it comes to why estimates are difficult, most engineers and engineering leads throw their hands up in the air and say, *“Software has too many unknowns! We can’t tell what unknowns we’ll find, even with the simplest task!”* This is how I thought, when I started out. But when you end up giving estimates, then miss them by a large margin, you cannot avoid having an honest conversation with yourself and your team. *What* did we miss? *Why* did we miss it? *How* can we try to account for it, the next time?

If you don’t have estimates, you’ll end up asking these questions far fewer times, if even. I’ve been burnt by my estimates countless times. After every time, I understood more about the type of unknown that I was not aware of. I started to see technology risks, early adopter risks, integration risks – and built up a toolset on how to mitigate these. Do early prototyping. Talk with the team who owns the integration. Do timebox researching. Do this long enough, and many of the common unknowns go from wild and unpredictable to tame and domesticated.

**But what about tech and architecture debt? Estimates also help to pay these down.** Every business stakeholder working with engineers has heard “tech debt” more times than they care to remember. And most stakeholders also associate this term with an endless pit of work. *“I won’t allow this team to work on this ‘tech debt’ as they always end up taking months doing nothing I see value in”* – they think to themselves. But what if you can estimate, or at least time box the time spent on tech debt?

My team estimates tech debt work with time-based measurements. Because we have a perception of being timely in shipping, we get buy-in from the business much easier. When there’s trust, everything is easier to agree on. And speaking the same language – time-based estimates – is a good way to earn the trust of the business.

## Yes, you should estimate

**Yes, it’s ridiculously hard to do good estimates on software. Yes, most engineers are bad at it. And yes, being good at this will make you stand out.** Saying that “software is just too complex” is an easy way out over asking the hard questions on *why* estimating is hard and *how* you can get better at it. Start with [sensible project management](https://blog.pragmaticengineer.com/efficient-software-project-management-at-its-roots/), focusing on [principles to reduce risk](https://blog.pragmaticengineer.com/efficient-software-project-management-at-its-roots#clarityfromthestart), over one-size-fits-all practices like Scrum. Reflect on why you under- or over-estimated. Adjust for next time. Rinse and repeat. I could write a post about just on this – wait, [I actually did](https://blog.pragmaticengineer.com/efficient-software-project-management-at-its-roots) – but this is the gist of it.

If you never give estimates, you’ll never become good at them. If you practice and learn from how things went, you’ll keep improving and slowly build up the reputation of that person who’s pretty reliable on how long things take.

**Estimating and being deadline-driven *is* a lot less comfortable than choosing not to estimate. But this is not an excuse to not grow your estimations skill.** I’ve seen teams burn out after sprinting to make deadline after deadline. Too much of this is stressful. This is similar to how teams get unmotivated after doing sprint after sprint without the slightest pressure of shipping. Too much of the same is never good. Mix things up – and use estimates/deadlines to keep the focus and move faster.