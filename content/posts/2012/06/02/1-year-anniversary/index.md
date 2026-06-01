---
title: 1 year Anniversary
date: '2012-06-02T17:22:19+00:00'
format: image
service: flickr
tags:
- anniversary
- erika
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7770964618_96d7a64a85_o.jpg?resize=607%2C813
---

[![1 year Anniversary](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7770964618_96d7a64a85_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/06/02/1-year-anniversary/) 
# [1 year Anniversary](http://dentedreality.com.au/2012/06/02/1-year-anniversary/)





* #[anniversary](http://dentedreality.com.au/tags/anniversary/)
* #[erika](http://dentedreality.com.au/tags/erika/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770964618/) [5:22 pm, June 2, 2012](http://dentedreality.com.au/2012/06/02/1-year-anniversary/ "5:22 pm") 
jQuery(document).ready(function(){
var gmap\_md887e98b2af3d09d2918e1b9eefdf5c2 = {
positions : {
174 : new google.maps.LatLng( '37.773333', '-122.421334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md887e98b2af3d09d2918e1b9eefdf5c2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.positions ) {
gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.bounds.extend( gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.positions[m] );
}
// Render markers
for ( var m in gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.positions ) {
gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.map,
position : gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.map.setCenter( gmap\_md887e98b2af3d09d2918e1b9eefdf5c2.positions[174] );
});