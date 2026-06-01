---
title: ''
date: '2010-11-17T20:59:00+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/6fc14558167b43fbb57c278a9f45b800_7.jpg?resize=607%2C607
---

[![Streaks In The Sky](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/6fc14558167b43fbb57c278a9f45b800_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/11/17/streaks-in-the-sky/) 

Streaks In The Sky





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SIqY/) [8:59 pm, November 17, 2010](http://dentedreality.com.au/2010/11/17/streaks-in-the-sky/ "8:59 pm") 
jQuery(document).ready(function(){
var gmap\_m7bfc1fc23a5944c96e87c13bcebffc14 = {
positions : {
832 : new google.maps.LatLng( '37.789423349', '-122.420498557' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7bfc1fc23a5944c96e87c13bcebffc14' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.positions ) {
gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.bounds.extend( gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.positions[m] );
}
// Render markers
for ( var m in gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.positions ) {
gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.map,
position : gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.map.setCenter( gmap\_m7bfc1fc23a5944c96e87c13bcebffc14.positions[832] );
});