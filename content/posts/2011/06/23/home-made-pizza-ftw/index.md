---
title: ''
date: '2011-06-23T23:11:43+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/0cae45440f2c4584b38a1b58fcc81ea8_7.jpg?resize=607%2C607
---

[![Home made pizza FTW](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/0cae45440f2c4584b38a1b58fcc81ea8_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/06/23/home-made-pizza-ftw/) 

Home made pizza FTW





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/GRISi/) [11:11 pm, June 23, 2011](http://dentedreality.com.au/2011/06/23/home-made-pizza-ftw/ "11:11 pm") 
jQuery(document).ready(function(){
var gmap\_mac4e21b0339608e4457192328676a6cd = {
positions : {
902 : new google.maps.LatLng( '37.73588', '-122.4337' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mac4e21b0339608e4457192328676a6cd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mac4e21b0339608e4457192328676a6cd.positions ) {
gmap\_mac4e21b0339608e4457192328676a6cd.bounds.extend( gmap\_mac4e21b0339608e4457192328676a6cd.positions[m] );
}
// Render markers
for ( var m in gmap\_mac4e21b0339608e4457192328676a6cd.positions ) {
gmap\_mac4e21b0339608e4457192328676a6cd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mac4e21b0339608e4457192328676a6cd.map,
position : gmap\_mac4e21b0339608e4457192328676a6cd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mac4e21b0339608e4457192328676a6cd.map.setCenter( gmap\_mac4e21b0339608e4457192328676a6cd.positions[902] );
});