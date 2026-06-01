---
title: People & Places
date: '2016-12-31T20:28:41+00:00'
format: link
service: jetpack
tags:
- data
- geo
- keyring
- keyring social importers
- people
- places
- plugin
- taxonomies
- wordpress
categories:
- personal
- posts
external_url: https://beau.blog/2017/01/people-places/
---

Over the years, I’ve been working on a system to aggregate data that I publish to other social networks/sites back into my control, on my own WordPress install. Thus far, that has resulted in the creation of [Keyring](https://wordpress.org/plugins/keyring/) (plugin) to provide an abstracted interface to all of the web services I’m interested in, [Keyring Social Importers](https://wordpress.org/plugins/keyring-social-importers/) (plugin) to do the basics of importing the data from different places, and [Homeroom](https://github.com/beaulebens/homeroom) (theme) to display it all. Today, I’ve been working on a system that will detect people who are mentioned in an interaction, and link them across posts using a custom taxonomy. It does the same for physical locations, so I’ve called it [People & Places](https://github.com/beaulebens/people-places).

Essentially, this plugin is just a pair of custom taxonomies, with some specific ways of referring to things. Pretty basic. It gets more interesting though when you update Keyring Social Importers to the trunk version, which will now work in tandem with People & Places to link everything up. I wouldn’t recommend it on a production site just yet — there’s a lot of rough edges still.

When KSI is pulling in content from each service (currently looking at Twitter, Instagram and Foursquare), there’s a new block of code that makes sure People & Places is available, and then looks for certain pieces of data. If it finds them, it bundles up the details, and passes that along in the import process. When posts are actually inserted, it will attempt to link up that post to the People/Places it found. If the People already exist, then they’ll just be linked, in the same way tags work. If they don’t exist yet, then a new Person entry will be created, and that will be used.

I plan to add in a basic term-merging function, so that you can manually (maybe automatically?) identify “duplicate people” across different networks, and intelligently merge their entires (re-linking any posts involved), so that you build up a single, combined view of your interactions with a particular person. I envisage some interesting possibilities with the archive pages for these taxonomies, and that over time it will build a really interesting dataset of your interactions, the places you physically go, etc.

I’ll probably still move the code around a bit, and there are definitely some bugs around duplicates and handling things across different networks, but it seems to be working so far. This is also probably the time to figure out a decent way to allow re-processing of imported data from the raw copy that the importers save in postmeta. Installing this new code will start gathering data on *new* imported entries, but won’t go back and do the same on all the posts you’ve already got. Rather than deleting all that data and re-importing/processing everything, I’d like to have a simple way to re-process the raw data that’s already stored locally.