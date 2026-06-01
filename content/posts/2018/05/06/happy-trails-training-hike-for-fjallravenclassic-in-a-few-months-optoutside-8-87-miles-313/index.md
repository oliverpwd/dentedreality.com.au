---
title: ''
date: '2018-05-06T14:10:14-06:00'
format: image
service: instagram
tags:
- fjallravenclassic
- optoutside
latitude: '39.63072'
longitude: '-105.225878'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/05/14182158/31016744_1943836319240788_5124740619511529472_n.jpg?resize=607%2C607&ssl=1
---

[![Happy trails. Training hike for #fjallravenclassic in a few months. #optoutside. 8.87 miles. 3:13.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/05/14182158/31016744_1943836319240788_5124740619511529472_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/05/06/happy-trails-training-hike-for-fjallravenclassic-in-a-few-months-optoutside-8-87-miles-313/) 

[![Happy trails. Training hike for #fjallravenclassic in a few months. #optoutside. 8.87 miles. 3:13.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/05/14182158/31016744_1943836319240788_5124740619511529472_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BicurMWFJau/)

Happy trails. Training hike for #fjallravenclassic in a few months. #optoutside. 8.87 miles. 3:13.

39.63072-105.225878




* #[fjallravenclassic](https://dentedreality.com.au/tags/fjallravenclassic/)
* #[optoutside](https://dentedreality.com.au/tags/optoutside/)

Posted on [Instagram](https://www.instagram.com/p/BicurMWFJau/) [2:10 pm, May 6, 2018](https://dentedreality.com.au/2018/05/06/happy-trails-training-hike-for-fjallravenclassic-in-a-few-months-optoutside-8-87-miles-313/ "2:10 pm") 
jQuery(document).ready(function(){
var gmap\_m9d0422e5647ceea60b43cc123b8adb6d = {
positions : {
602 : new google.maps.LatLng( '39.63072', '-105.225878' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9d0422e5647ceea60b43cc123b8adb6d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9d0422e5647ceea60b43cc123b8adb6d.positions ) {
gmap\_m9d0422e5647ceea60b43cc123b8adb6d.bounds.extend( gmap\_m9d0422e5647ceea60b43cc123b8adb6d.positions[m] );
}
// Render markers
for ( var m in gmap\_m9d0422e5647ceea60b43cc123b8adb6d.positions ) {
gmap\_m9d0422e5647ceea60b43cc123b8adb6d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9d0422e5647ceea60b43cc123b8adb6d.map,
position : gmap\_m9d0422e5647ceea60b43cc123b8adb6d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9d0422e5647ceea60b43cc123b8adb6d.map.setCenter( gmap\_m9d0422e5647ceea60b43cc123b8adb6d.positions[602] );
});