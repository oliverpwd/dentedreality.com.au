---
title: Social Importer Upgrade
date: '2017-01-08T22:02:20+00:00'
format: link
service: jetpack
tags:
- keyring social importers
- people
- places
- plugin
- social
- wordpress
categories:
- personal
- posts
external_url: https://beau.blog/2017/01/social-importer-upgrade/
image: http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.50.45-PM.png
---

Today I pushed some updates to:

1. [People & Places](https://github.com/beaulebens/people-places)
2. [Keyring Social Importers](https://github.com/beaulebens/keyring-social-importers/)

These updates make it so that the Twitter, Foursquare and Instagram importers are now dynamically identifying and indexing People and Places, and marking them with a taxonomy within WordPress. I’ve also added a new system for “reprocessing” old posts which Keyring imported, so that you can go back and perform some function on those posts without having to import them again. You’ll find reprocessing tools under Tools > Import > Reprocess Keyring Data.

![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.50.45-PM.png)![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.50.45-PM.png)

Reprocessing works by using the locally-stored copy of import data that is saved during the initial import of everything. The system is fully hookable, so you can add other reprocessing routines in via plugin. The core file comes bundled with one that attempts to address an old JSON-data-escaping issue, and I’ve added extensions to the importers listed above which allow you to go back and reprocess your posts for People/Places.

If you’re going to use them, I suggest you run the first one first, then you can run the others in any order you like. Doing the first one first will just make sure that as much of your data as possible is processable.

![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.51.33-PM.png)![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.51.33-PM.png)

It’s worth mentioning that if you use these reprocessors, they can take a while (especially if you have a lot of data already), and that they will likely create a lot of new data (in the form of People and Place terms being created in their respective taxonomies). After running all of them over all of my data, I have almost 1,800 People and just over 3,000 Places in my database.

The other tool added in this upgrade is the ability to merge terms, which becomes important with all of this data.

![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.54.49-PM.png)![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-9.54.49-PM.png)

When the importers are dynamically adding People and Places, they only match based on known identifiers. This means that you’re likely to end up with duplicate entries, especially if you’re processing multiple services (e.g. Foursquare and Instagram). Using the merge tool, you can browse through your entries and select 2 or more, then use the Bulk Actions drop-down to select “Merge” and hit “Apply”. Terms will be merged together as intelligently as possible, which basically means that the shortest slug of the group will be kept, and the longest strings for any conflicting fields will be kept. You can of course edit the resulting composite term afterwards and tweak things as you see fit. If you’re looking for a shortcut to identify duplicate entries, try searching for “-2”, which will give you a list of duplicates, then you’ll need to search for something that will bring up each of the dupes, select, merge, repeat. It’s a little bit tedious, but you’ll only need to do it once for each duplicate, and all future imports should match against the composite entry.

Oh, and one last thing — I threw in a quick map on the details page for Places, which provides a nice quick, visual confirmation that it’s the correct location. For now it’s using a very basic [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Main_Page) example, but I might switch it out to [Leaflet](http://leafletjs.com/) at some point, which is pretty nice.

![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-10.00.16-PM.png)![Social Importer Upgrade](http://dentedreality.com.au/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-10.00.16-PM.png)