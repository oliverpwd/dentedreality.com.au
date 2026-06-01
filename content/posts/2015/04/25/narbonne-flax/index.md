---
title: ''
date: '2015-04-25T18:01:49+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/04/11192901_1610498975861430_1039287439_n.jpg?resize=640%2C640
---

[![Narbonne Flax](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/04/11192901_1610498975861430_1039287439_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/04/25/narbonne-flax/) 

Narbonne Flax





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/16tMsjCmOK/) [6:01 pm, April 25, 2015](http://dentedreality.com.au/2015/04/25/narbonne-flax/ "6:01 pm") 
jQuery(document).ready(function(){
var gmap\_m074e4fd13b6adacb1e943ff34de793fe = {
positions : {
510 : new google.maps.LatLng( '39.73206264', '-104.961084383' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m074e4fd13b6adacb1e943ff34de793fe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m074e4fd13b6adacb1e943ff34de793fe.positions ) {
gmap\_m074e4fd13b6adacb1e943ff34de793fe.bounds.extend( gmap\_m074e4fd13b6adacb1e943ff34de793fe.positions[m] );
}
// Render markers
for ( var m in gmap\_m074e4fd13b6adacb1e943ff34de793fe.positions ) {
gmap\_m074e4fd13b6adacb1e943ff34de793fe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m074e4fd13b6adacb1e943ff34de793fe.map,
position : gmap\_m074e4fd13b6adacb1e943ff34de793fe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m074e4fd13b6adacb1e943ff34de793fe.map.setCenter( gmap\_m074e4fd13b6adacb1e943ff34de793fe.positions[510] );
});