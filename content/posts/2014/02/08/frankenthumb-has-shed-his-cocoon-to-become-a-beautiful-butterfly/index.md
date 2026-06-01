---
title: ''
date: '2014-02-08T02:09:52+00:00'
format: image
tags:
- Frankenthumb
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/e59c3b38908f11e3a53e123976fa0e75_8.jpg?resize=640%2C640
---

[![#Frankenthumb has shed his cocoon to become a beautiful butterfly!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/e59c3b38908f11e3a53e123976fa0e75_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/02/08/frankenthumb-has-shed-his-cocoon-to-become-a-beautiful-butterfly/) 

#Frankenthumb has shed his cocoon to become a beautiful butterfly!





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/kJW1G5CmC1/) [2:09 am, February 8, 2014](http://dentedreality.com.au/2014/02/08/frankenthumb-has-shed-his-cocoon-to-become-a-beautiful-butterfly/ "2:09 am") 
jQuery(document).ready(function(){
var gmap\_m4ebc8d8db6207e1d1b41e0a463036948 = {
positions : {
848 : new google.maps.LatLng( '38.955386878', '-77.073314728' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4ebc8d8db6207e1d1b41e0a463036948' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4ebc8d8db6207e1d1b41e0a463036948.positions ) {
gmap\_m4ebc8d8db6207e1d1b41e0a463036948.bounds.extend( gmap\_m4ebc8d8db6207e1d1b41e0a463036948.positions[m] );
}
// Render markers
for ( var m in gmap\_m4ebc8d8db6207e1d1b41e0a463036948.positions ) {
gmap\_m4ebc8d8db6207e1d1b41e0a463036948.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4ebc8d8db6207e1d1b41e0a463036948.map,
position : gmap\_m4ebc8d8db6207e1d1b41e0a463036948.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4ebc8d8db6207e1d1b41e0a463036948.map.setCenter( gmap\_m4ebc8d8db6207e1d1b41e0a463036948.positions[848] );
});