---
title: ''
date: '2014-09-17T19:48:06+00:00'
format: image
tags:
- a8cgm
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10644088_1486384968294270_2087168442_n.jpg?resize=640%2C640
---

[![Silverado Tablemates! #a8cgm](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10644088_1486384968294270_2087168442_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/17/silverado-tablemates-a8cgm/) 

Silverado Tablemates! #a8cgm





* #[a8cgm](http://dentedreality.com.au/tags/a8cgm/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/tEaet1imBY/) [7:48 pm, September 17, 2014](http://dentedreality.com.au/2014/09/17/silverado-tablemates-a8cgm/ "7:48 pm") 
jQuery(document).ready(function(){
var gmap\_macb62596c27a7ebccd1f0f34b050ae76 = {
positions : {
77 : new google.maps.LatLng( '40.685043627', '-111.55658947' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_macb62596c27a7ebccd1f0f34b050ae76' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_macb62596c27a7ebccd1f0f34b050ae76.positions ) {
gmap\_macb62596c27a7ebccd1f0f34b050ae76.bounds.extend( gmap\_macb62596c27a7ebccd1f0f34b050ae76.positions[m] );
}
// Render markers
for ( var m in gmap\_macb62596c27a7ebccd1f0f34b050ae76.positions ) {
gmap\_macb62596c27a7ebccd1f0f34b050ae76.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_macb62596c27a7ebccd1f0f34b050ae76.map,
position : gmap\_macb62596c27a7ebccd1f0f34b050ae76.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_macb62596c27a7ebccd1f0f34b050ae76.map.setCenter( gmap\_macb62596c27a7ebccd1f0f34b050ae76.positions[77] );
});