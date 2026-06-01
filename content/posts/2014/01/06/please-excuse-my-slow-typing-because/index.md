---
title: ''
date: '2014-01-06T09:32:37+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/4ec97f1e76df11e3a1ec12b3b547f831_8.jpg?resize=640%2C640
---

[![Please excuse my slow typing because:](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/4ec97f1e76df11e3a1ec12b3b547f831_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/06/please-excuse-my-slow-typing-because/) 

Please excuse my slow typing because:





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/i1LRClCmAE/) [9:32 am, January 6, 2014](http://dentedreality.com.au/2014/01/06/please-excuse-my-slow-typing-because/ "9:32 am") 
jQuery(document).ready(function(){
var gmap\_m55611dda9ebc8056671ecb0b393e5501 = {
positions : {
718 : new google.maps.LatLng( '40.669897', '-73.985667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m55611dda9ebc8056671ecb0b393e5501' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m55611dda9ebc8056671ecb0b393e5501.positions ) {
gmap\_m55611dda9ebc8056671ecb0b393e5501.bounds.extend( gmap\_m55611dda9ebc8056671ecb0b393e5501.positions[m] );
}
// Render markers
for ( var m in gmap\_m55611dda9ebc8056671ecb0b393e5501.positions ) {
gmap\_m55611dda9ebc8056671ecb0b393e5501.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m55611dda9ebc8056671ecb0b393e5501.map,
position : gmap\_m55611dda9ebc8056671ecb0b393e5501.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m55611dda9ebc8056671ecb0b393e5501.map.setCenter( gmap\_m55611dda9ebc8056671ecb0b393e5501.positions[718] );
});