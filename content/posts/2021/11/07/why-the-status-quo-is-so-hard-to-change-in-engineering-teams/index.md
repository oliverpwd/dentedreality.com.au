---
title: Why the Status Quo Is So Hard to Change in Engineering Teams
date: '2021-11-07T22:17:20-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.okayhq.com/blog/status-quo-is-so-hard-to-change-in-engineering-teams
---

[Why the Status Quo Is So Hard to Change in Engineering Teams](https://www.okayhq.com/blog/status-quo-is-so-hard-to-change-in-engineering-teams)  



## A BigCo Story

*Welcome to BigCo Inc!*

*It’s your first day as a software engineer and you’re excited to start your first commit. As your new co-worker Bill shows you around the codebase, you can’t help but notice how often Bill answers notifications on his phone. “Do you want to continue later?”, you ask. “Nah it’s just that I’m on-call this week. Don’t worry I’m used to it – those are not that important”. You’re a little perplexed but, as the phone vibrations keep rattling your desk, you let Bill show you the innerworkings of BigCo’s codebase.*

*A year later, you’re walking towards building C, where Bill is holding his farewell party, when you feel the now familiar vibration of the phone in your pocket. “Why did Bill quit so suddenly? He never really complained about anything”, you wonder while absentmindedly silencing the notification. It’s been a tiring week for sure and you could use some sleep.*

*As you keep walking, you hear a group of freshly onboarded engineers excitedly talking on their way out of their orientation session.*

This small example illustrates the notion of [learned helplessness](https://en.wikipedia.org/wiki/Learned_helplessness):

> A set of behaviors where we give up on escaping a painful situation, because our brain has gradually been taught to assume powerlessness in that situation.

In this case, BigCo’s culture has **normalized** receiving noisy on-call pages at all times of the day and night. While it may be obvious to an outsider that there is a problem to fix, insiders have given up on improving the on-call experience. They are passive, and they may even volunteer reasons why nothing can be done: “it’s always been like this” or “this is how we ensure our site is always up”. But then one day, they quit.

While this example focuses on the developer experience, learned helplessness also presents a paradoxical challenge to engineering managers: **here is a situation where a manager should be deeply concerned about their team’s well-being, engagement and ultimately retention, but the symptoms are invisible.** Their reports won’t tell the manager that they are having a terrible on-call experience – they might even reject any attempt to improve the situation at first, because fixing the problem *feels* unusual.

## How learned helplessness happens in engineering teams

Before we talk about how to prevent it, let’s see how learned helplessness can happen in a development team.

There are 2 main patterns:

### Pattern #1: Process-related Learned Helplessness

In this case, the team needs to follow processes that have either been externally imposed, or internally imposed but no-one remembers exactly why. Some examples:

* Engineers need to follow a long deployment checklist or get their deployment approved by several committees (e.g. a security committee and an API standards committee). Soon enough, engineers start self-censoring innovative ideas or tell other engineers that their new features won’t pass the committees’ checks.
* A tenured engineer is taking on a very large amount of the code review load for the team, assuming everyone is working as much as them. Other engineers start complaining that this engineer is not very responsive to code reviews.

### Pattern #2: Complexity-related Learned Helplessness

In this other case, the source of powerlessness is sheer scale and/or complexity. There is truly no-one who understands the emergent behavior of the system. For example:

* Slow creep / *boiling frog* situations where existing tools have become ineffective. This could be a release system involving many manual steps, which worked when the codebase was 1/10th of its current size, and is now requiring an entire release team to be maintained. Paradoxically, this same team might not have time to look for a newer, more automated system.
* Particularly bad cases of technical debt, where a sub-system or a common library has become resistant to any change. Engineers assigned to these components gradually reduce their ambitions to fix the technical debt, push back on newcomers’ attempts to fix the debt, and ultimately ask to get re-assigned somewhere else.
* In bigger companies, managers forwarding top-down asks and pressure to their teams without pausing to understand the business reason behind the request. In this case, the manager has given up on protecting their team’s focus from bureaucratic pressures of various kinds.

## What are the consequences?

The story usually goes like this:

1. Employee joins
2. Employee is faced with a first source of learned helplessness.
3. Another employee or their manager *teaches* them it’s a *normal* situation at this company
4. … many quarters pass and this situation repeats itself many times
5. Employee quits and their manager is blindsided

> In a word, we could call this *resignation by a thousand cuts*, which makes it unexpected for managers.

However, if we adopt the point-of-view of the employee, they should have resigned a lot earlier in this process. The main reason they stayed is that they *learned to be helpless* – not that the situation was improving or even stabilizing.

As individual contributors or as managers, we also strive to work in and build great company cultures. Learned helplessness can cause a great loss of human talent and we should find ways to combat it. Let’s see what we can do to detect and avoid it.

## What can you do ?

Before taking action, it is important to become aware of this phenomenon. As we wrote above, learned helpessness tends to be hard to detect by nature. In the following sections, we thus share both how to detect that learned helplessness is happening, and then how to take action against it.

### As an individual contributor

#### Detection

* **Do not second-guess your intuitions**: going back to the BigCo story above, it is easier to have clarity when you are first faced with the issue. In that case, noisy oncall pages. Pay attention to ineffiencies and processes that don’t feel useful anymore, and react earlier rather than later.
* **Take a step back**: later on, make sure you regularly assess the “why?” behind your company’s processes and cultural norms. In particular, pay attention to what people around you consider “obvious”. For example, everyone might consider it obvious that pull requests take more than 3 days to get reviewed. Ask yourself why.

#### Resolution

* **Work with your team to implement solutions**: this can either be actively noticing when you are “teaching” others to accept an already broken situation (Bill, in our story), or find creative ways to improve processes. In particular, agile rituals like retrospectives can be pretty effective to raise issues and agree to fix them together.
* **Hold managers accountable**: one of the key responsibilities of leaders is to create positive change for their teams. Once you notice a situation where you think everyone is in learned helplessness mode, make sure to notify your manager and follow-up until the problem is addressed. It may also be useful to literally frame the issue as a “learned helplessness” situation.

### As a manager

#### Detection

* **Regularly get in your team’s shoes**: by design, a manager is not involved in every day-to-day activity (e.g. PR reviews, on-call, experiencing the build system, etc.). This is both a weakness and a strength: it can lead you to get disconnected from your team’s pain-points but, on the other hand, it will give you a fresh outlook when you do get back to experiencing the life of an IC. For example, you add yourself to the on-call rotation of one of your teams and you realize that it is a terrible experience. People on that rotation might be so used to the noise that they have stopped complaining about it but, as a “newcomer”, you quickly spot the issue.
* **Notice subtle changes in behavior**: the most useful hint here is when someone who used to be very vocal about an issue stops complaining. You should not always interpret this change as a positive, “problem solved” resolution. Make sure you seek closure with the person or teams involved.
* **Measure**: build a list of common sources of learned helplessness (high meeting load, broken CI, build too slow, noisy pages, etc.) and create a set of metrics that you regularly monitor or get alerts on. Having an objective measurement enable spotting abnormal trends that you would otherwise gradually consider “normal”.

#### Resolution

* **Encourage engineers to have autonomy**: teaching people — directly and through cultural norms — that they are *powerful*, not powerless, to change and fix broken things is the key. This means welcoming criticism and enabling people to address problems.
* **Declare process bankruptcy**: not every process is meant to exist forever. For example, do your engineers really need to fill out a checklist for every PR they merge ? Do you still need that on-call rotation where engineers just acknowledge and silence alerts 99% of the time? It may be more comfortable to not upset the status quo, but more effective to remove useless processes.
* **Start small, lead with empathy**: one of the surprising aspects of learned helplessness is that people are so used to a bad situation that they may initially resist your attempts to fix it. Focusing on small, tactical wins can help at first. You might also think that there is *obviously* an issue, but it’s important to reconnect with how your team has been feeling the whole time. It will help you find more effective ways to help them.

Hopefully, this article has shed light on a recurring source of issues in engineering teams, and it has given you several keys to solve them!  

If you’d like to see how Okay can help, [let us know](https://okayhq.typeform.com/to/O47Fx3Q7).

**— Okay founders**