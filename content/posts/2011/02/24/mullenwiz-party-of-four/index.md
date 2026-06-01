---
title: ''
date: '2011-02-24T23:28:03+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/99bd6b3d287448c789acb08a71babbcc_7.jpg?resize=607%2C607
---

[![Mullenwiz, party of four?](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/99bd6b3d287448c789acb08a71babbcc_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/02/24/mullenwiz-party-of-four/) 

Mullenwiz, party of four?





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/B03up/) [11:28 pm, February 24, 2011](http://dentedreality.com.au/2011/02/24/mullenwiz-party-of-four/ "11:28 pm") 
jQuery(document).ready(function(){
var gmap\_m246e1f8a5ffccf5f55d4835ac61712c6 = {
positions : {
478 : new google.maps.LatLng( '40.730852901', '-74.000853718' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m246e1f8a5ffccf5f55d4835ac61712c6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.positions ) {
gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.bounds.extend( gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.positions[m] );
}
// Render markers
for ( var m in gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.positions ) {
gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.map,
position : gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.map.setCenter( gmap\_m246e1f8a5ffccf5f55d4835ac61712c6.positions[478] );
});