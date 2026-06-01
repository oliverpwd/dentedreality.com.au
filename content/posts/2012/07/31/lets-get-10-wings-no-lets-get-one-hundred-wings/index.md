---
title: ''
date: '2012-07-31T21:27:51+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/1c2826b8db7811e1a15422000a1e8687_7.jpg?resize=607%2C607
---

[![Let's get 10 wings. No. Let's get ONE HUNDRED WINGS!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/1c2826b8db7811e1a15422000a1e8687_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/07/31/lets-get-10-wings-no-lets-get-one-hundred-wings/) 

Let’s get 10 wings. No. Let’s get ONE HUNDRED WINGS!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/NxFtmMCmF2/) [9:27 pm, July 31, 2012](http://dentedreality.com.au/2012/07/31/lets-get-10-wings-no-lets-get-one-hundred-wings/ "9:27 pm") 
jQuery(document).ready(function(){
var gmap\_me0d026180517cb092f915173599396bd = {
positions : {
531 : new google.maps.LatLng( '40.7328', '-73.954692' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me0d026180517cb092f915173599396bd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me0d026180517cb092f915173599396bd.positions ) {
gmap\_me0d026180517cb092f915173599396bd.bounds.extend( gmap\_me0d026180517cb092f915173599396bd.positions[m] );
}
// Render markers
for ( var m in gmap\_me0d026180517cb092f915173599396bd.positions ) {
gmap\_me0d026180517cb092f915173599396bd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me0d026180517cb092f915173599396bd.map,
position : gmap\_me0d026180517cb092f915173599396bd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me0d026180517cb092f915173599396bd.map.setCenter( gmap\_me0d026180517cb092f915173599396bd.positions[531] );
});