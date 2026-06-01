---
title: Invisible Bridge
date: '2010-12-09T06:02:49+00:00'
format: image
service: flickr
tags:
- bridge
- fog
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434640484_d2d97be14d_o.jpg?resize=607%2C452
---

[![Invisible Bridge](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434640484_d2d97be14d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/09/invisible-bridge/) 
# [Invisible Bridge](http://dentedreality.com.au/2010/12/09/invisible-bridge/)





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[fog](http://dentedreality.com.au/tags/fog/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434640484/) [6:02 am, December 9, 2010](http://dentedreality.com.au/2010/12/09/invisible-bridge/ "6:02 am") 
jQuery(document).ready(function(){
var gmap\_mb4547c726ad84f7f860dbc8633372855 = {
positions : {
38 : new google.maps.LatLng( '37.783833', '-122.388' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb4547c726ad84f7f860dbc8633372855' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb4547c726ad84f7f860dbc8633372855.positions ) {
gmap\_mb4547c726ad84f7f860dbc8633372855.bounds.extend( gmap\_mb4547c726ad84f7f860dbc8633372855.positions[m] );
}
// Render markers
for ( var m in gmap\_mb4547c726ad84f7f860dbc8633372855.positions ) {
gmap\_mb4547c726ad84f7f860dbc8633372855.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb4547c726ad84f7f860dbc8633372855.map,
position : gmap\_mb4547c726ad84f7f860dbc8633372855.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb4547c726ad84f7f860dbc8633372855.map.setCenter( gmap\_mb4547c726ad84f7f860dbc8633372855.positions[38] );
});