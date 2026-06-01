---
title: ''
date: '2012-01-29T00:34:24+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/856332584a3211e1a87612313804ec91_7.jpg?resize=607%2C607
---

[![Birthday girl!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/856332584a3211e1a87612313804ec91_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/01/29/birthday-girl/) 

Birthday girl!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/lu4lV/) [12:34 am, January 29, 2012](http://dentedreality.com.au/2012/01/29/birthday-girl/ "12:34 am") 
jQuery(document).ready(function(){
var gmap\_mb7f919670173285f9778544d3cab16a1 = {
positions : {
735 : new google.maps.LatLng( '37.76083', '-122.4215' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb7f919670173285f9778544d3cab16a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb7f919670173285f9778544d3cab16a1.positions ) {
gmap\_mb7f919670173285f9778544d3cab16a1.bounds.extend( gmap\_mb7f919670173285f9778544d3cab16a1.positions[m] );
}
// Render markers
for ( var m in gmap\_mb7f919670173285f9778544d3cab16a1.positions ) {
gmap\_mb7f919670173285f9778544d3cab16a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb7f919670173285f9778544d3cab16a1.map,
position : gmap\_mb7f919670173285f9778544d3cab16a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb7f919670173285f9778544d3cab16a1.map.setCenter( gmap\_mb7f919670173285f9778544d3cab16a1.positions[735] );
});