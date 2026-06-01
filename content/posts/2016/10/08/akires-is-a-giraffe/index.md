---
title: ''
date: '2016-10-08T18:02:30+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/10/14659351_341063919576857_9205135554176352256_n.jpg?fit=640%2C640
---

[![@akires is a giraffe!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/10/14659351_341063919576857_9205135554176352256_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/10/08/akires-is-a-giraffe/) 

@akires is a giraffe!





Posted on [Instagram](https://www.instagram.com/p/BLUkLMtjpQs/) [6:02 pm, October 8, 2016](http://dentedreality.com.au/2016/10/08/akires-is-a-giraffe/ "6:02 pm") 
jQuery(document).ready(function(){
var gmap\_md12dcaec62783b1946d9ab249dc8e5f9 = {
positions : {
562 : new google.maps.LatLng( '39.7', '-104.971' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md12dcaec62783b1946d9ab249dc8e5f9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md12dcaec62783b1946d9ab249dc8e5f9.positions ) {
gmap\_md12dcaec62783b1946d9ab249dc8e5f9.bounds.extend( gmap\_md12dcaec62783b1946d9ab249dc8e5f9.positions[m] );
}
// Render markers
for ( var m in gmap\_md12dcaec62783b1946d9ab249dc8e5f9.positions ) {
gmap\_md12dcaec62783b1946d9ab249dc8e5f9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md12dcaec62783b1946d9ab249dc8e5f9.map,
position : gmap\_md12dcaec62783b1946d9ab249dc8e5f9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md12dcaec62783b1946d9ab249dc8e5f9.map.setCenter( gmap\_md12dcaec62783b1946d9ab249dc8e5f9.positions[562] );
});