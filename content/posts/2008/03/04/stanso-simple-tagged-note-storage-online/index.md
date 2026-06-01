---
title: 'Stanso: Simple TAgged Note Storage Online'
date: '2008-03-04'
categories:
- projects
- tech
---

## Background/Motivation

In amongst some work that I’ve been doing recently, and looking at my own work habits and trends, I realized that something super-useful to have would be a very accessible “microcontent storage system” where you would be able to store small snippets of information, tag them, have them fully-indexed and searchable using a simple, slick interface. Basically, I’m seeing this as [del.icio.us](http://del.icio.us), with more space for storing text, and no requirement for a link.

## General Idea

So I see this as a series of “items”, stored with a note/body item of some sort, which would normally be text. In addition to that, you’d have an optional title and link/URL. You’d have a list of tags/keywords, and perhaps allow for arbitrary meta-data. I like the idea of the meta-data because it makes the system simple, yes extensible in ways that simple tags don’t provide (easily).

The UI would probably be largely based around search (a la [Google](http://www.google.com)), and would provide a list of items recently added as the default result-set. When searching, we’d probably use AJAX to make it “live search” to aid progressive discovery. I’d like to be able to save a search as well, and have that available as a navigation item of some sort (e.g. All items tagged “work” and “urgent” but note “done”). Adding an item should be a matter of clicking a link, then typing a few items and hitting a button. You’d also want a [bookmarklet](http://www.dentedreality.com.au/notes/2005/12/12/google-maps-bookmarklet/) to be available so you could do this from anywhere. Perhaps even a Firefox plugin a la the del.icio.us one.

I’d also want RSS feeds available, specifically “recent items added” and “all items tagged x”.

Privacy controls, the ability to share items (or tags) and some other things like that would come down the line. I’d specifically like to be able to invite people to access my stream, and grant them the ability to see only items tagged with certain tags.

From here, we would also want a robust API so that we could plug the system in as the storage/backend behind any number of other apps. I see the use of POST to create new items, GET being able to retrieve a simple XML description of an item, PUT updating existing ones, and DELETE removing one. Standard REST stuff. The interesting thing here is that there’s no real reason why you couldn’t do it all with namespaced RSS (2.0) or Atom. I think that’d be a good approach because the basic structure is there, you just need to add some meta-data options which is no real problem.

The API is where the real fun lies – this could be the [Twitter](http://www.twitter.com) of… everything else. I see it as a generalized micro-content publishing system. Two immediate things that I think would be fun to plug on top of it (perhaps as paid services?) would be an email reader and an RSS reader. Basically these 2 systems would periodically check email/RSS feeds, then parse new items, tag them (using existing tags or some style of content analysis) and then POST the new item to your Stanso stream. It’d be interesting to see your email, notes, RSS feeds and potentially other things all mixed in together, tagged using a common scheme etc. Who knows where it could go? This could be a todo list, an email client, a news reader, a blogging platform, a status system, a bookmark repository, a password storage tool, a file manager, or all sorts of other things.

## Technology Options

Obviously this could be built very simply using something like [Scuttle](http://sourceforge.net/projects/scuttle/) (del.icio.us clone), or just from scratch using the normal LAMP stack (or RoR, or whatever). Another option I’ve been pondering is [Amazon Web Services](http://aws.amazon.com/). Of particular interest are [SimpleDB](http://aws.amazon.com/simpledb) (still in beta, waiting on the list…) and potentially [S3](http://aws.amazon.com/s3).

SimpleDB allows you to store a very loosely-structured set of data around a “record” in a fast-lookup, easily-queryable environment. Seems perfect for the task. It could handle arbitrary meta-data per item if you wanted, and could handle unlimited tags per item easily as well. I think S3 could be an interesting addition if you added the ability to upload a file (with tags etc), which was sidelined into S3, then automatically linked (via the URL field in an item) into your Stanso stream.

Another possibility would be to use something like [WordPress](http://www.wordpress.org) to build this, since it actually handles a lot of elements of the system already (post title, body, tags, meta-data, the general blogging/posting flow). Having worked with WordPress a lot in the last 6 months though, I’d have to think that it was overkill for this, and provides a lot of other (wasted) functionality that provides more overhead than is worth adopting. Probably taking something like Scuttle and modifying it would be a best bet for a prototype at least. If building on AWS then you’d have to get pretty custom.

## Possible Implementations/Features

* Simple note storage — you post small notes and snippets to remind you of things, or to hang on to passwords etc so you can find them later.
* Feed reader — feeds come in, are tagged and added to your stream, you navigate by tag or by “recentness”.
* Email client — email is pulled in and automatically tagged based on content analysis, sender details, etc. Being able to add your own tags would be **awesome.**
* Todo list — post items that you need to do, tagging them as “not done” perhaps. When they are done, you remove that tag (or just delete the item).
* Micro-blogging — post small updates on what you’re doing, what you’re thinking etc, then publish it out from the system via the “recent” RSS feed
* Bookmark storage — as per del.icio.us, minus all the social stuff.
* File manager — with file uploads going to S3, and meta stored in Stanso, you could store things in any “structure” (via tags) you wanted.

The cool thing is that you could actually do a number of these (if not all) at once, since you would have the ability to segment out your storage/retrieval of items based on tags as well.

Of course, after I started writing all of this, I realized it was just a slimmed down version of [HTFS](http://dentedreality.com.au/htfs/)… so yes, I really should be building that system ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=584)