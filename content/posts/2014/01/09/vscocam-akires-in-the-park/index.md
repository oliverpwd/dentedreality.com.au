---
title: ''
date: '2014-01-09T14:03:12+00:00'
format: image
tags:
- photo
- vscocam
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/adbdbd18796011e3a8af0e0b4f6d16dc_8.jpg?resize=640%2C640
---

[![#vscocam @akires in the park](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/adbdbd18796011e3a8af0e0b4f6d16dc_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/09/vscocam-akires-in-the-park/) 

#vscocam @akires in the park





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[vscocam](http://dentedreality.com.au/tags/vscocam/)

Posted on [Instagram](http://instagram.com/p/i9YnecCmKN/) [2:03 pm, January 9, 2014](http://dentedreality.com.au/2014/01/09/vscocam-akires-in-the-park/ "2:03 pm") 
jQuery(document).ready(function(){
var gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac = {
positions : {
551 : new google.maps.LatLng( '40.668388333', '-73.97075' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.positions ) {
gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.bounds.extend( gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.positions[m] );
}
// Render markers
for ( var m in gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.positions ) {
gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.map,
position : gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.map.setCenter( gmap\_m8f17d11553a4f8e3ddecdba5e092c3ac.positions[551] );
});