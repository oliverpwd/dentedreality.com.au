---
title: ''
date: '2014-10-10T20:35:25+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/925928_1497487087171518_1023853001_n.jpg?resize=640%2C640
---

[![Posted on Instagram](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/925928_1497487087171518_1023853001_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/10/posted-on-instagram-22/) 




* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/t_uLbnCmOf/) [8:35 pm, October 10, 2014](http://dentedreality.com.au/2014/10/10/posted-on-instagram-22/ "8:35 pm") 
jQuery(document).ready(function(){
var gmap\_m4a3d6c36506ea1ab2a222e1f325851eb = {
positions : {
589 : new google.maps.LatLng( '43.082350232', '-73.784184905' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4a3d6c36506ea1ab2a222e1f325851eb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.positions ) {
gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.bounds.extend( gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.positions[m] );
}
// Render markers
for ( var m in gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.positions ) {
gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.map,
position : gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.map.setCenter( gmap\_m4a3d6c36506ea1ab2a222e1f325851eb.positions[589] );
});