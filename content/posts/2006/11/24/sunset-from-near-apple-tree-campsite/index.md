---
title: Sunset From Near ‘Apple Tree’ Campsite
date: '2006-11-24T15:10:16+00:00'
format: image
service: flickr
tags:
- bigsur
- bottchersgap
- california
- lospadresnationalpark
- sky
- sunset
- view
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308100337_6931681fee_o.jpg?resize=607%2C455
---

[![Sunset From Near 'Apple Tree' Campsite](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308100337_6931681fee_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/11/24/sunset-from-near-apple-tree-campsite/) 
# [Sunset From Near ‘Apple Tree’ Campsite](http://dentedreality.com.au/2006/11/24/sunset-from-near-apple-tree-campsite/)

Turns out that we accidentally didn’t sleep at the actual Apple Tree campsite, but we had this view, so it was well worth it.





* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308100337/) [3:10 pm, November 24, 2006](http://dentedreality.com.au/2006/11/24/sunset-from-near-apple-tree-campsite/ "3:10 pm") 
jQuery(document).ready(function(){
var gmap\_m5ad7e7c6e16ca3e6005131b21957b231 = {
positions : {
270 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5ad7e7c6e16ca3e6005131b21957b231' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5ad7e7c6e16ca3e6005131b21957b231.positions ) {
gmap\_m5ad7e7c6e16ca3e6005131b21957b231.bounds.extend( gmap\_m5ad7e7c6e16ca3e6005131b21957b231.positions[m] );
}
// Render markers
for ( var m in gmap\_m5ad7e7c6e16ca3e6005131b21957b231.positions ) {
gmap\_m5ad7e7c6e16ca3e6005131b21957b231.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5ad7e7c6e16ca3e6005131b21957b231.map,
position : gmap\_m5ad7e7c6e16ca3e6005131b21957b231.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5ad7e7c6e16ca3e6005131b21957b231.map.setCenter( gmap\_m5ad7e7c6e16ca3e6005131b21957b231.positions[270] );
});