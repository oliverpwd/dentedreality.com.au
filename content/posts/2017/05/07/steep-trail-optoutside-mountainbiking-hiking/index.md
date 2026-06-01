---
title: ''
date: '2017-05-07T17:16:26+00:00'
format: image
service: instagram
tags:
- hiking
- mountainbiking
- optoutside
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18299820_122710678291098_3346364730057949184_n.jpg?fit=640%2C640
---

[![Steep trail. #optoutside #mountainbiking #hiking](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18299820_122710678291098_3346364730057949184_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/07/steep-trail-optoutside-mountainbiking-hiking/) 

Steep trail. #optoutside #mountainbiking #hiking





* #[hiking](https://dentedreality.com.au/tags/hiking/)
* #[mountainbiking](https://dentedreality.com.au/tags/mountainbiking/)
* #[optoutside](https://dentedreality.com.au/tags/optoutside/)

Posted on [Instagram](https://www.instagram.com/p/BTzyohxBgos/) [5:16 pm, May 7, 2017](https://dentedreality.com.au/2017/05/07/steep-trail-optoutside-mountainbiking-hiking/ "5:16 pm") 
jQuery(document).ready(function(){
var gmap\_mefb7d7bdeadc64ca355859ae66095fa1 = {
positions : {
256 : new google.maps.LatLng( '39.804645818434', '-105.2691078186' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mefb7d7bdeadc64ca355859ae66095fa1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mefb7d7bdeadc64ca355859ae66095fa1.positions ) {
gmap\_mefb7d7bdeadc64ca355859ae66095fa1.bounds.extend( gmap\_mefb7d7bdeadc64ca355859ae66095fa1.positions[m] );
}
// Render markers
for ( var m in gmap\_mefb7d7bdeadc64ca355859ae66095fa1.positions ) {
gmap\_mefb7d7bdeadc64ca355859ae66095fa1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mefb7d7bdeadc64ca355859ae66095fa1.map,
position : gmap\_mefb7d7bdeadc64ca355859ae66095fa1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mefb7d7bdeadc64ca355859ae66095fa1.map.setCenter( gmap\_mefb7d7bdeadc64ca355859ae66095fa1.positions[256] );
});