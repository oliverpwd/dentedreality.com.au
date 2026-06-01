---
title: ''
date: '2014-06-29T23:38:15+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10507930_693659320707250_311304143_n.jpg?resize=640%2C640
---

[![Packing Progress.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10507930_693659320707250_311304143_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/06/29/packing-progress/) 

Packing Progress.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/p2uW6mimOk/) [11:38 pm, June 29, 2014](http://dentedreality.com.au/2014/06/29/packing-progress/ "11:38 pm") 
jQuery(document).ready(function(){
var gmap\_m5a168dd25c80cb5759089607e7612b01 = {
positions : {
804 : new google.maps.LatLng( '40.669333333', '-73.984903333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5a168dd25c80cb5759089607e7612b01' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5a168dd25c80cb5759089607e7612b01.positions ) {
gmap\_m5a168dd25c80cb5759089607e7612b01.bounds.extend( gmap\_m5a168dd25c80cb5759089607e7612b01.positions[m] );
}
// Render markers
for ( var m in gmap\_m5a168dd25c80cb5759089607e7612b01.positions ) {
gmap\_m5a168dd25c80cb5759089607e7612b01.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5a168dd25c80cb5759089607e7612b01.map,
position : gmap\_m5a168dd25c80cb5759089607e7612b01.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5a168dd25c80cb5759089607e7612b01.map.setCenter( gmap\_m5a168dd25c80cb5759089607e7612b01.positions[804] );
});