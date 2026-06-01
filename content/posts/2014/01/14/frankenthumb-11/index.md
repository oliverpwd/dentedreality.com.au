---
title: Frankenthumb
date: '2014-01-14T15:30:04+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924806615_00e2e33a1c_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924806615_00e2e33a1c_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/14/frankenthumb-11/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/14/frankenthumb-11/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924806615/) [3:30 pm, January 14, 2014](http://dentedreality.com.au/2014/01/14/frankenthumb-11/ "3:30 pm") 
jQuery(document).ready(function(){
var gmap\_m71b8b2bf121ad211c213cb7e804c55f7 = {
positions : {
131 : new google.maps.LatLng( '40.669413', '-73.984956' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m71b8b2bf121ad211c213cb7e804c55f7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m71b8b2bf121ad211c213cb7e804c55f7.positions ) {
gmap\_m71b8b2bf121ad211c213cb7e804c55f7.bounds.extend( gmap\_m71b8b2bf121ad211c213cb7e804c55f7.positions[m] );
}
// Render markers
for ( var m in gmap\_m71b8b2bf121ad211c213cb7e804c55f7.positions ) {
gmap\_m71b8b2bf121ad211c213cb7e804c55f7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m71b8b2bf121ad211c213cb7e804c55f7.map,
position : gmap\_m71b8b2bf121ad211c213cb7e804c55f7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m71b8b2bf121ad211c213cb7e804c55f7.map.setCenter( gmap\_m71b8b2bf121ad211c213cb7e804c55f7.positions[131] );
});