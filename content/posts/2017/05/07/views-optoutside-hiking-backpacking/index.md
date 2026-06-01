---
title: ''
date: '2017-05-07T17:18:25+00:00'
format: image
service: instagram
tags:
- backpacking
- hiking
- optoutside
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18299207_229874767496521_3870633198694170624_n.jpg?fit=640%2C640
---

[![Views. #optoutside #hiking #backpacking](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18299207_229874767496521_3870633198694170624_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/07/views-optoutside-hiking-backpacking/) 

Views. #optoutside #hiking #backpacking





* #[backpacking](https://dentedreality.com.au/tags/backpacking/)
* #[hiking](https://dentedreality.com.au/tags/hiking/)
* #[optoutside](https://dentedreality.com.au/tags/optoutside/)

Posted on [Instagram](https://www.instagram.com/p/BTzy3Dsh76G/) [5:18 pm, May 7, 2017](https://dentedreality.com.au/2017/05/07/views-optoutside-hiking-backpacking/ "5:18 pm") 
jQuery(document).ready(function(){
var gmap\_ma452eae95040ccf72a916a3ad1cccd08 = {
positions : {
921 : new google.maps.LatLng( '39.804645818434', '-105.2691078186' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma452eae95040ccf72a916a3ad1cccd08' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma452eae95040ccf72a916a3ad1cccd08.positions ) {
gmap\_ma452eae95040ccf72a916a3ad1cccd08.bounds.extend( gmap\_ma452eae95040ccf72a916a3ad1cccd08.positions[m] );
}
// Render markers
for ( var m in gmap\_ma452eae95040ccf72a916a3ad1cccd08.positions ) {
gmap\_ma452eae95040ccf72a916a3ad1cccd08.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma452eae95040ccf72a916a3ad1cccd08.map,
position : gmap\_ma452eae95040ccf72a916a3ad1cccd08.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma452eae95040ccf72a916a3ad1cccd08.map.setCenter( gmap\_ma452eae95040ccf72a916a3ad1cccd08.positions[921] );
});