---
title: ''
date: '2014-05-26T19:17:57+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10354469_1428306004097812_1767526236_n.jpg?resize=640%2C640
---

[![Chicken heart soup for dinner, care of @akires' mom.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10354469_1428306004097812_1767526236_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/05/26/chicken-heart-soup-for-dinner-care-of-akires-mom/) 

Chicken heart soup for dinner, care of @akires’ mom.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/oetimYimEM/) [7:17 pm, May 26, 2014](http://dentedreality.com.au/2014/05/26/chicken-heart-soup-for-dinner-care-of-akires-mom/ "7:17 pm") 
jQuery(document).ready(function(){
var gmap\_mf6ce513e0e5f22ab38cccef96a52e96b = {
positions : {
540 : new google.maps.LatLng( '40.66937', '-73.98497' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf6ce513e0e5f22ab38cccef96a52e96b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.positions ) {
gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.bounds.extend( gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.positions[m] );
}
// Render markers
for ( var m in gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.positions ) {
gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.map,
position : gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.map.setCenter( gmap\_mf6ce513e0e5f22ab38cccef96a52e96b.positions[540] );
});