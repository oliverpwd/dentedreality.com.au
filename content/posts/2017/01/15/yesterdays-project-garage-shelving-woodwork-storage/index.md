---
title: ''
date: '2017-01-15T13:04:37+00:00'
format: image
service: instagram
tags:
- garage
- shelving
- storage
- woodwork
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/15876599_1276622909097794_5396099625390178304_n.jpg?fit=640%2C640
---

[![Yesterday's project. #garage #shelving #woodwork #storage](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/15876599_1276622909097794_5396099625390178304_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/01/15/yesterdays-project-garage-shelving-woodwork-storage/) 

Yesterday’s project. #garage #shelving #woodwork #storage





* #[garage](http://dentedreality.com.au/tags/garage/)
* #[shelving](http://dentedreality.com.au/tags/shelving/)
* #[storage](http://dentedreality.com.au/tags/storage/)
* #[woodwork](http://dentedreality.com.au/tags/woodwork/)

Posted on [Instagram](https://www.instagram.com/p/BPTDpgmjO54/) [1:04 pm, January 15, 2017](http://dentedreality.com.au/2017/01/15/yesterdays-project-garage-shelving-woodwork-storage/ "1:04 pm") 
jQuery(document).ready(function(){
var gmap\_m2b9f0ce5b804e6d91de06e2180842c44 = {
positions : {
87 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2b9f0ce5b804e6d91de06e2180842c44' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2b9f0ce5b804e6d91de06e2180842c44.positions ) {
gmap\_m2b9f0ce5b804e6d91de06e2180842c44.bounds.extend( gmap\_m2b9f0ce5b804e6d91de06e2180842c44.positions[m] );
}
// Render markers
for ( var m in gmap\_m2b9f0ce5b804e6d91de06e2180842c44.positions ) {
gmap\_m2b9f0ce5b804e6d91de06e2180842c44.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2b9f0ce5b804e6d91de06e2180842c44.map,
position : gmap\_m2b9f0ce5b804e6d91de06e2180842c44.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2b9f0ce5b804e6d91de06e2180842c44.map.setCenter( gmap\_m2b9f0ce5b804e6d91de06e2180842c44.positions[87] );
});