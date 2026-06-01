---
title: The Majestic Monolith
date: '2020-06-24T23:19:06-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://m.signalvnoise.com/the-majestic-monolith/
---

[The Majestic Monolith](https://m.signalvnoise.com/the-majestic-monolith/)  



![](https://i1.wp.com/m.signalvnoise.com/wp-content/uploads/2016/02/1C0WR8CjuV3MCbuukjOqeUg.png?w=640&ssl=1)![](https://i1.wp.com/m.signalvnoise.com/wp-content/uploads/2016/02/1C0WR8CjuV3MCbuukjOqeUg.png?w=640&ssl=1)

[Monolith by Rene Aigner](http://reneaigner.deviantart.com/art/Monolith-283096035)

Some patterns are just about the code. If your code looks like this, and you need it to do that, here’s what to do. You’d do well to [study](http://www.amazon.com/Smalltalk-Best-Practice-Patterns-Kent/dp/013476904X) [such](http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672) [patterns](http://www.amazon.com/Patterns-Enterprise-Application-Architecture-Martin/dp/0321127420/), as they give you a deep repertoire of solutions ready to apply and make your code better every time you hit their context.

Then there are other patterns that are less about the code and more about how the code is being written, by whom, and within which organization. The Majestic Monolith is one of those patterns. But before we dive into all its glory, let’s first examine its opposite pattern: Micro/services oriented architecture.

M/SOA is a prescription to break down an application into many smaller parts, run each of these parts as their own application, and then let the constellation solve the grand problem you really care about.

This is a great pattern. No, really. Not being sarcastic here. If you’re Amazon or Google or any other software organization with thousands of developers, it’s a wonderful way to parallelize opportunities for improvement. Each service can be its own team with its own timeline, staff, and objectives. It can evolve independently, at least somewhat, of whatever else the rest of the constellation is doing.

When you reach a certain scale, there simply is no other reasonable way to make coordination of effort happen. Otherwise everyone will step on each other’s feet, and you’ll have to deal with endless merge conflicts. (Well, at least in theory, I hear Facebook is having a great time with a monolith, whether it’s majestic or not is a different discussion).

In other words, M/SOA fits the organizational shape of very large corporations. So far so good!

Where things go astray is when people look at, say, Amazon or Google or whoever else might be commanding a fleet of services, and think, hey it works for The Most Successful, I’m sure it’ll work for me too. Bzzzzzzzzt!! Wrong!

The patterns that make sense for organizations orders of magnitude larger than yours, are often the exact opposite ones that’ll make sense for you. It’s the essence of cargo culting. If I dance like these behemoths, surely I too will grow into one. I’m sorry, but that’s just not how the tango goes.

This is true of not just technical patterns, but general organizational approaches too. But that you shouldn’t run HR like a 50,000-person company when you have 50 seems obvious to most though (with some exceptions).

The problem with prematurely turning your application into a range of services is chiefly that it violates the #1 rule of distribute computing: Don’t distribute your computing! At least if you can in any way avoid it.

Every time you extract a collaboration between objects to a collaboration between systems, you’re accepting a world of hurt with a myriad of liabilities and failure states. What to do when services are down, how to migrate in concert, and all the pain of running many services in the first place.

As I said, all that pain is worth it when you have no choice. But most people do have a choice, and they do have an alternative. So allow me to present just one such choice: The Majestic Monolith!

Having your system described as “monolithic” is usually a point of derision. Them be fighting words amongst many programmers! I say don’t just turn the other cheek, but embrace the monolith with pride and a salute! Don’t just accidentally waltz your system into a monolithic design, do so with intent and with your head held high. Any monolith worth erecting is worth making majestic!

So what is a majestic monolith exactly? It’s an integrated system that collapses as many unnecessary conceptual models as possible. Eliminates as much needless abstraction as you can swing a hammer at. It’s a big fat no to distributing your system lest it truly prevents you from doing what really needs to be done.

#### Enter the case study: Basecamp

I’ve been writing Basecamp as a majestic monolith since 2003. The latest iteration, version 3, takes this pattern to new heights and renders under its domain not just the web, but all of our native platforms as well.

Basecamp 3 is available via the web, as native mobile apps on iOS and Android, as native desktop apps on Windows and Mac, and through email as well. That’s a lot of platforms to juggle concurrently! And I believe the only possible way to do so with a small team of ~12 programmers is do explicitly choose and commit to The Majestic Monolith, in all its controversial glory.

In summary, the pressures that drove us to embrace this pattern are as follows:

**Basecamp is a large application**. There are literally hundreds of screens of various kinds under its domain. We have 200 controllers with a total of 900 methods! This combined with a model of 190 classes with some 1473 methods. And that’s just what’s directly inside app/\*, not to talk about our front-end, like the Trix text editor.

**Basecamp is a small team**. As I mentioned, we have just 12 programmers, and many of those are busy keeping the systems we’ve been creating over the last decade operational. In addition, we have just 7 designers (counting Jason, my partner and our CEO).

**Basecamp is available on 6 platforms**: Web + iOS + Android + Mac + Windows + Email.

**Basecamp has millions of users and a back catalogue** of many apps we’ve committed to maintaining until The End of the Internet.

So a very broad scope, deep commitments, and a very small budget, all comparably speaking. The necessity of this situation simply isn’t compatible with a highly labour intensive pattern like M/SOA. It’s not compatible with writing 100% native apps, but it fits the [hybrid application model](https://signalvnoise.com/posts/3743-hybrid-sweet-spot-native-navigation-web-content) like a glove.

In addition to these formal constraints is the mission to write beautiful, understandable, and succinct code. Code that not only makes us smile while we write it, but also when we later have to extend or patch it. Such a mission is simply not compatible with an accidental monolith. It just gotta be majestic.

One of the benefits to the majestic monolith is that it basically presumes that the people who work on it also understand it. It’s much easier to silo knowledge and responsibilities with a proliferation of smaller systems. We’ve had that happen for the few external, shared services we do have, like Basecamp ID (shared authentication for all generations of the Basecamp app). “Oh, you gotta talk to Jeff about that”.

This in turn puts immense pressure on making the application understandable and changeable by individuals, not teams. Which in turn again forces you to take the time to [turn a long letter into a short one](http://www.goodreads.com/quotes/21422-i-didn-t-have-time-to-write-a-short-letter-so). If your standards are slipping, you’re not just pissing in your own corner, you’re pissing all over that majestic monolith we all have to polish every day. Don’t do that!

In many ways, this goes right to the essence of Ruby and Rails’ perception of programmers. That given the right incentives and nudges, most will rise to the occasion and write beautiful code. That our systems should be a red carpet invitation to become a better, more productive programmer. Who cares if those who aren’t invested in walking that path use the tools and patterns to screw themselves over? Maybe everyone needs to do that once or twice before appreciating the ropes that guides you into the gala premiere.

The Majestic Monolith doesn’t pretend to provide a failsafe architectural road to glory. That’s a fool’s errand. Many programmers suffering under many oppressive influences will turn any architecture made with any tool into a big pile of mud. So worrying too much about how to save those who’s likely out of reach anyway isn’t a productive use of energy. And it takes all the ones who do care down the wrong path.

TL;DR: Run a small team, not a tech behemoth? Embrace the monolith and make it majestic. You Deserve It!