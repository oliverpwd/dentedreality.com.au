---
title: ''
date: '2017-05-16T09:41:09+00:00'
format: image
service: instagram
tags:
- rebrandcities
- rebranddetroit
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18512346_1161895093918799_3117181512752037888_n.jpg?fit=640%2C640
---

[![Hearing from our driver, getting this show on the road. #rebrandcities #rebranddetroit](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18512346_1161895093918799_3117181512752037888_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/16/hearing-from-our-driver-getting-this-show-on-the-road-rebrandcities-rebranddetroit/) 

Hearing from our driver, getting this show on the road. #rebrandcities #rebranddetroit





* #[rebrandcities](https://dentedreality.com.au/tags/rebrandcities/)
* #[rebranddetroit](https://dentedreality.com.au/tags/rebranddetroit/)

Posted on [Instagram](https://www.instagram.com/p/BUKJrxNha2X/) [9:41 am, May 16, 2017](https://dentedreality.com.au/2017/05/16/hearing-from-our-driver-getting-this-show-on-the-road-rebrandcities-rebranddetroit/ "9:41 am") 
jQuery(document).ready(function(){
var gmap\_m6f7eb59bf4f94050694a2578ea322075 = {
positions : {
477 : new google.maps.LatLng( '42.32833', '-83.04835' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6f7eb59bf4f94050694a2578ea322075' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6f7eb59bf4f94050694a2578ea322075.positions ) {
gmap\_m6f7eb59bf4f94050694a2578ea322075.bounds.extend( gmap\_m6f7eb59bf4f94050694a2578ea322075.positions[m] );
}
// Render markers
for ( var m in gmap\_m6f7eb59bf4f94050694a2578ea322075.positions ) {
gmap\_m6f7eb59bf4f94050694a2578ea322075.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6f7eb59bf4f94050694a2578ea322075.map,
position : gmap\_m6f7eb59bf4f94050694a2578ea322075.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6f7eb59bf4f94050694a2578ea322075.map.setCenter( gmap\_m6f7eb59bf4f94050694a2578ea322075.positions[477] );
});