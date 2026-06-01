---
title: ''
date: '2013-10-06T21:42:31+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/bb7ca8382ef111e3b2a722000aaa0952_8.jpg?resize=640%2C640
---

[![Pooh](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/bb7ca8382ef111e3b2a722000aaa0952_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/10/06/pooh/) 

Pooh





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/fJezF4imBL/) [9:42 pm, October 6, 2013](http://dentedreality.com.au/2013/10/06/pooh/ "9:42 pm") 
jQuery(document).ready(function(){
var gmap\_m9dbdfec2a2eb0769d4e71e7db63de159 = {
positions : {
465 : new google.maps.LatLng( '37.758', '-122.418833333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9dbdfec2a2eb0769d4e71e7db63de159' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.positions ) {
gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.bounds.extend( gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.positions[m] );
}
// Render markers
for ( var m in gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.positions ) {
gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.map,
position : gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.map.setCenter( gmap\_m9dbdfec2a2eb0769d4e71e7db63de159.positions[465] );
});