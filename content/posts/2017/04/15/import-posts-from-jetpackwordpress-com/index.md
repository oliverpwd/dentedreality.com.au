---
title: Import posts from Jetpack/WordPress.com
date: '2017-04-15T17:07:47+00:00'
format: link
service: jetpack
tags:
- jetpack
- keyring
- keyring social importers
- wordpress
categories:
- personal
- posts
external_url: https://beau.blog/2017/04/import-posts-from-jetpackwordpress-com/
---

I’ve just released version 1.8 of both [Keyring](https://wordpress.org/plugins/keyring/), and the [Keyring Social Importers](https://wordpress.org/plugins/keyring-social-importers/). This version includes a new service file, and an accompanying importer, which allows you to import content from a Jetpack-powered WordPress site, using the [WordPress.com REST API](https://developer.wordpress.com/docs/). That means any site hosted on WordPress.com, or any self-hosted site with the [Jetpack](https://jetpack.com/) plugin installed. There are also a few key fixes for the Twitter and LinkedIn services/importers, so it’s a nice update.

The new importer will pull across the entire content of posts, including tags. Similar to the Instapaper importer, it attempts to avoid duplicate content issues by marking pages as `noindex` if they come from imported content.

This is another piece of the puzzle required for me to create a complete archive of my digital footprints over on [Dented Reality](http://dentedreality.com.au/), now that I’m blogging here. This post should be imported over there automatically within an hour.

Note that currently the importer doesn’t sideload any media items (will add that soon) or support geo data (again, I’ll add that when I get a chance).

Check it out, and please use responsibly!

![Screen Shot 2017-04-15 at 5.03.43 PM](https://i0.wp.com/beau.blog/wp-content/uploads/2017/04/Screen-Shot-2017-04-15-at-5.03.43-PM.png?resize=791%2C105&ssl=1)![Screen Shot 2017-04-15 at 5.03.43 PM](https://i0.wp.com/beau.blog/wp-content/uploads/2017/04/Screen-Shot-2017-04-15-at-5.03.43-PM.png?resize=791%2C105&ssl=1)

![Screen Shot 2017-04-15 at 5.05.32 PM](https://i1.wp.com/beau.blog/wp-content/uploads/2017/04/Screen-Shot-2017-04-15-at-5.05.32-PM.png?resize=959%2C701&ssl=1)![Screen Shot 2017-04-15 at 5.05.32 PM](https://i1.wp.com/beau.blog/wp-content/uploads/2017/04/Screen-Shot-2017-04-15-at-5.05.32-PM.png?resize=959%2C701&ssl=1)