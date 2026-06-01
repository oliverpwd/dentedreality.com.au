---
title: Wilderness Skills Clinic
date: '2011-12-11T07:58:46+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- camping
- disaster
- me
- outdoors
- survival
- wilderness
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812215180_d1b6317f35_o.jpg?resize=607%2C452
---

[![Wilderness Skills Clinic](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812215180_d1b6317f35_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-6/) 
# [Wilderness Skills Clinic](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-6/)

I’m in a debris hut





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812215180/) [7:58 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-6/ "7:58 am") 
jQuery(document).ready(function(){
var gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0 = {
positions : {
575 : new google.maps.LatLng( '38.001166', '-122.612' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.positions ) {
gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.bounds.extend( gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.positions[m] );
}
// Render markers
for ( var m in gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.positions ) {
gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.map,
position : gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.map.setCenter( gmap\_mc9a3d46eb502e1ea634b083fd1a7b1f0.positions[575] );
});