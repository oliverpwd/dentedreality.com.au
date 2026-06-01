---
title: ''
date: '2017-05-20T17:59:11+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18645299_1363435033738435_1798109739465310208_n.jpg?fit=640%2C640
---

[![Architectural](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18645299_1363435033738435_1798109739465310208_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/20/architectural/) 

Architectural





Posted on [Instagram](https://www.instagram.com/p/BUVV257hUt0/) [5:59 pm, May 20, 2017](https://dentedreality.com.au/2017/05/20/architectural/ "5:59 pm") 
jQuery(document).ready(function(){
var gmap\_ma54c58e1c651e67fbba3e31c513cf15e = {
positions : {
759 : new google.maps.LatLng( '42.3314', '-83.0458' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma54c58e1c651e67fbba3e31c513cf15e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma54c58e1c651e67fbba3e31c513cf15e.positions ) {
gmap\_ma54c58e1c651e67fbba3e31c513cf15e.bounds.extend( gmap\_ma54c58e1c651e67fbba3e31c513cf15e.positions[m] );
}
// Render markers
for ( var m in gmap\_ma54c58e1c651e67fbba3e31c513cf15e.positions ) {
gmap\_ma54c58e1c651e67fbba3e31c513cf15e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma54c58e1c651e67fbba3e31c513cf15e.map,
position : gmap\_ma54c58e1c651e67fbba3e31c513cf15e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma54c58e1c651e67fbba3e31c513cf15e.map.setCenter( gmap\_ma54c58e1c651e67fbba3e31c513cf15e.positions[759] );
});