---
title: Epic Australian Adventure, 2014
date: '2014-03-25T09:49:12+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928312054_07566921e3_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928312054_07566921e3_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-34/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-34/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928312054/) [9:49 am, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-34/ "9:49 am") 
jQuery(document).ready(function(){
var gmap\_m85b66abf2932ba7c17639ebf930a3272 = {
positions : {
202 : new google.maps.LatLng( '-37.823628', '144.952025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m85b66abf2932ba7c17639ebf930a3272' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m85b66abf2932ba7c17639ebf930a3272.positions ) {
gmap\_m85b66abf2932ba7c17639ebf930a3272.bounds.extend( gmap\_m85b66abf2932ba7c17639ebf930a3272.positions[m] );
}
// Render markers
for ( var m in gmap\_m85b66abf2932ba7c17639ebf930a3272.positions ) {
gmap\_m85b66abf2932ba7c17639ebf930a3272.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m85b66abf2932ba7c17639ebf930a3272.map,
position : gmap\_m85b66abf2932ba7c17639ebf930a3272.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m85b66abf2932ba7c17639ebf930a3272.map.setCenter( gmap\_m85b66abf2932ba7c17639ebf930a3272.positions[202] );
});