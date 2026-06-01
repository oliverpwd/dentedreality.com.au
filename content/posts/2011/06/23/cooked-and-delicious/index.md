---
title: ''
date: '2011-06-23T23:20:22+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/222a6948076e43bea5e8cfa11e44a98c_7.jpg?resize=607%2C607
---

[![Cooked and delicious](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/222a6948076e43bea5e8cfa11e44a98c_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/06/23/cooked-and-delicious/) 

Cooked and delicious





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/GRJ27/) [11:20 pm, June 23, 2011](http://dentedreality.com.au/2011/06/23/cooked-and-delicious/ "11:20 pm") 
jQuery(document).ready(function(){
var gmap\_m146e090175ddfefbd6666892749be339 = {
positions : {
696 : new google.maps.LatLng( '37.73588', '-122.4337' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m146e090175ddfefbd6666892749be339' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m146e090175ddfefbd6666892749be339.positions ) {
gmap\_m146e090175ddfefbd6666892749be339.bounds.extend( gmap\_m146e090175ddfefbd6666892749be339.positions[m] );
}
// Render markers
for ( var m in gmap\_m146e090175ddfefbd6666892749be339.positions ) {
gmap\_m146e090175ddfefbd6666892749be339.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m146e090175ddfefbd6666892749be339.map,
position : gmap\_m146e090175ddfefbd6666892749be339.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m146e090175ddfefbd6666892749be339.map.setCenter( gmap\_m146e090175ddfefbd6666892749be339.positions[696] );
});