---
title: ''
date: '2012-08-03T21:13:58+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/ab3af802ddd111e1b1c522000a1e86b4_7.jpg?resize=607%2C607
---

[![Never get sick of this view.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/ab3af802ddd111e1b1c522000a1e86b4_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/03/never-get-sick-of-this-view/) 

Never get sick of this view.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/N4ygm2imNO/) [9:13 pm, August 3, 2012](http://dentedreality.com.au/2012/08/03/never-get-sick-of-this-view/ "9:13 pm") 
jQuery(document).ready(function(){
var gmap\_me886fe06368d401614edfd22108baf89 = {
positions : {
531 : new google.maps.LatLng( '37.755230703', '-122.418396935' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me886fe06368d401614edfd22108baf89' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me886fe06368d401614edfd22108baf89.positions ) {
gmap\_me886fe06368d401614edfd22108baf89.bounds.extend( gmap\_me886fe06368d401614edfd22108baf89.positions[m] );
}
// Render markers
for ( var m in gmap\_me886fe06368d401614edfd22108baf89.positions ) {
gmap\_me886fe06368d401614edfd22108baf89.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me886fe06368d401614edfd22108baf89.map,
position : gmap\_me886fe06368d401614edfd22108baf89.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me886fe06368d401614edfd22108baf89.map.setCenter( gmap\_me886fe06368d401614edfd22108baf89.positions[531] );
});