---
title: ''
date: '2015-01-02T16:43:37+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10865223_746340555435680_218557643_n.jpg?resize=640%2C640
---

[![Posted on Instagram](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10865223_746340555435680_218557643_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/01/02/posted-on-instagram-23/) 




* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/xXtShnCmHR/) [4:43 pm, January 2, 2015](http://dentedreality.com.au/2015/01/02/posted-on-instagram-23/ "4:43 pm") 
jQuery(document).ready(function(){
var gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5 = {
positions : {
946 : new google.maps.LatLng( '39.653814619', '-105.36656843' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.positions ) {
gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.bounds.extend( gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.positions[m] );
}
// Render markers
for ( var m in gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.positions ) {
gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.map,
position : gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.map.setCenter( gmap\_m4d95d670beab2d4cfea7b6a4fe5029c5.positions[946] );
});