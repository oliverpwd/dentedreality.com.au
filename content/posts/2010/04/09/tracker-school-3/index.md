---
title: Tracker School
date: '2010-04-09T10:47:45+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- tombrown
- trackerschool
- tracking
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516465172_d8287e48e5_o.jpg?resize=607%2C455
---

[![Tracker School](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516465172_d8287e48e5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/tracker-school-3/) 
# [Tracker School](http://dentedreality.com.au/2010/04/09/tracker-school-3/)

Trying to get a little bit of cover on my head from the sun that was (finally!) out with a vengeance.





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516465172/) [10:47 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/tracker-school-3/ "10:47 am") 
jQuery(document).ready(function(){
var gmap\_m39e9ad14d4585043f039c84eb3617cf5 = {
positions : {
594 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m39e9ad14d4585043f039c84eb3617cf5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m39e9ad14d4585043f039c84eb3617cf5.positions ) {
gmap\_m39e9ad14d4585043f039c84eb3617cf5.bounds.extend( gmap\_m39e9ad14d4585043f039c84eb3617cf5.positions[m] );
}
// Render markers
for ( var m in gmap\_m39e9ad14d4585043f039c84eb3617cf5.positions ) {
gmap\_m39e9ad14d4585043f039c84eb3617cf5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m39e9ad14d4585043f039c84eb3617cf5.map,
position : gmap\_m39e9ad14d4585043f039c84eb3617cf5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m39e9ad14d4585043f039c84eb3617cf5.map.setCenter( gmap\_m39e9ad14d4585043f039c84eb3617cf5.positions[594] );
});