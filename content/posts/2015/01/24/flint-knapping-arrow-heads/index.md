---
title: Flint-Knapping Arrow Heads
date: '2015-01-24T16:37:23+00:00'
tags:
- arrowhead
- flint knapping
- primitive skills
- stone tools
- survival
- wilderness
categories:
- personal
- posts
---

![IMG_0557](http://dentedreality.com.au/wp-content/uploads/2015/01/IMG_0557.jpg)

*Image shows leather hand-pad, copper-tipped pressure flaker, small stone (Jasper?) arrow head and larger glass/beer bottle arrow head (both made by me, today).*

A few weeks ago I decided to have a look on [Meetup.com](http://meetup.com) and see if there were some meetups that looked interesting enough to attend in the area. I spotted the [Wilderness Awareness and Survival Skills in Denver](http://www.meetup.com/Wilderness-Awareness-And-Survival-Skills-in-Denver/) group, and joined it immediately. I’ve been interested in this sort of thing for a while, and even attended a [week-long school with Tom Brown](http://dentedreality.com.au/2011/04/16/tom-brown-jrs-tracker-school/ "Tom Brown Jr’s Tracker School") a few years ago. The next meetup was going to be a basic [flint-knapping](https://en.wikipedia.org/wiki/Knapping) class, which is something I’ve wanted to try for a while. We talked about it at the Tom Brown Tracker School class, but like so many other things, didn’t have time to get any hands-on experience. I’ve also been watching a bit of [Ray Mears](https://en.wikipedia.org/wiki/Wild_Food) stuff lately, and he does some basic knapping in some of his episodes, so I had some recent motivation to check it out.

The meetup was held in the court-yard/shared space between 2 apartment blocks, one of which our guide lived in. Andrew is a really personable guy who apparently works for Denver Parks & Rec at the moment. He’s also studied and been practicing primitive skills for a while, and these meetups are his way of passing those skills along to others. He was really well-prepared, and provided us with everything we needed (except a chair) to get started, and to make some simple blades/arrow-heads.

We were mostly aiming for 3-notch arrow heads, since they give a notch to got in the end of an arrow shaft, and then 2 side-notches for binding the head to the shaft. They are a little more complex than some of the others I’ve seen (or the ones that Ray Mears was making), but they aren’t that hard once you get the hang of things, and I guess could even work without any natural glue, which is an advantage. They definitely require a fine, strong point on your pressure-flaker though, so you need something like a deer antler, or if you’re using some modern tools, then a copper-tipped flaker like we used works nicely.

For practice, we used the bottom of beer bottles, which flake pretty nicely, are cheap and easy to acquire, and are pretty consistent (so you don’t have to figure out crazy impurities or anything). To get the base off, we put a giant steel nail inside the bottom, then just shook it up and down a little until it popped out the base. Then you start flaking off the edges and go from there.

You’ll need:

* A strip of leather (which you use in your hand, to guard against sharp flakes, and the tip of your pressure flaker)
* A round/smoothish rock (or a few different ones), for percussion flaking and also for “platforming”
* A pressure flaker, which you can see in the picture above (that’s a thick piece of copper wire in the tip of a piece of Aspen (I think, the wood doesn’t matter that much, just make it soft enough to get the wire in there). Traditionally, you’d use a deer antler (which we also tried). They are amazingly strong, and already pointed.
* Stone/glass to knap.

There are 3 main things we were told to keep in mind:

1. Platform: this refers to setting up the edge that you’re working on. Basically, you use a rounded stone to abrade/grind off the edge so that you can remove all the small irregularities and provide something a bit more substantial for your pressure flaker to grip onto.
2. Centerline: which is just referring to the rough centerline of the mass of your piece, on a horizontal plane. You always want to be flaking *down* from this line (into your hand, “under” the piece you’re working on).
3. Acute: you’re looking for acute angles, below the centerline. That’s where you can get good flakes, and make progress. If the angle is obtuse, there’s nowhere for your flaker to grip, and you won’t be able to flake anything off.

I went back and found my notes from Tracker School about flint knapping, and was impressed to see that they lined up almost 1:1 with what I learned today. Getting a chance to try my hand at it really made a difference though, and I’d like to give it a bit more of a shot in the future. I’m particularly interested in super-simple, percussion-flaking, which is something that seems like it could be immediately useful in a survival situation (where you’re not going to have something like antler or copper wire handy for true pressure flaking).

A big shout out to Andrew for being a great teacher, and I really look forward to having some more classes and adventures with him and the others.

jQuery(document).ready(function(){
var gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595 = {
positions : {
403 : new google.maps.LatLng( '39.7456285', '-104.8951983' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.positions ) {
gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.bounds.extend( gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.positions[m] );
}
// Render markers
for ( var m in gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.positions ) {
gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.map,
position : gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.map.setCenter( gmap\_m3ed719b773e0e7bbfb9854c5a9d1c595.positions[403] );
});