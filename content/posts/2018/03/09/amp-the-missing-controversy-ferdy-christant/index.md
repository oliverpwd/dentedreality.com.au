---
title: 'AMP: the missing controversy – Ferdy Christant'
date: '2018-03-09T17:32:42+00:00'
format: link
service: instapaper
tags:
- read
external_url: https://ferdychristant.com/amp-the-missing-controversy-3b424031047
---

[AMP: the missing controversy – Ferdy Christant](https://ferdychristant.com/amp-the-missing-controversy-3b424031047)  



[![](https://cdn-images-1.medium.com/fit/c/120/120/1*-gR3QVXyaUGn3KxjaKr1kw.jpeg)![](https://cdn-images-1.medium.com/fit/c/120/120/1*-gR3QVXyaUGn3KxjaKr1kw.jpeg)](https://ferdychristant.com/@ferdychristant?source=post_header_lockup)
[Ferdy Christant](https://ferdychristant.com/@ferdychristant?source=post_header_lockup)
Web developer, wildlife photographer, founder of www.jungledragon.com
Feb 9





![](https://cdn-images-1.medium.com/freeze/max/60/1*ceh7eagXiM6ahQTL_ZkXWw.png?q=20)![](https://cdn-images-1.medium.com/freeze/max/60/1*ceh7eagXiM6ahQTL_ZkXWw.png?q=20)![](https://cdn-images-1.medium.com/max/1600/1*ceh7eagXiM6ahQTL_ZkXWw.png)![](https://cdn-images-1.medium.com/max/1600/1*ceh7eagXiM6ahQTL_ZkXWw.png)

## How Google cheats with performance

### Introduction

AMP, Accelerated Mobile Pages, is a technology first launched in 2015 by Google. The main goal of the initiative is to drastically speed up the loading of web pages on mobile. Sorely needed, as the typical web page on slow 3G (a very typical network condition the world over) takes a long time to load.

So the goal in itself seems worthy. Yet the initiative has been met with lots of controversy over the years. I’m going to go briefly over these main points of controversy.

The main goal of this article though is to add a **new point of controversy**, one hardly discussed. **The reason why AMP has instant performance**.

First, let’s look at the other points of controversy.

#### Controversy #1: a new web “standard”

AMP has been created completely outside of W3C and WHATWG, the main standard bodies for the web. Standard bodies in which Google has a large, if not dominant presence.

AMP makes up its own standards that break with what is considered valid HTML. Case in point, have a look at how the AMP project’s homepage, which itself is an AMP page, produces over a 100 validation errors:

[**Showing results for https://www.ampproject.org/ – Nu Html Checker**  
*This tool is an ongoing experiment in better HTML checking, and its behavior remains subject to change*validator.w3.org](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.ampproject.org%2F)

In AMP’s defense, despite it breaking the standard, browsers will render that page just fine because browser know how to deal with invalid HTML quite well. Because, well, pretty much every web page ever created is invalid HTML.

So this is merely a theoretical controversy. We have a shared web, governed by standards bodies. AMP ignores this reality.

Google’s main defense is that AMP is open source. Which isn’t just a weak defense, it’s no defense at all. I can open source a plan for genocide. The term “open source” is meaningless if the thing that is open source is harmful.

#### Controversy #2: loss of sovereignty of your website

One of the main implications of publishing an AMP page is that the page will be served from the Google domain. Or whoever is serving the AMP cache, yet mostly that will be Google.

This means less direct traffic on your origin, and more time spent at Google. Less traffic on your origin could mean less monetization opportunities. In general, it means less control of anything. You’re subject to whatever the AMP standard allows or disallows.

You’re giving up the sovereignty of your web site. Similar to when you publish all your content directly inside Facebook, you’re effectively losing all control of it now and in the future.

A simple defense here could be to just not use AMP. Ironically, AMP can actually increase traffic and drive better conversions. For the simple reason that it performs so much better than a normal web page. Hence, in the desperate race for traffic, organizations are lured towards AMP. The only price they have to pay is an almost complete loss of control over their web experience.

Build faster web pages then, and don’t use AMP? Even with this strategy, you cannot win from AMP’s performance. More on this in a minute.

#### Controversy #3: loss of diversity

On a diverse web, you would visit different origins, each having a different experience. Now compare this to Facebook, where every piece of content looks the same, coming from all over the web, yet flattened into a dull timeline. You don’t get to experience the home of that content, just the content itself.

This same effect of everything looking the same applies to AMP, in a lesser extend. In AMP’s defense, it’s possible to style an AMP page to fit your brand, yet there’s severe limitations in what you can and cannot do. Not just in styling, even more so in interactivity.

#### Controversy #4: performance

The items discussed above are not new, they’ve been discussed for years. So let us move on to the point of this article: the **performance controversy of AMP**. Which hardly is a topic of discussion it seems.

What we know about AMP is that the technical standard in itself enforces good performance. For example, CSS is limited to 50KB and only inline, custom JS is not allowed (other than via an iframe method), and all images are guaranteed to be lazy loading.

Hence, this is why AMP pages load instantly compared to a “normal” web page. It’s enforced by the standard. Right?

**Wrong.**

Let us look at a typical AMP page:

[**De rode Tesla van Elon Musk gaat toch niet naar de planetoïdengordel**  
*Dat blijkt uit nieuwe baangegevens die SpaceX vanmorgen via het HORIZONS-systeem van NASA heeft vrijgegeven (voor de…*www.scientias.nl](https://www.scientias.nl/rode-tesla-elon-musk-gaat-toch-naar-planetoidengordel/amp/)

It’s an ordinary AMP page. I didn’t pick an intentionally bad example. We’re going to check the performance of this AMP page by directly measuring it from the origin itself (so not from AMP cache):

![](https://cdn-images-1.medium.com/freeze/max/60/1*zJ8s3Q2JFfRp5XajtbOlog.jpeg?q=20)![](https://cdn-images-1.medium.com/freeze/max/60/1*zJ8s3Q2JFfRp5XajtbOlog.jpeg?q=20)![](https://cdn-images-1.medium.com/max/1600/1*zJ8s3Q2JFfRp5XajtbOlog.jpeg)![](https://cdn-images-1.medium.com/max/1600/1*zJ8s3Q2JFfRp5XajtbOlog.jpeg)

On webpagetest.org/easy (which preselects average 3G), the first meaningful paint is at 3.5s. A number that is not terrible in itself, pretty good actually, yet strangely far away from AMP’s typical instant performance.

Testing directly in Chrome, using “low-end mobile” and “mid-tier mobile” as presets (these slow down both the network and the CPU), we get **8.4s** and **2.3s** as first meaningful paint. Both aren’t close to instant performance, and 8.4s is just plain awful. *This* is an AMP page!?

![](https://cdn-images-1.medium.com/freeze/max/60/1*6z2higw-CIOex7f3Eo18lw.jpeg?q=20)![](https://cdn-images-1.medium.com/freeze/max/60/1*6z2higw-CIOex7f3Eo18lw.jpeg?q=20)![](https://cdn-images-1.medium.com/max/1600/1*6z2higw-CIOex7f3Eo18lw.jpeg)![](https://cdn-images-1.medium.com/max/1600/1*6z2higw-CIOex7f3Eo18lw.jpeg)

Using a Lighthouse audit, the page fails to score on the good side of performance. **Despite being fully valid AMP, a standard that enforces performance**.

So whilst obviously the technical restrictions of the AMP standard **help** with performance, they are in no way responsible for having instant performance. **Technically correct AMP pages will perform very similar to any non-horrible web page.**

The difference between AMP performing instantly and getting numbers ranging from 2–8s as seen above have to be explained.

Part of that answer you can probably guess: the cache is simply very fast. It’s hard to compete with a Google-class CDN. I imagine thousands of servers strategically placed worldwide on the best connections available.

Yet this fast cache doesn’t explain a 2–8s difference. It hardly affects it. This is what does:


![](https://cdn-images-1.medium.com/freeze/max/60/1*YLUlRM3Ie_j_xVZPapWeMA.jpeg?q=20)![](https://cdn-images-1.medium.com/freeze/max/60/1*YLUlRM3Ie_j_xVZPapWeMA.jpeg?q=20)![](https://cdn-images-1.medium.com/max/2000/1*YLUlRM3Ie_j_xVZPapWeMA.jpeg)![](https://cdn-images-1.medium.com/max/2000/1*YLUlRM3Ie_j_xVZPapWeMA.jpeg)



Here we are on Google Search on mobile. We searched for a term (“Elon Musk”). We scroll down in the results, in the bottom you can start to see the “Scientias” article that we profiled starting to appear.

At this moment, the network panel fills up with resources from that AMP page. Pretty much anything that page needs to render is **preloaded**, whether you actually open it not. If you do, it’s going to render instantly.

Not in 2–8s. Instantly. Technically, a clever trick. It’s hard to argue with that. Yet I consider it cheating and anti competitive behavior.

> The AMP page, which we all believe to be super fast and optimized for slow mobiles because it is AMP, isn’t that fast. Its true speed comes from preloading.

#### What it means

The above findings have a few very serious implications:

* Although AMP as a standard helps with mobile performance, the standard itself is not responsible for instant performance. AMP fails at those first crucial seconds just like any other web page. AMP pages on their own are in no way faster than a well designed mobile web page (in which you would have freedom to do anything).
* You can never compete with AMP’s instant performance, even if you’d build the fastest website in the world.

Here’s why I consider the scenario described above cheating and anti-competitive:

You likely are not the owner of a search monopoly, hence you cannot control loading behavior. Only Google can. Taking that page from 2–8s to instant performance is something only Google is capable of, because it is the only entity in the world controlling the most important information portal: search.

Preloading is exclusive to AMP. Google does not preload non-AMP pages. If Google would have a genuine interest in speeding up the whole web on mobile, it could simply preload resources of non-AMP pages as well. Not doing this is a strong hint that another agenda is at work, to say the least.

#### What it means for you

> The dilemma that comes with AMP, is that it works. Very well. End users will experience much faster pages and it’s very likely that your conversions will improve dramatically. A tempting, almost irresistible proposition for many organizations and businesses.

The point of my article is not to point you in any direction, even though it seems that way. I merely point out the main controversial points of AMP, and how and why it works the way it does. In particular, why it’s so fast. Which is not because of AMP. **Not at all because of AMP**.