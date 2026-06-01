---
title: Tracker School
date: '2010-04-09T10:17:17+00:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515827177_104a380ee5_o.jpg?resize=607%2C809
---

[![Tracker School](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515827177_104a380ee5_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2010/04/09/tracker-school-4/) 
# [Tracker School](http://dentedreality.com.au/2010/04/09/tracker-school-4/)

As seen during our edible/medicinal plant walk.





* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515827177/) [10:17 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/tracker-school-4/ "10:17 am") 
jQuery(document).ready(function(){
var gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6 = {
positions : {
876 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.positions ) {
gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.bounds.extend( gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.positions[m] );
}
// Render markers
for ( var m in gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.positions ) {
gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.map,
position : gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.map.setCenter( gmap\_m7e2f2a0cd783ca57b03838de69b4cbe6.positions[876] );
});