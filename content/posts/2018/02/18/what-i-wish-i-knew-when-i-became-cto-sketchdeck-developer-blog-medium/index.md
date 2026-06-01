---
title: What I wish I knew when I became CTO – SketchDeck developer blog – Medium
date: '2018-02-18T19:11:23+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/sketchdeck-developer-blog/what-i-wish-i-knew-when-i-became-cto-fdc934b790e3
---

[What I wish I knew when I became CTO – SketchDeck developer blog – Medium](https://medium.com/sketchdeck-developer-blog/what-i-wish-i-knew-when-i-became-cto-fdc934b790e3)  



![](https://cdn-images-1.medium.com/max/1000/1*XQt_TyJk4PjuyKJeDU6sOw.png)![](https://cdn-images-1.medium.com/max/1000/1*XQt_TyJk4PjuyKJeDU6sOw.png)


Over the last four years I’ve been the CTO at [SketchDeck](https://sketchdeck.com) and now, as I leave and hand the reins onto the team, I wanted to reflect on the experience and what I wish I’d known at the start.

It’s been a wild and wonderful experience. Founding a startup is an upside-down version of traditional employment: initially you’ve no idea if the company will take off nor if it’ll ever turn into a full-time job, then as it grows you keep on being thrust into new and different jobs. It’s reasonably common to end up doing jobs you’ve never done before. **You can accumulate responsibility faster than you can learn how to harness it.**

Startups are agile boats, but the decisions you make on day one do have rippling consequences over time. **I now appreciate that the infrastructure, frameworks and languages you choose will stick with you for a really long time** (hence why cloud providers can offer $100,000 initial credit). As the company grows there is an incredibly strong pressure to build more features and sub-systems, each one further locking you into your choices. As you gain more momentum the feature-pressure grows and stopping to re-write things is unaffordable and unthinkable.

I’ve been pretty happy with our choices: Amazon Web Services, Elastic Beanstalk, Firebase, AngularJS, Coffeescript, Kafka, Simple Queue System, SocketStream, Docker, SemaphoreCI, MySQL. **Of the list, AngularJS and MySQL have been the only ones to give us scaling problems**. Our monolithic AngularJS code-bundle has got too big and the initial download takes quite a while and the application is a bit too slow. MySQL (in RDS) crashes and restarts due to growing BI query complexity and it’s been hard to fix this.

**I appreciate now that technologies have a surprisingly short lifespan.** CoffeeScript and AngularJS are our most obviously tired components (we plan to migrate to TypeScript and latest Angular). All of our technologies were fairly bleeding-edge when we adopted them and it’s a blessing that my predilection for hipster technologies has not caused any serious problems.

I’ve hugely appreciated the succinct functional syntax of CoffeeScript and **believe it’s helped me achieve greater personal productivity over the years.**

Building on the above, **I now know that you need to budget time and strategize for the replacement of technologies. You accept long-term “technical debt” with the adoption of any technology.**

Similarly, components and libraries you write are going to hang around for a long time. However nicely or badly you write them, they’ll remain in the same state — therefore **it’s good to invest a little more time than is comfortable building them well for the sake of future maintainers.**

I’ve always been resistant to “the grand re-write”, where one pauses on feature building and just re-creates parts of the system. It’s been a famous death spiral for many projects. One technique that has worked well for us is *The Boy Scout Rule*:

> “Try and leave this world a little better than you found it” — Robert Baden Powell, Founder of the Boy Scouts and Girl Guides

**We try to make small improvements to the areas of code we work on.** Sometimes it can be stressful to think about the (always imperfect) overall state of the codebase, instead I focus on continual small improvements.

Finally, a short note on testing: **I’ve found it a real struggle to get our team to adopt writing tests.** I’ve written tests of many different parts of the system, and set up servers to automatically run the tests on every check-in. Despite this, I seldom see anyone else add tests. I always wanted testing to flourish based on its inherit merit, but sadly this didn’t happen. My ideas for resolving this are:

* Run refresher sessions on how to write tests
* Require significant features to include at least one test
* Optimize our test server to complete within 10 seconds instead of ten minutes (ouch!) so its output is relied upon by code authors.

Stepping aside from pure technical decisions, the life-blood of being a CTO is people management. The majority of your day-to-day will be managing, leading, hiring and firing people. I’ve had to learn all of this on the way and it certainly could have been smoother.

**No matter how many times I’ve read about how a company’s most important asset are the people, it never prepared me for how exhausting and excruciating hiring is.** To anyone new to hiring: you probably need to spend more time hiring and reject more people. You probably need to filter more stringently. I never could have guessed how rare the perfect startup team member is, nor how much time and effort would be needed to find them.

Knowing when to hire is an early conundrum: do I hire for this role now, or later, and which roles do I hire first? This is particularly hard if you have received funding as now you feel obliged to put the money to work. Fortunately, we received some helpful advice on this from Michael Siebel and YC:

1. **Only hire when you feel you’re completely desperate for the role** (e.g. you cannot keep up with building the features needed to close new contracts)
2. **Hire to keep up with growth, not to generate it** (this applies primarily to early stage companies before you have scalable, repeatable sales process)
3. **Don’t hire someone to do something you’ve not yet figured out** (some exceptional candidates can bring new capabilities to companies, but often the most reliable route is for some “founder magic” to re-assemble the company until it can perform the new thing)

Summarizing those two pieces of advice, **if you feel uncertain if you need to hire a particular role, it’s probably too early**. We went through quite a few cycles of trying to hire people to generate growth in ways we’d personally not mastered, and it mostly failed.

Managing people has been relatively smooth sailing — having regular open and honest check-ins about what is good and what is bad has kept me and my colleagues having healthy productive relationships.

I’ve found firing people a tough part of the job. A lot of useful advice has been written elsewhere, I’ll simply re-iterate that **your gut often knows you need to fire someone long before you rationally accept and perform it, and it’s always difficult.** Having good check-ins can help both parties prepare for negative outcomes. Finally, given a personal development plan, some people really do rise to the occasion and become great productive team members; everyone should have the opportunity to.

One of the greatest joys in watching the company grow has been seeing other people emerging as new leaders of their areas. I offer my respect and congratulation to the entire team.