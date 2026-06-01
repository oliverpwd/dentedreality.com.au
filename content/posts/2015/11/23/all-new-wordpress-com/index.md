---
title: All New WordPress.com
date: '2015-11-23T11:23:39+00:00'
tags:
- api
- javascript
- wordpress
- wordpress.com
- opensource
- Nodejs
- reactjs
- calypso
categories:
- posts
---

![Screen Shot 2015-11-23 at 10.07.31 AM](http://dentedreality.com.au/wp-content/uploads/2015/11/Screen-Shot-2015-11-23-at-10.07.31-AM-1.png)

Almost 2 years ago, I [wrote about](http://dentedreality.com.au/2013/12/03/future-wordpress-rest-api-javascript/) how the future of WordPress needed to be a REST-based API, with a JavaScript client on top of that. There were even [public rumors](https://twitter.com/schnarfed/status/442378974182653953) that, *gasp*, we were thinking about porting WordPress to Node.js. Well, while that’s not exactly true, it’s closer to the truth than a lot of people probably realized.

We are in fact using [Node.js](https://nodejs.org/en/) to power part of [WordPress.com](https://wordpress.com/) now. If you go to <https://wordpress.com> while logged in, your request is handled by a Node.js server, and the entire UI is written in JavaScript, although the majority of it is actually [React.js](https://facebook.github.io/react/). Unless you end up back in wp-admin, your admin/editing/posting/dashboard experience on WordPress.com is now handled entirely (well, almost; we’re still working on some pieces still) with JavaScript.

The UI is fully responsive (optimized for multiple screensizes, and flexible in between). Data updates are live (combination of polling and websockets, moving more to sockets over time). No full-page refreshes (it’s a single-page app). All API-driven (which means we can, and are, using the same APIs to power portions of the [native mobile apps](https://apps.wordpress.org/)). Speaking of apps, we’re able to bundle our single-page, JavaScript application as a native app, [so we did](https://desktop.wordpress.com/) (OSX for now, Linux and Windows coming very soon). Leveraging our infrastructure, and the power of [Jetpack](https://jetpack.me), we can provide self-hosted users with the same experience as those we host directly (with more Jetpack-specific functionality coming soon as well).

This is a lot of change. But it goes deeper than just the entire technology stack we’re working on now. This was a complete culture-shift for Automattic, a now-400-person company traditionally made up of approximately 100% PHP developers. To get here, we at [Automattic](https://automattic.com) took a step back and asked ourselves;

> What would WordPress.com look like if we were to start building it today?

As part of answering that question, we made a lot of changes internally:

* Cross-trained all of our PHP developers (and some of our mobile developers!) into modern, performant JavaScript developers.
* Switched to a completely [GitHub](https://github.com)-based workflow.
* Every commit is now peer-reviewed.
* Shifted to a very component-minded architecture.
* Moved our WordPress codebase to be entirely API-driven. New features are now only launched as a new/modified API endpoint + data layer + UI layer.
* Change in thinking from being very “plugin-oriented” (similar to WP-core) to a much more integrated and cohesive way of thinking of things across the web and mobile apps.

So today, in keeping with the DNA of Automattic, which shares the DNA of WordPress, we’re [releasing what we’ve been working on as open source](https://github.com/Automattic/wp-calypso). It’s code-named “Calypso” (long story), and we’re extremely proud of what we’ve built over the last ~18 months. I truly hope that this can help guide or influence [WordPress.org](https://wordpress.org)‘s future.

I wrote this post in the Calypso/WordPress.com Desktop app, and published it via Jetpack. That feels pretty darned good.