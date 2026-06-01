---
title: Frankenthumb
date: '2014-01-13T08:42:12+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924805525_9dcdd04677_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924805525_9dcdd04677_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/13/frankenthumb-12/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/13/frankenthumb-12/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924805525/) [8:42 am, January 13, 2014](http://dentedreality.com.au/2014/01/13/frankenthumb-12/ "8:42 am") 
jQuery(document).ready(function(){
var gmap\_m7bd2f4abd62f1363425f93cffca410ae = {
positions : {
262 : new google.maps.LatLng( '40.6949', '-73.987428' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7bd2f4abd62f1363425f93cffca410ae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7bd2f4abd62f1363425f93cffca410ae.positions ) {
gmap\_m7bd2f4abd62f1363425f93cffca410ae.bounds.extend( gmap\_m7bd2f4abd62f1363425f93cffca410ae.positions[m] );
}
// Render markers
for ( var m in gmap\_m7bd2f4abd62f1363425f93cffca410ae.positions ) {
gmap\_m7bd2f4abd62f1363425f93cffca410ae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7bd2f4abd62f1363425f93cffca410ae.map,
position : gmap\_m7bd2f4abd62f1363425f93cffca410ae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7bd2f4abd62f1363425f93cffca410ae.map.setCenter( gmap\_m7bd2f4abd62f1363425f93cffca410ae.positions[262] );
});