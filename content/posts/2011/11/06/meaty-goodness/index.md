---
title: ''
date: '2011-11-06T14:08:09+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/48b4ed3c08a211e1a87612313804ec91_7.jpg?resize=607%2C607
---

[![Meaty Goodness](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/48b4ed3c08a211e1a87612313804ec91_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/11/06/meaty-goodness/) 

Meaty Goodness





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/TBmnm/) [2:08 pm, November 6, 2011](http://dentedreality.com.au/2011/11/06/meaty-goodness/ "2:08 pm") 
jQuery(document).ready(function(){
var gmap\_me528b6f54b4e221bc28cdba582321333 = {
positions : {
82 : new google.maps.LatLng( '34.05267', '-118.2525' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me528b6f54b4e221bc28cdba582321333' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me528b6f54b4e221bc28cdba582321333.positions ) {
gmap\_me528b6f54b4e221bc28cdba582321333.bounds.extend( gmap\_me528b6f54b4e221bc28cdba582321333.positions[m] );
}
// Render markers
for ( var m in gmap\_me528b6f54b4e221bc28cdba582321333.positions ) {
gmap\_me528b6f54b4e221bc28cdba582321333.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me528b6f54b4e221bc28cdba582321333.map,
position : gmap\_me528b6f54b4e221bc28cdba582321333.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me528b6f54b4e221bc28cdba582321333.map.setCenter( gmap\_me528b6f54b4e221bc28cdba582321333.positions[82] );
});