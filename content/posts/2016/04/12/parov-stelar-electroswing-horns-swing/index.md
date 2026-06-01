---
title: ''
date: '2016-04-12T07:44:14+00:00'
format: image
service: instagram
tags:
- electroswing
- horns
- swing
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12501818_1776044905949685_602809057_n.jpg?fit=640%2C640
---

[![Parov Stelar! #electroswing #horns #swing](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12501818_1776044905949685_602809057_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/04/12/parov-stelar-electroswing-horns-swing/) 

Parov Stelar! #electroswing #horns #swing





* #[electroswing](http://dentedreality.com.au/tags/electroswing/)
* #[horns](http://dentedreality.com.au/tags/horns/)
* #[swing](http://dentedreality.com.au/tags/swing/)

Posted on [Instagram](https://www.instagram.com/p/BEGjISaCmKW/) [7:44 am, April 12, 2016](http://dentedreality.com.au/2016/04/12/parov-stelar-electroswing-horns-swing/ "7:44 am") 
jQuery(document).ready(function(){
var gmap\_mae04290f78f168f16cc81ecb05b0ac6c = {
positions : {
454 : new google.maps.LatLng( '39.74039', '-104.97526' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mae04290f78f168f16cc81ecb05b0ac6c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mae04290f78f168f16cc81ecb05b0ac6c.positions ) {
gmap\_mae04290f78f168f16cc81ecb05b0ac6c.bounds.extend( gmap\_mae04290f78f168f16cc81ecb05b0ac6c.positions[m] );
}
// Render markers
for ( var m in gmap\_mae04290f78f168f16cc81ecb05b0ac6c.positions ) {
gmap\_mae04290f78f168f16cc81ecb05b0ac6c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mae04290f78f168f16cc81ecb05b0ac6c.map,
position : gmap\_mae04290f78f168f16cc81ecb05b0ac6c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mae04290f78f168f16cc81ecb05b0ac6c.map.setCenter( gmap\_mae04290f78f168f16cc81ecb05b0ac6c.positions[454] );
});