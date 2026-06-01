---
title: Frankenthumb
date: '2014-01-05T08:13:11+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924849773_fdc63ccd99_o.jpg?resize=607%2C809
---

[![Frankenthumb](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924849773_fdc63ccd99_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/01/05/frankenthumb-26/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/05/frankenthumb-26/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924849773/) [8:13 am, January 5, 2014](http://dentedreality.com.au/2014/01/05/frankenthumb-26/ "8:13 am") 
jQuery(document).ready(function(){
var gmap\_m63799db1a0bb0cd9203ac08b0f132e17 = {
positions : {
557 : new google.maps.LatLng( '40.670147', '-73.985564' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m63799db1a0bb0cd9203ac08b0f132e17' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m63799db1a0bb0cd9203ac08b0f132e17.positions ) {
gmap\_m63799db1a0bb0cd9203ac08b0f132e17.bounds.extend( gmap\_m63799db1a0bb0cd9203ac08b0f132e17.positions[m] );
}
// Render markers
for ( var m in gmap\_m63799db1a0bb0cd9203ac08b0f132e17.positions ) {
gmap\_m63799db1a0bb0cd9203ac08b0f132e17.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m63799db1a0bb0cd9203ac08b0f132e17.map,
position : gmap\_m63799db1a0bb0cd9203ac08b0f132e17.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m63799db1a0bb0cd9203ac08b0f132e17.map.setCenter( gmap\_m63799db1a0bb0cd9203ac08b0f132e17.positions[557] );
});