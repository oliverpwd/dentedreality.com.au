---
title: ''
date: '2012-05-03T16:44:07+00:00'
format: image
service: instagram
tags:
- photo
image: http://dentedreality.com.au/wp-content/uploads/2012/05/ba565516956011e181bd12313817987b_7.jpg
---

[![Awesome Dog](http://dentedreality.com.au/wp-content/uploads/2012/05/ba565516956011e181bd12313817987b_7.jpg)](https://dentedreality.com.au/2012/05/03/awesome-dog/) 

[![Awesome Dog](http://dentedreality.com.au/wp-content/uploads/2012/05/ba565516956011e181bd12313817987b_7.jpg)](http://instagram.com/p/KLafmuimIa/)

Awesome Dog





* #[photo](https://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/KLafmuimIa/) [4:44 pm, May 3, 2012](https://dentedreality.com.au/2012/05/03/awesome-dog/ "4:44 pm") 
jQuery(document).ready(function(){
var gmap\_m006187c42b6fa1ab1c06b51e4d047a61 = {
positions : {
927 : new google.maps.LatLng( '37.79096381', '-122.420701' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m006187c42b6fa1ab1c06b51e4d047a61' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m006187c42b6fa1ab1c06b51e4d047a61.positions ) {
gmap\_m006187c42b6fa1ab1c06b51e4d047a61.bounds.extend( gmap\_m006187c42b6fa1ab1c06b51e4d047a61.positions[m] );
}
// Render markers
for ( var m in gmap\_m006187c42b6fa1ab1c06b51e4d047a61.positions ) {
gmap\_m006187c42b6fa1ab1c06b51e4d047a61.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m006187c42b6fa1ab1c06b51e4d047a61.map,
position : gmap\_m006187c42b6fa1ab1c06b51e4d047a61.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m006187c42b6fa1ab1c06b51e4d047a61.map.setCenter( gmap\_m006187c42b6fa1ab1c06b51e4d047a61.positions[927] );
});