---
title: Composability Is the Only Game in Town – Roam, Shipping Containers, Lego and
  Twitter.
date: '2021-10-15T19:33:07-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://piszek.com/2021/02/07/composability/
---

[Composability Is the Only Game in Town – Roam, Shipping Containers, Lego and Twitter.](https://piszek.com/2021/02/07/composability/)  



Lego Blocks, Shipping Containers, Roam Research, Open Source, and any other unreasonably successful endeavor follows the fractal design of composability.

*Epistemic confidence: 3/5*. *I intend to return to this post in the future.*

## **Shipping containers**

The current iteration of global capitalism is built on the backbone of a shipping container. Not the car nor the plane. As much as I do think the washing machine is transformative ([and do check out this TED talk by Hans Rosling](https://href.li/?https://www.ted.com/talks/hans_rosling_the_magic_washing_machine)), it didn’t have an impact as huge as the shipping container.

From vgr’s [“The Epic Story of Container Shipping”](https://href.li/?https://www.ribbonfarm.com/2009/07/07/the-epic-story-of-container-shipping/):

> *At the beginning of the story, total port costs ate up a whopping 48% (or $1163 of $2386) of an illustrative shipment of one truckload of medicine from Chicago to Nancy, France, in 1960. In more comprehensible terms, an expert quoted in the book explains: “a four thousand mile shipment might consume 50 percent of its costs in covering just the two ten-mile movements through two ports.” For many goods then, shipping accounted for nearly 25% of total cost for a product sold beyond its local market. Fast forward to today: the book quotes economists Edward Glaeser and Janet Kohlhase: “It is better to assume that moving goods is essentially costless than to assume that moving goods is an important component of the production process.”*

Shipping containers are standardized and composable. Much like the most successful software.

## Open Source, and UNIX philosophy

As much as the container is the backbone of the current economy, the software will be the backbone of a new one that we all help to build. If we take the “evolutionary” definition of success, the most successful piece of software will be some obscure low-level library or a Unix tool running on every modern device. Here are the first two Unix principles [according to Wikipedia](https://href.li/?https://en.wikipedia.org/wiki/Unix_philosophy):

* **Make each program do one thing well**. To do a new job, build afresh rather than complicate old programs by adding new “features”.
* Expect the **output of every program to become the input to another**, as yet unknown, program. Don’t clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don’t insist on interactive input.

As you can see, these are interlocking – do one thing well, and build “higher” when connecting more things that do one thing well. In my mind, Unix philosophy, Open Source, and building an information economy go hand in hand. Each next iteration can stand on the shoulders of giants, using the abstractions built by previous developers. We don’t have to sync time anymore, allocate memory, or deal with disk I/O operations. We can use ready tools to do just that, to focus on building something more complex.

## Roam Research

You may have heard about Roam Research – a Note-Taking app that has gained a cult-like following, and a $200 million investment at a $900 million valuation. If you have not heard about Roam before – [Anne-Laure has a good introduction](https://href.li/?https://nesslabs.com/roam-research). If you feel like note-taking is suddenly hip without any reason, [I have an explainer here.](https://href.li/?https://deliber.at/2020/note-taking-apps/)

How has Roam gained this popularity? Is it all a scam? After trying it out – I’ve noticed two aha moments:

#### **The first Roam AHA moment**

You discover, that the expected value of your notes grows exponentially. If I have a 1:1 (a 2-person Team-Lead <-> Team member meeting) with David, I can type [[1:1]] with [[David]] and I create notes simultaneously:

* As my TODO in the daily note
* On the page called 1:1
* On the page called David

During the day – to the day I can also create a note [[David]] posted a good post here: (link).. When I later visit [[David]] page, I can see the history of our 1:1s and all data I meant to include in the formal feedback when the time comes.

**Even though I have never visited or even created “David” page before.**

This “higher expected value of each line of notes” is like crack – gets the thoughts out of my brain faster than any other tool, since it’s rewarding bringing concepts together.

#### **The second AHA moment is all about composability**

The real kicker is the second AHA moment. In Roam, not only EVERYTHING is a block, but also the blocks interact with each other sensibly while nested

**Table**

No interface, I just nest bullets and table appears

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**KANBAN**

I create a Kanban the same way I create a table – since everything is an interplay of nesting, I immediately know how to create this Kanban. Gutenberg is already pretty good at this – we are trying to follow similar patterns across our blocks, but there are a lot of custom interfaces.

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**How about table in a Kanban?**

EVERYTHING is composable

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Ok, enough about Roam Research. The message is that composability let’s you be way more creative by knowing a few basic principles. But to call something “composable”, we have to have:

* A canonical unit of “thought”
* Multiple nesting levels
* Lists of things behave differently than things themselves

### What about functional programming?

I do realize, that composability is an aspect of functional programming, and nothing new to the fans of closure, lisp, or even a functional approach to writing plain old JavaScript.

* Roam Research is written in closure, and transpiled to JavaScript
* Paul Graham (a startup demigod and a very clear thinker) is continuously playing with Bel – a variation of LISP

I do appreciate the elegance of a purely functional language and after realizing the closure-roam-research link I can see how that mindset translates. But nevertheless – relying on the language to translate into a better product is ignoring the messy complexity of the real world.

In the real world (unlike the comfortable world of the algorithms), the program has to interact with the vast spectrum of inputs and outputs – thus **npm with its library of packages may be better representing composability** than any functional language. In the end, composability’s goal is to achieve real-world results with simple, easy-to-reason blocks. And yes, I credit React’s success to the composability of JSX.

## Writing on the Internet

Publishing on the Internet at its core is composable too. We can argue if the sentence, a paragraph, or a blog post is the canonical unit of clear thought, but blogging lets you organize the uneasy mess of “stuff” into coherent blocks you can compose into more and more clear reasoning. The linear structure of the page lets you examine each and every paragraph for doing what they are supposed to be doing. The list of paragraphs is just like a row of containers organized in a higher-order unit (a ship) that makes it easy to move.

### Twitter

Twitter is similar to Roam in more ways than one. To the casual user, it’s a hellhole of political arguments and fabricated urgency, but for those who know how to use it, it has almost infinite expression power based on simple rules.

#### Twitter Threads are composable.

Remember the requirements for composability I have outlined above? Twitter satisfies them all.

* A tweet is a self-contained complete thought
* Threads let you organize these thoughts into more complex narratives
* You can nest and recombine them at will

> I still think about how [@artpi](https://twitter.com/artpi?ref_src=twsrc%5Etfw) described tweets as sushi <https://t.co/LBsAWrgwuO>
> 
> — visa is doing military stuff 🪖 (@visakanv) [October 1, 2020](https://twitter.com/visakanv/status/1311552102183825408?ref_src=twsrc%5Etfw)


*Sidenote: Follow [Visakan](https://twitter.com/visakanv) (a master of threads) if you want a kinder, more productive Twitter.*

### WordPress

WordPress has introduced a new, block-based editor for your posts and pages. [The underlying premise is that everything will be a block](https://wptavern.com/gutenberg-engineer-matias-ventura-unpacks-the-vision-for-gutenblocks-front-end-editing-and-the-future-of-wordpress-themes), unlocking new mental models for users of the CMS powering close to 40% of the Internet. I am proud to help make this vision a reality.

## Composability succeeds because it enables cooperation

When evaluating a product or endeavor we tend to focus on metrics, features, and shiny checklists:

* This has more bloblybums,
* That is soo shiny,
* The other thing succeeded because it’s just faster,

But over the long term, the thing that succeeds tends to do so, because it makes it easier for people to work together. Composability is a framework for putting new layers of abstraction in a predictable manner.

An average human can hold about seven items in short-term memory and successfully cooperate in a team of seven people. Composability reduces the cognitive load by organizing things into higher-order sets, which in turn – can be reasoned about or reduced further.

## Notable mentions

Other, successful composable things include:

* Lego blocks,
* Written word (letters -> sentences -> paragraphs -> pages),
* World Wide Web and HTML
* Matter in the Universe (The Elements are comprised of the same 3 building blocks)
* Memes (TikTok in particular)
* …

## Notable exceptions

Despite my clickbaity title, there are successful endeavors that are NOT composable:

* App Stores / App economy – apps usually don’t mix with each other

Anything else?

### *Related*