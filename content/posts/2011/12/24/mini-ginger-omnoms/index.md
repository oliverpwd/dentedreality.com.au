---
title: ''
date: '2011-12-24T18:53:18+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/128ef0582e8211e19e4a12313813ffc0_7.jpg?resize=607%2C607
---

[![Mini ginger omnoms!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/128ef0582e8211e19e4a12313813ffc0_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/12/24/mini-ginger-omnoms/) 

Mini ginger omnoms!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/bS7Dc/) [6:53 pm, December 24, 2011](http://dentedreality.com.au/2011/12/24/mini-ginger-omnoms/ "6:53 pm") 
jQuery(document).ready(function(){
var gmap\_me3a9347bf634d3b6ef40cc325b5464ce = {
positions : {
486 : new google.maps.LatLng( '37.736', '-122.4338' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me3a9347bf634d3b6ef40cc325b5464ce' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me3a9347bf634d3b6ef40cc325b5464ce.positions ) {
gmap\_me3a9347bf634d3b6ef40cc325b5464ce.bounds.extend( gmap\_me3a9347bf634d3b6ef40cc325b5464ce.positions[m] );
}
// Render markers
for ( var m in gmap\_me3a9347bf634d3b6ef40cc325b5464ce.positions ) {
gmap\_me3a9347bf634d3b6ef40cc325b5464ce.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me3a9347bf634d3b6ef40cc325b5464ce.map,
position : gmap\_me3a9347bf634d3b6ef40cc325b5464ce.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me3a9347bf634d3b6ef40cc325b5464ce.map.setCenter( gmap\_me3a9347bf634d3b6ef40cc325b5464ce.positions[486] );
});