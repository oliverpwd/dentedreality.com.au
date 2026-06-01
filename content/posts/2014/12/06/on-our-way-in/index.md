---
title: ''
date: '2014-12-06T07:15:39+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10831738_318630314998283_337665467_n.jpg?resize=640%2C640
---

[![On our way in!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10831738_318630314998283_337665467_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/06/on-our-way-in/) 

On our way in!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/wRK0_YimGx/) [7:15 am, December 6, 2014](http://dentedreality.com.au/2014/12/06/on-our-way-in/ "7:15 am") 
jQuery(document).ready(function(){
var gmap\_m2f64f4b6d3fd3e965407748ec8193373 = {
positions : {
939 : new google.maps.LatLng( '39.71227448', '-104.998468099' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2f64f4b6d3fd3e965407748ec8193373' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2f64f4b6d3fd3e965407748ec8193373.positions ) {
gmap\_m2f64f4b6d3fd3e965407748ec8193373.bounds.extend( gmap\_m2f64f4b6d3fd3e965407748ec8193373.positions[m] );
}
// Render markers
for ( var m in gmap\_m2f64f4b6d3fd3e965407748ec8193373.positions ) {
gmap\_m2f64f4b6d3fd3e965407748ec8193373.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2f64f4b6d3fd3e965407748ec8193373.map,
position : gmap\_m2f64f4b6d3fd3e965407748ec8193373.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2f64f4b6d3fd3e965407748ec8193373.map.setCenter( gmap\_m2f64f4b6d3fd3e965407748ec8193373.positions[939] );
});