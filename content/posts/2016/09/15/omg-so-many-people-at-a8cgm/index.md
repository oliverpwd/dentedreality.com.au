---
title: ''
date: '2016-09-15T22:24:59+00:00'
format: image
service: instagram
tags:
- a8cgm
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14280551_841505165983943_1129477514_n.jpg?fit=640%2C640
---

[![OMG so many people at #a8cgm](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14280551_841505165983943_1129477514_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/15/omg-so-many-people-at-a8cgm/) 

OMG so many people at #a8cgm





* #[a8cgm](http://dentedreality.com.au/tags/a8cgm/)

Posted on [Instagram](https://www.instagram.com/p/BKZz7k1gnQM/) [10:24 pm, September 15, 2016](http://dentedreality.com.au/2016/09/15/omg-so-many-people-at-a8cgm/ "10:24 pm") 
jQuery(document).ready(function(){
var gmap\_m9310356960413ae9be1b30280076e69a = {
positions : {
818 : new google.maps.LatLng( '50.112288625037', '-122.95582178407' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9310356960413ae9be1b30280076e69a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9310356960413ae9be1b30280076e69a.positions ) {
gmap\_m9310356960413ae9be1b30280076e69a.bounds.extend( gmap\_m9310356960413ae9be1b30280076e69a.positions[m] );
}
// Render markers
for ( var m in gmap\_m9310356960413ae9be1b30280076e69a.positions ) {
gmap\_m9310356960413ae9be1b30280076e69a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9310356960413ae9be1b30280076e69a.map,
position : gmap\_m9310356960413ae9be1b30280076e69a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9310356960413ae9be1b30280076e69a.map.setCenter( gmap\_m9310356960413ae9be1b30280076e69a.positions[818] );
});