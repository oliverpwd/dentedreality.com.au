---
title: Keyring 2.0 and Keyring Social Importers 2.0
date: '2019-06-16T19:26:56-06:00'
service: jetpack
tags:
- composer
- foursquare
- github
- gmail
- google
- google analytics
- indieweb
- keyring
- keyring social importers
- open source
- packagist
- strava
- swarm
- twitter
- wordpress
- youtube
categories:
- posts
---

Yesterday I released new versions of both [Keyring](https://wordpress.org/plugins/keyring/) and the [Keyring Social Importers](https://wordpress.org/plugins/keyring-social-importers/) packages, containing a bunch of updates and new additions. If you’re already using them, you should have update notices in wp-admin. If you’re not yet, then download them at the links above, or search for “keyring” in wp-admin under Plugins > Add New.

What’s changed? It’s [been a while](https://beau.blog/2018/02/keyring-v1-9/) since the last official release of Keyring, so there’s a bunch to catch up on:

* All Google services have been modified to use a shared base service (cuts down on code duplication significantly).
  + Added a GMail Service (props [@poisa](https://github.com/poisa)).
  + Added a YouTube Service (based heavily on [@superbia](https://github.com/superbia)‘s work with Google Analytics).
* Added a [Pocket](https://getpocket.com/) Service (props [@roccotripaldi](https://github.com/roccotripaldi)).
* Keyring is now available for use with [Composer](https://getcomposer.org/), via [Packagist](https://packagist.org/packages/beaulebens/keyring).
* Lots of bugfixes, including token refreshing should now work properly.

The Social Importers haven’t seen an official release since 2017, so there’s a ton going on there as well:

* Added a [Strava](https://www.strava.com/) importer (props [@mdrovdhal](https://github.com/mdrovdahl)) and introduced a bunch of improvements via iteration (props [@marekhrabe](https://github.com/marekhrabe)). Having another service with map-based data makes me want to add some core to make it easier to map things visually.
* Introduced a global option (for all importers) that allows you to set posts to published, draft, private, or pending when importing them. A lot of people were asking for/hacking this in, so I figured I’d just add it to the core package. Being able to import as draft and then selectively publish, or import an entire service to “private” posts is a nice addition.
* Lots of improvements and bugfixes to both Twitter (some props [@chrishardie](https://github.com/ChrisHardie)) and Swarm/Foursquare.
* Added a Pocket importer, again props @roccotripaldi. It works similarly to the Instapaper one, so if you’re using Pocket instead, check it out.

If you’d like to keep an eye on things more closely, or even contribute, check out [Keyring](https://github.com/beaulebens/keyring), and the [Keyring Social Importers](https://github.com/beaulebens/keyring-social-importers) on GitHub. It’s been really awesome to see some more contributions to both packages coming in, so I’d love to see more of that.

**Download** [**Keyring**](https://wordpress.org/plugins/keyring/) **and the** [**Keyring Social Importers**](https://wordpress.org/plugins/keyring-social-importers/) **plugins for WordPress.**