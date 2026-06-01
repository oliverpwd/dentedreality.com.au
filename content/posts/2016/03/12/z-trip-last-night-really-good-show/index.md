---
title: ''
date: '2016-03-12T11:22:03+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/925198_1579790625678099_366504864_n.jpg?fit=640%2C640
---

[![Z-Trip, last night. Really good show!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/925198_1579790625678099_366504864_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/03/12/z-trip-last-night-really-good-show/) 

Z-Trip, last night. Really good show!





Posted on [Instagram](https://www.instagram.com/p/BC3OR-kimBv/) [11:22 am, March 12, 2016](http://dentedreality.com.au/2016/03/12/z-trip-last-night-really-good-show/ "11:22 am") 
jQuery(document).ready(function(){
var gmap\_m12061f093253129bb91a5776bfcf2487 = {
positions : {
333 : new google.maps.LatLng( '39.754371122', '-104.978786362' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m12061f093253129bb91a5776bfcf2487' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m12061f093253129bb91a5776bfcf2487.positions ) {
gmap\_m12061f093253129bb91a5776bfcf2487.bounds.extend( gmap\_m12061f093253129bb91a5776bfcf2487.positions[m] );
}
// Render markers
for ( var m in gmap\_m12061f093253129bb91a5776bfcf2487.positions ) {
gmap\_m12061f093253129bb91a5776bfcf2487.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m12061f093253129bb91a5776bfcf2487.map,
position : gmap\_m12061f093253129bb91a5776bfcf2487.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m12061f093253129bb91a5776bfcf2487.map.setCenter( gmap\_m12061f093253129bb91a5776bfcf2487.positions[333] );
});