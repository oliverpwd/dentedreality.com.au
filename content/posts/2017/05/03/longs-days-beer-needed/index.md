---
title: ''
date: '2017-05-03T17:33:12+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18252046_640664216123668_2256360703881379840_n.jpg?fit=640%2C640
---

[![Longs days. Beer needed.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18252046_640664216123668_2256360703881379840_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/03/longs-days-beer-needed/) 

Longs days. Beer needed.





Posted on [Instagram](https://www.instagram.com/p/BTphXu0BjeD/) [5:33 pm, May 3, 2017](https://dentedreality.com.au/2017/05/03/longs-days-beer-needed/ "5:33 pm") 
jQuery(document).ready(function(){
var gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef = {
positions : {
289 : new google.maps.LatLng( '39.760583166684', '-104.98253524303' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.positions ) {
gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.bounds.extend( gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.positions[m] );
}
// Render markers
for ( var m in gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.positions ) {
gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.map,
position : gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.map.setCenter( gmap\_m7d5b88a6a8d28aa3cf7876f6f74d29ef.positions[289] );
});