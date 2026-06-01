---
title: ''
date: '2013-12-17T22:54:42+00:00'
format: image
tags:
- beau
- beaulebens
- me
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/1d06c870679811e3b7b512b39c87f905_8.jpg?resize=640%2C640
---

[![Posted on Instagram](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/1d06c870679811e3b7b512b39c87f905_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/12/17/posted-on-instagram-19/) 




* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/iDHKIKimEC/) [10:54 pm, December 17, 2013](http://dentedreality.com.au/2013/12/17/posted-on-instagram-19/ "10:54 pm") 
jQuery(document).ready(function(){
var gmap\_m5281984704d3e4fdbe0f005ec331c812 = {
positions : {
952 : new google.maps.LatLng( '40.72113', '-73.998825' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5281984704d3e4fdbe0f005ec331c812' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5281984704d3e4fdbe0f005ec331c812.positions ) {
gmap\_m5281984704d3e4fdbe0f005ec331c812.bounds.extend( gmap\_m5281984704d3e4fdbe0f005ec331c812.positions[m] );
}
// Render markers
for ( var m in gmap\_m5281984704d3e4fdbe0f005ec331c812.positions ) {
gmap\_m5281984704d3e4fdbe0f005ec331c812.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5281984704d3e4fdbe0f005ec331c812.map,
position : gmap\_m5281984704d3e4fdbe0f005ec331c812.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5281984704d3e4fdbe0f005ec331c812.map.setCenter( gmap\_m5281984704d3e4fdbe0f005ec331c812.positions[952] );
});