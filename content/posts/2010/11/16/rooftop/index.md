---
title: ''
date: '2010-11-16T18:06:42+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/09bd62a79ff04cd9a8a421a2739066ca_7.jpg?resize=607%2C607
---

[![Rooftop](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/09bd62a79ff04cd9a8a421a2739066ca_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/11/16/rooftop/) 

Rooftop





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/RgCn/) [6:06 pm, November 16, 2010](http://dentedreality.com.au/2010/11/16/rooftop/ "6:06 pm") 
jQuery(document).ready(function(){
var gmap\_ma1bcc7414503ef9a108cc7d3130f5807 = {
positions : {
900 : new google.maps.LatLng( '37.789404067', '-122.420525551' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma1bcc7414503ef9a108cc7d3130f5807' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma1bcc7414503ef9a108cc7d3130f5807.positions ) {
gmap\_ma1bcc7414503ef9a108cc7d3130f5807.bounds.extend( gmap\_ma1bcc7414503ef9a108cc7d3130f5807.positions[m] );
}
// Render markers
for ( var m in gmap\_ma1bcc7414503ef9a108cc7d3130f5807.positions ) {
gmap\_ma1bcc7414503ef9a108cc7d3130f5807.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma1bcc7414503ef9a108cc7d3130f5807.map,
position : gmap\_ma1bcc7414503ef9a108cc7d3130f5807.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma1bcc7414503ef9a108cc7d3130f5807.map.setCenter( gmap\_ma1bcc7414503ef9a108cc7d3130f5807.positions[900] );
});