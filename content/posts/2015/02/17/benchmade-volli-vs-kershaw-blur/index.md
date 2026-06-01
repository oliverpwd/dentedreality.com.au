---
title: Benchmade Volli vs Kershaw Blur
date: '2015-02-17T11:03:12+00:00'
tags:
- benchmade
- blur
- edc
- folder
- kershaw
- knife
- volli
categories:
- personal
- posts
- reviews
---

![IMG_0746](http://dentedreality.com.au/wp-content/uploads/2015/02/IMG_0746.jpg)

*Benchmade Volli on top, Kershaw Blur on bottom.*

I just got my hands on a [Benchmade](http://www.benchmade.com) [Volli](http://www.benchmade.com/products/1000001), and thought I’d do a quick comparison to the EDC knife that it’s replacing, the [Kershaw](http://kershaw.kaiusaltd.com) [Blur](http://kershaw.kaiusaltd.com/knives/knife/black-blur) (black non-serrated blade). Here are my observations so far:

* The Volli is clipped so that it sits tip-up in the pocket. The Blur is tip-down, so that’s taking some getting used to.
* The handle on the Volli is noticeably thicker/fatter than the handle on the Blur. Since the clip also has a higher profile, the entire package is quite a bit bulkier in a pocket
* The AXIS lock on the Volli is really nice, and the locking mechanism along the spine is a nice touch — you can double-lock the blade open for heavier work.
* The Blur has a faster spring-assist, and a more satisfying “clunk” when coming open. I think the sound/clunk comes partially from the aluminum frame (vs the Volli’s “G10″ handle, which is some kind of plastic/fiber stuff).
* The Volli has zero blade-play, which the Blur has a bit.
* The thumb-stud on the Blur is “one-sided”, and has a bit sharper of an edge on it, which can be good or bad.
* Because of the slightly wider handle (and thus wider arc to get around it), I find the Volli harder to close one-handed.
* The straight edge on the Volli’s blade is a big plus for me. The slightly curving blade on the Blur really annoyed me when sharpening it.
* Handle length is (almost?) identical. Blade is a little longer on the Blur.
* The Blur is a little heavier .
* I really like the blade grind on the Volli.
* The Volli’s blade is a little thinner than the Blur, and is also ground down along the spine to make it appear even thinner still.
* Since the handle on the Volli is plastic, I guess I won’t be able to use it as reliably as a bottle opener (note the scratched out surface on the Blur, where the blade meets the handle ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607) ).

Overall, I’m happy with the Volli, and will definitely keep is as my EDC (at least for now). I do think that if you could take the Volli blade and put it on something resembling the Blur handle, but keep the AXIS lock, you might really have a winner.

jQuery(document).ready(function(){
var gmap\_m7fcecca58b6f68930085731d5e9a816b = {
positions : {
589 : new google.maps.LatLng( '39.7392358', '-104.990251' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7fcecca58b6f68930085731d5e9a816b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7fcecca58b6f68930085731d5e9a816b.positions ) {
gmap\_m7fcecca58b6f68930085731d5e9a816b.bounds.extend( gmap\_m7fcecca58b6f68930085731d5e9a816b.positions[m] );
}
// Render markers
for ( var m in gmap\_m7fcecca58b6f68930085731d5e9a816b.positions ) {
gmap\_m7fcecca58b6f68930085731d5e9a816b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7fcecca58b6f68930085731d5e9a816b.map,
position : gmap\_m7fcecca58b6f68930085731d5e9a816b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7fcecca58b6f68930085731d5e9a816b.map.setCenter( gmap\_m7fcecca58b6f68930085731d5e9a816b.positions[589] );
});