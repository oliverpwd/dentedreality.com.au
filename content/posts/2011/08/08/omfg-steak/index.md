---
title: OMFG Steak
date: '2011-08-08T18:07:02+00:00'
format: image
service: flickr
tags:
- 4505meats
- steak
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322991197_c94c25ed7b_o.jpg?resize=607%2C813
---

[![OMFG Steak](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322991197_c94c25ed7b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/08/08/omfg-steak/) 
# [OMFG Steak](http://dentedreality.com.au/2011/08/08/omfg-steak/)

2.5 lb steaks from 4505 Meats





* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[steak](http://dentedreality.com.au/tags/steak/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322991197/) [6:07 pm, August 8, 2011](http://dentedreality.com.au/2011/08/08/omfg-steak/ "6:07 pm") 
jQuery(document).ready(function(){
var gmap\_m69a60e89f44e9f86a8016122fcd312b7 = {
positions : {
455 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m69a60e89f44e9f86a8016122fcd312b7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m69a60e89f44e9f86a8016122fcd312b7.positions ) {
gmap\_m69a60e89f44e9f86a8016122fcd312b7.bounds.extend( gmap\_m69a60e89f44e9f86a8016122fcd312b7.positions[m] );
}
// Render markers
for ( var m in gmap\_m69a60e89f44e9f86a8016122fcd312b7.positions ) {
gmap\_m69a60e89f44e9f86a8016122fcd312b7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m69a60e89f44e9f86a8016122fcd312b7.map,
position : gmap\_m69a60e89f44e9f86a8016122fcd312b7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m69a60e89f44e9f86a8016122fcd312b7.map.setCenter( gmap\_m69a60e89f44e9f86a8016122fcd312b7.positions[455] );
});