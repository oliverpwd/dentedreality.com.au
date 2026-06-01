---
title: Guts
date: '2013-12-29T05:54:16+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901125001_2d5dff30f3_o.jpg?fit=1500%2C1500
---

[![Guts](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901125001_2d5dff30f3_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/29/guts/) 
# [Guts](http://dentedreality.com.au/2013/12/29/guts/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901125001/) [5:54 am, December 29, 2013](http://dentedreality.com.au/2013/12/29/guts/ "5:54 am") 
jQuery(document).ready(function(){
var gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b = {
positions : {
52 : new google.maps.LatLng( '19.409522', '-70.641303' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.positions ) {
gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.bounds.extend( gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.positions[m] );
}
// Render markers
for ( var m in gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.positions ) {
gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.map,
position : gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.map.setCenter( gmap\_m6d8b25f0f50a579fc7a39ed27b61e31b.positions[52] );
});