---
title: ''
date: '2014-03-26T03:08:29+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/ccdf0a56b4bd11e396ca123a32d64061_8.jpg?resize=640%2C640
---

[![Getting there.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/ccdf0a56b4bd11e396ca123a32d64061_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/03/26/getting-there-2/) 

Getting there.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/l_6GsBCmBY/) [3:08 am, March 26, 2014](http://dentedreality.com.au/2014/03/26/getting-there-2/ "3:08 am") 
jQuery(document).ready(function(){
var gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119 = {
positions : {
437 : new google.maps.LatLng( '-37.825725', '144.956511667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.positions ) {
gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.bounds.extend( gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.positions[m] );
}
// Render markers
for ( var m in gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.positions ) {
gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.map,
position : gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.map.setCenter( gmap\_mbcb40a03e5e5da3cfaa4cfb55f0da119.positions[437] );
});