---
title: ''
date: '2011-12-28T00:13:13+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/42c226b6310a11e19896123138142014_7.jpg?resize=607%2C607
---

[![Glitter nails BuckyBalls snowflake love heart!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/42c226b6310a11e19896123138142014_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/12/28/glitter-nails-buckyballs-snowflake-love-heart/) 

Glitter nails BuckyBalls snowflake love heart!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/cRMKF/) [12:13 am, December 28, 2011](http://dentedreality.com.au/2011/12/28/glitter-nails-buckyballs-snowflake-love-heart/ "12:13 am") 
jQuery(document).ready(function(){
var gmap\_m345ce62f374f89d68114e0ab85a9bc89 = {
positions : {
541 : new google.maps.LatLng( '37.73576', '-122.4337' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m345ce62f374f89d68114e0ab85a9bc89' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m345ce62f374f89d68114e0ab85a9bc89.positions ) {
gmap\_m345ce62f374f89d68114e0ab85a9bc89.bounds.extend( gmap\_m345ce62f374f89d68114e0ab85a9bc89.positions[m] );
}
// Render markers
for ( var m in gmap\_m345ce62f374f89d68114e0ab85a9bc89.positions ) {
gmap\_m345ce62f374f89d68114e0ab85a9bc89.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m345ce62f374f89d68114e0ab85a9bc89.map,
position : gmap\_m345ce62f374f89d68114e0ab85a9bc89.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m345ce62f374f89d68114e0ab85a9bc89.map.setCenter( gmap\_m345ce62f374f89d68114e0ab85a9bc89.positions[541] );
});