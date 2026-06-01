---
title: Frankenthumb
date: '2014-01-15T17:52:25+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901702082_e2262300c0_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901702082_e2262300c0_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/15/frankenthumb-10/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/15/frankenthumb-10/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901702082/) [5:52 pm, January 15, 2014](http://dentedreality.com.au/2014/01/15/frankenthumb-10/ "5:52 pm") 
jQuery(document).ready(function(){
var gmap\_m57660453249362141e4d81935f0383f3 = {
positions : {
130 : new google.maps.LatLng( '40.669436', '-73.984948' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m57660453249362141e4d81935f0383f3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m57660453249362141e4d81935f0383f3.positions ) {
gmap\_m57660453249362141e4d81935f0383f3.bounds.extend( gmap\_m57660453249362141e4d81935f0383f3.positions[m] );
}
// Render markers
for ( var m in gmap\_m57660453249362141e4d81935f0383f3.positions ) {
gmap\_m57660453249362141e4d81935f0383f3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m57660453249362141e4d81935f0383f3.map,
position : gmap\_m57660453249362141e4d81935f0383f3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m57660453249362141e4d81935f0383f3.map.setCenter( gmap\_m57660453249362141e4d81935f0383f3.positions[130] );
});