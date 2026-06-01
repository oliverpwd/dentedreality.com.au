---
title: Planning Your Own Chaos Day
date: '2018-04-26T07:57:37+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.gremlin.com/community/tutorials/planning-your-own-chaos-day/
---

[Planning Your Own Chaos Day](https://www.gremlin.com/community/tutorials/planning-your-own-chaos-day/)  



![](https://www.gremlin.com/media/tammy_ho_ming_bw.jpg)![](https://www.gremlin.com/media/tammy_ho_ming_bw.jpg)
# What is a Chaos Day?

A Chaos Day is a dedicated team day focused on using chaos engineering to reveal weaknesses in your system. We’ve all heard of hack days and hack weeks, where you focus on building new features. Well, a Chaos Day is focused on building more resilient systems by breaking things on purpose.

# What is Chaos Engineering?

Thoughtful, planned experiments designed to reveal weaknesses in your system. Read more about Chaos Engineering here: [Chaos Engineering: the history, principles, and practice](https://www.gremlin.com/community/tutorials/chaos-engineering-the-history-principles-and-practice/).

# Exercise Your BCP Continuously

Large companies have BCPs (Business Continuity Plans). They aren’t exercised very frequently and are often out of date. However, having a BCP means you already do experiments in production (e.g. disaster recovery testing). Chaos Engineering is focused on making these experiments automated and continuous.

# What are Chaos Days inspired by?

Chaos Days are a fairly new concept, but they are inspired by many of the days at work we all love and look forward to including:

* GameDays
* Hack Days & Hack Weeks
* Capture The Flag

## GameDays

GameDays were coined by Jesse Robbins when he worked at Amazon and was responsible for availability. The goal was to increase reliability by purposefully creating major failures on a regular basis. You can read more about GameDays here: [How To Run a GameDay](https://www.gremlin.com/community/tutorials/how-to-run-a-gameday/).

## Hack Days and Hack Weeks

One of the earliest company Hack Days was held at Yahoo back in 2006. Many of our Gremlin team members (Grems as we are known to each other) have been participating in company Hack Days since the late 2000s.

Hack Days are entire days dedicated to building software with no meetings or other distractions. It’s heads-down time. Many of the greatest software features we know and love were created during Hack Days and Hack Weeks – they are a great way to encourage teamwork and drive innovation.

## Capture The Flag

Facebook recently open sourced their CTF (Capture The Flag) platform on [GitHub](https://github.com/facebook/fbctf). You can find it here: [Facebook CTF is now open source.](https://www.facebook.com/notes/facebook-ctf/facebook-ctf-is-now-open-source/525464774322241/) Facebook explains in the note:

“Today, Facebook hopes to make security education easier and more accessible, especially for students, with the release of our Capture the Flag (CTF) platform to open source on GitHub! CTFs provide a safe and legal way to try your hand at hacking challenges.”

![](https://www.gremlin.com/media/facebook_ctf.png)![](https://www.gremlin.com/media/facebook_ctf.png)

# Why Run A Chaos Day?

There are a variety of benefits for a variety of people. Let’s explore some of the common personalities and questions you may encounter.

***“we don’t learn by always doing things the way we have always done them”***

**Influencers**

Engineers who are on-call are your influencers when it comes to kicking off a Chaos Day at your company. They wear the pagers, they feel the pain. They will extract great value out of identifying weaknesses within their systems with Chaos Engineering.

**Waverers**

Engineering Managers will be interested in knowing what Chaos Engineering is – but it’s also helpful to share with them information about the actual cost of downtime. Chaos Engineering practitioners have been able to demonstrate that Chaos Engineering can reduce high severity incidents (SEVs) and overall downtime experienced by customers. Ask them what it would cost the company if it were down for 10 hours. British Airways recently experienced a 10 hour outage which was estimated to cost 80 million pounds.

**Passives**

Engineering Directors, VPs and CTOs will want you to explain why they should consider practicing Chaos Engineering. Here it’s helpful to highlight the business impact of incidents – The cost of downtime, the loss of customer trust, and the engineering resources spent fixing issues.

**Moaners**

There’s always someone (and you probably already know who they are). They will likely tell you that they are too busy and don’t have time for new practices. A great tip for interacting with moaners is to explain to them “we don’t learn by always doing things the way we have always done them.”

**Opponents**

You may also find yourself standing in-front of an opponent. An opponent is likely to tell you that “there’s so much chaos already”. This is a great conversation starter. Ask them what chaos they are dealing with at the moment. Then speak with them about the impact of high severity incidents on the business and all the teams across the company. Ask them what they think the top 5 most critical services are. Ask them which systems they think are the most fragile. Ask them if they were to practice chaos engineering, which system would they start with? Try to get them involved to see the value of being proactive.

**Fanatics**

There are some people you will meet on this journey who will proudly explain that what they do is the only way to improve reliability. For example, they might be diehard fans of unit tests . That too is an excellent conversation starter, you can follow it with “Chaos Engineering is unit tests for alerting and monitoring.”

**Skeptics**

There will always be skeptics and they will usually outright tell you “we won’t get value from this”. An important conversation to have with skeptics is one focused on defense protection and training. Security teams in large companies will often have security engineers train the greater engineering team on how to write more secure code. Who is training your team on building more resilient systems and improving your on-call habits?

**Mutineers**

The mutineers will be very forceful and explain “we don’t need to do this”. Share metrics with your mutineers. Give them the data on the top 5 most unreliable systems and focus on the importance of building more resilient systems.

# **Chaos Day Benefits**

* Up-skill your team on building software with failure in mind. Everyone in engineering has a learning budget, this is a real world education. Often learning budgets go unspent and are between $1k to $10k per engineer / per year.
* Gain a deeper understanding of your current system weaknesses
* Reduce the severity and frequency of incidents, e.g. set a goal to obtain a 10x reduction in incidents
* Prevent loss caused by outages
* Learn from failure

# How do you plan a Chaos Day?

Starting early and giving yourself plenty of time is a major advantage. The goal of your Chaos Day is to plan, create and host an impactful Chaos Day.

Your Chaos Day could be:

* An on-site
* An off-site
* During a company retreat

# Chaos Day Countdown: 90 Days

90 Days may sound like a long time, but getting everyone involved requires giving a large amount of lead time. This is especially important if you’d like your CTO and CEO to attend.

# Chaos Day Prerequisites:

* Know your top 5 critical systems
* Have monitoring & alerting
* Measure the cost of downtime

There are a number of questions which are useful to ask yourself before you start officially planning your Chaos Day: Who will attend? What is the focus? How will you measure success ? What is your budget? Where will it be?

# Chaos Day Timeline

Here is a Chaos Day timeline for you to use when planning your Chaos Day. This will help you ensure your Chaos Day is a success!

**Chaos Day Countdown: 90 Days**

* Create a Chaos Day Crew
* Determine Attendee Availability For Chaos Day
* Lock-In Chaos Day Venue

**Chaos Day Countdown: 60 Days**

* Send Chaos Day Placeholder Invites

**Chaos Day Countdown: 30 Days**

* Send your attendees Chaos Day Pre-Read information, we have created a GitHub repo here: [Chaos Day Pre-Read Pack](https://github.com/gremlininc/chaos-day)
* Create a Chaos Day agenda

**Chaos Day Countdown: 0 Days**

* Chaos Day! 💥

# Chaos Day Crew

The very first thing you need to tick off your list when planning a Chaos Day is creating an official Chaos Day Crew. It’s important to have a diverse team, we recommend you include the following people:

* VP Engineering / CTO / COO
* Executive Assistant
* Engineering Director / Manager
* Principal / Staff Engineer
* New Grad Engineer / Intern

Once you’ve created your Chaos Day, get together and determine who will be responsible, accountable, consulted or informed (RACI) when it comes to your Chaos Day tasks. You can read more about RACI here: [The RACI Matrix – Your blueprint for project success](https://www.cio.com/article/2395825/project-management/project-management-how-to-design-a-successful-raci-project-plan.html).

We recommend you collaboratively create a matrix together similar to the one below:

![](https://www.gremlin.com/media/raci_chaos_day.png)![](https://www.gremlin.com/media/raci_chaos_day.png)

# Chaos Day Planning Objectives

Planning a successful and impactful Chaos Day isn’t an overnight activity. It takes time and a great team. But the outcome will be well worth the effort.

Here are the top 3 objectives when planning your Chaos Day:

* Make Chaos Engineering Familiar
* Identify your key stakeholders
* Create the right story for your stakeholders

# Chaos Day Budget

You will need to determine how much your Chaos Day is going to cost. Remember to take into account venue, food, drink, whiteboards, and time away from your usual work.

## Chaos Day Attendee Availability

It’s important to determine who you need to attend Chaos Day before booking a specific date and venue.. Using a tool like [Doodle](https://doodle.com/) to send out a quick and simple poll will enable you to collect everyone’s available dates.

![](https://www.gremlin.com/media/doodle_chaos_day.png)![](https://www.gremlin.com/media/doodle_chaos_day.png)

# Chaos Day Venue

Where you choose to host your Chaos Day really comes down to three questions:

* How do you describe your team culture?
* How many people do you want to participate in the Chaos Day and can everyone fit?
* What is your available budget?

If your team culture could be described as “scientific, love experiments, and exploring new concepts”, you could host your Chaos Day at a Science Exploratorium event space. If you team culture is “serious, no nonsense” it would likely be more appropriate to host your Chaos Day on-site at your office.

There are many tools out there that can help you find a great venue, try out [Splacer:](https://www.splacer.co/)

![](https://www.gremlin.com/media/splacer_chaos_day.png)![](https://www.gremlin.com/media/splacer_chaos_day.png)

# Chaos Day Placeholder Invites

You really want everyone to be there, especially when you are putting in a ton of effort to make this an impactful and useful team day. Send all your attendees a very simple placeholder invite. Don’t give much away!

-——————————–

[Chaos Day is coming]

\*\*\*\*Placeholder\*\*\*

Keep this day free, we need you.

-——————————–

# Chaos Day Pre-Read Information

Many of your attendees may never have practiced Chaos Engineering. It’s still a very new concept for most engineers.

Sharing useful articles for your attendees to read 30 days before your Chaos Day will help them feel included. It will also give them time to learn more so they can do their best work on the day. This is very similar to giving everyone on your team time to prepare for Hack Days. It’s useful to have time to think about what Chaos Engineering experiments you will perform and which service you will target.

You can find the [Gremlin Chaos Day Pre-Read Pack on GitHub.](https://github.com/gremlininc/chaos-day)

![](https://www.gremlin.com/media/github_chaos_day_pack.png)![](https://www.gremlin.com/media/github_chaos_day_pack.png)

# Chaos Day Agenda

Now it’s time to create your Chaos Day Agenda.

* 11:00 – Start Time (11am)
* 11:15 – Whiteboarding & debate on assumptions
* 11:45 – Test cases and scoping
* 12:30 – Lunch
* 13:30 – Execution
* 15:00 – Recap / Review / Feedback
* 16:00 – Close

# What Chaos Engineering Experiments Should You Perform First?

When you are determining what experiments to run on your Chaos Day, ask yourself the following question:

**What are your top 5 most critical services?**

Remember that it is okay to start in staging and then later move to production. When you are practicing Chaos Engineering in production or staging, be sure to take into consideration the blast radius. Start small and measure the impact on your engineering team.

# Have an Exit Plan

Before you run your Chaos Engineering experiments make sure you have an exit plan. Gremlin has a built-in functionality to stop experiments.

# What Chaos Engineering experiments can your perform?

Gremlin has the following Chaos Engineering experiments available to you.

![](https://www.gremlin.com/media/gremlin_attacks_april_chaos_day.png)![](https://www.gremlin.com/media/gremlin_attacks_april_chaos_day.png)

# Whiteboarding

A very beneficial activity during your Chaos Day is having everyone in the room draw up a current diagram of the systems you will focus on for your Chaos Day. Use this time to your advantage. With so many great minds in the room, it’s a great opportunity to debate assumptions and gain consensus.

![](https://www.gremlin.com/media/whiteboarding_t_hml.jpg)![](https://www.gremlin.com/media/whiteboarding_t_hml.jpg)

# What is an Example of a Chaos Engineering Experiment

Chaos Engineering Hypothesis

* Calls to DynamoDB will timeout after 1500ms
* This will cause elevated 500 status codes in API
* The UI will degrade gracefully

# The Chaos Engineering Experiment

This is an example of a latency attack for 120 seconds impacting dynamodb with 1500 milliseconds of latency.

This will delay egress packets for 1500 milliseconds. This Chaos Engineering experiment is being performed on stage.

![](https://www.gremlin.com/media/chaos_day_ex_1.png)![](https://www.gremlin.com/media/chaos_day_ex_1.png)

## Analyze the Results of the Chaos Engineering Experiments

Gremlin gives you the ability to see the logs within the Gremlin Control Panel. This is useful because everyone who has access to your Gremlin account is able to see the progress of experiments in real-time.

![](https://www.gremlin.com/media/chaos_day_ex_2.png)![](https://www.gremlin.com/media/chaos_day_ex_2.png)

## Elevated 500 responses

You will then see raised 500 responses in your monitoring tooling.

![](https://www.gremlin.com/media/chaos_day_500s.png)![](https://www.gremlin.com/media/chaos_day_500s.png)

## Graceful degradation

You will also be able to confirm that graceful degradation occurs as expected. Here you can see that the Gremlin app gracefully degrades successfully.

![](https://www.gremlin.com/media/chaos_day_degrade.png)![](https://www.gremlin.com/media/chaos_day_degrade.png)

# Implement Continuous Chaos

Now that you have successfully run your experiment, it’s a good time to turn this experiment into continuous chaos. You can use Gremlin to automatically schedule this Chaos Engineering experiment to occur on a daily/weekly/monthly basis. This is great because you will be able to have confidence that you have the same level of resilience as you did on the day of your Chaos Day. It also frees your team up to think of new experiments to run for future Chaos Days.

# Establish a Chaos Day Crew For Your Next Chaos Day

Now that you have successfully run your experiment, it’s a good time to ask who would like to volunteer to run the next Chaos Day!

# Accoutrements

Finally, there are a number of important aspects of your Chaos Day that will make it really stand out. With these additional touches your Chaos Day could become the reason engineers want to join your company. You Chaos Day could be a day that every engineer looks forward to, thinks about and plans for.

## Chaos Day Food & Drinks

Don’t forget to order coffee, lunch, drinks and snacks. Everyone will need delicious brain food to do their best work on Chaos Day.

## Chaos Day Theme

Do you want a theme for your Chaos Day? Themes are very common at Hack Week. They get everyone generating new ideas and thinking about the upcoming activities.

You could use a technical theme like packet loss and hide physical packets around your office for engineers to find. What are your favorite chaos-filled movies and tv-shows?

## Chaos Day Theme: Outbreak

![](https://www.gremlin.com/media/outbreak.png)![](https://www.gremlin.com/media/outbreak.png)

## Chaos Day Theme: Mr Robot

![](https://www.gremlin.com/media/mr_robot.png)![](https://www.gremlin.com/media/mr_robot.png)

## Chaos Day Theme: Gremlins

![](https://www.gremlin.com/media/gremlins.png)![](https://www.gremlin.com/media/gremlins.png)

# Chaos Day Countdown: 1 Day

The day before your Chaos Day send out everyone a reminder with information on where they need to be, what they need to bring and what time they need to show up. Make sure to tell everyone to bring along their laptop and charge it in advance.

# Chaos Day Countdown: 0 Day

-——————————-

WELCOME TO CHAOS DAY

WE NEED YOU

WE ARE GLAD YOU ARE HERE

-—- END OF MESSAGE ——–