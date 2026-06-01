---
title: ''
date: '2012-08-25T14:42:01+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8eddd9b2eee411e1a74822000a1e8c8d_7.jpg?resize=607%2C607
---

[![Posted on Instagram](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8eddd9b2eee411e1a74822000a1e8c8d_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/25/posted-on-instagram-5/) 




* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/OwvJFVCmCp/) [2:42 pm, August 25, 2012](http://dentedreality.com.au/2012/08/25/posted-on-instagram-5/ "2:42 pm") 
jQuery(document).ready(function(){
var gmap\_m1952f592077003703e24c15572b0b1e7 = {
positions : {
518 : new google.maps.LatLng( '40.671399952', '-73.984520933' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1952f592077003703e24c15572b0b1e7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1952f592077003703e24c15572b0b1e7.positions ) {
gmap\_m1952f592077003703e24c15572b0b1e7.bounds.extend( gmap\_m1952f592077003703e24c15572b0b1e7.positions[m] );
}
// Render markers
for ( var m in gmap\_m1952f592077003703e24c15572b0b1e7.positions ) {
gmap\_m1952f592077003703e24c15572b0b1e7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1952f592077003703e24c15572b0b1e7.map,
position : gmap\_m1952f592077003703e24c15572b0b1e7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1952f592077003703e24c15572b0b1e7.map.setCenter( gmap\_m1952f592077003703e24c15572b0b1e7.positions[518] );
});