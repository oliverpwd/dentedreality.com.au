---
title: ''
date: '2011-03-26T04:28:40+00:00'
format: image
service: instagram
tags:
- photo
- winning
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/c3f43e7726434863a3a72e7b2f604b78_7.jpg?resize=607%2C607
---

[![#winning](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/c3f43e7726434863a3a72e7b2f604b78_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/03/26/winning/) 

#winning





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[winning](http://dentedreality.com.au/tags/winning/)

Posted on [Instagram](http://instagram.com/p/Ci_VD/) [4:28 am, March 26, 2011](http://dentedreality.com.au/2011/03/26/winning/ "4:28 am") 
jQuery(document).ready(function(){
var gmap\_ma05135166fc749f74b4fd092ec882a2c = {
positions : {
892 : new google.maps.LatLng( '37.782470318', '-122.39267081' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma05135166fc749f74b4fd092ec882a2c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma05135166fc749f74b4fd092ec882a2c.positions ) {
gmap\_ma05135166fc749f74b4fd092ec882a2c.bounds.extend( gmap\_ma05135166fc749f74b4fd092ec882a2c.positions[m] );
}
// Render markers
for ( var m in gmap\_ma05135166fc749f74b4fd092ec882a2c.positions ) {
gmap\_ma05135166fc749f74b4fd092ec882a2c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma05135166fc749f74b4fd092ec882a2c.map,
position : gmap\_ma05135166fc749f74b4fd092ec882a2c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma05135166fc749f74b4fd092ec882a2c.map.setCenter( gmap\_ma05135166fc749f74b4fd092ec882a2c.positions[892] );
});