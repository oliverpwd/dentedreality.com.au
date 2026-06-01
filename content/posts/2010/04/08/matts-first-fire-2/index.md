---
title: Matt’s First Fire
date: '2010-04-08T15:02:57+00:00'
format: image
service: flickr
tags:
- matt
- photomatt
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516456160_2da133fd93_o.jpg?resize=607%2C455
---

[![Matt's First Fire](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516456160_2da133fd93_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/matts-first-fire-2/) 
# [Matt’s First Fire](http://dentedreality.com.au/2010/04/08/matts-first-fire-2/)

Standard class, Tracker School.





* #[matt](http://dentedreality.com.au/tags/matt/)
* #[photomatt](http://dentedreality.com.au/tags/photomatt/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516456160/) [3:02 pm, April 8, 2010](http://dentedreality.com.au/2010/04/08/matts-first-fire-2/ "3:02 pm") 
jQuery(document).ready(function(){
var gmap\_md046ca1a15ed6da27cfc5227184a0555 = {
positions : {
97 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md046ca1a15ed6da27cfc5227184a0555' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md046ca1a15ed6da27cfc5227184a0555.positions ) {
gmap\_md046ca1a15ed6da27cfc5227184a0555.bounds.extend( gmap\_md046ca1a15ed6da27cfc5227184a0555.positions[m] );
}
// Render markers
for ( var m in gmap\_md046ca1a15ed6da27cfc5227184a0555.positions ) {
gmap\_md046ca1a15ed6da27cfc5227184a0555.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md046ca1a15ed6da27cfc5227184a0555.map,
position : gmap\_md046ca1a15ed6da27cfc5227184a0555.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md046ca1a15ed6da27cfc5227184a0555.map.setCenter( gmap\_md046ca1a15ed6da27cfc5227184a0555.positions[97] );
});