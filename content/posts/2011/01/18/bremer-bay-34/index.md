---
title: Bremer Bay
date: '2011-01-18T05:41:36+00:00'
format: image
service: flickr
tags:
- australia
- beach
- bremerbay
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434115737_7d05089fc2_o.jpg?resize=607%2C452
---

[![Bremer Bay](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434115737_7d05089fc2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/18/bremer-bay-34/) 
# [Bremer Bay](http://dentedreality.com.au/2011/01/18/bremer-bay-34/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[bremerbay](http://dentedreality.com.au/tags/bremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434115737/) [5:41 am, January 18, 2011](http://dentedreality.com.au/2011/01/18/bremer-bay-34/ "5:41 am") 
jQuery(document).ready(function(){
var gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d = {
positions : {
153 : new google.maps.LatLng( '-33.9205', '118.032666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.positions ) {
gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.bounds.extend( gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.positions[m] );
}
// Render markers
for ( var m in gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.positions ) {
gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.map,
position : gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.map.setCenter( gmap\_m779d6e7a7b6a5c063dc0da4fd38eaa6d.positions[153] );
});