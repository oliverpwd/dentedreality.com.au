---
title: ''
date: '2012-10-30T13:14:06+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/3623cd3622b511e2979f22000a1f8ae3_7.jpg?resize=607%2C607
---

[![Side street near Gowanus Canal](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/3623cd3622b511e2979f22000a1f8ae3_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/10/30/side-street-near-gowanus-canal-2/) 

Side street near Gowanus Canal





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/RahkR-CmH4/) [1:14 pm, October 30, 2012](http://dentedreality.com.au/2012/10/30/side-street-near-gowanus-canal-2/ "1:14 pm") 
jQuery(document).ready(function(){
var gmap\_m514554e0ffc1399165e3a853ec559dae = {
positions : {
178 : new google.maps.LatLng( '40.676049015', '-73.99017334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m514554e0ffc1399165e3a853ec559dae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m514554e0ffc1399165e3a853ec559dae.positions ) {
gmap\_m514554e0ffc1399165e3a853ec559dae.bounds.extend( gmap\_m514554e0ffc1399165e3a853ec559dae.positions[m] );
}
// Render markers
for ( var m in gmap\_m514554e0ffc1399165e3a853ec559dae.positions ) {
gmap\_m514554e0ffc1399165e3a853ec559dae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m514554e0ffc1399165e3a853ec559dae.map,
position : gmap\_m514554e0ffc1399165e3a853ec559dae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m514554e0ffc1399165e3a853ec559dae.map.setCenter( gmap\_m514554e0ffc1399165e3a853ec559dae.positions[178] );
});