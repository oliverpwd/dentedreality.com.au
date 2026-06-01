---
title: ''
date: '2015-02-27T16:17:38+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/11032855_1551295371818587_944972415_n.jpg?resize=640%2C640
---

[![FYI this is probably the tastiest packet-ramen I've had.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/11032855_1551295371818587_944972415_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/27/fyi-this-is-probably-the-tastiest-packet-ramen-ive-had/) 

FYI this is probably the tastiest packet-ramen I’ve had.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/zn21UjimIl/) [4:17 pm, February 27, 2015](http://dentedreality.com.au/2015/02/27/fyi-this-is-probably-the-tastiest-packet-ramen-ive-had/ "4:17 pm") 
jQuery(document).ready(function(){
var gmap\_m34073c07b4c4223f57804a2c88153420 = {
positions : {
857 : new google.maps.LatLng( '39.73478621', '-104.97856067' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m34073c07b4c4223f57804a2c88153420' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m34073c07b4c4223f57804a2c88153420.positions ) {
gmap\_m34073c07b4c4223f57804a2c88153420.bounds.extend( gmap\_m34073c07b4c4223f57804a2c88153420.positions[m] );
}
// Render markers
for ( var m in gmap\_m34073c07b4c4223f57804a2c88153420.positions ) {
gmap\_m34073c07b4c4223f57804a2c88153420.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m34073c07b4c4223f57804a2c88153420.map,
position : gmap\_m34073c07b4c4223f57804a2c88153420.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m34073c07b4c4223f57804a2c88153420.map.setCenter( gmap\_m34073c07b4c4223f57804a2c88153420.positions[857] );
});