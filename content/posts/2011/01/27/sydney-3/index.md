---
title: Sydney
date: '2011-01-27T08:35:06+00:00'
format: image
service: flickr
tags:
- australia
- sydney
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434807780_7958a2ff5f_o.jpg?resize=607%2C452
---

[![Sydney](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434807780_7958a2ff5f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/27/sydney-3/) 
# [Sydney](http://dentedreality.com.au/2011/01/27/sydney-3/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434807780/) [8:35 am, January 27, 2011](http://dentedreality.com.au/2011/01/27/sydney-3/ "8:35 am") 
jQuery(document).ready(function(){
var gmap\_m3613650587d216661a5a514b481a60b5 = {
positions : {
676 : new google.maps.LatLng( '-33.8585', '151.204999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3613650587d216661a5a514b481a60b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3613650587d216661a5a514b481a60b5.positions ) {
gmap\_m3613650587d216661a5a514b481a60b5.bounds.extend( gmap\_m3613650587d216661a5a514b481a60b5.positions[m] );
}
// Render markers
for ( var m in gmap\_m3613650587d216661a5a514b481a60b5.positions ) {
gmap\_m3613650587d216661a5a514b481a60b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3613650587d216661a5a514b481a60b5.map,
position : gmap\_m3613650587d216661a5a514b481a60b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3613650587d216661a5a514b481a60b5.map.setCenter( gmap\_m3613650587d216661a5a514b481a60b5.positions[676] );
});