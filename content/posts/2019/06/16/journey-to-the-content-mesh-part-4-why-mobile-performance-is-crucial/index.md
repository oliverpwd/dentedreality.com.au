---
title: 'Journey to the Content Mesh Part 4: Why Mobile Performance Is Crucial'
date: '2019-06-16T18:44:42-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.gatsbyjs.org/blog/2018-10-16-why-mobile-performance-is-crucial/
---

[Journey to the Content Mesh Part 4: Why Mobile Performance Is Crucial](https://www.gatsbyjs.org/blog/2018-10-16-why-mobile-performance-is-crucial/)  



*This is Part 4 of a series. Part 1 is* The Journey to a Content Mesh*; Part 2 is* Unbundling of the CMS*; Part 3 is* The Rise of Modern Web Development.

Mobile traffic now makes up over half of all site visits, and more than half of mobile site visits are abandoned if a page takes [over 3 seconds to load](https://www.thinkwithgoogle.com/data-gallery/detail/mobile-site-abandonment-three-second-load/).

With the Fortune 500 spending millions of marketing dollars on marketing initiatives aimed at driving traffic to their site, the business impact of bouncing visitors is clear — [every 100ms of latency costs 1% of sales.](https://www.digitalrealty.com/blog/the-cost-of-latency/)

Unfortunately, in practice, great performance is surprisingly hard to achieve — average page load times *haven’t improved* over several years of increasing connection speed.

Why is that? Increased site complexity often distributes bottlenecks across multiple code points and teams of stakeholders. While performance checklists exist, they’ve ballooned to 40+ items — making them costly and time-consuming for teams to implement.

As Gatsby’s co-founder Kyle Mathews likes to say (paraphrasing Tolstoy):

> All fast websites are alike, but all slow websites are slow in different ways.

Ultimately, we’ll argue, performance must be solved *at the framework level* — that is, in the content mesh.

## The rise of smartphone usage

Between 2014 and 2017, mobile usage (including tablets) rose from 20% of site visits to 50% of site visits.

Source: [StatCounter](http://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/worldwide/2011)

When smartphones were first created, the first key challenge of website teams was to offer a responsive version of their site that worked on mobile devices *at all.*

As mobile has grown to half of internet traffic, the key challenge has shifted to performance.

## Faster connections haven’t translated to faster sites

While average phone connection speed, as well as processing power, has increased over the last several years, sites haven’t gotten faster. In fact, load times **have increased**.

Data from the HTTPArchive shows how long it’s taken for the average page on the Internet to completely load all content (including images, script files, CSS files, etc.):

![](https://www.gatsbyjs.org/static/1d2fb9958f7c0ef36bb3ed19b59c535d/07137/web-perf-over-time.png)![](https://www.gatsbyjs.org/static/1d2fb9958f7c0ef36bb3ed19b59c535d/07137/web-perf-over-time.png)  


Web performance over time  





Source: [HTTPArchive](https://httparchive.org/reports/loading-speed?start=2014_02_01&end=latest&view=list#ol)

Why is that?

Connection speeds for mobile device have increased, while Moore’s Law has made devices faster. However, these speed dividends have been eaten up by two things.

First, **[heavier page weights](https://www.keycdn.com/support/the-growth-of-web-page-size/)**.

This has generally driven by increased page complexity driven by increased user expectations.

Second, the **growing complexity of websites**. Non-critical images, CSS, JS libraries, and 3rd party tracking software will often unintentionally end up on the critical path to page load:

* A marketing analyst drops a `<script>` tag from a hot new vendor inside a Google Tag Manager container. This triggers a blocking network call to a pixel provider on page loads. Time To Interactive (TTI) now averages 800ms longer.
* After a team whiteboarding session, the lead designer for a popular lifestyle magazine decides to switch to a custom default site font. On Friday afternoon, a developer scans the JIRA ticket, thinks “this should be easy” and implements a two-line code change. The site now takes 20% longer to load.
* The business unit of an e-commerce store needs additional inventory management tools, so they purchase a popular plugin in their CMS ecosystem that offers this functionality. What they don’t know is that this plugin adds additional database calls every time a user loads a product page, delaying overall page loads by 500ms.

With website performance rarely tracked, almost never systematically, and with no performance “owner”, it’s easy to see how load times can balloon.

Like factory floors before the advent of [just-in-time manufacturing](https://en.wikipedia.org/wiki/Just-in-time_manufacturing), website page loading paths are clogged with work being done prematurely, creating resource contention and increasing cycle time.

## Growing attention to the crisis of mobile performance

In the last 2-3 years, there’s been growing attention to the crisis of mobile performance from a number of different corners:

* As e-commerce grows globally, enterprises are increasingly targeting users on smartphones, often outside the fast-connection First World.
* In January 2018, Google announced that [it would use mobile page speed](https://webmasters.googleblog.com/2018/01/using-page-speed-in-mobile-search.html) as a ranking for mobile SEO. In July 2018, those changes took effect.
* Movements such as [Progressive Web Apps](https://developers.google.com/web/progressive-web-apps/) and the [JAMstack](https://jamstack.org/) have brought attention to site performance as a first-order goal.

*Performant* is the new *responsive*.

For digital agencies and enterprises, the challenge becomes: how to achieve performance, while delivering websites on time and within project budgets?

## How performance optimization works

There are two *types* of performance optimizations.

Teams can optimize the *payload* — what they’re serving users. Or they can optimize *delivery* — how it gets to the client.

**Payload optimization**

*Payload optimizations* involve items like reducing image and JS weight, deferring below-the-fold image calls, and inlining critical CSS.

When the amount of content and number of requests sent over the wire are minimized, users can interact with your site more quickly.

**Delivery optimization**

*Delivery optimizations* involve serving files from a content delivery network (CDN) — whether you’re compiling to files or caching — rather than letting each request hit your app server and database.

CDNs are globally available, so they’ll be closer to your customer than your systems, which reduces [round-trip time](https://en.wikipedia.org/wiki/Round-trip_delay_time) (RTT). Serving files means that users get content immediately without requests waiting in queues or requiring database queries.

**You may need to do both**

Payload optimization and delivery optimization are complementary approaches. That’s both good news — you *can* do both — and bad news — you often *need* to do both.

For example, if you use a CDN to serve 3MB JavaScript bundles, your site is still going to be slow, especially on medium- and low-end mobile devices.

![](https://www.gatsbyjs.org/static/52f077157bf90dfcc2a7062952121765/07137/network-requests-adobe-com.png)![](https://www.gatsbyjs.org/static/52f077157bf90dfcc2a7062952121765/07137/network-requests-adobe-com.png)  


Part of a network request waterfall chart for a typical enterprise website ([adobe.com](https://www.adobe.com)). The full waterfall chart is three times longer.  





Performance is an *emergent characteristic* of a system. It requires getting a lot little things right and is easy to mess up. That’s *why* fast websites are similar, but slow websites are slow in different ways.

## Optimizing performance is difficult and expensive

The challenge for digital agencies and enterprises is that both payload and delivery optimizations can require significant developer time to implement.

**Delivery optimization**

For delivery optimization, one approach is to use a JAMStack solution like Hugo or Gatsby, which compile your site to static files that can be served from a global CDN, rather than scaling app servers and databases. This approach, when used for initial site construction, requires little developer time in return for large performance gains.

Caching a traditional CMS website is another possibility — though this often creates bugs (what if an item goes out of stock?), as well as confusion around the content go-live process.

**Payload optimization**

But if delivery optimization is *hard*, payload optimization can be *near impossible* to deliver within time and budget for many agencies and enterprises.

Comprehensive checklists [weigh in at around 40 items](https://www.smashingmagazine.com/2019/01/front-end-performance-checklist-2019-pdf-pages/), including points like route-based code splitting, HTTP/2 asset serving, background prefetching, lazy-loading non-critical assets, service workers, dead code elimination, and server-side rendering. Each of these points is technically feasible but quite rare.

Among the many implementation challenges are:

* **Time and budget**. Performance optimization happens at the end of projects, which means that even in the rare case time is allocated, it can be dropped in the rush to fix bugs and make up for inevitable schedule slippage.
* **Skill mismatches**. Performance optimization is not in the skillset of many frontend developers. Simple changes by non-performance-oriented developers can easily undo days or weeks of dedicated performance work without dedicated training or stringent code review.
* **Lack of executive visibility**. Regular site performance reporting is rare, and difficult to track over time.
* **Lack of developer visibility**. While systems like Bugsnag can tie errors to specific lines of code, performance visibility is much higher level, even with detailed tools like Google Lighthouse. For non-experts, it’s difficult to pinpoint performance regressions to specific code commits.

## Performance should be solved at the framework level

Web performance is critical for retaining and engaging users, especially on mobile. If [every 100ms of latency costs 1% of sales](https://www.digitalrealty.com/blog/the-cost-of-latency/), reducing average page load times from 5 seconds to 1-2 seconds could generate 30-40% more sales.

But just because performance is the *right* thing doesn’t make it the *easy* thing. Implementing performance optimizations on a *per-site basis* is often *difficult* and *costly*.

To overcome these obstacles, high-performing website teams should look to a content mesh that bakes in performance on a *framework* level.

One example is Gatsby, which includes both delivery optimization and payload optimization out of the box.

In the next and final post in this series, Creating Compelling Experiences, we’ll explain how to implement a content mesh and get all the benefits of best-of-breed content systems, modern development frameworks, and high-performing websites.

![](https://www.gatsbyjs.org/static/cba6bb1f4ca309ec62ce91ae4b64b306/07137/modern-website-performance.png)![](https://www.gatsbyjs.org/static/cba6bb1f4ca309ec62ce91ae4b64b306/07137/modern-website-performance.png)  


Achieving modern website performance