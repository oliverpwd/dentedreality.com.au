---
title: AWS, MongoDB, and the Economic Realities of Open Source
date: '2020-01-11T16:26:48-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://stratechery.com/2019/aws-mongodb-and-the-economic-realities-of-open-source/
---

[AWS, MongoDB, and the Economic Realities of Open Source](https://stratechery.com/2019/aws-mongodb-and-the-economic-realities-of-open-source/)  



In 1999, music industry revenue in the United States peaked at $14.6 billion (all numbers are from the [RIAA](https://www.riaa.com/u-s-sales-database/)). It is important to be precise, though, about what was being sold:

* $12.8 billion was from the sale of CDs
* $1.1 billion was from the sale of cassettes
* $378 million was from the sale of music videos on physical media
* $222.4 million was from the sale of CD singles

In short, the music industry was primarily selling plastic discs in jewel cases; the music encoded on those discs was a means of differentiating those pieces of plastic from other ones, but music itself was not being sold.

This may sounds like a stupid distinction, but it explains what happened after that peak:

[![](https://stratechery.com/wp-content/uploads/2019/01/Screen-Shot-2019-01-14-at-1.27.11-AM-1024x768.png)![](https://stratechery.com/wp-content/uploads/2019/01/Screen-Shot-2019-01-14-at-1.27.11-AM-1024x768.png)](https://www.riaa.com/u-s-sales-database/)

Music industry revenue plummeted, even as the distribution and availability of music skyrocketed: the issue is that people were no longer buying plastic discs, which is what the music industry was selling; they were simply downloading music directly.

#### Selling Convenience

The problem is that recorded music has always been worthless: once a recording is made, it can be copied endlessly, which means the supply is effectively infinite; it follows that to capture value from a recording depends on the imposition of scarcity. That is exactly what plastic discs were: a finite supply of a physical good differentiated by their being the most convenient way to get music. Pirating MP3s from sites like Napster or its descendants, though, was even more convenient — and cheaper.

As you can see from the chart, the industry started to stabilize in 2010, and in 2016 returned to growth; 2018 looks to be up around 10% from 2017’s $8.7 billion number, and it seems likely the industry will pass that 1999 peak in the not-too-distant future.

What happened is that the music industry — prodded in large part by Spotify, and then Apple — found something new to sell. No, they are still not selling music; in fact, they are beating piracy at its own game: the music industry is selling convenience. Get nearly any piece of recorded music ever made, for a mere $10/month.

#### DocumentDB (with MongoDB compatibility)

Last week, from the [AWS blog](https://aws.amazon.com/blogs/aws/new-amazon-documentdb-with-mongodb-compatibility-fast-scalable-and-highly-available/):

> Today we are launching [Amazon DocumentDB (with MongoDB compatibility)](https://aws.amazon.com/documentdb/), a fast, scalable, and highly available document database that is designed to be compatible with your existing MongoDB applications and tools. Amazon DocumentDB uses a purpose-built SSD-based storage layer, with 6x replication across 3 separate Availability Zones. The storage layer is distributed, fault-tolerant, and self-healing, giving you the the performance, scalability, and availability needed to run production-scale MongoDB workloads.

The specifics of MongoDB and now DocumentDB are not particularly important to this article; basically, MongoDB created a type of database that is more flexible and better suited to large

 

1 amounts of both structured and unstructured data, making it useful for large scale applications that traditional [relational databases](https://stratechery.com/2016/oracles-cloudy-future/) were never designed to accommodate.

And now you can run it on AWS. Kind of.

#### Open Source Licensing

Like an increasing number of such projects, MongoDB is open source…or it was anyways. MongoDB Inc., a venture-backed company that IPO’d in October, 2017, made its core database server product available under the [GNU Affero General Public License (AGPL)](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License).

 

2

AGPL is a close relative of the [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License), the copyleft license created by [Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman). “Copyleft” means that the license allows for the free distribution, use, and modification of copyrighted material (in this case software), with the stipulation that those same rights extend to all derivative works; that means that any project built using GPL code must itself have a GPL license. This is in contrast to “permissive” open source licenses that allow others to use the copyrighted material however they wish, without a stipulation that derivative works also be open-sourced. AGPL extended the GPL to apply to software accessed over a network; since the software is only being used, not copied, the GPL would not triggered, but the end result is even more onerous than the GPL.

Both GPL and especially AGPL tend to be very problematic for companies: Apple, for example, [does not allow software licensed with the GPL on the App Store](https://www.zdnet.com/article/android-vs-iphone-the-gpl-question/), because the App Store requires that apps be licensed for a single user; apps with permissive licenses are fine — their license can be replaced — but the GPL, once applied, cannot be removed. AGPL is worse, because its provisions are triggered by users simply using the software; that’s why Google bans its use internally. The company notes in its [open source documentation](https://opensource.google.com/docs/using/agpl-policy/):

> The license places restrictions on software used over a network which are extremely difficult for Google to comply with. Using AGPL software requires that anything it links to must also be licensed under the AGPL. Even if you think you aren’t linking to anything important, it still presents a huge risk to Google because of how integrated much of our code is. The risks heavily outweigh the benefits.

There is one addendum to the policy:

> In some cases, we may have alternative licenses available for AGPL licensed code.

This is MongoDB’s business.

 

3

#### MongoDB’s Business Model

MongoDB explained in their [S-1](https://www.sec.gov/Archives/edgar/data/1441816/000104746917006014/a2233365zs-1.htm):

> We believe we have a highly differentiated business model that combines the developer mindshare and adoption benefits of open source with the economic benefits of a proprietary software subscription business model. To encourage developer usage, familiarity and adoption of our platform, we offer Community Server as an open source offering, analogous to a “freemium” offering. Community Server is a free-to-download version of our database that does not include all of the features of our commercial platform. This allows developers to evaluate our platform in a frictionless manner, which we believe has contributed to our platform’s popularity among developers and driven enterprise adoption of our subscription offering…
> 
> Unlike software companies built around third-party open source projects, we own the intellectual property of our offerings since we are the creators of the software, enabling our proprietary software subscription business model…Our primary subscription package is MongoDB Enterprise Advanced, our comprehensive offering for enterprise customers that can be run in the cloud, on-premise or in a hybrid environment. MongoDB Enterprise Advanced includes our proprietary database server, advanced security, enterprise management capabilities, our graphical user interface, analytics integrations, technical support and a commercial license to our platform. We also offer MongoDB Atlas, our cloud hosted database-as-a-service, or DBaaS, offering that includes comprehensive infrastructure and management of our Community Server offering.

Basically, MongoDB sells three things on top of its open source database server:

* Additional tools for enterprise companies to implement MongoDB
* A hosted service for smaller companies to use MongoDB
* Legal certainty

The importance of this last one can not be overstated: MongoDB’s enterprise version and hosted service are not governed by the AGPL — or, as of late last year, a new MongoDB-created license called the [Server Side Public License (SSPL)](https://www.mongodb.com/blog/post/mongodb-now-released-under-the-server-side-public-license). The SSPL is like the AGPL on steroids: it compels companies selling MongoDB-as-a-service to not only open-source their modifications, but also open-source their entire stack.

 

4

#### What AWS Sells

The largest company selling software-as-a-service is, of course, Amazon. That, though, does not mean that Amazon is selling “software.” The reality is that software is no different than music: it is infinitely reproducible, and thus, in isolation, worth nothing.

Instead, the value of software is typically realized in three ways:

* First is hardware. The most famous example is the iPhone, which is the only way to obtain iOS, but there are countless other examples.
* Second is licenses. This was Microsoft’s core business for decades: licenses sold to OEMs (for the consumer market) or to companies directly (for the enterprise market). Indeed, there is a bit of irony in that both Microsoft and open source, for all their historical opposition to each other, both depended on copyright, strong legal regimes, and companies doing the right thing.
* Third is software-as-a-service. This is Microsoft’s new model, as well as Amazon’s, and almost all new enterprise software companies.
   
  
  5 In this case what is being sold is not the software per se, but rather the utility of the software: the company doing the selling does everything else, including making the software available reliably.

With that in mind, read again what AWS announced last week:

> The storage layer is distributed, fault-tolerant, and self-healing, giving you the the performance, scalability, and availability needed to run production-scale MongoDB workloads.

AWS is not selling MongoDB: what they are selling is “performance, scalability, and availability.” DocumentDB is just one particular area of many where those benefits are manifested on AWS.

Make no mistake: these benefits are valuable. There is a secular shift in enterprise computing moving to the cloud, not because it is necessarily cheaper (although costs are more closely aligned to usage), but because performance, scalability, and availability are hard problems that have little to do with the core competency and point of differentiation of most companies.

Those are, though, the core competency of AWS, which can bring unmatched scale to bear on solving them: by effectively operating the servers for millions of customers Amazon can apply more resources to all of those issues than any one company could on its own, as well as develop its own customer architecture, from datacenter software down to custom chips (and drive a hard bargain for hardware from suppliers like Intel).

The result is that “performance, scalability, and availability” is a tremendously attractive business: the more customers AWS has not only drive that much more recurring revenue, but also deepen AWS’ moat by allowing the company to bring that many more resources to bear on ever more obscure use cases, making AWS that much more attractive to new customers. Microsoft is competing but is a distant second; Google is even further behind. In fact, even MongoDB’s managed service runs on the three giants: it simply makes no sense to go it alone.

#### The Open Source Conundrum

Thus we have arrived at a conundrum for open source companies:

* MongoDB leveraged open source to gain mindshare.
* MongoDB Inc. built a successful company selling additional tools for enterprises to run MongoDB.
* More and more enterprises don’t want to run their own software: they want to hire AWS (or Microsoft
   
  
  6 or Google) to run it for them, because they value performance, scalability, and availability.

This leaves MongoDB Inc. not unlike the record companies after the advent of downloads: what they sold was not software but rather the tools that made that software usable, but those tools are increasingly obsolete as computing moves to the cloud. And now AWS is selling what enterprises really want.

Worse, because AWS doesn’t have access to MongoDB (it is only matching the API) it only supports MongoDB 3.6; the current version is 4.0.5. It is possible that if AWS’ service becomes popular MongoDB will effectively stagnate: sure, you can get a better version from MongoDB Inc., but then you have to manage it yourself or go the effort to tie in all of your AWS services with MongoDB’s offering (then again, the potential for differentiation may be MongoDB’s salvation, and an important lesson for other companies).

Not that permissive licensing would necessarily help: Redis Labs offers its Redis database under a permissive license; that means that [AWS’ offering](https://aws.amazon.com/redis/) is usually up-to-date, which is good for Redis development, but doesn’t help Redis Labs make any money. That compelled Redis Labs to [change the licensing on its add-on modules](https://www.zdnet.com/article/open-source-licensing-war-commons-clause/) to add the “Commons Clause”; this compels service providers to pay for their use, effectively making them proprietary software.

It’s hard to not be sympathetic to MongoDB Inc. and Redis Labs: both spent a lot of money and effort building their products, and now Amazon is making money off of them. But that’s the thing: Amazon isn’t making money by selling software, they are making money by providing a service that enterprises value, and both MongoDB and Redis are popular in large part because they were open source to begin with.

#### Economic Realities and the Future

Little of what I wrote is new to folks in the open source community: the debate over the impact of cloud services on open source has been a strident one for a while now. I think, though, that the debate gets sidetracked by (understandable) discussions about “fairness” and what AWS supposedly owes open source. Yes, companies like MongoDB Inc. and Redis Labs worked hard, and yes, AWS is largely built on open source, but the world is governed by economic realities, not subjective judgments of fairness.

And that is why I started with music: it wasn’t necessarily “fair” that music industry sales plummeted, and yes, companies like Apple with its iPod business made billions off of piracy. The only reality that mattered, though, was that music itself, thanks to its infinite reproducibility, was as pure a commodity as there could be.

It’s the same situation with software: bits on a disk are fundamentally free — just ask Richard Stallman. In his seminal essay [Why Software Should Be Free](https://www.gnu.org/philosophy/shouldbefree.en.html) Stallman wrote:

 

7

> A copy of a program has nearly zero marginal cost (and you can pay this cost by doing the work yourself), so in a free market, it would have nearly zero price. A license fee is a significant disincentive to use the program. If a widely useful program is proprietary, far fewer people will use it.
> 
> It is easy to show that the total contribution of a program to society is reduced by assigning an owner to it. Each potential user of the program, faced with the need to pay to use it, may choose to pay, or may forego use of the program. When a user chooses to pay, this is a zero-sum transfer of wealth between two parties. But each time someone chooses to forego use of the program, this harms that person without benefiting anyone. The sum of negative numbers and zeros must be negative.
> 
> But this does not reduce the amount of work it takes to develop the program. As a result, the efficiency of the whole process, in delivered user satisfaction per hour of work, is reduced.

This tradeoff is inescapable, and it is fair to wonder if the golden age of VC-funded open source companies will start to fade (although not open source generally). The monetization model depends on the friction of on-premise software; once cloud computing is dominant, the economic model is much more challenging.

That, though, should give pause to AWS, Microsoft, and Google. It is hard to imagine them ever paying for open source software, but at the same time, writing (public-facing) software isn’t necessarily the core competency of their cloud businesses. They too have benefited from open-source companies: they provide the means by which their performance, scalability, and availability are realized. Right now everyone is winning: simply following economic realities could, in the long run, mean everyone is worse off.

*I wrote a follow-up to this article in [this Daily Update](https://stratechery.com/2019/mongodb-follow-up-aws-incentives-batteries-the-iphones-missing-miss/).*

### *Related*

[Apple and the Oak Tree](https://stratechery.com/2017/apple-and-the-oak-tree/)Wednesday, August 2, 2017

[Spotify’s Podcast Aggregation Play](https://stratechery.com/2019/spotifys-podcast-aggregation-play/)Thursday, February 7, 2019

[Apple Should Buy Netflix](https://stratechery.com/2016/apple-should-buy-netflix/)Monday, October 31, 2016


1. *humongous* []
2. I’m sorry, but this next bit is going to be dry; bear with me please []
3. To be clear, I’m not saying that Google has a license; rather, that MongoDB offers alternative licenses []
4. I’m using software-as-a-service as an umbrella term for infrastructure-as-a-service and platform-as-a-service []
5. To be clear, I don’t agree with Stallman on a whole host of things; that doesn’t diminish his importance as a thinker or influence on the industry, though, or his insights on the nature of software []