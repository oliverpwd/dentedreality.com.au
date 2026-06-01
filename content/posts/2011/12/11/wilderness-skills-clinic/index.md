---
title: Wilderness Skills Clinic
date: '2011-12-11T12:03:48+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- survival
- wilderness
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958326469_710fd9bf1c_o.jpg?resize=607%2C452
---

[![Wilderness Skills Clinic](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958326469_710fd9bf1c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic/) 
# [Wilderness Skills Clinic](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic/)

There are 2 debris huts in this picture. Can you see them?





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958326469/) [12:03 pm, December 11, 2011](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic/ "12:03 pm") 
jQuery(document).ready(function(){
var gmap\_meff49a062f9a7c6bff97bc827ef3a10b = {
positions : {
42 : new google.maps.LatLng( '38', '-122.6125' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meff49a062f9a7c6bff97bc827ef3a10b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meff49a062f9a7c6bff97bc827ef3a10b.positions ) {
gmap\_meff49a062f9a7c6bff97bc827ef3a10b.bounds.extend( gmap\_meff49a062f9a7c6bff97bc827ef3a10b.positions[m] );
}
// Render markers
for ( var m in gmap\_meff49a062f9a7c6bff97bc827ef3a10b.positions ) {
gmap\_meff49a062f9a7c6bff97bc827ef3a10b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meff49a062f9a7c6bff97bc827ef3a10b.map,
position : gmap\_meff49a062f9a7c6bff97bc827ef3a10b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meff49a062f9a7c6bff97bc827ef3a10b.map.setCenter( gmap\_meff49a062f9a7c6bff97bc827ef3a10b.positions[42] );
});