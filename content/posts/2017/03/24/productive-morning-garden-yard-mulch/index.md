---
title: ''
date: '2017-03-24T13:22:27-06:00'
format: image
service: instagram
tags:
- garden
- mulch
- yard
latitude: '39.7572'
longitude: '-104.967'
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17438590_143842176142309_1894034286378483712_n.jpg?fit=640%2C640
---

[![Productive morning. #garden #yard #mulch](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17438590_143842176142309_1894034286378483712_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/03/24/productive-morning-garden-yard-mulch/) 

[![Productive morning. #garden #yard #mulch](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17438590_143842176142309_1894034286378483712_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BSCE4NBhr3e/)

Productive morning. #garden #yard #mulch

39.7572-104.967




* #[garden](https://dentedreality.com.au/tags/garden/)
* #[mulch](https://dentedreality.com.au/tags/mulch/)
* #[yard](https://dentedreality.com.au/tags/yard/)

Posted on [Instagram](https://www.instagram.com/p/BSCE4NBhr3e/) [1:22 pm, March 24, 2017](https://dentedreality.com.au/2017/03/24/productive-morning-garden-yard-mulch/ "1:22 pm") 
jQuery(document).ready(function(){
var gmap\_m3f8522e130bcac9c8c0956aee689e52a = {
positions : {
218 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3f8522e130bcac9c8c0956aee689e52a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3f8522e130bcac9c8c0956aee689e52a.positions ) {
gmap\_m3f8522e130bcac9c8c0956aee689e52a.bounds.extend( gmap\_m3f8522e130bcac9c8c0956aee689e52a.positions[m] );
}
// Render markers
for ( var m in gmap\_m3f8522e130bcac9c8c0956aee689e52a.positions ) {
gmap\_m3f8522e130bcac9c8c0956aee689e52a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3f8522e130bcac9c8c0956aee689e52a.map,
position : gmap\_m3f8522e130bcac9c8c0956aee689e52a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3f8522e130bcac9c8c0956aee689e52a.map.setCenter( gmap\_m3f8522e130bcac9c8c0956aee689e52a.positions[218] );
});