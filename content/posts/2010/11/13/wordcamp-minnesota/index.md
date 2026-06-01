---
title: WordCamp Minnesota
date: '2010-11-13T05:26:20+00:00'
format: image
service: flickr
tags:
- minnesota
- wcmsp
- wordcamp
- wordcampmsp
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183209161_26190e4dbc_o.jpg?resize=607%2C452
---

[![WordCamp Minnesota](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183209161_26190e4dbc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/13/wordcamp-minnesota/) 
# [WordCamp Minnesota](http://dentedreality.com.au/2010/11/13/wordcamp-minnesota/)





* #[minnesota](http://dentedreality.com.au/tags/minnesota/)
* #[wcmsp](http://dentedreality.com.au/tags/wcmsp/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampmsp](http://dentedreality.com.au/tags/wordcampmsp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183209161/) [5:26 am, November 13, 2010](http://dentedreality.com.au/2010/11/13/wordcamp-minnesota/ "5:26 am") 
jQuery(document).ready(function(){
var gmap\_me6a1546781493041887a8b20ca7eb330 = {
positions : {
924 : new google.maps.LatLng( '44.8635', '-93.304834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me6a1546781493041887a8b20ca7eb330' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me6a1546781493041887a8b20ca7eb330.positions ) {
gmap\_me6a1546781493041887a8b20ca7eb330.bounds.extend( gmap\_me6a1546781493041887a8b20ca7eb330.positions[m] );
}
// Render markers
for ( var m in gmap\_me6a1546781493041887a8b20ca7eb330.positions ) {
gmap\_me6a1546781493041887a8b20ca7eb330.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me6a1546781493041887a8b20ca7eb330.map,
position : gmap\_me6a1546781493041887a8b20ca7eb330.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me6a1546781493041887a8b20ca7eb330.map.setCenter( gmap\_me6a1546781493041887a8b20ca7eb330.positions[924] );
});