---
title: ''
date: '2014-01-13T13:44:01+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/9847187e7c8211e3a0b30ebe944ce6f7_8.jpg?resize=640%2C640
---

[![Frankenthumb is looking "good". Stitches out tomorrow I think.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/9847187e7c8211e3a0b30ebe944ce6f7_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/13/frankenthumb-is-looking-good-stitches-out-tomorrow-i-think/) 

Frankenthumb is looking “good”. Stitches out tomorrow I think.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jHpmiaCmGZ/) [1:44 pm, January 13, 2014](http://dentedreality.com.au/2014/01/13/frankenthumb-is-looking-good-stitches-out-tomorrow-i-think/ "1:44 pm") 
jQuery(document).ready(function(){
var gmap\_mdd5d844d3428c74b28f1e94028fb5282 = {
positions : {
233 : new google.maps.LatLng( '40.6949', '-73.987428333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdd5d844d3428c74b28f1e94028fb5282' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdd5d844d3428c74b28f1e94028fb5282.positions ) {
gmap\_mdd5d844d3428c74b28f1e94028fb5282.bounds.extend( gmap\_mdd5d844d3428c74b28f1e94028fb5282.positions[m] );
}
// Render markers
for ( var m in gmap\_mdd5d844d3428c74b28f1e94028fb5282.positions ) {
gmap\_mdd5d844d3428c74b28f1e94028fb5282.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdd5d844d3428c74b28f1e94028fb5282.map,
position : gmap\_mdd5d844d3428c74b28f1e94028fb5282.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdd5d844d3428c74b28f1e94028fb5282.map.setCenter( gmap\_mdd5d844d3428c74b28f1e94028fb5282.positions[233] );
});