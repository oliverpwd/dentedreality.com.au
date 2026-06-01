---
title: So Official
date: '2012-05-18T12:31:01+00:00'
format: image
service: flickr
tags:
- noparking
- sign
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/7770797282_a99b51c047_o.jpg?resize=607%2C813
---

[![So Official](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/7770797282_a99b51c047_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/05/18/so-official/) 
# [So Official](http://dentedreality.com.au/2012/05/18/so-official/)





* #[noparking](http://dentedreality.com.au/tags/noparking/)
* #[sign](http://dentedreality.com.au/tags/sign/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770797282/) [12:31 pm, May 18, 2012](http://dentedreality.com.au/2012/05/18/so-official/ "12:31 pm") 
jQuery(document).ready(function(){
var gmap\_med1e91a898b168972bfde49feaf026c7 = {
positions : {
984 : new google.maps.LatLng( '37.791', '-122.418667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_med1e91a898b168972bfde49feaf026c7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_med1e91a898b168972bfde49feaf026c7.positions ) {
gmap\_med1e91a898b168972bfde49feaf026c7.bounds.extend( gmap\_med1e91a898b168972bfde49feaf026c7.positions[m] );
}
// Render markers
for ( var m in gmap\_med1e91a898b168972bfde49feaf026c7.positions ) {
gmap\_med1e91a898b168972bfde49feaf026c7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_med1e91a898b168972bfde49feaf026c7.map,
position : gmap\_med1e91a898b168972bfde49feaf026c7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_med1e91a898b168972bfde49feaf026c7.map.setCenter( gmap\_med1e91a898b168972bfde49feaf026c7.positions[984] );
});