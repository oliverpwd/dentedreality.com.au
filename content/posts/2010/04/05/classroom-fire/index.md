---
title: Classroom Fire!
date: '2010-04-05T08:30:07-06:00'
format: image
service: flickr
tags:
- fire
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185627/4515799419_f2fa49b7e9_o.jpg
---

[![Classroom Fire!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185627/4515799419_f2fa49b7e9_o.jpg)](https://dentedreality.com.au/2010/04/05/classroom-fire/) 
# [Classroom Fire!](https://dentedreality.com.au/2010/04/05/classroom-fire/)

[![Classroom Fire!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185627/4515799419_f2fa49b7e9_o.jpg)](http://www.flickr.com/photos/borkazoid/4515799419/)

During demonstration of the Bow Drill.

37.177141-122.116744




* #[fire](https://dentedreality.com.au/tags/fire/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515799419/) [8:30 am, April 5, 2010](https://dentedreality.com.au/2010/04/05/classroom-fire/ "8:30 am") 
jQuery(document).ready(function(){
var gmap\_m415d4e168ddd84f77cd6cc781e86c149 = {
positions : {
66 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m415d4e168ddd84f77cd6cc781e86c149' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m415d4e168ddd84f77cd6cc781e86c149.positions ) {
gmap\_m415d4e168ddd84f77cd6cc781e86c149.bounds.extend( gmap\_m415d4e168ddd84f77cd6cc781e86c149.positions[m] );
}
// Render markers
for ( var m in gmap\_m415d4e168ddd84f77cd6cc781e86c149.positions ) {
gmap\_m415d4e168ddd84f77cd6cc781e86c149.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m415d4e168ddd84f77cd6cc781e86c149.map,
position : gmap\_m415d4e168ddd84f77cd6cc781e86c149.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m415d4e168ddd84f77cd6cc781e86c149.map.setCenter( gmap\_m415d4e168ddd84f77cd6cc781e86c149.positions[66] );
});