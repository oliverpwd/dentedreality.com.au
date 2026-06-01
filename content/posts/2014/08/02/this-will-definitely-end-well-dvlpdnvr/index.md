---
title: ''
date: '2014-08-02T17:39:25+00:00'
format: image
service: instagram
tags:
- dvlpdnvr
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/915689_333329353459103_1347373419_n.jpg?resize=640%2C640
---

[![This will definitely end well. #dvlpdnvr](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/915689_333329353459103_1347373419_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/08/02/this-will-definitely-end-well-dvlpdnvr/) 

This will definitely end well. #dvlpdnvr





* #[dvlpdnvr](http://dentedreality.com.au/tags/dvlpdnvr/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/rNoUb3imOs/) [5:39 pm, August 2, 2014](http://dentedreality.com.au/2014/08/02/this-will-definitely-end-well-dvlpdnvr/ "5:39 pm") 
jQuery(document).ready(function(){
var gmap\_m29626dd12141e46f063a1920cbb8b463 = {
positions : {
569 : new google.maps.LatLng( '39.733684146', '-104.992721656' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m29626dd12141e46f063a1920cbb8b463' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m29626dd12141e46f063a1920cbb8b463.positions ) {
gmap\_m29626dd12141e46f063a1920cbb8b463.bounds.extend( gmap\_m29626dd12141e46f063a1920cbb8b463.positions[m] );
}
// Render markers
for ( var m in gmap\_m29626dd12141e46f063a1920cbb8b463.positions ) {
gmap\_m29626dd12141e46f063a1920cbb8b463.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m29626dd12141e46f063a1920cbb8b463.map,
position : gmap\_m29626dd12141e46f063a1920cbb8b463.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m29626dd12141e46f063a1920cbb8b463.map.setCenter( gmap\_m29626dd12141e46f063a1920cbb8b463.positions[569] );
});