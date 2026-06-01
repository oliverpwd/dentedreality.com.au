---
title: A Whole New Dented Reality
date: '2013-09-15T22:03:03+00:00'
tags:
- dented reality
- homeroom
- theme
- wordpress
categories:
- posts
- projects
- site-news
- tech
---

Back in April, this blog celebrated [10 years of existence](http://dentedreality.com.au/2013/04/09/10-year-blogoversary/ "10 Year Blogoversary!"), and it’s been almost *five years* since the theme on this site changed. Yesterday I decided to just go ahead and flip the switch on something I’ve been working on here and there since late last year. It’s a complete new, very experimental theme that I call “**Homeroom**“.

There are some specific things driving what I was aiming for with Homeroom:

1. First and foremost, a lot of the decisions are based around the intention that it would use [Keyring](http://wordpress.org/plugins/keyring/) and the [Social Importers](http://wordpress.org/plugins/keyring-social-importers/) to pull in my content from all over the web. With that much data being collected and displayed here, I realized I couldn’t go exactly with a traditional blog layout, and had to get a bit creative with some types of data.
2. It’s intentionally heavily integrated with [Jetpack](http://jetpack.me/) (although it works without it). Jetpack powers the comments, infinite scroll, sharing buttons and more. I’ve taken care to try to make that integration feel as native as possible (although I know there’s more to be done there).
3. Homeroom started out as an [\_s-based theme](http://underscores.me/), although it’s been pretty radically modified from there.
4. I’m using a technique that I’ll call “post lookahead” when going through the loop to check the next post, and do some things like collapse sequential posts if they’re the sam type of thing.
5. I wanted something with a bit of a timeline feel, since it’s now collecting some much data, and it’s all sequential; I wanted to show the relationship of different things along that sequence of time.

It’s not particularly beautiful because, well, I’m not a designer ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607) In the near future I’ll be talking to some friends who are though, so hopefully I can get some advice on improving things there. I’ve been mainly focused on getting it working the way that I wanted it to. Here are some other bits that might be interesting:

* Allows custom Header and Backgrounds via wp-admin
* Options (currently defined in a file, because I haven’t built a UI) to control some preferences around stuff like hiding Foursquare check-ins until a set amount of time after they happened (to help avoid the creepers!).
* Heavy use of Post Formats
* Ability to hide Twitter replies, which you probably don’t want showing up on your site.
* There’s the beginnings of a front-end post box (partially inspired by [o2](http://geto2.com)), although it doesn’t actually work yet
* Handles Foursquare checkins differently. Rather than showing them all as individual posts, it “collects” them and shows a single, multi-point map at the end of each day.
* Shows a map automatically on any post using the [WordPress-recommended postmeta](http://codex.wordpress.org/Geodata) fields.
* Using the [new taxonomy](http://dentedreality.com.au/2013/09/15/keyring-v1-5-social-importers-v1-4/) introduced in Keyring Social Importers 1.4, allows you to easily filter your display based on where posts were imported from.
* Includes a custom icon font from [IcoMoon](http://icomoon.io/app) to display social icons indicating where things were imported from.
* Search results use a [Masonry-based layout](http://masonry.desandro.com/) so that you can quickly scan the results. Unfortunately something is broken with the search mechanism on this site right now, so that’s not working ![:(](http://i1.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_sad.gif?w=607)
* Automatically lists out child-pages when you view a Page that has them, for example my [Projects page](http://dentedreality.com.au/projects/).
* Dynamic heading re-writes: format your posts for individual viewing, and the H1 etc tags are automatically “stepped down” on listing pages to maintain hierarchy
* Has some fun mapping stuff for TripIt in particular, which draws out a “flight path” between airports. Check it it out in [my TripIt section](http://dentedreality.com.au/service/tripit/). [Here’s a fun one](http://dentedreality.com.au/2013/01/22/flew-lasmialga/).
* Uses [Photon](http://developer.wordpress.com/docs/photon/) to apply some effects to images in places
* Borrows liberally from the styling of sites like [Instapaper](http://www.instapaper.com/) and [Readability](http://www.readability.com/).

There’s still a *lot* of work to go, both on the theme itself and the importers that power a lot of the content. I wanted to get this online because I knew that’d motivate me to spend more time on it. I’m also hoping that other folks might be interested and/or have some ideas on ways to improve the theme. I haven’t got all of my content imported yet (that takes a while ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607) ), but you’ll see more and more things fill in over the coming week hopefully.

If you’ve got any ideas for improvements, I’d love to hear them down in the comments!