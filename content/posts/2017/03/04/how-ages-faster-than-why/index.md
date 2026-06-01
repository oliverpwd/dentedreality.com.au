---
title: “How” ages faster than “Why”
date: '2017-03-04T22:16:18+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://hackernoon.com/how-ages-faster-than-why-712e25c9eb3b
---

[“How” ages faster than “Why”](https://hackernoon.com/how-ages-faster-than-why-712e25c9eb3b)  



# “How” ages faster than “Why”

I used to write a lot of Angular back in 2015. But recently, the JS community has largely moved on from Angular 1 to other libraries, and in turn, so have my projects. I always knew in the back of my mind that technology — and the knowledge that goes along with it — becomes outdated, but this was the first time I experienced it for myself. I wondered: what parts of my Angular knowledge are now obsolete? What parts are long-lasting? And most importantly, how can I make sure that I always get better as an engineer in the face of all those fleeting frameworks and libraries?

### Fleeting Knowledge

Let’s start by identifying the fleeting knowledge — the kind that won’t help us 10 years from now. That would be a framework’s API and syntax, like Angular’s syntax for one-way vs two-way binding, or the mechanics for how to make a directive. Knowing those nitty gritty details of Angular and its API is necessary to be productive in an Angular codebase, but it’s useless in any other codebase. I refer to this type of knowledge as the “how” — as in, “How do I do X in Angular?”.

It’s also the kind of knowledge that’s easy to acquire. Picking up the keywords of a framework is easy — just google it, copy paste from StackOverflow, some basic pattern matching here and there, and we’re done. So not only is this type of knowledge fleeting, it’s also less valuable since it’s so commonplace. Companies don’t hire senior engineers for this type of knowledge.

### Enduring Knowledge

The more enduring kind of knowledge is the “why”. Why does Angular exist? Why does it have the features that it has? What problems is it trying to solve?

Frameworks like Angular may have a short lifespan, but the problems they tackle live on for much longer. Angular was built to tackle the problem of writing, maintaining, and iterating on complex web apps. Any knowledge that helps us approach this problem will be valuable for a long time. In fact, it’s not a huge stretch to swap “web apps” for “software”, and suddenly we’ve got a problem that’s going to last an entire career! That’s the kind of knowledge we want — the **enduring** kind.

### Diving Deep

Asking “why” and getting to those enduring nuggets of knowledge isn’t always easy unfortunately. The context and motivation behind a particular feature is the kind of knowledge that’s harder to come by, but it’s well worth the effort. Let’s go through an example.

Say I google “Why should I use Angular”. I might run into reasons like this:

* MVC and separation of concerns
* Two-way data binding
* Dependency Injection

If I don’t know what MVC and dependency injection are and why they’re good practices, then I’m simply left with more questions. Why would I want dependency injection? And why is separation of concerns useful?

So let’s keep digging (disclaimer — this is super simplified):

* Angular uses dependency injection…
* …and dependency injection is useful for writing unit tests
* …and unit tests are useful for maintaining and iterating on software

Got it! Now I learned about dependency injection, which a generic design pattern that’ll be useful to me past Angular’s lifetime. This knowledge also helps me better understand how and when to use that Angular feature, and when I can ignore it. Practical knowledge for our Angular work today, and enduring design pattern knowledge for the future. Win-win!

In general, asking why is a **recursive** process, just like installing a software dependency. We have to follow all the recursive dependencies until they all resolve, otherwise we end up with broken software — or in this case, incomplete understanding. We have to continually dig deeper until we hit a layer whose value we understand. [Kids know this intuitively](https://www.youtube.com/watch?v=BJlV49RDlLE)!

### Your brain’s dependency tree

Here’s how I (simplistically) imagine the “Why Angular” knowledge dependency tree:

```
Angular  
├─┬ MVC  
| ├─┬ Separation of concerns  
| | ├── Software Maintainability  
├─┬ Dependency Injection  
| ├─┬ Unit Testing  
| | ├── Software Maintainability  
| | ├── Development iteration speed  
├─┬ Two way data binding  
| ├─┬ Reconciling state  
| | ├── Reducing bugs
```

At the top level we have the most specialized and most fleeting solutions: frameworks like Angular. One level deeper, we get into specific patterns that are common across different frameworks: DI, MVC, etc. As we dive deeper, we get into more fundamental software engineering practices, and so on until we arrive at core problems in software engineering.

I love this visualization because it exposes the deeper level concepts for what they are: **building blocks**. Once we dive deep into a framework that uses MVC and learn what MVC is all about, then we’ll carry that understanding over to any other MVC framework we use in the future. It’s just like when a package manager installs a new package and finds one of the dependencies already installed — it can just reuse it.

Having more building blocks doesn’t just makes us faster learners, it’s also essential for innovating new solutions. Almost every new piece of software is inspired by many other ideas before it. One example is [redux](http://redux.js.org/), which is inspired by [Flux](http://facebook.github.io/flux), [CQRS](http://martinfowler.com/bliki/CQRS.html), [Event Sourcing](http://martinfowler.com/eaaDev/EventSourcing.html), and probably more (perhaps [Clojure atoms](https://clojure.org/reference/atoms)). We stand on the shoulders of giants not just by using the software they built, but by understanding the ideas they introduced.

### Personal Reflection

I often find that the path of least resistance when working on a project is to just look up exactly what I need, paste it in, and ship it. But now I realize that plowing through projects semi-blindly isn’t the best idea for my personal growth.

Looking back, I could’ve gotten more out of my Angular experience by:

* understanding Angular’s decisions within the context of the problems it was solving
* asking why and not being afraid of following the rabbit holes
* understanding the motivations and tradeoffs behind the Angular features

We should learn frameworks not just to build stuff, but to learn new ideas because once a framework is out of use, the ideas are all that’s left. But when a framework doesn’t teach us anything new, I am reminded of Alan Perlis’s quote:

> *“A language [or framework] that doesn’t affect the way you think about programming, is not worth knowing.”*

Even if frameworks come and go, we can still learn the ideas behind them and become better engineers, as long as we dive deep enough.