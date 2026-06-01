---
title: ''
date: '2014-03-29T12:07:44+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/99eb6c8ab76411e3b88512e7cafcbe78_8.jpg?resize=640%2C640
---

[![The things we do for love.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/99eb6c8ab76411e3b88512e7cafcbe78_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/03/29/the-things-we-do-for-love/) 

The things we do for love.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/mImM4NCmAI/) [12:07 pm, March 29, 2014](http://dentedreality.com.au/2014/03/29/the-things-we-do-for-love/ "12:07 pm") 
jQuery(document).ready(function(){
var gmap\_m006c9484a0dfa237c84ff3e62f7a1c31 = {
positions : {
715 : new google.maps.LatLng( '-37.686804', '144.848394' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m006c9484a0dfa237c84ff3e62f7a1c31' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.positions ) {
gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.bounds.extend( gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.positions[m] );
}
// Render markers
for ( var m in gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.positions ) {
gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.map,
position : gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.map.setCenter( gmap\_m006c9484a0dfa237c84ff3e62f7a1c31.positions[715] );
});