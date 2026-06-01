---
title: My House
date: '2011-01-13T09:51:10+00:00'
format: image
service: flickr
tags:
- ellenbrook
- house
- property
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434110999_0c3c07d862_o.jpg?resize=607%2C452
---

[![My House](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434110999_0c3c07d862_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/13/my-house/) 
# [My House](http://dentedreality.com.au/2011/01/13/my-house/)





* #[ellenbrook](http://dentedreality.com.au/tags/ellenbrook/)
* #[house](http://dentedreality.com.au/tags/house/)
* #[property](http://dentedreality.com.au/tags/property/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434110999/) [9:51 am, January 13, 2011](http://dentedreality.com.au/2011/01/13/my-house/ "9:51 am") 
jQuery(document).ready(function(){
var gmap\_m2431a4c362697c0129e1b8113c0c2d2c = {
positions : {
621 : new google.maps.LatLng( '-31.775167', '115.968666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2431a4c362697c0129e1b8113c0c2d2c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2431a4c362697c0129e1b8113c0c2d2c.positions ) {
gmap\_m2431a4c362697c0129e1b8113c0c2d2c.bounds.extend( gmap\_m2431a4c362697c0129e1b8113c0c2d2c.positions[m] );
}
// Render markers
for ( var m in gmap\_m2431a4c362697c0129e1b8113c0c2d2c.positions ) {
gmap\_m2431a4c362697c0129e1b8113c0c2d2c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2431a4c362697c0129e1b8113c0c2d2c.map,
position : gmap\_m2431a4c362697c0129e1b8113c0c2d2c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2431a4c362697c0129e1b8113c0c2d2c.map.setCenter( gmap\_m2431a4c362697c0129e1b8113c0c2d2c.positions[621] );
});