---
title: Jetboil
date: '2014-01-01T11:42:54+00:00'
format: image
service: flickr
tags:
- camping
- hiking
- jetboil
- stove
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901640612_9f8308cc22_o.jpg?resize=607%2C809
---

[![Jetboil](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901640612_9f8308cc22_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/01/01/jetboil/) 
# [Jetboil](http://dentedreality.com.au/2014/01/01/jetboil/)





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[jetboil](http://dentedreality.com.au/tags/jetboil/)
* #[stove](http://dentedreality.com.au/tags/stove/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901640612/) [11:42 am, January 1, 2014](http://dentedreality.com.au/2014/01/01/jetboil/ "11:42 am") 
jQuery(document).ready(function(){
var gmap\_m4d1de20a45a9dac6e2f37301a3428211 = {
positions : {
936 : new google.maps.LatLng( '40.669349', '-73.984939' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4d1de20a45a9dac6e2f37301a3428211' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4d1de20a45a9dac6e2f37301a3428211.positions ) {
gmap\_m4d1de20a45a9dac6e2f37301a3428211.bounds.extend( gmap\_m4d1de20a45a9dac6e2f37301a3428211.positions[m] );
}
// Render markers
for ( var m in gmap\_m4d1de20a45a9dac6e2f37301a3428211.positions ) {
gmap\_m4d1de20a45a9dac6e2f37301a3428211.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4d1de20a45a9dac6e2f37301a3428211.map,
position : gmap\_m4d1de20a45a9dac6e2f37301a3428211.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4d1de20a45a9dac6e2f37301a3428211.map.setCenter( gmap\_m4d1de20a45a9dac6e2f37301a3428211.positions[936] );
});