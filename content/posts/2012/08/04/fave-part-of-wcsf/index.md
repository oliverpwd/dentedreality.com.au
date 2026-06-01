---
title: ''
date: '2012-08-04T15:20:04+00:00'
format: image
service: instagram
tags:
- photo
- wcsf
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/6523dcc4de6911e19d0322000a1d02f2_7.jpg?resize=607%2C607
---

[![Fave part of #wcsf?](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/6523dcc4de6911e19d0322000a1d02f2_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/04/fave-part-of-wcsf/) 

Fave part of #wcsf?





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)

Posted on [Instagram](http://instagram.com/p/N6uzbgimBu/) [3:20 pm, August 4, 2012](http://dentedreality.com.au/2012/08/04/fave-part-of-wcsf/ "3:20 pm") 
jQuery(document).ready(function(){
var gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000 = {
positions : {
69 : new google.maps.LatLng( '37.767941464', '-122.392834425' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.positions ) {
gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.bounds.extend( gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.positions ) {
gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.map,
position : gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.map.setCenter( gmap\_ma8e1bbd57e0ef3a3422ea9b5f77d3000.positions[69] );
});