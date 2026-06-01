---
title: 4th of July, 2013
date: '2013-07-04T17:57:07+00:00'
format: image
service: flickr
tags:
- '20130704'
- 4thofjuly
- fireworks
- sparklers
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437058269_472dc1be1b_o.jpg?resize=607%2C452
---

[![4th of July, 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437058269_472dc1be1b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-3/) 
# [4th of July, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-3/)





* #[20130704](http://dentedreality.com.au/tags/20130704/)
* #[4thofjuly](http://dentedreality.com.au/tags/4thofjuly/)
* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[sparklers](http://dentedreality.com.au/tags/sparklers/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437058269/) [5:57 pm, July 4, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-3/ "5:57 pm") 
jQuery(document).ready(function(){
var gmap\_m12bb9110e9890251d6773bc4106cc889 = {
positions : {
623 : new google.maps.LatLng( '40.716666', '-73.946' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m12bb9110e9890251d6773bc4106cc889' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m12bb9110e9890251d6773bc4106cc889.positions ) {
gmap\_m12bb9110e9890251d6773bc4106cc889.bounds.extend( gmap\_m12bb9110e9890251d6773bc4106cc889.positions[m] );
}
// Render markers
for ( var m in gmap\_m12bb9110e9890251d6773bc4106cc889.positions ) {
gmap\_m12bb9110e9890251d6773bc4106cc889.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m12bb9110e9890251d6773bc4106cc889.map,
position : gmap\_m12bb9110e9890251d6773bc4106cc889.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m12bb9110e9890251d6773bc4106cc889.map.setCenter( gmap\_m12bb9110e9890251d6773bc4106cc889.positions[623] );
});