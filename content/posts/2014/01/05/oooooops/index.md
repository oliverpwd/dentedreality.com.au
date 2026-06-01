---
title: ''
date: '2014-01-05T13:57:32+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/28985238763b11e3b0fd12440ac5900d_8.jpg?resize=640%2C640
---

[![Oooooops.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/28985238763b11e3b0fd12440ac5900d_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/05/oooooops/) 

Oooooops.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/izEybmCmPi/) [1:57 pm, January 5, 2014](http://dentedreality.com.au/2014/01/05/oooooops/ "1:57 pm") 
jQuery(document).ready(function(){
var gmap\_m7a750dce2adfcde39b92db52911d01ef = {
positions : {
904 : new google.maps.LatLng( '40.669463333', '-73.984878333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7a750dce2adfcde39b92db52911d01ef' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7a750dce2adfcde39b92db52911d01ef.positions ) {
gmap\_m7a750dce2adfcde39b92db52911d01ef.bounds.extend( gmap\_m7a750dce2adfcde39b92db52911d01ef.positions[m] );
}
// Render markers
for ( var m in gmap\_m7a750dce2adfcde39b92db52911d01ef.positions ) {
gmap\_m7a750dce2adfcde39b92db52911d01ef.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7a750dce2adfcde39b92db52911d01ef.map,
position : gmap\_m7a750dce2adfcde39b92db52911d01ef.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7a750dce2adfcde39b92db52911d01ef.map.setCenter( gmap\_m7a750dce2adfcde39b92db52911d01ef.positions[904] );
});