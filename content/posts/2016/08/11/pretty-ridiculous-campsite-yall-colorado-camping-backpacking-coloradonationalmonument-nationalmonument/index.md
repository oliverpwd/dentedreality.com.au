---
title: ''
date: '2016-08-11T20:34:06+00:00'
format: image
service: instagram
tags:
- backpacking
- camping
- colorado
- coloradonationalmonument
- nationalmonument
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13649108_1563293077312835_1165323786_n.jpg?fit=640%2C640
---

[![Pretty ridiculous campsite y'all. #colorado #camping #backpacking #coloradonationalmonument #nationalmonument](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13649108_1563293077312835_1165323786_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/11/pretty-ridiculous-campsite-yall-colorado-camping-backpacking-coloradonationalmonument-nationalmonument/) 

Pretty ridiculous campsite y’all. #colorado #camping #backpacking #coloradonationalmonument #nationalmonument





* #[backpacking](http://dentedreality.com.au/tags/backpacking/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[coloradonationalmonument](http://dentedreality.com.au/tags/coloradonationalmonument/)
* #[nationalmonument](http://dentedreality.com.au/tags/nationalmonument/)

Posted on [Instagram](https://www.instagram.com/p/BI_fa0fArEx/) [8:34 pm, August 11, 2016](http://dentedreality.com.au/2016/08/11/pretty-ridiculous-campsite-yall-colorado-camping-backpacking-coloradonationalmonument-nationalmonument/ "8:34 pm") 
jQuery(document).ready(function(){
var gmap\_m2b90c5173029d803d03afc85ea0e6fc6 = {
positions : {
105 : new google.maps.LatLng( '39.100965816009', '-108.73441429808' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2b90c5173029d803d03afc85ea0e6fc6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2b90c5173029d803d03afc85ea0e6fc6.positions ) {
gmap\_m2b90c5173029d803d03afc85ea0e6fc6.bounds.extend( gmap\_m2b90c5173029d803d03afc85ea0e6fc6.positions[m] );
}
// Render markers
for ( var m in gmap\_m2b90c5173029d803d03afc85ea0e6fc6.positions ) {
gmap\_m2b90c5173029d803d03afc85ea0e6fc6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2b90c5173029d803d03afc85ea0e6fc6.map,
position : gmap\_m2b90c5173029d803d03afc85ea0e6fc6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2b90c5173029d803d03afc85ea0e6fc6.map.setCenter( gmap\_m2b90c5173029d803d03afc85ea0e6fc6.positions[105] );
});