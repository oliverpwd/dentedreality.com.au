---
title: Framing → Shaping
date: '2022-11-06T22:02:33-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://world.hey.com/rjs/20-framing-2f64ddca
---

[Framing → Shaping](https://world.hey.com/rjs/20-framing-2f64ddca)  



Over the last few months I’ve worked with teams to help them adapt Shape Up to their specific context. Talking to a wider variety of teams has been eye-opening. It’s helped me discover many hidden factors that were present at Basecamp when I first wrote the book. This is now leading to a whole new iteration of the process and steps that I’m teaching teams to improve their product development.

In this post I want to introduce one of the most fundamental changes.

In Shape Up, a key concept is the Betting Table. The principle of treating projects as bets and capping our downside is sound. But there’s a problem with where the Betting Table sits in the order of operations.

According to the book, shapers prepare pitches, pitches go to the betting table, and then the business decides at the last moment which pitches to “bet on.” Teams who follow this to the letter encounter a problem: how do you justify spending the time to shape something when you don’t know if the business will value it?

This easily leads to a situation where shaping is … underdone. Pitches become *sales pitches* to convince the business to spend time — to bet on — this or that problem or feature request. Those pitches focus on making the case to work on something, and they lack the rigor that goes into shaping a viable technical solution.

Shaping properly takes time. When projects aren’t fully shaped, teams pay for it with unexpected issues, unanswered questions, and unforeseen trade-offs in the build cycle. This frustrates the product and business people: “Why are we still talking about this! Why are we still in this phase? I thought we defined what to do and agreed what we’re working on!”

To spend time on shaping, there has to be impetus from the business up front that says “this problem matters.” Especially in growth-stage companies, carving out time on the calendar isn’t easy. There has to be justification and support for the shaper and a lead dev to say ‘no’ to other things and spend a few hours this week in shaping sessions.

To solve this, I’ve coached teams to introduce a new step before Shaping that we call **Framing.** Framing is all about the problem and the business value. It’s the work we do to challenge a problem, to narrow it down, and to find out if the business has interest and urgency to solve it.

The framing session is where a feature request or complaint gets evaluated to judge what it really means, who’s really affected, and whether now is the time to try and shape a solution.

When I describe this to product managers, their eyes light up with recognition. “Yes, that’s what I do!” They know that prioritization is not just dragging things up and down a list. It’s digging in and trying to understand and define the problem. It’s work that takes time.

Communicating this — that framing takes time and effort — can improve the dynamics around the backlog. When PMs feel there are too many things in the “suggestion box” to prioritize, I advise them to hold regular office-hours where anyone can bring in their top issues for conversation. The language of framing helps everyone to understand that deciding what to do involves doing follow-up work and digging in, not just saying yes or no.

What happens in a framing session? In a typical framing session, a shaper and a product manager or business person are digging into what they know about the business and the customer to narrow down the problem. Which customer segment is affected? How valuable is this segment compared to the others? What other things are going on in the business that need our attention? You’ll sometimes see live SQL queries and people pulling up past customer research data in a framing session to answer a question or narrow down the opportunity.

The output of a framing session is a well-framed problem: something where the business says “if we can shape this into something doable and execute within X weeks, that will be meaningful to us.” There’s a commitment to spend time shaping, but not yet a commitment to go into a build cycle. That final bet still needs to be made based on how the shaping goes.

 [![](https://world.hey.com/rjs/2f64ddca/representations/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCQldISmk4PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--d3d2d7332bcf4e9591117d8fdf22aa78cb3012af/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDam9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJQUQya0NBQW82REhGMVlXeHBkSGxwUVRvTGJHOWhaR1Z5ZXdZNkNYQmhaMlV3T2cxamIyRnNaWE5qWlZRPSIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--435325a84611f9b4e2210760d04bed2a88c1f429/Screen%20Shot%202022-03-23%20at%202.00.31%20PM.png)![](https://world.hey.com/rjs/2f64ddca/representations/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCQldISmk4PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--d3d2d7332bcf4e9591117d8fdf22aa78cb3012af/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDam9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJQUQya0NBQW82REhGMVlXeHBkSGxwUVRvTGJHOWhaR1Z5ZXdZNkNYQmhaMlV3T2cxamIyRnNaWE5qWlZRPSIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--435325a84611f9b4e2210760d04bed2a88c1f429/Screen%20Shot%202022-03-23%20at%202.00.31%20PM.png)](https://world.hey.com/rjs/2f64ddca/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCQldISmk4PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--d3d2d7332bcf4e9591117d8fdf22aa78cb3012af/Screen%20Shot%202022-03-23%20at%202.00.31%20PM.png?disposition=attachment)  

How does this impact what Shape Up called the Pitch? Teams who adopt the Framing → Shaping process actually find that “pitching” better describes the *input* to *framing* than the *output* of *shaping*. With blessing from the business up front, shaping is less about pitching and more about to getting to a viable approach for a problem we all care about. When I work with teams today, we call the output of shaping a “Package.” That’s because all the necessary variables for a project have been brought together: the problem, the ingredients of the solution, the time to spend on it, etc. What’s left is for the betting table to stamp the package with approval so it can move forward to delivery.

© Ryan Singer