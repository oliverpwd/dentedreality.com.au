---
title: ''
date: '2014-12-22T20:10:51+00:00'
format: image
tags:
- photo
- selfiestick
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10860096_732813133469276_634091896_n.jpg?resize=640%2C640
---

[![#selfiestick](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10860096_732813133469276_634091896_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/22/selfiestick/) 

#selfiestick





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[selfiestick](http://dentedreality.com.au/tags/selfiestick/)

Posted on [Instagram](http://instagram.com/p/w7wQx5CmKZ/) [8:10 pm, December 22, 2014](http://dentedreality.com.au/2014/12/22/selfiestick/ "8:10 pm") 
jQuery(document).ready(function(){
var gmap\_m3f510d140dfb1060ff60fc27747ed1cd = {
positions : {
281 : new google.maps.LatLng( '39.732238333', '-105.005088883' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3f510d140dfb1060ff60fc27747ed1cd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3f510d140dfb1060ff60fc27747ed1cd.positions ) {
gmap\_m3f510d140dfb1060ff60fc27747ed1cd.bounds.extend( gmap\_m3f510d140dfb1060ff60fc27747ed1cd.positions[m] );
}
// Render markers
for ( var m in gmap\_m3f510d140dfb1060ff60fc27747ed1cd.positions ) {
gmap\_m3f510d140dfb1060ff60fc27747ed1cd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3f510d140dfb1060ff60fc27747ed1cd.map,
position : gmap\_m3f510d140dfb1060ff60fc27747ed1cd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3f510d140dfb1060ff60fc27747ed1cd.map.setCenter( gmap\_m3f510d140dfb1060ff60fc27747ed1cd.positions[281] );
});