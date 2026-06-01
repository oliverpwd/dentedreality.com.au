---
title: Burned Fingers
date: '2010-04-09T12:45:39+00:00'
format: image
service: flickr
tags:
- bowdrill
- burn
- fingers
- tombrown
- trackerschool
- tracking
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516471488_678c162636_o.jpg?resize=607%2C455
---

[![Burned Fingers](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516471488_678c162636_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/burned-fingers/) 
# [Burned Fingers](http://dentedreality.com.au/2010/04/09/burned-fingers/)

Apparently I was handling my tinder bundle/coal a little too much, and slowly roasted my fingers when practicing Bow Drill.





* #[bowdrill](http://dentedreality.com.au/tags/bowdrill/)
* #[burn](http://dentedreality.com.au/tags/burn/)
* #[fingers](http://dentedreality.com.au/tags/fingers/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516471488/) [12:45 pm, April 9, 2010](http://dentedreality.com.au/2010/04/09/burned-fingers/ "12:45 pm") 
jQuery(document).ready(function(){
var gmap\_md781a30cf0d4a30f58aaa4c2dc133806 = {
positions : {
190 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md781a30cf0d4a30f58aaa4c2dc133806' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md781a30cf0d4a30f58aaa4c2dc133806.positions ) {
gmap\_md781a30cf0d4a30f58aaa4c2dc133806.bounds.extend( gmap\_md781a30cf0d4a30f58aaa4c2dc133806.positions[m] );
}
// Render markers
for ( var m in gmap\_md781a30cf0d4a30f58aaa4c2dc133806.positions ) {
gmap\_md781a30cf0d4a30f58aaa4c2dc133806.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md781a30cf0d4a30f58aaa4c2dc133806.map,
position : gmap\_md781a30cf0d4a30f58aaa4c2dc133806.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md781a30cf0d4a30f58aaa4c2dc133806.map.setCenter( gmap\_md781a30cf0d4a30f58aaa4c2dc133806.positions[190] );
});