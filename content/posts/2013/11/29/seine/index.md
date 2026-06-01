---
title: Seine
date: '2013-11-29T14:13:00+00:00'
format: image
service: flickr
tags:
- france
- paris
- seine
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900361476_ca12f10d22_o.jpg?fit=1500%2C1500
---

[![Seine](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900361476_ca12f10d22_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/11/29/seine/) 
# [Seine](http://dentedreality.com.au/2013/11/29/seine/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[seine](http://dentedreality.com.au/tags/seine/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900361476/) [2:13 pm, November 29, 2013](http://dentedreality.com.au/2013/11/29/seine/ "2:13 pm") 
jQuery(document).ready(function(){
var gmap\_m2adf34408e7c541cf8bb32157be54d63 = {
positions : {
306 : new google.maps.LatLng( '48.859694', '2.333363' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2adf34408e7c541cf8bb32157be54d63' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2adf34408e7c541cf8bb32157be54d63.positions ) {
gmap\_m2adf34408e7c541cf8bb32157be54d63.bounds.extend( gmap\_m2adf34408e7c541cf8bb32157be54d63.positions[m] );
}
// Render markers
for ( var m in gmap\_m2adf34408e7c541cf8bb32157be54d63.positions ) {
gmap\_m2adf34408e7c541cf8bb32157be54d63.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2adf34408e7c541cf8bb32157be54d63.map,
position : gmap\_m2adf34408e7c541cf8bb32157be54d63.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2adf34408e7c541cf8bb32157be54d63.map.setCenter( gmap\_m2adf34408e7c541cf8bb32157be54d63.positions[306] );
});