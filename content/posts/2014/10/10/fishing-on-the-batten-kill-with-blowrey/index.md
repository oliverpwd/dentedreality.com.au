---
title: ''
date: '2014-10-10T19:46:58+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10727361_649760235144406_1649513076_n.jpg?resize=640%2C640
---

[![Fishing on the Batten Kill with @blowrey](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10727361_649760235144406_1649513076_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/10/fishing-on-the-batten-kill-with-blowrey/) 

Fishing on the Batten Kill with @blowrey





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/t_oodXCmGb/) [7:46 pm, October 10, 2014](http://dentedreality.com.au/2014/10/10/fishing-on-the-batten-kill-with-blowrey/ "7:46 pm") 
jQuery(document).ready(function(){
var gmap\_m139df10c16e7eae6e59b1ca24ac76c1c = {
positions : {
254 : new google.maps.LatLng( '43.087558333', '-73.345536667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m139df10c16e7eae6e59b1ca24ac76c1c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.positions ) {
gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.bounds.extend( gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.positions[m] );
}
// Render markers
for ( var m in gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.positions ) {
gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.map,
position : gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.map.setCenter( gmap\_m139df10c16e7eae6e59b1ca24ac76c1c.positions[254] );
});