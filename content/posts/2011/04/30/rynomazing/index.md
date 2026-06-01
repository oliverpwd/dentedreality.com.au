---
title: ''
date: '2011-04-30T22:07:17+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/485739adb786496b973704d45a4b8ca0_7.jpg?resize=607%2C607
---

[![Rynomazing](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/485739adb786496b973704d45a4b8ca0_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/04/30/rynomazing/) 

Rynomazing





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/Duoov/) [10:07 pm, April 30, 2011](http://dentedreality.com.au/2011/04/30/rynomazing/ "10:07 pm") 
jQuery(document).ready(function(){
var gmap\_m7b76297642cdfa9a6716094c983a47de = {
positions : {
568 : new google.maps.LatLng( '36.10123', '-115.1457' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7b76297642cdfa9a6716094c983a47de' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7b76297642cdfa9a6716094c983a47de.positions ) {
gmap\_m7b76297642cdfa9a6716094c983a47de.bounds.extend( gmap\_m7b76297642cdfa9a6716094c983a47de.positions[m] );
}
// Render markers
for ( var m in gmap\_m7b76297642cdfa9a6716094c983a47de.positions ) {
gmap\_m7b76297642cdfa9a6716094c983a47de.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7b76297642cdfa9a6716094c983a47de.map,
position : gmap\_m7b76297642cdfa9a6716094c983a47de.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7b76297642cdfa9a6716094c983a47de.map.setCenter( gmap\_m7b76297642cdfa9a6716094c983a47de.positions[568] );
});