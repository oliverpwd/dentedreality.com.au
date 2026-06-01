---
title: Simple Search Operators
date: '2014-10-16T11:22:36+00:00'
tags:
- plugin
- search
- simple search operators
- wordpress
categories:
- posts
- tech
---

I’ve long wanted to be able to do some simple, operated-powered searches within WordPress (especially relevant in [a project I’m working on](http://geto2.com) at [Automattic](http://automattic.com)). After a conversation with [Allen](http://allendav.com/), where he wanted to do the same thing, I figured I’d just whip up a quick plugin to see how hard it’d be. Turns out the answer is “not very”.

**[Simple Search Operators](https://github.com/beaulebens/simple-search-operators)** is a quick plugin that expands the functionality of the default search system in WordPress so that you can use a few useful operators (might look at adding some more at some point) [all links in the following list go to live searches on this site, using that operator]:

* [`author:beau`](http://dentedreality.com.au/?s=author%3Abeau) will limit results to posts written by the author with the username/slug ‘beau’
* [`tag:burrito`](http://dentedreality.com.au/?s=tag%3Aburrito) will only return posts which are tagged with ‘burrito’
* [`category:posts`](http://dentedreality.com.au/?s=category%3Aposts) (or `cat:posts`) to search for posts categorized as ‘posts’
* [`tag:burritofriday cancun author:beau`](http://dentedreality.com.au/?s=tag%3Aburritofriday+cancun+author%3Abeau) to search for posts containing ‘cancun’, written by ‘beau’, tagged as ‘burritofriday’

Some caveats:

* Not heavily tested! May well be capable of generating server-melting queries
* Only supports one of each operator for now
* Operators and freeform searches may be combined (e.g.: “tag:burrito cancun”)
* Does not support spaced strings for operators, so you can only do things where a no-space string attached to an operator will get you what you want
* Because of the way it manipulates query variables, might mess with other plugins or themes in adverse ways. Like I said, not heavily tested.
* Not available via the WP Plugin Repo yet; will get it up there once it’s baked a little bit

If you’d like to give it a shot, please do. If you’d like to add more operators; shoot me a pull request and we can expand this out a bit.