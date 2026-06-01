---
title: 'The Future of WordPress: REST API + Javascript single-page app?'
date: '2013-12-03T14:11:02+00:00'
tags:
- api
- backbone
- future
- javascript
- jquery
- rest
- web apps
- wordpress
categories:
- posts
---

*DISCLAIMER: Personal thoughts only, based on what I’m seeing around the web over the last few years.*

Working on [o2](http://geto2.com) for the last few months, and spending more and more time in amongst the Javascript community at events like [jQueryConf](http://events.jquery.org/2013/portland/), [BackboneConf](http://backboneconf.com/2013/) and [dotJS](http://www.dotjs.eu/), I’ve started thinking about the future of [WordPress](http://wordpress.org/) differently.

WordPress currently consists of a large, complex, PHP codebase, sitting on top of a MySQL backend. plugins are primarily PHP, with a light sprinkling on Javascript to mostly provide UI “candy”. Part of the reason for that is probably because:

1. It’s pretty hard to interact with WordPress on any real depth using Javascript, and;
2. If you’re trying to provide any custom functionality for WordPress, you pretty quickly end up doing it in PHP because that’s where all of the internal APIs and functionality resides.

That’s been a fine approach for the last 10 years, but I believe that [things are changing](http://readwrite.com/2013/08/09/why-javascript-will-become-the-dominant-programming-language-of-the-enterprise#awesm=~ooYUQVoMtjAJ9g), and we need to change with them to remain relevant. Full page reloads with heavy server-based everything is no longer really acceptable for a solid UX. With that in mind, here’s a possible future for WordPress, extrapolated out from where some things seem to be going (on the wider web, not necessarily currently within WordPress development):

WordPress core becomes 2 “separate” portions; one is a PHP-based REST-style API. Effectively, a layer that provides a structured API onto our database. That would cover all posts, users, settings, queries, meta data etc that lives within the WP DB. The other piece would be (ideally) a pure Javascript, single-page web application which fully implements the API to deliver what we currently know as wp-admin.

Plugins would create additional endpoints within the backend API, or would supplement existing ones (e.g. post/meta) with additional data and/or actions. They could also be implemented via pure JS, depending on what they were built to do. Themes could potentially be built using no PHP at all — making queries directly to the API via JS, and then using something like [Mustache](http://mustache.github.io/) to template the output back to the user. This would have SEO ramifications, but we can always figure something out there, and search engines are constantly improving.

To get there would take a long time, and at many points it would no doubt break all sorts of plugins. This would be a huge shift and I think would actually be really hard to accomplish within the community, which makes me scared because I think it will be rejected as a direction (or at least slowed down a LOT) because of backwards compatibility at the very least. Perhaps we can maintain backwards compatibility for some plugins by at least making the new wp-admin a hybrid app, which leverages a JS-based approach for all truly core functionality/views, and then falls back to full page reloads for plugin-based admin functionality. Without a lot of work, that approach would still break for “integrated” plugins (where they inject settings  into or manipulate existing admin pages), if we assume that all of those pages would become powered by/created via Javascript + API interactions.

Unfortunately a crucial point where backwards compatibility would be important would be the Post Editor, which is also where some big performance/UX improvements could potentially be seen by switching to a largely JS-powered UI.

I don’t know if this is really where WordPress will go, or if it is, exactly how it will get there. There’s a project currently to build a [core REST API](https://wpapiteam.wordpress.com/) which I’m eagerly observing and will be trying to get more involved in. It has the potential to become the kernel of the future of WordPress if it’s done right. This is going to be a long road either way, so I’m excited for where we can all go from here.

Do you think WordPress can (or should) move in this direction?