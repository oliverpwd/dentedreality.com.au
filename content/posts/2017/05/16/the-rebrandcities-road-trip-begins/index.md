---
title: ''
date: '2017-05-16T11:03:53+00:00'
format: image
service: instagram
tags:
- rebrandcities
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18512740_527023961021748_4313850931465682944_n.jpg?fit=640%2C640&ssl=1
---

[![The #rebrandcities road trip begins!](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18512740_527023961021748_4313850931465682944_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/05/16/the-rebrandcities-road-trip-begins/) 

The #rebrandcities road trip begins!





* #[rebrandcities](https://dentedreality.com.au/tags/rebrandcities/)

Posted on [Instagram](https://www.instagram.com/p/BUKTJp1hk1u/) [11:03 am, May 16, 2017](https://dentedreality.com.au/2017/05/16/the-rebrandcities-road-trip-begins/ "11:03 am") 
jQuery(document).ready(function(){
var gmap\_md1a4f2b60da673373cca2fdbe8d3d253 = {
positions : {
654 : new google.maps.LatLng( '42.3581102', '-83.022511' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md1a4f2b60da673373cca2fdbe8d3d253' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md1a4f2b60da673373cca2fdbe8d3d253.positions ) {
gmap\_md1a4f2b60da673373cca2fdbe8d3d253.bounds.extend( gmap\_md1a4f2b60da673373cca2fdbe8d3d253.positions[m] );
}
// Render markers
for ( var m in gmap\_md1a4f2b60da673373cca2fdbe8d3d253.positions ) {
gmap\_md1a4f2b60da673373cca2fdbe8d3d253.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md1a4f2b60da673373cca2fdbe8d3d253.map,
position : gmap\_md1a4f2b60da673373cca2fdbe8d3d253.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md1a4f2b60da673373cca2fdbe8d3d253.map.setCenter( gmap\_md1a4f2b60da673373cca2fdbe8d3d253.positions[654] );
});