---
title: Keyring v1.5 & Social Importers v1.4
date: '2013-09-15T21:24:26+00:00'
tags:
- foursquare
- importer
- keyring
- keyring social importers
- movesapp
- plugin
- twitter
- wordpress
categories:
- posts
---

Yesterday, I released [version 1.5](http://downloads.wordpress.org/plugin/keyring.1.5.zip) of [Keyring](http://wordpress.org/plugins/keyring/), and [version 1.4](http://downloads.wordpress.org/plugin/keyring-social-importers.1.4.zip) of the [Keyring Social Importers](http://wordpress.org/plugins/keyring-social-importers/) bundle for WordPress. This update moves the Social Importers away from using a postmeta value (keyring\_service) and introduces a new taxonomy that keeps track of where posts were imported from. It’s optimized towards management within wp-admin, but you can also use it for front-end queries of your posts. The update for Keyring introduces a new service file for [Moves](http://moves-app.com), and fixes a bug in the OAuth2 base service.

The new taxonomy for the Importers is called keyring\_services on the backend, and is labeled “Imported From” in the admin UI. It will auto-create itself based on all of the importers installed. You’ll see it within wp-admin under the Posts menu, and will be listed on the “All Posts” listing as well:

![Screen Shot 2013-09-15 at 9.10.59 PM](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/Screen-Shot-2013-09-15-at-9.10.59-PM.png?resize=155%2C191)

Clicking the name of a service under the “Imported From” heading will filter the posts list by that service (e.g. Twitter). The main reason that the taxonomy is exposed through the admin UI is so that you can tweak the slugs if you’d like to. I noticed that on my install, I’d already used things like ‘twitter’ and ‘foursquare’ as tags, and so they had claimed the namespace for that slug. WordPress’ shared terms are annoying like that ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607) . So, if you’d like to use the slugs of source services in URLs, you might want to rename them:

1. Go to Posts → Tags
2. Search for and rename the slug for each of the services (e.g ‘twitter’, ‘foursquare’, ‘flickr’). Name the slugs something like ‘twitter-3′
3. Go to Posts → Imported From and rename the slugs for each service to the “clean” version (without a ‘-2′).
4. Optionally go back to Posts → Tags and rename those tags again back to the -2 versions.

As part of this change, you’ll want to update any previous posts that you imported to using the new taxonomy. I’ve included a quick and dirty script to do this. It’s called migrate-keyring-postmeta-to-taxonomy.php and can be found in the root of the plugin. To use it, you need to move it to the root of your WordPress install, and then you can just access it through your browser. It’s likely that it’ll run out of memory or time out, but it’s written in a way that you can just run it over and over again until it finishes cleanly. On my server, once it was finished and produced no output, Chrome decided to display a “friendly” error message instead of anything useful. Once that’s done, your existing posts should all be converted over to using the new taxonomy, and there should be no more postmeta entries for keyring\_service.

If you’re doing a clean import, I recommend doing it **without** auto-import enabled, and then once you’ve fully imported everything, enable auto-import and let it run from there.