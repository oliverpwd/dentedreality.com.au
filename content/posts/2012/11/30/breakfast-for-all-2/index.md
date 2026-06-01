---
title: ''
date: '2012-11-30T12:02:28+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/57469b003b0711e2a9d822000a9e29af_7.jpg?resize=607%2C607
---

[![Breakfast for all.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/57469b003b0711e2a9d822000a9e29af_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/30/breakfast-for-all-2/) 

Breakfast for all.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SqN_cCimF4/) [12:02 pm, November 30, 2012](http://dentedreality.com.au/2012/11/30/breakfast-for-all-2/ "12:02 pm") 
jQuery(document).ready(function(){
var gmap\_m970130637522da44a42802564fa87631 = {
positions : {
650 : new google.maps.LatLng( '29.93354161', '-90.098043001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m970130637522da44a42802564fa87631' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m970130637522da44a42802564fa87631.positions ) {
gmap\_m970130637522da44a42802564fa87631.bounds.extend( gmap\_m970130637522da44a42802564fa87631.positions[m] );
}
// Render markers
for ( var m in gmap\_m970130637522da44a42802564fa87631.positions ) {
gmap\_m970130637522da44a42802564fa87631.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m970130637522da44a42802564fa87631.map,
position : gmap\_m970130637522da44a42802564fa87631.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m970130637522da44a42802564fa87631.map.setCenter( gmap\_m970130637522da44a42802564fa87631.positions[650] );
});