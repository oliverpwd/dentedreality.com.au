---
title: Shipping is the beginning of a process – Inside Intercom
date: '2017-11-28T19:01:49+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://blog.intercom.com/shipping-is-the-beginning/
---

[Shipping is the beginning of a process – Inside Intercom](https://blog.intercom.com/shipping-is-the-beginning/)  



All too often, shipping product is seen as an end. A milestone reached, a good time to move onto the next project, an even better time to move onto another team. We believe the opposite is true, that shipping is a beginning.

A few weeks ago, [Fabrizio](https://twitter.com/f_menghini) and [Stephen](https://twitter.com/steobrien), two product engineers, joined our team at Intercom. On his second day, Fabrizio pushed code to production, reducing our number of message types from five to three. On his third day, we designed a new in-line reply, and Fabrizio had it live a few days later. By the end of the first week, Stephen had shipped a range of product changes, including new action buttons in our inbox and a redesigned message summary.

How do we enable new product engineers, having never seen our codebase nor fully understand our product, ship new user facing features within days of joining the company?

## Embrace imperfection, scope small

**We’re comfortable knowing new features aren’t perfect.**

We recently shipped the ability to save a reply. For [common responses to customers](https://www.intercom.com/customer-support?utm_source=ii-blog&utm_medium=cta&utm_campaign=201701-customer-support), you can save a previous reply to reuse again and again. Yet what we shipped wasn’t perfect. We had a list of things that could be better, for example having a way to edit the default saved reply. But this wasn’t something that we thought would be commonly used, so we didn’t build it in order to increase speed to production. We believe that [shipping is your company’s heartbeat](http://blog.intercom.io/shipping-is-your-companys-heartbeat/), and that we’ll quickly learn from our customers whether it is more important than we thought.

We also recently shipped the ability to tag a message, for example a ‘great user quote’, a great customer ‘testimonial’ or a well articulated ‘important problem’. Yet there was no ability to view all the tagged messages, so we clearly built something incomplete. But we shipped it to get people tagging, to learn what kind of tags they use, *to learn if people even bothered to tag at all.* We quickly learned that people do use tags, and later today we’ll launch the ability to view all tagged messages.

**We carefully define self-contained, well scoped projects.**

Self contained projects mean that engineers don’t have to understand lots of different parts of the codebase to get building. This is great for new people as they can jump right in.

Well scoped projects mean that we can ship something within a week. The temptation is always to bite off something bigger, something more ambitious, something more groundbreaking. But the opposite approach often works better: paint the bigger picture, then break it down into lots of smaller pieces that ship bit by bit, gradually replacing parts of the experience. This means being comfortable knowing that parts of the product are inconsistent, but it also means you can adapt and learn as you continuously push code to production.

## Shipping is about learning

We believe that shipping is the beginning of a process rather than the end. It is primarily about learning.

No product team can fully predict how their users will behave or react. I learned this at Google, and later again at Facebook. You need to give people a basic feature set, see how they behave, and iterate quickly from there. We ship to learn. We know that we will be wrong more often than we will be right. Because we care most about learning, we prioritise speed to execution.

Shipping is not an end goal. Unfortunately too many teams launch and move on to the next thing. Learning from what you shipped takes discipline. The larger and longer the project, the harder it is to stay focused on it and learn. The natural temptation is to take the accomplishment and move on to something new. I’ve been in many situations where some of the best people left the team shortly after a major release. They see it as a natural end to something. We believe that if shipping is the beginning of a process, projects need to be set up and framed that way.

In Fabrizio and Stephen’s second week, we shipped a bunch of improvements. We fixed some bugs that surfaced, many of which couldn’t have been predicted beforehand. When we made changes to our reply composer, we removed the ability to preview a message as we felt it was an edge case. We figured that most users want to type quickly and hit reply, and the simpler the UI for doing that the better. Within a day or two, we learned that our users using markdown needed the preview to see how their message rendered before sending it. A few days after we shipped the original feature, we shipped the updated version with Preview back in.

Within one week we shipped, we learned, we shipped again.