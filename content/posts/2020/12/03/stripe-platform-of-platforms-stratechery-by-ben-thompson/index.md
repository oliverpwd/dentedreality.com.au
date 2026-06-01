---
title: 'Stripe: Platform of Platforms – Stratechery by Ben Thompson'
date: '2020-12-03T22:08:47-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://stratechery.com/2020/stripe-platform-of-platforms/
---

[Stripe: Platform of Platforms – Stratechery by Ben Thompson](https://stratechery.com/2020/stripe-platform-of-platforms/)  



Today [Stripe is announcing Stripe Treasury](https://www.wsj.com/articles/stripe-to-offer-banking-services-in-deal-with-goldman-sachs-citigroup-11607007608); from the company’s [press release](https://stripe.com/newsroom/news/treasury):

> Stripe, the technology company building economic infrastructure for the Internet, today announced that it is launching Stripe Treasury. This gives Stripe’s platform users powerful APIs to embed financial services, enabling their customers to easily send, receive and store funds…
> 
> Stripe Treasury…enabl[es] platforms like Shopify to easily offer its merchants access to critical financial products to manage their businesses’ finances. With Stripe Treasury, platforms can offer their users interest-earning accounts eligible for FDIC insurance in minutes, enabled by Evolve Bank & Trust. Platform business customers can have near-instant access to revenue earned through Stripe, spend this directly from their balance with a dedicated card, transfer it via ACH or wire transfer, pay bills, and more.

Stripe Treasury, [as its website notes](https://stripe.com/treasury), is banking-as-a-service, but, critically, Stripe is not a bank; look carefully at the product’s press image:

[![](https://stratechery.com/wp-content/uploads/2020/12/stripe-3-1024x614.png)![](https://stratechery.com/wp-content/uploads/2020/12/stripe-3-1024x614.png)](https://stripe.com/treasury)

That is an API call creating a bank account at Goldman Sachs for a pilot on the [Rocket Rides](https://rocketrides.io/) platform. Notably, Goldman Sachs is not the only big bank on board; again from the press release:

> Stripe is enabling standardized access to global banking capabilities via APIs by developing its bank partner network to include Goldman Sachs Bank USA and Evolve Bank & Trust as US partners, and Citibank N.A. and Barclays as global expansion partners. Stripe will fulfill compliance and regulatory requirements in partnership with its US banking partners to make it easy for platform customers using Stripe Treasury to embed banking experiences into their products. And through Stripe, these banks are able to extend their reach to millions of businesses.

This is a textbook example of the power of platforms; consider an operating system like Windows: any number of applications can run on any number of computers thanks to there being an abstraction layer in the middle:

[![](https://stratechery.com/wp-content/uploads/2017/01/FullSizeRender-1024x861.jpg)![](https://stratechery.com/wp-content/uploads/2017/01/FullSizeRender-1024x861.jpg)](https://stratechery.com/2017/amazons-operating-system/)

This is analogous to the layer for banking that Stripe is offering with Treasury:

![](https://stratechery.com/wp-content/uploads/2020/12/stripe-2-1024x767.png)![](https://stratechery.com/wp-content/uploads/2020/12/stripe-2-1024x767.png)

This explains that API call above: a Rocket Rides pilot doesn’t have the wherewithal to open a business bank account at Goldman Sachs, and Goldman Sachs doesn’t have the flexibility to offer a banking account to individual entrepreneurs. This, though, is the exact sort of problem platforms solve: they provide an abstraction layer that connects different sides of a market, even if those different sides have dramatically different needs and capabilities.

#### Stripe and Shopify

It is Stripe’s partnership with Shopify, though, that is particularly compelling, and emblematic of both how powerful Treasury can be, and how extensive Stripe’s platform ambitions are. Again from the press release:

> For businesses today, accessing financial services can typically involve a series of bureaucratic hoops and a lengthy application process. According to recent Stripe research, setting up an account takes 5 and a half days on average (and 7 days on average for online businesses), around one in four (23%) businesses have to send a fax to open an account, and over half of businesses (55%) are required to visit a branch in person to open a bank account. Financial services simply weren’t designed for the modern internet, and this is a pain point for businesses today: nearly half (46%) of companies report that their banking experience has hindered their company growth.

This is a pain point I know quite well; Stratechery is incorporated in the U.S., and I had to fly back to the U.S. for the express purpose of opening a business bank account!

> This kind of off-line banking experience is increasingly incongruous in a world where 76% of businesses (e.g. retailers) use an industry-specific software platform to manage their business, a figure that increases to 92% for businesses with more than 500 employees. The feedback from Stripe’s users is that they want a digital solution for financial services available directly within the software platform that powers their operations. On the flipside, Stripe’s platform customers are increasingly looking to embed financial services into their own product, but oftentimes face barriers to doing so.

Now with Treasury, someone starting up a new Internet business can simply start selling goods, services, or yes, subscriptions, and have their banking needs met by the same software which is powering their business. Stripe co-founder and President John Collison explained in [an interview](https://stratechery.com/2020/an-interview-with-stripe-president-john-collison):

> Which seems more ergonomic for a business? That they decide they’re going to start an online store and the very first thing they do is go down to a bank, and maybe in person, and they’re going through that process, they’re setting up their accounts, then they come back and do some white boarding. And they’re like, “Hmm, what should our business be?” That’s not how it works.
> 
> How it works is they have this cool idea and they try it out and they open a Shopify store for it and they have this money coming in. So we need a way to access those funds, now they will be able to, with Shopify Balance, manage their funds directly within Shopify. That latter thing sounds like a much more natural and ergonomic way to handle the cash flows of their business.

What is notable about Shopify is that it too is a platform, and a very powerful one at that. This is how I described the company’s then-new logistics offering in 2019’s [Shopify and the Power of Platforms](https://stratechery.com/2019/shopify-and-the-power-of-platforms/):

> What Shopify is doing is what platforms do best: act as an interface between two modularized pieces of a value chain.
> 
> [![](https://stratechery.com/wp-content/uploads/2019/07/IMG_272058378EFF-2.jpeg)![](https://stratechery.com/wp-content/uploads/2019/07/IMG_272058378EFF-2.jpeg)](https://stratechery.com/2019/shopify-and-the-power-of-platforms/)
> 
> Every referral partner, developer, theme designer, and now 3PL provider are simultaneously incentivized to compete with each other narrowly and ensure that Shopify succeeds broadly, because that means the pie is bigger for everyone.
> 
> On one side are all of Shopify’s hundreds of thousands of merchants: interfacing with all of them on an individual basis is not scalable for those 3PL companies; now, though, they only need to interface with Shopify.

Thus the title of this Article: Stripe isn’t simply a platform, it is a platform for platforms.

#### Stripe Capital

This broader understanding of Stripe’s ambition became clear to me earlier this week with another announcement, [Capital for platforms](https://stripe.com/capital/platforms). Stripe Capital itself is not new; launched in 2019 the service lends money to businesses that use Stripe’s payments processor; as [Bloomberg noted at the time](https://www.bloomberg.com/news/articles/2019-09-05/fintech-startup-stripe-will-lend-money-to-customers):

> As the industry has become more digital, PayPal Holdings Inc., Square and even Amazon have introduced small business lending programs, as have a slew of startups including SoftBank Group Corp.-backed Kabbage Inc. and public company OnDeck Capital Inc. Though lending poses risks, Stripe, much like other payment services, says the extra data it has on customers will give it a better idea of whether borrowers can repay loans. The company believes that edge will protect it from significant losses during an economic downturn.

Stripe Capital seemed both obvious and, as the article notes, rather unoriginal; this week’s expansion — which was announced with a [29-word blog post](https://stripe.com/blog/capital-for-platforms) — makes clear it is much more. Carefully read this tweet from founder and CEO Patrick Collison:

> Mundane though it sounds, access to capital is the primary bottleneck that limits the growth and expansion of most small businesses.
> 
> So we built Capital for platforms: <https://t.co/3BvZhCz9Bo>. Help \*your\* customers grow faster by using our lending infrastructure. [pic.twitter.com/z7xxfM9GFD](https://t.co/z7xxfM9GFD)
> 
> — Patrick Collison (@patrickc) [December 1, 2020](https://twitter.com/patrickc/status/1333834822330896384?ref_src=twsrc%5Etfw)

Note the word Patrick Collison emphasized: *\*your\**. Capital for platforms is not for Stripe’s customers, but rather the customer of Stripe’s customers, which is to say, Stripe is asserting itself as the platform of platforms; go back to the news that [Shopify Balance](https://www.shopify.com/balance) will be powered by Treasury:

![](https://stratechery.com/wp-content/uploads/2020/12/stripe-1-1024x767.png)![](https://stratechery.com/wp-content/uploads/2020/12/stripe-1-1024x767.png)

Stripe does not have a customer relationship with all of the Shops on Shopify; that is exactly what Shopify is good at, so why would they? Instead, Stripe is focusing on what it is good at: providing that API layer to banks that will never have the capability to serve Shopify Shops, and exposing said layer to Shopify to incorporate into their product.

Notably, Treasury skipped the intervening step that Capital started with: Stripe isn’t exposing banking-as-a-service to customers directly on Stripe, but rather making an API available to those customers to offer to their customers. John Collison explained to me:

> We have a lot of conviction about this idea that the financial services that a plumber needs will be different from financial services that an e-commerce company needs will be different than financial services that a gym or a yoga studio needs, and they will be provisioned by different companies. Given that we have lots and lots of exposure to those kinds of businesses with our platform partners, this is a great way to get started with that.

This means the above illustration, fully realized, looks a bit like this:

![](https://stratechery.com/wp-content/uploads/2020/12/stripe-5-1024x767.png)![](https://stratechery.com/wp-content/uploads/2020/12/stripe-5-1024x767.png)

#### Stripe’s Ambition

Here I think Stripe’s goal — building the economic infrastructure for the Internet — is instructive. Consider the Internet itself: you are reading this Article on the Internet via a connection provided by an Internet Service Provider, which is a relatively local affair that is designed for a particular geography. It is Internet Service Providers that connect to a grand network of cables that is known as the Internet backbone; this map from [Telegeography](https://www.submarinecablemap.com/), for example, shows the world’s submarine cables:

[![](https://stratechery.com/wp-content/uploads/2020/12/stripe-4-1024x629.png)![](https://stratechery.com/wp-content/uploads/2020/12/stripe-4-1024x629.png)](https://www.submarinecablemap.com/)

This image is incomplete — major portions of the Internet backbone obviously run overland — but is sufficient for the analogy: Stripe isn’t necessarily competing with other fintech providers — ISPs in this analogy — but instead is seeking to be the backbone for all of them, as well as an entirely new universe of platforms that can offer their unique customers financial services that are perfectly tuned to their needs.

Stripe is ten years old now, but the ambition implied by these announcements explain why the founders claim they are just getting started. John Collison noted:

> We are still very early in developing the set of Stripe products beyond the core payments engine, things like Treasury. We’re building a global payments and treasury network, and we are in November of 2020 launching the Treasury part of it, and so we are just now filling out all the acronyms in our product suite, and that’s the version one of the product. And from a growth point of view, our business is growing really rapidly in APAC and EMEA, and so we’re just early in the business trajectory with all the helter-skelter-ness that comes from that.

Speaking as an analyst, I would like nothing more than to see an S-1 from Stripe, but it sounds like it’s not coming anytime soon (and I can state with a high degree of confidence that Stripe will not be doing a SPAC with any of its rumored suitors); the company is [reportedly raising more money](https://www.bloomberg.com/news/articles/2020-11-24/payments-startup-stripe-is-said-in-talks-to-raise-new-funding), but is increasingly spending the money it raises on acquisitions and investments (one would certainly assume that the core payments business is not only profitable but also has a very attractive cash conversion cycle).

Instead the company is busy building, well, exactly what it has said it was building all along: economic infrastructure. And, I will freely admit, until this week I didn’t completely appreciate just how mammoth an undertaking that was.

*Stratechery subscribers can read the full interview with John Collison [here](https://stratechery.com/2020/an-interview-with-stripe-president-john-collison); it is also available for subscribers [via podcast](https://stratechery.com/podcasts).*

### *Related*