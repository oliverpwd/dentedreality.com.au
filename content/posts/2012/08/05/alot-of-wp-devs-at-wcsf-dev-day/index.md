---
title: ''
date: '2012-08-05T21:27:02+00:00'
format: image
service: instagram
tags:
- photo
- wcsf
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/d3636b94df6511e19f8e22000a1d0105_7.jpg?resize=607%2C607
---

[![ALOT of WP Devs at #wcsf dev day!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/d3636b94df6511e19f8e22000a1d0105_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/05/alot-of-wp-devs-at-wcsf-dev-day/) 

ALOT of WP Devs at #wcsf dev day!





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)

Posted on [Instagram](http://instagram.com/p/N99mEXimO_/) [9:27 pm, August 5, 2012](http://dentedreality.com.au/2012/08/05/alot-of-wp-devs-at-wcsf-dev-day/ "9:27 pm") 
jQuery(document).ready(function(){
var gmap\_m095a28a73710564723bd03172ae18d39 = {
positions : {
426 : new google.maps.LatLng( '37.755230703', '-122.418396935' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m095a28a73710564723bd03172ae18d39' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m095a28a73710564723bd03172ae18d39.positions ) {
gmap\_m095a28a73710564723bd03172ae18d39.bounds.extend( gmap\_m095a28a73710564723bd03172ae18d39.positions[m] );
}
// Render markers
for ( var m in gmap\_m095a28a73710564723bd03172ae18d39.positions ) {
gmap\_m095a28a73710564723bd03172ae18d39.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m095a28a73710564723bd03172ae18d39.map,
position : gmap\_m095a28a73710564723bd03172ae18d39.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m095a28a73710564723bd03172ae18d39.map.setCenter( gmap\_m095a28a73710564723bd03172ae18d39.positions[426] );
});