---
title: ''
date: '2014-03-28T08:48:54+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/abad1bacb67f11e392f11272c16e65b0_8.jpg?resize=640%2C640
---

[![Melbourne from above.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/abad1bacb67f11e392f11272c16e65b0_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/03/28/melbourne-from-above/) 

Melbourne from above.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/mFqpvVimMl/) [8:48 am, March 28, 2014](http://dentedreality.com.au/2014/03/28/melbourne-from-above/ "8:48 am") 
jQuery(document).ready(function(){
var gmap\_m76190c1da0057f4bff624bd87b0b9249 = {
positions : {
583 : new google.maps.LatLng( '-37.821310849', '144.964642525' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m76190c1da0057f4bff624bd87b0b9249' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m76190c1da0057f4bff624bd87b0b9249.positions ) {
gmap\_m76190c1da0057f4bff624bd87b0b9249.bounds.extend( gmap\_m76190c1da0057f4bff624bd87b0b9249.positions[m] );
}
// Render markers
for ( var m in gmap\_m76190c1da0057f4bff624bd87b0b9249.positions ) {
gmap\_m76190c1da0057f4bff624bd87b0b9249.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m76190c1da0057f4bff624bd87b0b9249.map,
position : gmap\_m76190c1da0057f4bff624bd87b0b9249.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m76190c1da0057f4bff624bd87b0b9249.map.setCenter( gmap\_m76190c1da0057f4bff624bd87b0b9249.positions[583] );
});