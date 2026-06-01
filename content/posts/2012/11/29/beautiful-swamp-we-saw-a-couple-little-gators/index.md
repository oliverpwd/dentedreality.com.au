---
title: ''
date: '2012-11-29T15:43:04+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/fda654643a5c11e289bf22000a1fa4a9_7.jpg?resize=607%2C607
---

[![Beautiful Swamp. We saw a couple little 'gators!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/fda654643a5c11e289bf22000a1fa4a9_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/29/beautiful-swamp-we-saw-a-couple-little-gators/) 

Beautiful Swamp. We saw a couple little ‘gators!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SoCcMACmA4/) [3:43 pm, November 29, 2012](http://dentedreality.com.au/2012/11/29/beautiful-swamp-we-saw-a-couple-little-gators/ "3:43 pm") 
jQuery(document).ready(function(){
var gmap\_m8ffb3df189adc0d0f091259031f07c7a = {
positions : {
158 : new google.maps.LatLng( '29.925747039', '-90.418499012' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8ffb3df189adc0d0f091259031f07c7a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8ffb3df189adc0d0f091259031f07c7a.positions ) {
gmap\_m8ffb3df189adc0d0f091259031f07c7a.bounds.extend( gmap\_m8ffb3df189adc0d0f091259031f07c7a.positions[m] );
}
// Render markers
for ( var m in gmap\_m8ffb3df189adc0d0f091259031f07c7a.positions ) {
gmap\_m8ffb3df189adc0d0f091259031f07c7a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8ffb3df189adc0d0f091259031f07c7a.map,
position : gmap\_m8ffb3df189adc0d0f091259031f07c7a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8ffb3df189adc0d0f091259031f07c7a.map.setCenter( gmap\_m8ffb3df189adc0d0f091259031f07c7a.positions[158] );
});