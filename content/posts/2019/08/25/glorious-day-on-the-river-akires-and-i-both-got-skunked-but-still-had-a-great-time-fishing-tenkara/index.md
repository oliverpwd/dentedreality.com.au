---
title: ''
date: '2019-08-25T15:47:02-06:00'
format: image
service: instagram
tags:
- fishing
- Tenkara
latitude: '40.41617'
longitude: '-105.3732'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/25160705/68816657_2410033499220471_8643420029897657555_n.jpg
---

[![Glorious day on the river. @akires and I both got skunked, but still had a great time. #fishing #tenkara](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/25160705/68816657_2410033499220471_8643420029897657555_n.jpg)](https://dentedreality.com.au/2019/08/25/glorious-day-on-the-river-akires-and-i-both-got-skunked-but-still-had-a-great-time-fishing-tenkara/) 

[![Glorious day on the river. @akires and I both got skunked, but still had a great time. #fishing #tenkara](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/25160705/68816657_2410033499220471_8643420029897657555_n.jpg)](https://www.instagram.com/p/B1mkIuqpKvu/)

Glorious day on the river. @akires and I both got skunked, but still had a great time. #fishing #tenkara

40.41617-105.3732




* #[fishing](https://dentedreality.com.au/tags/fishing/)
* #[Tenkara](https://dentedreality.com.au/tags/tenkara/)

Posted on [Instagram](https://www.instagram.com/p/B1mkIuqpKvu/) [3:47 pm, August 25, 2019](https://dentedreality.com.au/2019/08/25/glorious-day-on-the-river-akires-and-i-both-got-skunked-but-still-had-a-great-time-fishing-tenkara/ "3:47 pm") 
jQuery(document).ready(function(){
var gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a = {
positions : {
69 : new google.maps.LatLng( '40.41617', '-105.3732' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.positions ) {
gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.bounds.extend( gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.positions[m] );
}
// Render markers
for ( var m in gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.positions ) {
gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.map,
position : gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.map.setCenter( gmap\_ma882980de5c4305d3a2ab1a3c1ecc66a.positions[69] );
});