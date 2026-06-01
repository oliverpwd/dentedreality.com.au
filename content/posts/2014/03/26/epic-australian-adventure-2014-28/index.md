---
title: Epic Australian Adventure, 2014
date: '2014-03-26T17:56:06+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927922583_74ccfeb716_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927922583_74ccfeb716_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/26/epic-australian-adventure-2014-28/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/26/epic-australian-adventure-2014-28/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927922583/) [5:56 pm, March 26, 2014](http://dentedreality.com.au/2014/03/26/epic-australian-adventure-2014-28/ "5:56 pm") 
jQuery(document).ready(function(){
var gmap\_m52db8309b627af39405b2dd8c3d2f623 = {
positions : {
469 : new google.maps.LatLng( '-37.819856', '144.964936' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m52db8309b627af39405b2dd8c3d2f623' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m52db8309b627af39405b2dd8c3d2f623.positions ) {
gmap\_m52db8309b627af39405b2dd8c3d2f623.bounds.extend( gmap\_m52db8309b627af39405b2dd8c3d2f623.positions[m] );
}
// Render markers
for ( var m in gmap\_m52db8309b627af39405b2dd8c3d2f623.positions ) {
gmap\_m52db8309b627af39405b2dd8c3d2f623.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m52db8309b627af39405b2dd8c3d2f623.map,
position : gmap\_m52db8309b627af39405b2dd8c3d2f623.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m52db8309b627af39405b2dd8c3d2f623.map.setCenter( gmap\_m52db8309b627af39405b2dd8c3d2f623.positions[469] );
});