---
title: Frankenthumb
date: '2014-01-05T08:24:00+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901671591_7188407043_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901671591_7188407043_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/05/frankenthumb-23/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/05/frankenthumb-23/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901671591/) [8:24 am, January 5, 2014](http://dentedreality.com.au/2014/01/05/frankenthumb-23/ "8:24 am") 
jQuery(document).ready(function(){
var gmap\_m3f0e66e15dcec0931a50cb6beab540dd = {
positions : {
849 : new google.maps.LatLng( '40.6701', '-73.985595' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3f0e66e15dcec0931a50cb6beab540dd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3f0e66e15dcec0931a50cb6beab540dd.positions ) {
gmap\_m3f0e66e15dcec0931a50cb6beab540dd.bounds.extend( gmap\_m3f0e66e15dcec0931a50cb6beab540dd.positions[m] );
}
// Render markers
for ( var m in gmap\_m3f0e66e15dcec0931a50cb6beab540dd.positions ) {
gmap\_m3f0e66e15dcec0931a50cb6beab540dd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3f0e66e15dcec0931a50cb6beab540dd.map,
position : gmap\_m3f0e66e15dcec0931a50cb6beab540dd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3f0e66e15dcec0931a50cb6beab540dd.map.setCenter( gmap\_m3f0e66e15dcec0931a50cb6beab540dd.positions[849] );
});