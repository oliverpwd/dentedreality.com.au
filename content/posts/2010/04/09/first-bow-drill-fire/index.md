---
title: First Bow Drill Fire
date: '2010-04-09T09:13:44+00:00'
format: image
service: flickr
tags:
- bowdrill
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515823049_387cf5fe01_o.jpg?resize=607%2C455
---

[![First Bow Drill Fire](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515823049_387cf5fe01_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/first-bow-drill-fire/) 
# [First Bow Drill Fire](http://dentedreality.com.au/2010/04/09/first-bow-drill-fire/)

This was taken right after I got my first fire from a Bow Drill.





* #[bowdrill](http://dentedreality.com.au/tags/bowdrill/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515823049/) [9:13 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/first-bow-drill-fire/ "9:13 am") 
jQuery(document).ready(function(){
var gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e = {
positions : {
583 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.positions ) {
gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.bounds.extend( gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.positions[m] );
}
// Render markers
for ( var m in gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.positions ) {
gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.map,
position : gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.map.setCenter( gmap\_m7dedaa2ea0981afaed2a85b233f3ee1e.positions[583] );
});