---
title: Usnea
date: '2010-04-09T10:42:01-06:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
- usnea
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185647/4516464230_b6129ba434_o.jpg
---

[![Usnea](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185647/4516464230_b6129ba434_o.jpg)](https://dentedreality.com.au/2010/04/09/usnea/) 
# [Usnea](https://dentedreality.com.au/2010/04/09/usnea/)

[![Usnea](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185647/4516464230_b6129ba434_o.jpg)](http://www.flickr.com/photos/borkazoid/4516464230/)

As seen during our edible/medicinal plant walk.

37.177141-122.116744




* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)
* #[usnea](https://dentedreality.com.au/tags/usnea/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516464230/) [10:42 am, April 9, 2010](https://dentedreality.com.au/2010/04/09/usnea/ "10:42 am") 
jQuery(document).ready(function(){
var gmap\_mc32a340a408a00f8c6ad95dbe6790f60 = {
positions : {
98 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc32a340a408a00f8c6ad95dbe6790f60' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc32a340a408a00f8c6ad95dbe6790f60.positions ) {
gmap\_mc32a340a408a00f8c6ad95dbe6790f60.bounds.extend( gmap\_mc32a340a408a00f8c6ad95dbe6790f60.positions[m] );
}
// Render markers
for ( var m in gmap\_mc32a340a408a00f8c6ad95dbe6790f60.positions ) {
gmap\_mc32a340a408a00f8c6ad95dbe6790f60.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc32a340a408a00f8c6ad95dbe6790f60.map,
position : gmap\_mc32a340a408a00f8c6ad95dbe6790f60.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc32a340a408a00f8c6ad95dbe6790f60.map.setCenter( gmap\_mc32a340a408a00f8c6ad95dbe6790f60.positions[98] );
});