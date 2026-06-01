---
title: ''
date: '2012-11-27T14:15:37+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/71491cee38be11e2943422000a9f1416_7.jpg?resize=607%2C607
---

[![Mmmmmm latte.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/71491cee38be11e2943422000a9f1416_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/27/mmmmmm-latte/) 

Mmmmmm latte.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/Siu16vCmLE/) [2:15 pm, November 27, 2012](http://dentedreality.com.au/2012/11/27/mmmmmm-latte/ "2:15 pm") 
jQuery(document).ready(function(){
var gmap\_m240784846bd8c4a6d1f1312d1c47f7a7 = {
positions : {
477 : new google.maps.LatLng( '29.92137981', '-90.117926944' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m240784846bd8c4a6d1f1312d1c47f7a7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.positions ) {
gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.bounds.extend( gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.positions[m] );
}
// Render markers
for ( var m in gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.positions ) {
gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.map,
position : gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.map.setCenter( gmap\_m240784846bd8c4a6d1f1312d1c47f7a7.positions[477] );
});