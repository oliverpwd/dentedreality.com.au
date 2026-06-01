---
title: Chipping Away at a Monolith
date: '2020-08-12T23:25:29-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/gusto-engineering/chipping-away-at-a-monolith-de93b28e555b
---

[Chipping Away at a Monolith](https://medium.com/gusto-engineering/chipping-away-at-a-monolith-de93b28e555b)  



My team recently embarked on a journey toward unbundling our part of Gusto’s monolithic Ruby on Rails app.

A monolithic app is a single application that contains code across many domains. The boundaries are unclear. The domains are fuzzy. Typically, as a monolithic app grows, it becomes increasingly difficult for developers to make changes due to unexpected consequences. This is especially true for Ruby on Rails applications, as the ✨ Rails magic ✨ encourages side effects, indistinct domains, and generally [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code).

Gusto has a monolith problem. This is a good problem! It means we have been lucky enough to grow, build new features for our customers, and expand our abilities. However, for software engineers it slows down the development process as the tangled code results in unexpected bugs or overcautious programming. To help solve this problem, Gusto decided it was time to start unbundling the monolith.

My team, Partners Engineering, builds the experience for accountants within Gusto. Our domain is so distinct from the rest of Gusto that there is potential to eventually separate entirely from the core Gusto app. We could build a separate app with its own entities, database, and API, communicating with the rest of Gusto but living separately from the monolith.

We embarked on this project with this vision in mind — a completely separated Partners app with clearly defined boundaries.

# Where to start

## Understand your domain

The first step in separating from a monolith is understanding your domain. My entire team was relatively new to Gusto, meaning we had a lot to learn about our own domain. If you’ve been with the codebase from the beginning, this might look different, but chances are there’s some interaction with another area of the code that you do not know as well.

For several months, my team met weekly to discuss [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) and how our domain fits into it. Spreading these discussions out over a larger period of time gave the team space to discover more in our codebase, read more about different architectures, and get input from other teams. Over the course of several weeks we began to see a clear picture of an ideal Partners domain.

## Start small

Deciding where to start felt like a daunting task. There were a lot of directions we could go. Should we begin with something small or should we gravitate towards the area that could have the biggest impact? Should we tidy up our code first or jump right in to defining boundaries between Partners and external groups?

I was tasked with finding a starting point for my team. I started by creating a list of models that belong in the Partners domain. I was searching for a complex model that should undeniably reside within Partners. One model in particular rose to the top as core to our future domain — Accounting Firm. Accounting Firm is a key concept within our domain. It is heavily bundled with external domains, but not in a way that would be impossible to separate. It would be the perfect place to start unbundling and defining a Partners boundary.

With this new Accounting Firm focus, I dove into a deeper audit of the model. I paid particular attention to concerns, callbacks, relationships, and methods that tied Accounting Firm to another Gusto model — Company. Company is a [god model](https://en.wikipedia.org/wiki/God_object) within Gusto. It belongs within the core Gusto domain as a model that Accounting Firm should never access directly.

The results of this in depth analysis of the Accounting Firm model were overwhelming. By just taking time to review one model I created several epics to clean up the model. However, we needed to focus on one, achievable area where we could make an improvement.

We decided to start by removing one method — `accounting_firm.companies`. This method was the perfect place to start because it:

* Reaches across multiple boundaries
* Is a crucial method for accounting firm
* Could be removed without help from external teams
* Would help us start defining Partners domain boundaries

## Tidy up

While [tidying up](https://medium.com/gusto-engineering/does-this-code-spark-joy-23b1d7706bc0) our code will not help us define domain boundaries, or unbundle the monolith, it can help us prepare to take these larger steps. It is an incredibly helpful practice that allows us to pave the way for bigger changes.

During my investigation of Accounting Firm, I found a questionable area of code. In it there was orphaned code. There were strange relationships that resulted in two sources of truth. There was a test factory that created inaccurate duplicate data.

> *While untidy code is not directly related to unbundling, it makes the unbundling efforts more difficult.*

I started unbundling with this basic cleanup. I removed the orphaned code. I spent several days fixing the bug in our tests that created duplicate data. It was not possible to tidy everything, but I tidied as much as I could. This paved a clear path for us to begin truly unbundling.

# Problems you may encounter

We wanted two minds on this unbundling problem. So, my teammate [Grex](https://medium.com/u/e1abe1fd9081?source=post_page-----de93b28e555b----------------------) and I decided to pair full time for two weeks. Armed with our ownership mentality and the ability to approve our work as a team, we jumped into our unbundling epic.

We encountered a few obstacles when tackling this unbundling project. When you are working within a system that is completely intertwined, without clear boundaries, it is impossible to predict every issue you will find. Here are a few of the stumbling blocks that Grex and I came across while working on this project.

## Crossing into other domains

Our work frequently took us outside of our domain into other areas of our code — with and without clear code owners. We had to give ourselves permission to make decisions in these other domains. For example, we wanted to create a service to retrieve Companies. This service was generic enough that it could potentially be useful to other teams, especially teams working on similar unbundling projects. What should this service look like? Where should it go?

Without a clear owner of Company, we had to give ourselves permission to make the best decisions with the knowledge we had. Without the power to make these fast decisions, our project might have taken six weeks instead of two. Besides, we could always make changes later!

## Shaving the yak

When almost everything you see could be improved, how do you stay focused on the task at hand? Our team lead Matt calls this “ [shaving the yak](https://americanexpress.io/yak-shaving/) “ — also known as going down a rabbit hole.

For example, Grex and I encountered many examples of the reverse method `company.accounting_firm`, which is also on our unbundling chopping block. We could potentially reuse some of the use cases we built for this purpose. Would it hurt to knock a few out while we were working on this anyway?

Yes, yes it would. This distraction would surely have led us to further distractions. When unbundling, it is important to have a clear goal in mind and stick with that goal even if other opportunities for unbundling arise. Instead of becoming distracted, we wrote down ideas for areas to return to later and continued on our mission to eliminate `accounting_firm.companies`.

## Unbundling tests

When estimating unbundling time, do not forget about tests. Many of our tests utilized `accounting_firm.companies`. Some of our tests even stubbed out this method to control what was returned. Once we removed the `companies` method, these tests started to fail.

Fixing the tests took us a surprising amount of time, at least 50% of our pairing over the two weeks.

> *Do not assume unbundling tests will be a fast process — it will probably take some time.*

## Fear of breaking things

Two weeks and many planning sessions later, Grex and I had replaced all instances of `accounting_firm.companies` with ten new service classes. These new services did a variety of things, from simply returning the ids of companies related to the firm to returning filtered and refined company data. We were theoretically ready to remove this method entirely, cementing the new boundary we had drawn between Accounting Firm and Company. There was one problem – we were scared.

This had been such a crucial method, what if there were some uses that we had not caught with our text searches? Some critical function still using `accounting_firm.companies` that would cause some fatal bug that our tests did not catch?

We decided to remove `#companies` in baby steps. First, we added a comment deprecating the method. Second, we added some bug tracking to determine if anyone was indeed secretly using this method. After 24 hours without any reports, we felt confident that this method had truly been eliminated. We deleted `accounting_firm.companies`.

The harsh truth is, when unbundling there is a good chance you are going to break things. The best you can do is move slowly and cautiously, adding tests or logs where they were missing before to catch any bugs before they make it to production.

# What next?

When you are working inside a monolith, unbundling can feel like an insurmountable task. This initial project was our first small step towards unbundling our domain. For the next several years, my team will likely be chipping away at our monolith. From this initial project, my team has created several epics and has an idea of where to move next. We have a better understanding of our domain and a little practice under our belt.

When it comes to unbundling, figuring out where to start can be the hardest part. Put in the work to understand your domain and codebase. Then just pick somewhere you think is useful, and get going. It is an impossible problem to solve all at once. Chipping away at the monolith bit by bit is how it will slowly become untangled.