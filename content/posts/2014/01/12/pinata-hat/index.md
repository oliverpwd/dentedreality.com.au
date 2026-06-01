---
title: ''
date: '2014-01-12T00:26:10+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/f79ae5567b4911e3991c129765e30c64_8.jpg?resize=640%2C640
---

[![Piñata Hat.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/f79ae5567b4911e3991c129765e30c64_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/12/pinata-hat/) 

Piñata Hat.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jDpf9eimGE/) [12:26 am, January 12, 2014](http://dentedreality.com.au/2014/01/12/pinata-hat/ "12:26 am") 
jQuery(document).ready(function(){
var gmap\_ma43c62114da28c8611d6ccff068a0d7b = {
positions : {
799 : new google.maps.LatLng( '23.006943231', '-109.71449141' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma43c62114da28c8611d6ccff068a0d7b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma43c62114da28c8611d6ccff068a0d7b.positions ) {
gmap\_ma43c62114da28c8611d6ccff068a0d7b.bounds.extend( gmap\_ma43c62114da28c8611d6ccff068a0d7b.positions[m] );
}
// Render markers
for ( var m in gmap\_ma43c62114da28c8611d6ccff068a0d7b.positions ) {
gmap\_ma43c62114da28c8611d6ccff068a0d7b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma43c62114da28c8611d6ccff068a0d7b.map,
position : gmap\_ma43c62114da28c8611d6ccff068a0d7b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma43c62114da28c8611d6ccff068a0d7b.map.setCenter( gmap\_ma43c62114da28c8611d6ccff068a0d7b.positions[799] );
});