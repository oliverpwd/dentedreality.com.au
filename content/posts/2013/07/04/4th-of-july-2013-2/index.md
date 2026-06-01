---
title: 4th of July, 2013
date: '2013-07-04T17:57:10+00:00'
format: image
service: flickr
tags:
- '20130704'
- 4thofjuly
- fireworks
- sparklers
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9439840542_c5caa4b1a0_o.jpg?resize=607%2C452
---

[![4th of July, 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9439840542_c5caa4b1a0_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-2/) 
# [4th of July, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-2/)





* #[20130704](http://dentedreality.com.au/tags/20130704/)
* #[4thofjuly](http://dentedreality.com.au/tags/4thofjuly/)
* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[sparklers](http://dentedreality.com.au/tags/sparklers/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439840542/) [5:57 pm, July 4, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-2/ "5:57 pm") 
jQuery(document).ready(function(){
var gmap\_mccbb7c247a63d72829d50c0623516711 = {
positions : {
134 : new google.maps.LatLng( '40.716666', '-73.945834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mccbb7c247a63d72829d50c0623516711' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mccbb7c247a63d72829d50c0623516711.positions ) {
gmap\_mccbb7c247a63d72829d50c0623516711.bounds.extend( gmap\_mccbb7c247a63d72829d50c0623516711.positions[m] );
}
// Render markers
for ( var m in gmap\_mccbb7c247a63d72829d50c0623516711.positions ) {
gmap\_mccbb7c247a63d72829d50c0623516711.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mccbb7c247a63d72829d50c0623516711.map,
position : gmap\_mccbb7c247a63d72829d50c0623516711.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mccbb7c247a63d72829d50c0623516711.map.setCenter( gmap\_mccbb7c247a63d72829d50c0623516711.positions[134] );
});