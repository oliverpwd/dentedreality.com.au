---
title: ''
date: '2011-03-31T21:11:53+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/9659f109294447d8b8902371e97094d4_7.jpg?resize=607%2C607
---

[![South Bay is full of scary stuff!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/9659f109294447d8b8902371e97094d4_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/03/31/south-bay-is-full-of-scary-stuff/) 

South Bay is full of scary stuff!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/Ctl8l/) [9:11 pm, March 31, 2011](http://dentedreality.com.au/2011/03/31/south-bay-is-full-of-scary-stuff/ "9:11 pm") 
jQuery(document).ready(function(){
var gmap\_m7bc7945de9fe4fad65147b5718091a39 = {
positions : {
232 : new google.maps.LatLng( '37.395749482', '-122.052118778' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7bc7945de9fe4fad65147b5718091a39' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7bc7945de9fe4fad65147b5718091a39.positions ) {
gmap\_m7bc7945de9fe4fad65147b5718091a39.bounds.extend( gmap\_m7bc7945de9fe4fad65147b5718091a39.positions[m] );
}
// Render markers
for ( var m in gmap\_m7bc7945de9fe4fad65147b5718091a39.positions ) {
gmap\_m7bc7945de9fe4fad65147b5718091a39.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7bc7945de9fe4fad65147b5718091a39.map,
position : gmap\_m7bc7945de9fe4fad65147b5718091a39.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7bc7945de9fe4fad65147b5718091a39.map.setCenter( gmap\_m7bc7945de9fe4fad65147b5718091a39.positions[232] );
});