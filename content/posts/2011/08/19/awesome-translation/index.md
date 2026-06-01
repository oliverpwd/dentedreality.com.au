---
title: Awesome Translation
date: '2011-08-19T17:51:39+00:00'
format: image
service: flickr
tags:
- awesome
- engrish
- translation
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322993497_71311db334_o.jpg?resize=607%2C452
---

[![Awesome Translation](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322993497_71311db334_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/08/19/awesome-translation/) 
# [Awesome Translation](http://dentedreality.com.au/2011/08/19/awesome-translation/)





* #[awesome](http://dentedreality.com.au/tags/awesome/)
* #[engrish](http://dentedreality.com.au/tags/engrish/)
* #[translation](http://dentedreality.com.au/tags/translation/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322993497/) [5:51 pm, August 19, 2011](http://dentedreality.com.au/2011/08/19/awesome-translation/ "5:51 pm") 
jQuery(document).ready(function(){
var gmap\_m7f0031db2339b95ef4f09fdd984a9c3d = {
positions : {
358 : new google.maps.LatLng( '37.736', '-122.433501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7f0031db2339b95ef4f09fdd984a9c3d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.positions ) {
gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.bounds.extend( gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.positions[m] );
}
// Render markers
for ( var m in gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.positions ) {
gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.map,
position : gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.map.setCenter( gmap\_m7f0031db2339b95ef4f09fdd984a9c3d.positions[358] );
});