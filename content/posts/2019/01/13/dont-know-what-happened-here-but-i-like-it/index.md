---
title: ''
date: '2019-01-13T19:05:47-06:00'
format: image
service: instagram
latitude: '39.6042'
longitude: '-105.948'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181946/49717543_351970052058032_59061576809427532_n.jpg?resize=607%2C607&ssl=1
---

[![Don't know what happened here, but I like it.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181946/49717543_351970052058032_59061576809427532_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2019/01/13/dont-know-what-happened-here-but-i-like-it/) 

[![Don't know what happened here, but I like it.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181946/49717543_351970052058032_59061576809427532_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BsmPryqAOD-/)

Don’t know what happened here, but I like it.

39.6042-105.948




Posted on [Instagram](https://www.instagram.com/p/BsmPryqAOD-/) [7:05 pm, January 13, 2019](https://dentedreality.com.au/2019/01/13/dont-know-what-happened-here-but-i-like-it/ "7:05 pm") 
jQuery(document).ready(function(){
var gmap\_mada6a3d163f958839af1dbd4c70de581 = {
positions : {
681 : new google.maps.LatLng( '39.6042', '-105.948' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mada6a3d163f958839af1dbd4c70de581' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mada6a3d163f958839af1dbd4c70de581.positions ) {
gmap\_mada6a3d163f958839af1dbd4c70de581.bounds.extend( gmap\_mada6a3d163f958839af1dbd4c70de581.positions[m] );
}
// Render markers
for ( var m in gmap\_mada6a3d163f958839af1dbd4c70de581.positions ) {
gmap\_mada6a3d163f958839af1dbd4c70de581.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mada6a3d163f958839af1dbd4c70de581.map,
position : gmap\_mada6a3d163f958839af1dbd4c70de581.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mada6a3d163f958839af1dbd4c70de581.map.setCenter( gmap\_mada6a3d163f958839af1dbd4c70de581.positions[681] );
});