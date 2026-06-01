---
title: ''
date: '2015-04-18T20:10:04+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/04/11084977_384734301709660_1244277584_n.jpg?resize=640%2C640
---

[![Team Mercury Guac-Off](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/04/11084977_384734301709660_1244277584_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/04/18/team-mercury-guac-off/) 

Team Mercury Guac-Off





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/1o6T-zCmI2/) [8:10 pm, April 18, 2015](http://dentedreality.com.au/2015/04/18/team-mercury-guac-off/ "8:10 pm") 
jQuery(document).ready(function(){
var gmap\_m7eaa148c391c98f759e77bcb232e9efb = {
positions : {
475 : new google.maps.LatLng( '32.848786667', '-117.261986667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7eaa148c391c98f759e77bcb232e9efb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7eaa148c391c98f759e77bcb232e9efb.positions ) {
gmap\_m7eaa148c391c98f759e77bcb232e9efb.bounds.extend( gmap\_m7eaa148c391c98f759e77bcb232e9efb.positions[m] );
}
// Render markers
for ( var m in gmap\_m7eaa148c391c98f759e77bcb232e9efb.positions ) {
gmap\_m7eaa148c391c98f759e77bcb232e9efb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7eaa148c391c98f759e77bcb232e9efb.map,
position : gmap\_m7eaa148c391c98f759e77bcb232e9efb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7eaa148c391c98f759e77bcb232e9efb.map.setCenter( gmap\_m7eaa148c391c98f759e77bcb232e9efb.positions[475] );
});