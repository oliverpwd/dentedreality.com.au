---
title: Doors
date: '2013-12-05T06:43:52+00:00'
format: image
service: flickr
tags:
- door
- france
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900383656_5fdae424c0_o.jpg?fit=1500%2C1500
---

[![Doors](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900383656_5fdae424c0_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/05/doors-2/) 
# [Doors](http://dentedreality.com.au/2013/12/05/doors-2/)





* #[door](http://dentedreality.com.au/tags/door/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900383656/) [6:43 am, December 5, 2013](http://dentedreality.com.au/2013/12/05/doors-2/ "6:43 am") 
jQuery(document).ready(function(){
var gmap\_md4d8749ada1ec5b406447d3df34ab0a1 = {
positions : {
96 : new google.maps.LatLng( '48.849347', '2.350072' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md4d8749ada1ec5b406447d3df34ab0a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md4d8749ada1ec5b406447d3df34ab0a1.positions ) {
gmap\_md4d8749ada1ec5b406447d3df34ab0a1.bounds.extend( gmap\_md4d8749ada1ec5b406447d3df34ab0a1.positions[m] );
}
// Render markers
for ( var m in gmap\_md4d8749ada1ec5b406447d3df34ab0a1.positions ) {
gmap\_md4d8749ada1ec5b406447d3df34ab0a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md4d8749ada1ec5b406447d3df34ab0a1.map,
position : gmap\_md4d8749ada1ec5b406447d3df34ab0a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md4d8749ada1ec5b406447d3df34ab0a1.map.setCenter( gmap\_md4d8749ada1ec5b406447d3df34ab0a1.positions[96] );
});