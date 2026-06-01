---
title: ''
date: '2015-01-17T17:10:48+00:00'
format: image
service: instagram
tags:
- nofilter
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/927768_1529878690596569_567374321_n.jpg?resize=640%2C640
---

[![Solid sunset, Denver. #nofilter](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/927768_1529878690596569_567374321_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/01/17/solid-sunset-denver-nofilter/) 

Solid sunset, Denver. #nofilter





* #[nofilter](http://dentedreality.com.au/tags/nofilter/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/x-YUyECmHk/) [5:10 pm, January 17, 2015](http://dentedreality.com.au/2015/01/17/solid-sunset-denver-nofilter/ "5:10 pm") 
jQuery(document).ready(function(){
var gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7 = {
positions : {
256 : new google.maps.LatLng( '39.750743361', '-104.991288949' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.positions ) {
gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.bounds.extend( gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.positions[m] );
}
// Render markers
for ( var m in gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.positions ) {
gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.map,
position : gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.map.setCenter( gmap\_m1b899c7a8f8b3bf75ee924f5a83908f7.positions[256] );
});