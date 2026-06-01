---
title: Snow in Prospect Park
date: '2014-01-04T09:46:39+00:00'
format: image
service: flickr
tags:
- brooklyn
- newyork
- prospectpark
- snow
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924749325_2ff841a1fb_o.jpg?resize=607%2C455
---

[![Snow in Prospect Park](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924749325_2ff841a1fb_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-3/) 
# [Snow in Prospect Park](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-3/)





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[prospectpark](http://dentedreality.com.au/tags/prospectpark/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924749325/) [9:46 am, January 4, 2014](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-3/ "9:46 am") 
jQuery(document).ready(function(){
var gmap\_m2cead171ba21157b4d508c5ce871f9a5 = {
positions : {
350 : new google.maps.LatLng( '40.668388', '-73.97075' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2cead171ba21157b4d508c5ce871f9a5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2cead171ba21157b4d508c5ce871f9a5.positions ) {
gmap\_m2cead171ba21157b4d508c5ce871f9a5.bounds.extend( gmap\_m2cead171ba21157b4d508c5ce871f9a5.positions[m] );
}
// Render markers
for ( var m in gmap\_m2cead171ba21157b4d508c5ce871f9a5.positions ) {
gmap\_m2cead171ba21157b4d508c5ce871f9a5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2cead171ba21157b4d508c5ce871f9a5.map,
position : gmap\_m2cead171ba21157b4d508c5ce871f9a5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2cead171ba21157b4d508c5ce871f9a5.map.setCenter( gmap\_m2cead171ba21157b4d508c5ce871f9a5.positions[350] );
});