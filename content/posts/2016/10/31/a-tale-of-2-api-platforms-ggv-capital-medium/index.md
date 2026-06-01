---
title: A Tale of 2 API Platforms – GGV Capital – Medium
date: '2016-10-31T09:52:20-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/ggv-capital/a-tale-of-2-api-platforms-39f8dfd77436
---

[A Tale of 2 API Platforms – GGV Capital – Medium](https://medium.com/ggv-capital/a-tale-of-2-api-platforms-39f8dfd77436)  



Opening up an API is a big commitment, one that needs to be managed well over time in order to ensure a healthy and thriving ecosystem. If a company is still in the throes of developing a product strategy and business model, it’s worth waiting to offer a highly accessible, external API. It’s better to understand first where you’re going as a company, and then enable a massive network of partnerships to accelerate your product in that direction, with complementary experiences. If your company is thinking about offering a public API, this post is for your consideration. Let’s take a look at Twitter and Slack to illustrate the ways this can play out.

**The Twitter API & Ecosystem Misalignment**

In the summer of 2012, Twitter made significant changes to their API, sunsetting version 1 and introducing 1.1, with limited access and a host of new usage policies. Of all the changes to the API, the most controversial was Twitter limiting how many users a third-party client app could have. This ensured that these client apps (which largely replicated the core Twitter experience) could not grow too big and thus, not competitive. Prior to this, Twitter’s API offered largely unfettered access with little applied policy. Early on, Twitter was extremely busy just trying to maintain the service — remember the [fail whale](https://upload.wikimedia.org/wikipedia/en/d/de/Failwhale.png)? When the API was published, the only first-party Twitter client was the website. The API enabled an incredible flood of mobile third-party clients spanning all major mobile platforms of the day: iOS, Android, Blackberry, and so on.

The early days were magical, with apps such as Tweetbot, Twitterlator, Twitterific, UberTwitter, Seesmic, Brizzly, Falcon, and many others driving meaningful feature development. At this time, the API already had 900k apps registered from 600k developers, and it was processing an insane 13 billion requests a day. The “Twitterverse” was massive. It was undoubtedly one of the most exciting APIs to build with in recent memory.

![](https://cdn-images-1.medium.com/max/800/1*2klOdzufUpTIqE6n3Zs-8w.jpeg)![](https://cdn-images-1.medium.com/max/800/1*2klOdzufUpTIqE6n3Zs-8w.jpeg)

However, as Twitter increasingly felt that their most scalable business model would be advertising, it became crucial that Twitter own the direct UI relationship with users. This became particularly pronounced when Twitter purchased Tweetie, the iOS client, and in that moment this new first-party app suddenly became indistinguishable from the service itself. Additionally, for every great client out there, there were many poorly made clients with bad user experiences. This was toxic for users trying the service for the first time, causing high churn and further forcing Twitter to offer a first-party mobile app.

But **most** important, it was around this time that a bomb went off in the ecosystem. Bill Gross’ company UberMedia began buying up several third-party Twitter clients: Echofon, UberTwitter, Twidroyd, and was looking to buy Tweetdeck. Had UberMedia successfully bought Tweetdeck, they’d have controlled a significant base of clients: dictating how many users would create and consume Tweets. There was an acute awareness within Twitter of what an existential threat this posed — if UberMedia created a shadow network, siphoned off users, and dropped Twitter out of the equation entirely, it would have been disastrous.

In a sense, this meant that all of the consumer-facing third-party clients and aggregation apps were suddenly competitive — leading to misaligned incentives, and a major tightening of policies. Below is the infamous “API quadrant”, illustrating where it was and wasn’t safe to play.

![](https://cdn-images-1.medium.com/max/800/1*y9z1Om35UJZ2i7A9YGMgJg.png)![](https://cdn-images-1.medium.com/max/800/1*y9z1Om35UJZ2i7A9YGMgJg.png)

This was largely the end of Twitter’s API “golden age”. An API is a contract with external developers, and once it’s out there taking it away is like trying to put toothpaste back in the tube: it’s hard. Are there other ways this v1.1 transition could have been managed, like continued unfettered access without user limits but with an ad syndication model for third-party clients? Yes, absolutely — but that’s for another post. Even though only a small subset of developers was actually affected by the v1.1 changes (remember, the ecosystem was huge and there were many different classes of apps), the impact of v1.1 sent shockwaves through the developer community and resulted in an erosion of trust, paramount to a flourishing platform.

![](https://cdn-images-1.medium.com/max/800/1*Q1E-ebmTR8efsvl4XuUezg.png)![](https://cdn-images-1.medium.com/max/800/1*Q1E-ebmTR8efsvl4XuUezg.png)

**Slack’s API & Aligned Incentives**

Contrast Twitter’s approach with the way Slack manages their API ecosystem. Slack has deliberately aligned incentives with their ecosystem, focusing on complimentary apps that are weaved into their service. For instance, some of the top apps on Slack’s API cover functions such as project management, calendar control, expense accounting, and more. These Slack apps that utilize a subset of scopes & permissions (via OAuth) are featured in an [app directory](https://ggvc.slack.com/apps) after a review is conducted. This directory helps increase discoverability and distribution, crucial to removing friction and providing apps with the user liquidity they need to thrive.

These third-party apps enrich the core Slack experience in complementary ways. This is good for all participants: users get a better experience, developers acquire more users, and Slack gets far more functionality than it could have developed in house. The incentives are aligned. Slack is taking a proactive approach to guiding and managing their ecosystem. Despite the dangers of publishing a [roadmap](https://www.slack.com/apps) that’s certain to change, Slack has done so in the spirit of setting expectations. Furthermore, they’ve provisioned an “[Ideaboard](https://trello.com/b/HPpcIqd8/slack-app-ideaboard)” to relay market feedback they get from customers; giving developers a sense of the problems that customers need solved.

![](https://cdn-images-1.medium.com/max/800/1*lmXJpF8es_KFOg6q9EJoxA.png)![](https://cdn-images-1.medium.com/max/800/1*lmXJpF8es_KFOg6q9EJoxA.png)

Perhaps most impressive, Slack assembled an $80M fund to directly invest in third-party apps. This is putting money where Slack’s mouth is, provisioning capital to the developer community and allowing them to sustain operations while they build a business. Slack has invested almost $2M into 14 apps, with a particular focus on bot-style apps. This is a fantastic approach to ensuring that the best apps are rewarded and encouraged to maintain a high quality experience.

**Managing an Ecosystem**

So we return to a common question many companies face today: whether they should open an API to become a data service or platform? Opening an API is a huge commitment, and it’s easy to underestimate the amount of work that goes along with enabling a healthy ecosystem. To be entirely fair to Twitter the API was launched incredibly early, well before the business model was figured out and obviously before there was an existential threat of client consolidation by a single external player. This made it extremely difficult for the company to continue pursuing a wide open API and spin up a healthy ad business in parallel. Remember that there are huge expectations of a company in its hyper-growth stages, in particular on when said company is going to make **a lot** of money. It’s important to note here too, that the third-party developers who built clients in the early days benefited greatly: they got users of their own (a subset of Twitter users), positive social regard in the developer community, and many of them made varying amounts of money (some of them made a lot of money).

Healthy APIs should drive reciprocal benefits to the provider, third-party app developers, and users. If your company is going to offer an API and you want to facilitate a strong ecosystem, you must invest heavily. You must constantly be working to set your developer community up for success. It’s not enough to just publish the API and hope things works out. It requires a lot of forethought to properly orchestrate the right set of incentives, access, and policies for developers. Think through the types of experiences that you want your ecosystem to enable (and which experiences you want to directly own); then build out the APIs to enable such functionality. Configure your APIs, documentation, and policies to guide developers higher up the value chain. And make your core product experience **great**, so that there’s not demand for alternative core experiences.

Conversely, don’t offer APIs for functionality that you must own in-house. If you offer an API that powers the core facets of your product, then you’re effectively guiding your developer base to build the same service or some close derivative thereof; imagine if Twitter had never publicly offered the home timeline API. Lastly, when you find those keystone integrations in the ecosystem that illustrate watermark use cases you’d like to see tackled by the developer community — bang the drum for these apps! Let the ecosystem know this is the level of quality all other apps should aspire to. Demonstrate how you take care of players who hit this watermark with increased distribution, co-marketing opportunities, increased API access, and more. At the end of the day, if there’s trust, clear lines of communication, well set expectations, and reciprocal benefit being driven across all participants in a platform — an incredible ecosystem can flourish. Look no further than companies like Stripe, Twilio, and others to see how powerful this can be. Just go in eyes wide open that it is a meaningful investment, and one that you must be committed to for the long term.




*Jason Costa is currently an EIR at* [*GGV Capital*](http://www.ggvc.com/companies)*. This post is part of an ongoing series aimed at exploring topics such as consumer product development, platform analysis, and strategy.*