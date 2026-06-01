---
title: Skyview
date: '2013-12-05T08:38:41+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923943844_3437e15d5e_o.jpg?fit=1500%2C1500
---

[![Skyview](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923943844_3437e15d5e_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/05/skyview/) 
# [Skyview](http://dentedreality.com.au/2013/12/05/skyview/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923943844/) [8:38 am, December 5, 2013](http://dentedreality.com.au/2013/12/05/skyview/ "8:38 am") 
jQuery(document).ready(function(){
var gmap\_m8f7a0203e4078fccb181623a370990b0 = {
positions : {
83 : new google.maps.LatLng( '48.858861', '2.349561' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8f7a0203e4078fccb181623a370990b0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8f7a0203e4078fccb181623a370990b0.positions ) {
gmap\_m8f7a0203e4078fccb181623a370990b0.bounds.extend( gmap\_m8f7a0203e4078fccb181623a370990b0.positions[m] );
}
// Render markers
for ( var m in gmap\_m8f7a0203e4078fccb181623a370990b0.positions ) {
gmap\_m8f7a0203e4078fccb181623a370990b0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8f7a0203e4078fccb181623a370990b0.map,
position : gmap\_m8f7a0203e4078fccb181623a370990b0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8f7a0203e4078fccb181623a370990b0.map.setCenter( gmap\_m8f7a0203e4078fccb181623a370990b0.positions[83] );
});