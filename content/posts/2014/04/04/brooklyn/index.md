---
title: ''
date: '2014-04-04T14:22:04+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/63a6666abc2e11e3ae6d0002c9de874c_8.jpg?resize=640%2C640
---

[![Brooklyn](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/63a6666abc2e11e3ae6d0002c9de874c_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/04/brooklyn/) 

Brooklyn





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/mYSWFPimI-/) [2:22 pm, April 4, 2014](http://dentedreality.com.au/2014/04/04/brooklyn/ "2:22 pm") 
jQuery(document).ready(function(){
var gmap\_mb8b256fb39624c9b676c3a51f94e3404 = {
positions : {
997 : new google.maps.LatLng( '40.672', '-73.990471667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb8b256fb39624c9b676c3a51f94e3404' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb8b256fb39624c9b676c3a51f94e3404.positions ) {
gmap\_mb8b256fb39624c9b676c3a51f94e3404.bounds.extend( gmap\_mb8b256fb39624c9b676c3a51f94e3404.positions[m] );
}
// Render markers
for ( var m in gmap\_mb8b256fb39624c9b676c3a51f94e3404.positions ) {
gmap\_mb8b256fb39624c9b676c3a51f94e3404.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb8b256fb39624c9b676c3a51f94e3404.map,
position : gmap\_mb8b256fb39624c9b676c3a51f94e3404.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb8b256fb39624c9b676c3a51f94e3404.map.setCenter( gmap\_mb8b256fb39624c9b676c3a51f94e3404.positions[997] );
});