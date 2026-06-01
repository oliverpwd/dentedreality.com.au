---
title: Eating the Cloud from Outside In
date: '2021-10-13T20:45:39-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.swyx.io/cloudflare-go
---

[Eating the Cloud from Outside In](https://www.swyx.io/cloudflare-go)  



Cloudflare launched on September 27, 2010, and every year since, it has made it a point to celebrate “[Birthday Week](https://blog.cloudflare.com/tag/birthday-week/)” with a raft of launches. By far, the show-stopper this year was the announcement of [R2 Storage](https://blog.cloudflare.com/introducing-r2-object-storage/), an S3-compatible Object Storage service that directly takes aim at [AWS’ “Hotel California” business model](https://blog.cloudflare.com/aws-egregious-egress/). This has been extremely well received, going by the response on [HN](https://news.ycombinator.com/item?id=28682237) and [Twitter](https://twitter.com/QuinnyPig/status/1443028078196711426). In its past 5 birthdays, Cloudflare has gone from world-class CDN to offering:

* 2017: [serverless compute](https://workers.cloudflare.com/)
* 2019: [website hosting](https://blog.cloudflare.com/extending-the-workers-platform/)
* 2021: object storage

…and declaring that they will be “[the fourth major public cloud](https://www.protocol.com/enterprise/cloudflare-r2-storage-aws)“. When your market cap is $36 billion and your next biggest competitor is worth $1.6 *trillion* (~45x larger, albeit not pure-play), this is a bold statement. Many startups are trying by offering specialized [Cloud Distros](https://www.swyx.io/cloud-distros/), but all building with AWS as the presumptive winner of the “first layer cloud” rather than trying to compete.

What’s Cloudflare’s strategy here?

**My realization: The big 3 clouds are playing Chess, but *Cloudflare is playing Go*.**

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dojvxo0i0u5v7cmm1d4p.png)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dojvxo0i0u5v7cmm1d4p.png)

The canonical thoughtleader of Disruption theory is the legendary HBS Professor Clayton Christensen, and a lot has been made of [Cloudflare’s Disruption](https://stratechery.com/2021/cloudflares-disruption/) of AWS; in fact, Cloudflare cofounders Matthew Prince and Michelle Zatlyn were [students of him](https://harbus.org/2011/cloudflare/) at HBS. James Allworth, their Head of Innovation, studied and [co-authored a book](https://claytonchristensen.com/books/how-will-you-measure-your-life/) with him. Prince [namechecked the Innovator’s Dilemma at Cloudflare’s launch](https://youtu.be/XeKWeBw1R5A?t=646) in 2010, and in 2021 is still proudly showing off a [handwritten note from him](https://news.ycombinator.com/item?id=28708636); in short, you can be sure his lessons are never far from Cloudflare’s minds.

As Ben Thompson noted in [his now-famous takedown of Christensen on the iPhone](https://stratechery.com/2013/clayton-christensen-got-wrong/), people often miss that he had *two* theories of disruption:

* **New Market Disruption**: When incumbents ignore new technologies until it is too late.
  + Allworth recently wrote an instant-classic application of this on [Intel (x86/CISC) vs Apple Silicon (ARM/RISC)](https://jamesallworth.medium.com/intels-disruption-is-now-complete-d4fa771f0f2c)
* **Low-End Disruption**: When vertically integrated premium incumbents get disrupted by “cheap and good enough” modular providers.

> A third model of disruption comes from Kevin Kwok’s [Atomic Concepts](https://kwokchain.com/2021/02/05/atomic-concepts/), but that is a closer fit for the [Cloud Distros](https://www.swyx.io/cloud-distros/) thesis than Cloudflare.

On the first theory: Cloudflare has some excellent technologists — [John Graham-Cumming](https://en.wikipedia.org/wiki/John_Graham-Cumming), [Kenton Varda](https://www.linkedin.com/in/kenton-varda-5b96a2a4/) and [Rita Kozlov](https://ritakozlov.com/about/) come to mind — and it is doing some cool things with V8 isolates and dynamic routing, but it doesn’t (in my mind) have a clear claim on the overall new technology angle, since AWS created the modern serverless paradigm, [open-sourced Firecracker](https://www.amazon.science/blog/how-awss-firecracker-virtual-machines-work), and [is using Lambda for half of all new applications](https://www.protocol.com/newsletters/protocol-enterprise/serverless-container-aws) (though Cloudflare is also [aggressively dogfooding Workers](https://blog.cloudflare.com/the-secret-to-cloudflare-pace-of-innovation/)).

Most of the disruption discussion focuses on the second model of disruption, and it rings true. Cloudflare took a part of the cloud nobody valued, gave away an insanely good free offering, and quietly accumulated an [80% market share](https://w3techs.com/technologies/cross/proxy/content_delivery). Meanwhile, when people think of “Tier 1” AWS services, its Cloudflare equivalent, Amazon CloudFront, rarely gets any love, and the official AWS Twitter account [hasn’t tweeted about it in almost a year](https://twitter.com/search?q=from%3Aawscloud%20cloudfront&src=typed_query&f=live). Cloudflare leveraged their foothold into selling premium security services, and now is expanding into other value added pieces by leaning into a fundamentally different (high fixed cost, near zero marginal cost) business model the larger incumbents structurally cannot follow.

This, at least, is how Ben Thompson framed it in [his writeup on Cloudflare’s Disruption](https://stratechery.com/2021/cloudflares-disruption/):

[![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7258tf9irknumz5db2vg.png)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7258tf9irknumz5db2vg.png)](https://stratechery.com/2021/cloudflares-disruption/)

But this diagram is a little too neat. It imagines the two clouds as worlds apart. Yet R2 is explicitly designed as S3-compatible; in Prince’s words, you can [set it to “slurp” mode](https://news.ycombinator.com/item?id=28703464) and you magically have a S3 interface with egress that is [six orders of magnitude cheaper](https://twitter.com/QuinnyPig/status/1443076111651401731?s=20). Similarly, the original Cloudflare service could always be used together with EC2, and Cloudflare Workers have different enough usecases and limitations from AWS Lambda and Lambda@Edge that you could conceivably have a stack using all of them.

This isn’t Apple vs Android; premium and vertically integrated vs cheap and modular; incompatible ecosystems, and never the twain shall meet.

This is something else.


In the classic game of Go, you [capture pieces](https://www.pandanet.co.jp/English/learning_go/learning_go_6.html) by surrounding your opponents, instead of directly replacing their spot.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7idppjskwr10z817xo42.gif)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7idppjskwr10z817xo42.gif)


You could view Cloudflare’s Bandwidth Alliance and R2 as an “encircling” move around AWS’ previously secure market position with S3. By promising to be API compatible (including offering S3’s eleven-nines durability guarantee and free infrequent access), Cloudflare has cut off nearly all of AWS’ remaining “liberties”, putting it in “[atari](https://en.wikipedia.org/wiki/List_of_Go_terms#Atari)“. If Cloudflare’s offering matures enough to be seen as a strict superset, it places the final stone, capturing the “cloud storage” territory.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o4kk6ucmg8mbqd0t0yzw.gif)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o4kk6ucmg8mbqd0t0yzw.gif)


In Chess, pieces have different values and capabilities. Bishops are worth 3 points and move diagonally, Rooks are worth 5 and move in straight lines, and so on. Pieces are best deployed in a sequence chain where higher value pieces support lower value ones.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/buwls1amzbahfv0q30d6.png)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/buwls1amzbahfv0q30d6.png)

In Go, each piece is indistinguishable from the other; it is the *network position* that counts, not any individual piece. Support doesn’t matter so much as adjacent territory claimed; in the picture below, the four white pieces on the left do far less than the four black pieces on the right.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pwwiby0brxdq3d7mzt6r.png)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pwwiby0brxdq3d7mzt6r.png)

Compare this to public statements about how Cloudflare works. [From Prince](https://news.ycombinator.com/item?id=28703194):

> **Since every server in our network runs every service**, once we’re in for one thing means everything we do in the region gets better and less expensive to operate. This means, counter intuitively, as we add more locations to our network our costs generally go down, not up.

So while AWS has [17 ways to run containers](https://www.lastweekinaws.com/blog/the-17-ways-to-run-containers-on-aws/) and [7 ways to do async message processing](https://serverlessfirst.com/aws-async-message-services/), all overlapping and reinforcing and supporting each other, Cloudflare will tend toward introducing singular primitives, [stuff them in a box](https://blog.cloudflare.com/cloudflare-for-offices/#built-for-purpose), and try to ship those boxes to [as many places as will possibly take them](https://blog.cloudflare.com/cloudflare-for-offices/). If they could install Cloudflare on your mobile phone, they would (this gets them dangerously close to being a [real life Pied Piper](https://www.youtube.com/watch?v=5JM8bkJLLjM)).


In Chess, you win when you take the King, which in effect has infinite point value, and it is relatively uncommon to come to a draw. In Go, you win by amount of territory claimed, and it is near impossible for one side to end up with zero territory. Perhaps this is more true to real life.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q8ne0yo5vzoytu04qdkv.png)![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q8ne0yo5vzoytu04qdkv.png)

While AWS boasts an impressive [230+ points of presence](https://aws.amazon.com/about-aws/global-infrastructure/), Cloudflare has [interconnects with 10,000 networks](https://www.cloudflare.com/network/) including “every major ISP, cloud provider, and enterprise”. These aren’t the same thing, but it reflects the substantially different game that Cloudflare is playing. From the point of view of users, Cloudflare can be much easier to use and is much more of a painkiller than other big cloud services in their stack, despite perhaps having a single digit % of mindshare and wallet share. This puts Cloudflare within a stone’s throw of Ben Thompson’s other big claim to fame in Tech Strategy, [Aggregation Theory](https://stratechery.com/aggregation-theory/) (the Intro to Tech Strategy chapter in [my book](https://www.learninpublic.org/) is free if you want my take on it).

Strategically, “Territory over Positioning” happens to be exactly the right call. In a zero-sum market that isn’t growing, you want to jockey for position and take out enemies. In a positive-sum, infinitely expanding market like Cloud, you want to encircle them.


To [quote Wikipedia](https://en.wikipedia.org/wiki/List_of_Go_terms#Gote,_sente_and_tenuki), a move that overwhelmingly compels a player into a particular follow-up move is said to have “sente” (先手), or “initiative”. In most games, the player who maintains “sente” most of the time will win.

There is a lot of speculation that AWS will have to respond somehow to Cloudflare’s provocations:

But beyond a [standard PR response](https://www.infoworld.com/article/3634406/cloudflare-hopes-lack-of-outbound-data-fees-will-convert-aws-s3-users-to-its-r2-storage-service.html), I doubt AWS will respond to mere noise – S3 data egress revenues have to take a significant downturn before AWS will be compelled to act. But when it does, every future move of Cloudflare’s will be taken increasingly seriously. Cloudflare acts and talks like it has “sente” now, but it isn’t real until AWS (or the other big clouds for that matter) feel forced to specifically respond.


While the tech industry is used to come-from-below disruption, and the software industry is increasingly grasping class-for-the-masses atomic concepts, I believe Cloudflare is writing a new playbook that is the little-guy counterpart of the [embrace, extend, extinguish](https://en.wikipedia.org/wiki/Embrace,_extend,_and_extinguish) model used by Microsoft.

Because it involves API compatibility, this playbook is particularly relevant to developer tools, and is protected by [the Supreme Court ruling in Google v Oracle](https://twitter.com/swyx/status/1379091545102503937). If I were to summarize it in three words, looking over Cloudflare’s history and [annual report](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001477333/fa0c28c8-a883-45cd-aba8-0b9c3249cc14.pdf), I might call it:

* **Establish**: Establish a foothold in something incumbents don’t care enough about
* **Envelop**: Reverse-proxy something that incumbents don’t serve customers well on
* **Expand**: cross-sell other premium products and services until they are more customers of you than they are customers of the incumbent.

Given Cloudflare’s fundamentally less-centralized approach to growing its cloud, it is no surprise that it [announced its first Ethereum product](https://blog.cloudflare.com/announcing-web3-gateways/) this Birthday Week; although it remains to be seen if a Web2-native company can really drop enough of its assumptions to handle Web3 threats or opportunities. If we are truly in the “early Internet” days of Web3, only the paranoid might survive here. Fortunately, Prince seems to be a [vocal fan of Andy Grove](https://twitter.com/search?q=from%3Aeastdakota%20grove&src=typed_query&f=top) as well.