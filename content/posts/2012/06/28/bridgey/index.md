---
title: ''
date: '2012-06-28T20:29:25+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7b35e76ec18111e1b10e123138105d6b_7.jpg?resize=607%2C607
---

[![Bridgey](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7b35e76ec18111e1b10e123138105d6b_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/06/28/bridgey/) 

Bridgey





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/McAzAyimNu/) [8:29 pm, June 28, 2012](http://dentedreality.com.au/2012/06/28/bridgey/ "8:29 pm") 
jQuery(document).ready(function(){
var gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef = {
positions : {
482 : new google.maps.LatLng( '40.702407028', '-73.988751007' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.positions ) {
gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.bounds.extend( gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.positions[m] );
}
// Render markers
for ( var m in gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.positions ) {
gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.map,
position : gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.map.setCenter( gmap\_m6bd8701fe9df1cb3a9559f20373cd9ef.positions[482] );
});