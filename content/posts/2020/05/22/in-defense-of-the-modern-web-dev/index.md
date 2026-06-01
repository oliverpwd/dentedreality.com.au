---
title: In defense of the modern web – DEV
date: '2020-05-22T23:13:35-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://dev.to/richharris/in-defense-of-the-modern-web-2nia
---

[In defense of the modern web – DEV](https://dev.to/richharris/in-defense-of-the-modern-web-2nia)  



I expect I’ll annoy everyone with this post: the anti-JavaScript crusaders, justly aghast at how much of the stuff we slather onto modern websites; the people arguing the web is a broken platform for interactive applications *anyway* and we should start over; React users; the old guard with their artisanal JS and hand authored HTML; and [Tom MacWright](https://twitter.com/tmcw), someone I’ve admired from afar since I first became aware of his work on Mapbox many years ago. But I guess that’s the price of having opinions.

Tom recently posted [Second-guessing the modern web](https://macwright.org/2020/05/10/spa-fatigue.html), and it took the front end world by storm. You should read it, or at the very least the [CliffsNotes](https://twitter.com/tmcw/status/1259600386094030848). There’s a lot of stuff I agree with to varying degrees:

> There is a sweet spot of React: in moderately interactive interfaces … But there’s a lot on either side of that sweet spot.

It’s absolutely the case that running React in the client for a largely static site is overkill. It’s also true that you have to avoid React if your app is very heavily interactive — it’s widely understood that if you want 60fps animation, you will likely have to bypass the React update cycle and do things in a more imperative fashion (indeed, this is what libraries like [react-spring](https://www.react-spring.io/) do). But while all this is true of React, it’s much less true of component frameworks *in general*.

> User sessions are surprisingly long: someone might have your website open in a tab for weeks at a time. I’ve seen it happen. So if they open the ‘about page’, keep the tab open for a week, and then request the ‘home page’, then the home page that they request is dictated by *the index bundle that they downloaded last week*. This is a deeply weird and under-discussed situation.

It’s an excellent point that isn’t really being addressed, though (as Tom acknowledges) it’s really just exacerbating a problem that was always there. I think there *are* solutions to it — we can iterate on the ‘index bundle’ approach, we could include the site version in a cookie and use that to show actionable feedback if there’s a mismatch — but we do need to spend time on it.

> It’s your startup’s homepage, and it has a “Sign up” button, but until the JavaScript loads, that button doesn’t do anything. So you need to compensate.

This is indeed very annoying, though it’s easy enough to do this sort of thing — we just need to care enough:

```
<button class="sign-up" disabled={!is_browser}>
  {is_browser ? 'Sign up' : 'Loading'}
</button>

```

But I’m not sure what this has to do with React-style frameworks — this issue exists *whatever* form your front end takes, unless you make it work without JS (which you should!).

> Your formerly-lightweight application server is now doing quite a bit of labor, running React & making API requests in order to do this pre-rendering.

Again, this is true but more React-specific than anything. React’s approach to server-side rendering — constructing a component tree, then serialising it — involves overhead that isn’t shared by frameworks that, for example, compile your components ([hi!](https://svelte.dev)) to functions that just concatenate strings for SSR, which is faster by a dramatic amount. And those API requests were going to have to get made anyway, so it makes sense to do them as early as possible, especially if your app server and API server are close to each other (or even the same thing).

> The dream of APIs is that you have generic, flexible endpoints upon which you can build any web application. That idea breaks down pretty fast.

Amen. [Just go and read](https://macwright.org/2020/05/10/spa-fatigue.html) the whole ‘APIs’ section several times.

Minor quibbles aside, Tom identifies some real problems with the state of the art in web development. But I think the article reaches a dangerous conclusion.

Let’s start by dissecting this statement:

> I can, for example, guarantee that this blog is faster than any Gatsby blog (and much love to the Gatsby team) because there is nothing that a React static site can do that will make it faster than a non-React static site.

With all due respect to those involved, I don’t think Gatsby is a particularly relevant benchmark. The `gatsby new my-site` starter app executes 266kB of minified JavaScript for a completely static page in production mode; for [gatsbyjs.org](https://gatsbyjs.org) it’s 808kB. Honestly, these are not impressive numbers.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--L4S_VLxO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/1162160/82001896-43e38b00-962a-11ea-9ae7-bda853a8cec1.png)![](https://res.cloudinary.com/practicaldev/image/fetch/s--L4S_VLxO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/1162160/82001896-43e38b00-962a-11ea-9ae7-bda853a8cec1.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--L4S_VLxO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/1162160/82001896-43e38b00-962a-11ea-9ae7-bda853a8cec1.png)

The [Lighthouse score](https://webpagetest.org/lighthouse.php?test=200515_N4_a92cbdd5b87d402522f710a8d82d2228&run=1) for Gatsby’s homepage, obtained via [webpagetest.org/easy](https://webpagetest.org/easy).

Leaving that aside, I disagree with the premise. When I tap on a link on Tom’s JS-free website, the browser first waits to confirm that it was a tap and not a brush/swipe, then makes a request, and then we have to wait for the response. With a framework-authored site with client-side routing, we can start to do more interesting things. We can make informed guesses based on analytics about which things the user is likely to interact with and preload the logic and data for them. We can kick off requests as soon as the user first *touches* (or hovers) the link instead of waiting for confirmation of a tap — worst case scenario, we’ve loaded some stuff that will be useful later if they *do* tap on it. We can provide better visual feedback that loading is taking place and a transition is about to occur. And we don’t need to load the entire contents of the page — often, we can make do with a small bit of JSON because we already have the JavaScript for the page. This stuff gets fiendishly difficult to do by hand.

Beyond that, vanilla static sites are not an ambitious enough goal. Take transitions for example. Web developers are currently trapped in a mindset of discrete pages with jarring transitions — click a link, see the entire page get replaced whether through client-side routing or a page reload — while native app developers are thinking on another level:

> ![](https://res.cloudinary.com/practicaldev/image/fetch/s--EvUdPIJ5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://pbs.twimg.com/ext_tw_video_thumb/1186675126902779905/pu/img/JiHzCMbNwT-_nVXG.jpg)![](https://res.cloudinary.com/practicaldev/image/fetch/s--EvUdPIJ5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://pbs.twimg.com/ext_tw_video_thumb/1186675126902779905/pu/img/JiHzCMbNwT-_nVXG.jpg)  
> 
> ![](https://dev.to/assets/play-butt.svg)![](https://dev.to/assets/play-butt.svg)
> 
> 
> 
> ![](https://res.cloudinary.com/practicaldev/image/fetch/s--lfBp00Wj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://pbs.twimg.com/profile_images/1257111841508974592/2_rEXazl_normal.jpg)![](https://res.cloudinary.com/practicaldev/image/fetch/s--lfBp00Wj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://pbs.twimg.com/profile_images/1257111841508974592/2_rEXazl_normal.jpg)
> Ryan Florence
> 
> 
> ![](https://res.cloudinary.com/practicaldev/image/fetch/s--52oNvK_0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-ff4bdab814039c4cb172a35ea369e0ea9c6a4b59b631a293896ae195fa26a99d.svg)![](https://res.cloudinary.com/practicaldev/image/fetch/s--52oNvK_0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-ff4bdab814039c4cb172a35ea369e0ea9c6a4b59b631a293896ae195fa26a99d.svg)
> 
> 
> This is what I’ve had in mind for the web with React Router. We say these kinds of animations are “good for phones but not desktop”.
> 
> My iPad pro is as big as my laptop and these apps are shopping/content (most of the web).
> 
> These transitions are such a great UX.
> 
> 
> 16:06 PM – 22 Oct 2019
> 
>  [![](https://dev.to/assets/twitter-retweet-action.svg)![](https://dev.to/assets/twitter-retweet-action.svg)](https://twitter.com/intent/retweet?tweet_id=1186675229621248000)  
> 
> 20  
> 
>  [![](https://dev.to/assets/twitter-like-action.svg)![](https://dev.to/assets/twitter-like-action.svg)](https://twitter.com/intent/like?tweet_id=1186675229621248000)  
> 
> 197

It will take more than technological advancement to get the web there; it will take a cultural shift as well. But we certainly can’t get there if we abandon our current trajectory. Which is exactly what Tom *seems* to be suggesting.

I’m not aware of any other platform where you’re expected to write the logic for your initial render using a different set of technologies than the logic for subsequent interactions. The very idea sounds daft. But on the web, with its unique history, that was the norm for many years — we’d generate some HTML with PHP or Rails or whatever, and then ‘sprinkle some jQuery’ on it.

With the advent of Node, that changed. The fact that we can do server-side rendering and communicate with databases and what-have-you *using a language native to the web* is a wonderful development.

There are problems with this model. Tom identifies some of them. Another major issue he doesn’t discuss is that the server-rendered SPA model typically ‘hydrates’ the entire initial page in a way that requires you to duplicate a ton of data — once in the HTML, once in the JSON blob that’s passed to the client version of the app to produce the exact same result — and can block the main thread during the period the user is starting to interact with the app.

But we can fix those problems. [Next](https://nextjs.org/) is doing amazing innovation around (for example) mixing static and dynamic pages within a single app, so you get the benefits of the purely static model without ending up finding yourself constrained by it. [Marko](https://medium.com/@mlrawlings/maybe-you-dont-need-that-spa-f2c659bc7fec) does intelligent component-level hydration, something I expect other frameworks to adopt. [Sapper](https://sapper.svelte.dev/), the companion framework to [Svelte](https://svelte.dev/), has a stated goal of eventually not sending any JS other than the (tiny) router itself for pages that don’t require it.

The future I want — the future I *see* — is one with tooling that’s accessible to the greatest number of people (including designers), that can intelligently move work between server and client as appropriate, that lets us build experiences that compete with native on UX (yes, even for blogs!), and where upgrading part of a site to ‘interactive’ or from ‘static’ to ‘dynamic’ doesn’t involve communication across disparate teams using different technologies. We can only get there by committing to the paradigm Tom critiques — the JavaScript-ish component framework server-rendered SPA. (Better names welcomed.)

The modern web has flaws, and we should talk about them. But let’s not give up on it.