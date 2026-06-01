---
title: ''
date: '2016-08-21T21:40:18+00:00'
format: image
service: instagram
tags:
- fjallclassic2016
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13721323_649311421891707_1126890662_n.jpg?fit=640%2C640
---

[![Log-bridge creek crossings under sunny lens-flares. #fjallclassic2016 @fjallravenusa](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13721323_649311421891707_1126890662_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/21/log-bridge-creek-crossings-under-sunny-lens-flares-fjallclassic2016-fjallravenusa/) 

Log-bridge creek crossings under sunny lens-flares. #fjallclassic2016 @fjallravenusa





* #[fjallclassic2016](http://dentedreality.com.au/tags/fjallclassic2016/)

Posted on [Instagram](https://www.instagram.com/p/BJZW8bLAuHH/) [9:40 pm, August 21, 2016](http://dentedreality.com.au/2016/08/21/log-bridge-creek-crossings-under-sunny-lens-flares-fjallclassic2016-fjallravenusa/ "9:40 pm") 
jQuery(document).ready(function(){
var gmap\_mb485e20ff238e9d73b7d63477d285e3e = {
positions : {
291 : new google.maps.LatLng( '40.5113831', '-106.0084839' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb485e20ff238e9d73b7d63477d285e3e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb485e20ff238e9d73b7d63477d285e3e.positions ) {
gmap\_mb485e20ff238e9d73b7d63477d285e3e.bounds.extend( gmap\_mb485e20ff238e9d73b7d63477d285e3e.positions[m] );
}
// Render markers
for ( var m in gmap\_mb485e20ff238e9d73b7d63477d285e3e.positions ) {
gmap\_mb485e20ff238e9d73b7d63477d285e3e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb485e20ff238e9d73b7d63477d285e3e.map,
position : gmap\_mb485e20ff238e9d73b7d63477d285e3e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb485e20ff238e9d73b7d63477d285e3e.map.setCenter( gmap\_mb485e20ff238e9d73b7d63477d285e3e.positions[291] );
});