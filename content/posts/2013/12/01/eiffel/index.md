---
title: Eiffel
date: '2013-12-01T09:18:53+00:00'
format: image
service: flickr
tags:
- eiffel
- france
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923928224_e511f16b4e_o.jpg?fit=1500%2C1500
---

[![Eiffel](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923928224_e511f16b4e_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/eiffel/) 
# [Eiffel](http://dentedreality.com.au/2013/12/01/eiffel/)





* #[eiffel](http://dentedreality.com.au/tags/eiffel/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923928224/) [9:18 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/eiffel/ "9:18 am") 
jQuery(document).ready(function(){
var gmap\_m40d1bdc8cdb87ce462effb031e499c07 = {
positions : {
878 : new google.maps.LatLng( '48.857788', '2.295313' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m40d1bdc8cdb87ce462effb031e499c07' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m40d1bdc8cdb87ce462effb031e499c07.positions ) {
gmap\_m40d1bdc8cdb87ce462effb031e499c07.bounds.extend( gmap\_m40d1bdc8cdb87ce462effb031e499c07.positions[m] );
}
// Render markers
for ( var m in gmap\_m40d1bdc8cdb87ce462effb031e499c07.positions ) {
gmap\_m40d1bdc8cdb87ce462effb031e499c07.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m40d1bdc8cdb87ce462effb031e499c07.map,
position : gmap\_m40d1bdc8cdb87ce462effb031e499c07.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m40d1bdc8cdb87ce462effb031e499c07.map.setCenter( gmap\_m40d1bdc8cdb87ce462effb031e499c07.positions[878] );
});