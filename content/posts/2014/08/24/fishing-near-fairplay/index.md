---
title: ''
date: '2014-08-24T19:01:43+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10598590_763612363685625_1658448944_n.jpg?resize=640%2C640
---

[![Fishing near Fairplay.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10598590_763612363685625_1658448944_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/08/24/fishing-near-fairplay/) 

Fishing near Fairplay.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/sGiF7jimL_/) [7:01 pm, August 24, 2014](http://dentedreality.com.au/2014/08/24/fishing-near-fairplay/ "7:01 pm") 
jQuery(document).ready(function(){
var gmap\_m7e95e079654694d2ffc497bcaadb6f18 = {
positions : {
858 : new google.maps.LatLng( '39.222636738', '-105.998082377' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7e95e079654694d2ffc497bcaadb6f18' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7e95e079654694d2ffc497bcaadb6f18.positions ) {
gmap\_m7e95e079654694d2ffc497bcaadb6f18.bounds.extend( gmap\_m7e95e079654694d2ffc497bcaadb6f18.positions[m] );
}
// Render markers
for ( var m in gmap\_m7e95e079654694d2ffc497bcaadb6f18.positions ) {
gmap\_m7e95e079654694d2ffc497bcaadb6f18.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7e95e079654694d2ffc497bcaadb6f18.map,
position : gmap\_m7e95e079654694d2ffc497bcaadb6f18.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7e95e079654694d2ffc497bcaadb6f18.map.setCenter( gmap\_m7e95e079654694d2ffc497bcaadb6f18.positions[858] );
});