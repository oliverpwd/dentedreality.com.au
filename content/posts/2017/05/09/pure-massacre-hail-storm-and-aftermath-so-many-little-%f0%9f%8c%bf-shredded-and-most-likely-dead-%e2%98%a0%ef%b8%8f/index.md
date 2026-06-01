---
title: ''
date: '2017-05-09T21:25:38+00:00'
format: image
service: instagram
tags:
- hail
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18380409_1924679867808034_590242941579034624_n.jpg?fit=640%2C640
---

[![Pure Massacre. #hail storm and aftermath. So many little 🌿 shredded and most likely dead ☠️](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18380409_1924679867808034_590242941579034624_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/09/pure-massacre-hail-storm-and-aftermath-so-many-little-%f0%9f%8c%bf-shredded-and-most-likely-dead-%e2%98%a0%ef%b8%8f/) 

Pure Massacre. #hail storm and aftermath. So many little 🌿 shredded and most likely dead ☠️





* #[hail](https://dentedreality.com.au/tags/hail/)

Posted on [Instagram](https://www.instagram.com/p/BT5YvYChFVy/) [9:25 pm, May 9, 2017](https://dentedreality.com.au/2017/05/09/pure-massacre-hail-storm-and-aftermath-so-many-little-%f0%9f%8c%bf-shredded-and-most-likely-dead-%e2%98%a0%ef%b8%8f/ "9:25 pm") 
jQuery(document).ready(function(){
var gmap\_m4168420a2acb68191b9b358fc1c7d1e1 = {
positions : {
803 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4168420a2acb68191b9b358fc1c7d1e1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4168420a2acb68191b9b358fc1c7d1e1.positions ) {
gmap\_m4168420a2acb68191b9b358fc1c7d1e1.bounds.extend( gmap\_m4168420a2acb68191b9b358fc1c7d1e1.positions[m] );
}
// Render markers
for ( var m in gmap\_m4168420a2acb68191b9b358fc1c7d1e1.positions ) {
gmap\_m4168420a2acb68191b9b358fc1c7d1e1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4168420a2acb68191b9b358fc1c7d1e1.map,
position : gmap\_m4168420a2acb68191b9b358fc1c7d1e1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4168420a2acb68191b9b358fc1c7d1e1.map.setCenter( gmap\_m4168420a2acb68191b9b358fc1c7d1e1.positions[803] );
});