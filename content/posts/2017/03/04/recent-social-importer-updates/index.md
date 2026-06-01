---
title: Recent Social Importer Updates
date: '2017-03-04T13:43:58+00:00'
format: link
service: jetpack
tags:
- instagram
- keyring
- keyring social importers
- nest
- nest camera
- people
- places
- rest api
- tripit
- twitter
- wordpress
categories:
- personal
- posts
external_url: https://beau.blog/2017/03/recent-social-importer-updates/
image: http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.11.22-PM.png
---

I’ve been trying to make small improvements to the [Keyring Social Importers](https://wordpress.org/plugins/keyring-social-importers/) package (and People & Places) that I maintain, and have made a number of them over the last few weeks. Here are some details of recent updates which you may have missed:

[**People & Places**](https://github.com/beaulebens/people-places/commits/master)

* Improved the labels being used for each taxonomy, so that you don’t get random mentions of “tags” in the WordPress UI.
* Improved the `add_place_to_post()` method so that you can add multiple Places to a single Post.
* Now exposing both the `people` and `places` taxonomies [via the REST API](http://dentedreality.com.au/wp-json/wp/v2/posts/47837?_embed).

[**Keyring Social Importers**](https://github.com/beaulebens/keyring-social-importers/commits/master)

* [Added a filter](https://github.com/beaulebens/keyring-social-importers/commit/368822387735dc2b6971de73d07a9e498ff9a918) so that you can easily (and globally) disable downloading of full content for Instapaper articles.
* Made it easy to [inject custom CSS](https://github.com/beaulebens/keyring-social-importers/commit/92fd6a7b4d44f8935cd60820af76f16f3c86358f) for a specific importer.
* Added a [Nest Camera](https://nest.com/camera/meet-nest-cam/) service and [importer](https://github.com/beaulebens/keyring-social-importers/commit/81e30831ec1a9b90cb141abfa13e22eda0df1766). Including recent updates, it will download a snapshot from the specified camera(s) during the hour indicated, auto-tag it using the location of the camera, and also associate it with a Place if People & Places is co-installed.
* The Instagram importer [now handles video posts properly](https://github.com/beaulebens/keyring-social-importers/commit/465c6c83de6c3c4802a351694392b9150a74e219), and will download the full video and [embed it into your posts](http://dentedreality.com.au/2017/02/26/this-was-happening-a-few-days-ago-today-its-sunny-and-gorgeous-cowx/). Bundled a reprocessor to fix old posts, which would have previously been handled as image posts.
* Also made the Instagram importer link up People mentioned in captions (not just those who are properly tagged as being in a post).
* Fixed a bug in the Twitter importer which was mangling newlines. Added a reprocessor to fix it in old posts as well.
* Now exposing where a post was imported from in the REST API.
* Added Places support to the TripIt importer, which associates each post with Places for each airport flown through on that trip.

Keyring Social Importers has been [updated in the WordPress.org plugin directory](https://wordpress.org/plugins/keyring-social-importers/) (version 1.7, or [get it from Github](https://github.com/beaulebens/keyring-social-importers/releases/tag/v1.7)) and you can get the latest version of [People & Places from Github](https://github.com/beaulebens/people-places) (still not an “official” plugin yet).

You can see most of them in action on my site, [Dented Reality](http://dentedreality.com.au/), which uses them to aggregate most of my online social activity. The People & Places data is not directly exposed yet, but you can see it in the REST API output.

![Recent Social Importer Updates](http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.11.22-PM.png)![Recent Social Importer Updates](http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.11.22-PM.png)

Places support added to TripIt importer.


![Recent Social Importer Updates](http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.13.38-PM.png)![Recent Social Importer Updates](http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.13.38-PM.png)

Added a Nest Camera importer.


![Recent Social Importer Updates](http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.18.56-PM.png)![Recent Social Importer Updates](http://dentedreality.com.au/wp-content/uploads/2017/03/Screen-Shot-2017-03-04-at-1.18.56-PM.png)

Current list of data reprocessors.