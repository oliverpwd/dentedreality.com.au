---
title: ''
date: '2014-06-28T22:21:11+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10483402_457603044384299_1268681272_n.jpg?resize=640%2C640
---

[![Goodbye Picasso](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10483402_457603044384299_1268681272_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/06/28/goodbye-picasso-3/) 

Goodbye Picasso





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/p0AvhUCmKH/) [10:21 pm, June 28, 2014](http://dentedreality.com.au/2014/06/28/goodbye-picasso-3/ "10:21 pm") 
jQuery(document).ready(function(){
var gmap\_mf114364c5902e65eeffc653dbff3b4f8 = {
positions : {
351 : new google.maps.LatLng( '40.722243859', '-73.988778775' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf114364c5902e65eeffc653dbff3b4f8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf114364c5902e65eeffc653dbff3b4f8.positions ) {
gmap\_mf114364c5902e65eeffc653dbff3b4f8.bounds.extend( gmap\_mf114364c5902e65eeffc653dbff3b4f8.positions[m] );
}
// Render markers
for ( var m in gmap\_mf114364c5902e65eeffc653dbff3b4f8.positions ) {
gmap\_mf114364c5902e65eeffc653dbff3b4f8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf114364c5902e65eeffc653dbff3b4f8.map,
position : gmap\_mf114364c5902e65eeffc653dbff3b4f8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf114364c5902e65eeffc653dbff3b4f8.map.setCenter( gmap\_mf114364c5902e65eeffc653dbff3b4f8.positions[351] );
});