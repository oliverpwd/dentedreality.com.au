---
title: ''
date: '2011-02-26T15:39:35+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/111cd8d3ae7c4b948a2ac77511209bc1_7.jpg?resize=607%2C607
---

[![I got your heart attack right here!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/111cd8d3ae7c4b948a2ac77511209bc1_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/02/26/i-got-your-heart-attack-right-here/) 

I got your heart attack right here!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/B3due/) [3:39 pm, February 26, 2011](http://dentedreality.com.au/2011/02/26/i-got-your-heart-attack-right-here/ "3:39 pm") 
jQuery(document).ready(function(){
var gmap\_med80e7ae6196b0bd72e6b3ccfecffd38 = {
positions : {
306 : new google.maps.LatLng( '40.647726858', '-73.790745735' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_med80e7ae6196b0bd72e6b3ccfecffd38' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.positions ) {
gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.bounds.extend( gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.positions[m] );
}
// Render markers
for ( var m in gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.positions ) {
gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.map,
position : gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.map.setCenter( gmap\_med80e7ae6196b0bd72e6b3ccfecffd38.positions[306] );
});