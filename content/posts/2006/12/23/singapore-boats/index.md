---
title: Singapore Boats
date: '2006-12-23T17:30:33+00:00'
format: image
service: flickr
tags:
- boats
- river
- singapore
- thailand06
---

[![Singapore Boats](http://i0.wp.com/farm1.staticflickr.com/136/348117942_2a2591b3f3_o.jpg?w=607)](http://dentedreality.com.au/2006/12/23/singapore-boats/) 
# [Singapore Boats](http://dentedreality.com.au/2006/12/23/singapore-boats/)





* #[boats](http://dentedreality.com.au/tags/boats/)
* #[river](http://dentedreality.com.au/tags/river/)
* #[singapore](http://dentedreality.com.au/tags/singapore/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348117942/) [5:30 pm, December 23, 2006](http://dentedreality.com.au/2006/12/23/singapore-boats/ "5:30 pm") 
jQuery(document).ready(function(){
var gmap\_m35e6957087b86bdb98372dff6b204c7c = {
positions : {
852 : new google.maps.LatLng( '1.300394', '103.873157' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m35e6957087b86bdb98372dff6b204c7c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m35e6957087b86bdb98372dff6b204c7c.positions ) {
gmap\_m35e6957087b86bdb98372dff6b204c7c.bounds.extend( gmap\_m35e6957087b86bdb98372dff6b204c7c.positions[m] );
}
// Render markers
for ( var m in gmap\_m35e6957087b86bdb98372dff6b204c7c.positions ) {
gmap\_m35e6957087b86bdb98372dff6b204c7c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m35e6957087b86bdb98372dff6b204c7c.map,
position : gmap\_m35e6957087b86bdb98372dff6b204c7c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m35e6957087b86bdb98372dff6b204c7c.map.setCenter( gmap\_m35e6957087b86bdb98372dff6b204c7c.positions[852] );
});