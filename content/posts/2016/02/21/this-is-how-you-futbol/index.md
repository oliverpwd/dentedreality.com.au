---
title: ''
date: '2016-02-21T08:10:26+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12749958_155627354821337_150088584_n.jpg?fit=640%2C640
---

[![This is how you futbol.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12749958_155627354821337_150088584_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/02/21/this-is-how-you-futbol/) 

This is how you futbol.





Posted on [Instagram](https://www.instagram.com/p/BCDYdBHCmCG/) [8:10 am, February 21, 2016](http://dentedreality.com.au/2016/02/21/this-is-how-you-futbol/ "8:10 am") 
jQuery(document).ready(function(){
var gmap\_m52548888c32d8db23019f89c41c26ac7 = {
positions : {
914 : new google.maps.LatLng( '-12.067277778', '-77.033722222' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m52548888c32d8db23019f89c41c26ac7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m52548888c32d8db23019f89c41c26ac7.positions ) {
gmap\_m52548888c32d8db23019f89c41c26ac7.bounds.extend( gmap\_m52548888c32d8db23019f89c41c26ac7.positions[m] );
}
// Render markers
for ( var m in gmap\_m52548888c32d8db23019f89c41c26ac7.positions ) {
gmap\_m52548888c32d8db23019f89c41c26ac7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m52548888c32d8db23019f89c41c26ac7.map,
position : gmap\_m52548888c32d8db23019f89c41c26ac7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m52548888c32d8db23019f89c41c26ac7.map.setCenter( gmap\_m52548888c32d8db23019f89c41c26ac7.positions[914] );
});