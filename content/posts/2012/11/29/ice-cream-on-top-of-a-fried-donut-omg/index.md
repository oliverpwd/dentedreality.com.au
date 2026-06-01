---
title: ''
date: '2012-11-29T23:16:03+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/45bd81d43a9c11e2a57122000a1fbe0e_7.jpg?resize=607%2C607
---

[![Ice cream. On top of a fried donut. OMG.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/45bd81d43a9c11e2a57122000a1fbe0e_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/29/ice-cream-on-top-of-a-fried-donut-omg/) 

Ice cream. On top of a fried donut. OMG.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/So2R90imEV/) [11:16 pm, November 29, 2012](http://dentedreality.com.au/2012/11/29/ice-cream-on-top-of-a-fried-donut-omg/ "11:16 pm") 
jQuery(document).ready(function(){
var gmap\_m3c0db354f8f993fe13ab23044cebf58a = {
positions : {
161 : new google.maps.LatLng( '29.935063', '-90.104307' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c0db354f8f993fe13ab23044cebf58a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c0db354f8f993fe13ab23044cebf58a.positions ) {
gmap\_m3c0db354f8f993fe13ab23044cebf58a.bounds.extend( gmap\_m3c0db354f8f993fe13ab23044cebf58a.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c0db354f8f993fe13ab23044cebf58a.positions ) {
gmap\_m3c0db354f8f993fe13ab23044cebf58a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c0db354f8f993fe13ab23044cebf58a.map,
position : gmap\_m3c0db354f8f993fe13ab23044cebf58a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c0db354f8f993fe13ab23044cebf58a.map.setCenter( gmap\_m3c0db354f8f993fe13ab23044cebf58a.positions[161] );
});