---
title: ''
date: '2014-03-15T05:31:59+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/0979a00aac2d11e3a1b012ac658f7817_8.jpg?resize=640%2C640
---

[![Horrible beach.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/0979a00aac2d11e3a1b012ac658f7817_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/03/15/horrible-beach-2/) 

Horrible beach.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/lj1yH_imKJ/) [5:31 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/horrible-beach-2/ "5:31 am") 
jQuery(document).ready(function(){
var gmap\_m8a4b209f22c1f56a56205b53aed663c2 = {
positions : {
432 : new google.maps.LatLng( '-32.034377833', '115.7455' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8a4b209f22c1f56a56205b53aed663c2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8a4b209f22c1f56a56205b53aed663c2.positions ) {
gmap\_m8a4b209f22c1f56a56205b53aed663c2.bounds.extend( gmap\_m8a4b209f22c1f56a56205b53aed663c2.positions[m] );
}
// Render markers
for ( var m in gmap\_m8a4b209f22c1f56a56205b53aed663c2.positions ) {
gmap\_m8a4b209f22c1f56a56205b53aed663c2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8a4b209f22c1f56a56205b53aed663c2.map,
position : gmap\_m8a4b209f22c1f56a56205b53aed663c2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8a4b209f22c1f56a56205b53aed663c2.map.setCenter( gmap\_m8a4b209f22c1f56a56205b53aed663c2.positions[432] );
});