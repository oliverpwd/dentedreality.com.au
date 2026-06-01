---
title: ''
date: '2010-10-31T15:09:36+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/84bf5452cc77498d89fbd266b122b74d_7.jpg?resize=607%2C607
---

[![Amazing Brunch](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/84bf5452cc77498d89fbd266b122b74d_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/10/31/amazing-brunch/) 

Amazing Brunch





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/HaoF/) [3:09 pm, October 31, 2010](http://dentedreality.com.au/2010/10/31/amazing-brunch/ "3:09 pm") 
jQuery(document).ready(function(){
var gmap\_md23423e91c1190290e99ec30acdbe5b7 = {
positions : {
695 : new google.maps.LatLng( '37.78827', '-122.423802' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md23423e91c1190290e99ec30acdbe5b7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md23423e91c1190290e99ec30acdbe5b7.positions ) {
gmap\_md23423e91c1190290e99ec30acdbe5b7.bounds.extend( gmap\_md23423e91c1190290e99ec30acdbe5b7.positions[m] );
}
// Render markers
for ( var m in gmap\_md23423e91c1190290e99ec30acdbe5b7.positions ) {
gmap\_md23423e91c1190290e99ec30acdbe5b7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md23423e91c1190290e99ec30acdbe5b7.map,
position : gmap\_md23423e91c1190290e99ec30acdbe5b7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md23423e91c1190290e99ec30acdbe5b7.map.setCenter( gmap\_md23423e91c1190290e99ec30acdbe5b7.positions[695] );
});