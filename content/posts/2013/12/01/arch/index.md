---
title: Arch
date: '2013-12-01T11:03:35+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900361571_64f75c86fc_o.jpg?fit=1500%2C1500
---

[![Arch](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900361571_64f75c86fc_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/arch/) 
# [Arch](http://dentedreality.com.au/2013/12/01/arch/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900361571/) [11:03 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/arch/ "11:03 am") 
jQuery(document).ready(function(){
var gmap\_me4e0d8e59b2f73df71ec9afd6af6778e = {
positions : {
190 : new google.maps.LatLng( '48.861908', '2.332474' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me4e0d8e59b2f73df71ec9afd6af6778e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.positions ) {
gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.bounds.extend( gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.positions[m] );
}
// Render markers
for ( var m in gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.positions ) {
gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.map,
position : gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.map.setCenter( gmap\_me4e0d8e59b2f73df71ec9afd6af6778e.positions[190] );
});