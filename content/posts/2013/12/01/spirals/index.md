---
title: Spirals
date: '2013-12-01T08:27:22+00:00'
format: image
service: flickr
tags:
- france
- paris
- spiral
- staircase
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900378602_a877606f4a_o.jpg?fit=1500%2C1500
---

[![Spirals](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900378602_a877606f4a_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/spirals/) 
# [Spirals](http://dentedreality.com.au/2013/12/01/spirals/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[spiral](http://dentedreality.com.au/tags/spiral/)
* #[staircase](http://dentedreality.com.au/tags/staircase/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900378602/) [8:27 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/spirals/ "8:27 am") 
jQuery(document).ready(function(){
var gmap\_m3e95dd537c15add907b334814f6f241f = {
positions : {
665 : new google.maps.LatLng( '48.874661', '2.300494' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3e95dd537c15add907b334814f6f241f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3e95dd537c15add907b334814f6f241f.positions ) {
gmap\_m3e95dd537c15add907b334814f6f241f.bounds.extend( gmap\_m3e95dd537c15add907b334814f6f241f.positions[m] );
}
// Render markers
for ( var m in gmap\_m3e95dd537c15add907b334814f6f241f.positions ) {
gmap\_m3e95dd537c15add907b334814f6f241f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3e95dd537c15add907b334814f6f241f.map,
position : gmap\_m3e95dd537c15add907b334814f6f241f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3e95dd537c15add907b334814f6f241f.map.setCenter( gmap\_m3e95dd537c15add907b334814f6f241f.positions[665] );
});