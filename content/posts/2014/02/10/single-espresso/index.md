---
title: ''
date: '2014-02-10T13:00:25+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/24d0d28e927d11e39bef0e0423ac1ff3_8.jpg?resize=640%2C640
---

[!["Single" espresso!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/24d0d28e927d11e39bef0e0423ac1ff3_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/02/10/single-espresso/) 

“Single” espresso!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/kPq3oyimKL/) [1:00 pm, February 10, 2014](http://dentedreality.com.au/2014/02/10/single-espresso/ "1:00 pm") 
jQuery(document).ready(function(){
var gmap\_m9435ee3eea94639211ec054e1e7a9e29 = {
positions : {
648 : new google.maps.LatLng( '40.675115681', '-73.981261096' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9435ee3eea94639211ec054e1e7a9e29' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9435ee3eea94639211ec054e1e7a9e29.positions ) {
gmap\_m9435ee3eea94639211ec054e1e7a9e29.bounds.extend( gmap\_m9435ee3eea94639211ec054e1e7a9e29.positions[m] );
}
// Render markers
for ( var m in gmap\_m9435ee3eea94639211ec054e1e7a9e29.positions ) {
gmap\_m9435ee3eea94639211ec054e1e7a9e29.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9435ee3eea94639211ec054e1e7a9e29.map,
position : gmap\_m9435ee3eea94639211ec054e1e7a9e29.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9435ee3eea94639211ec054e1e7a9e29.map.setCenter( gmap\_m9435ee3eea94639211ec054e1e7a9e29.positions[648] );
});