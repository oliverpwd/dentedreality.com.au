---
title: ''
date: '2015-02-06T10:12:38+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10958387_1394385244202458_1571051968_n.jpg?resize=640%2C640
---

[![First ever shots at 20 yards.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10958387_1394385244202458_1571051968_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/06/first-ever-shots-at-20-yards/) 

First ever shots at 20 yards.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/yxIXm_CmG6/) [10:12 am, February 6, 2015](http://dentedreality.com.au/2015/02/06/first-ever-shots-at-20-yards/ "10:12 am") 
jQuery(document).ready(function(){
var gmap\_m70576759989338da2187d86febdb0e2a = {
positions : {
558 : new google.maps.LatLng( '39.780010548', '-104.915660719' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m70576759989338da2187d86febdb0e2a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m70576759989338da2187d86febdb0e2a.positions ) {
gmap\_m70576759989338da2187d86febdb0e2a.bounds.extend( gmap\_m70576759989338da2187d86febdb0e2a.positions[m] );
}
// Render markers
for ( var m in gmap\_m70576759989338da2187d86febdb0e2a.positions ) {
gmap\_m70576759989338da2187d86febdb0e2a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m70576759989338da2187d86febdb0e2a.map,
position : gmap\_m70576759989338da2187d86febdb0e2a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m70576759989338da2187d86febdb0e2a.map.setCenter( gmap\_m70576759989338da2187d86febdb0e2a.positions[558] );
});