---
title: America!
date: '2013-07-06T02:59:40+00:00'
format: image
service: flickr
tags:
- america
- costarica
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437210275_da6b580caf_o.jpg?resize=607%2C452
---

[![America!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437210275_da6b580caf_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/06/america/) 
# [America!](http://dentedreality.com.au/2013/07/06/america/)

Fuck Yeah!





* #[america](http://dentedreality.com.au/tags/america/)
* #[costarica](http://dentedreality.com.au/tags/costarica/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437210275/) [2:59 am, July 6, 2013](http://dentedreality.com.au/2013/07/06/america/ "2:59 am") 
jQuery(document).ready(function(){
var gmap\_m718e7aaadd987139f03bb8904d6111bb = {
positions : {
685 : new google.maps.LatLng( '40.697999', '-74.179167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m718e7aaadd987139f03bb8904d6111bb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m718e7aaadd987139f03bb8904d6111bb.positions ) {
gmap\_m718e7aaadd987139f03bb8904d6111bb.bounds.extend( gmap\_m718e7aaadd987139f03bb8904d6111bb.positions[m] );
}
// Render markers
for ( var m in gmap\_m718e7aaadd987139f03bb8904d6111bb.positions ) {
gmap\_m718e7aaadd987139f03bb8904d6111bb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m718e7aaadd987139f03bb8904d6111bb.map,
position : gmap\_m718e7aaadd987139f03bb8904d6111bb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m718e7aaadd987139f03bb8904d6111bb.map.setCenter( gmap\_m718e7aaadd987139f03bb8904d6111bb.positions[685] );
});