---
title: Bundle Method
date: '2011-01-23T07:25:18+00:00'
format: image
service: flickr
tags:
- australia
- bundlemethod
- packing
- shirts
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434805550_e1dfcf080b_o.jpg?resize=607%2C452
---

[![Bundle Method](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434805550_e1dfcf080b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/23/bundle-method/) 
# [Bundle Method](http://dentedreality.com.au/2011/01/23/bundle-method/)

Packing my shirts using the "bundle method", where you wrap them around a core of some sort, rather than folding them





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bundlemethod](http://dentedreality.com.au/tags/bundlemethod/)
* #[packing](http://dentedreality.com.au/tags/packing/)
* #[shirts](http://dentedreality.com.au/tags/shirts/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434805550/) [7:25 am, January 23, 2011](http://dentedreality.com.au/2011/01/23/bundle-method/ "7:25 am") 
jQuery(document).ready(function(){
var gmap\_m25ddff5d4acd994f1beffbe0d63952b5 = {
positions : {
911 : new google.maps.LatLng( '-32.053167', '115.846333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m25ddff5d4acd994f1beffbe0d63952b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m25ddff5d4acd994f1beffbe0d63952b5.positions ) {
gmap\_m25ddff5d4acd994f1beffbe0d63952b5.bounds.extend( gmap\_m25ddff5d4acd994f1beffbe0d63952b5.positions[m] );
}
// Render markers
for ( var m in gmap\_m25ddff5d4acd994f1beffbe0d63952b5.positions ) {
gmap\_m25ddff5d4acd994f1beffbe0d63952b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m25ddff5d4acd994f1beffbe0d63952b5.map,
position : gmap\_m25ddff5d4acd994f1beffbe0d63952b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m25ddff5d4acd994f1beffbe0d63952b5.map.setCenter( gmap\_m25ddff5d4acd994f1beffbe0d63952b5.positions[911] );
});