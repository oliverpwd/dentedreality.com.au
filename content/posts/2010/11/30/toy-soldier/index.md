---
title: ''
date: '2010-11-30T13:07:54+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/62dbab765abb48c8956ba391a4374f3b_7.jpg?resize=607%2C607
---

[![Toy Soldier](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/62dbab765abb48c8956ba391a4374f3b_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/11/30/toy-soldier/) 

Toy Soldier





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/amRb/) [1:07 pm, November 30, 2010](http://dentedreality.com.au/2010/11/30/toy-soldier/ "1:07 pm") 
jQuery(document).ready(function(){
var gmap\_m9a0357e9b350d6eb99f7706dd2bcad25 = {
positions : {
4 : new google.maps.LatLng( '37.791029', '-122.417442' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9a0357e9b350d6eb99f7706dd2bcad25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.positions ) {
gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.bounds.extend( gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.positions[m] );
}
// Render markers
for ( var m in gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.positions ) {
gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.map,
position : gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.map.setCenter( gmap\_m9a0357e9b350d6eb99f7706dd2bcad25.positions[4] );
});