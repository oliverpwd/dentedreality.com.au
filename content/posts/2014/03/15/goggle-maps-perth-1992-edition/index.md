---
title: ''
date: '2014-03-15T05:32:27+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/1a28f04aac2d11e381ef12a1d68e45c4_8.jpg?resize=640%2C640
---

[![Goggle Maps, Perth 1992 Edition.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/1a28f04aac2d11e381ef12a1d68e45c4_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/03/15/goggle-maps-perth-1992-edition/) 

Goggle Maps, Perth 1992 Edition.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/lj11g0CmKL/) [5:32 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/goggle-maps-perth-1992-edition/ "5:32 am") 
jQuery(document).ready(function(){
var gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8 = {
positions : {
399 : new google.maps.LatLng( '-32.007763883', '115.757203333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.positions ) {
gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.bounds.extend( gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.positions[m] );
}
// Render markers
for ( var m in gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.positions ) {
gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.map,
position : gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.map.setCenter( gmap\_m1330bd1e4982e8b9e98aa7822ecc37a8.positions[399] );
});