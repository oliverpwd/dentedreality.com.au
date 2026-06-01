---
title: ''
date: '2018-12-01T16:41:31-06:00'
format: image
service: instagram
tags:
- Denver
- drone
- mavicair
- skyline
- sunset
latitude: '39.7391'
longitude: '-104.9836'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14182037/46313029_208570836699636_913984668807625455_n.jpg?resize=607%2C455&ssl=1
---

[![Downtown Denver Sunset. Taken from Five Points with a @djiglobal Mavic Air #drone #mavicair #denver #sunset #skyline](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14182037/46313029_208570836699636_913984668807625455_n.jpg?resize=607%2C455&ssl=1)](https://dentedreality.com.au/2018/12/01/downtown-denver-sunset-taken-from-five-points-with-a-djiglobal-mavic-air-drone-mavicair-denver-sunset-skyline/) 

[![Downtown Denver Sunset. Taken from Five Points with a @djiglobal Mavic Air #drone #mavicair #denver #sunset #skyline](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14182037/46313029_208570836699636_913984668807625455_n.jpg?resize=607%2C455&ssl=1)](https://www.instagram.com/p/Bq3Q_kLgyCy/)

Downtown Denver Sunset. Taken from Five Points with a @djiglobal Mavic Air #drone #mavicair #denver #sunset #skyline

39.7391-104.9836




* #[Denver](https://dentedreality.com.au/tags/denver/)
* #[drone](https://dentedreality.com.au/tags/drone/)
* #[mavicair](https://dentedreality.com.au/tags/mavicair/)
* #[skyline](https://dentedreality.com.au/tags/skyline/)
* #[sunset](https://dentedreality.com.au/tags/sunset/)

Posted on [Instagram](https://www.instagram.com/p/Bq3Q_kLgyCy/) [4:41 pm, December 1, 2018](https://dentedreality.com.au/2018/12/01/downtown-denver-sunset-taken-from-five-points-with-a-djiglobal-mavic-air-drone-mavicair-denver-sunset-skyline/ "4:41 pm") 
jQuery(document).ready(function(){
var gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b = {
positions : {
411 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.positions ) {
gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.bounds.extend( gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.positions[m] );
}
// Render markers
for ( var m in gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.positions ) {
gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.map,
position : gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.map.setCenter( gmap\_m2b4e0f6dfbb0b6e0763d78d6dacf141b.positions[411] );
});