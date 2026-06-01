---
title: ''
date: '2016-06-05T20:36:08+00:00'
format: image
service: instagram
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13408692_125555021198116_924127471_n.jpg?fit=640%2C640
---

[![Beauty over trash.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13408692_125555021198116_924127471_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/06/05/beauty-over-trash/) 

Beauty over trash.





Posted on [Instagram](https://www.instagram.com/p/BGS-ZFiimI2/) [8:36 pm, June 5, 2016](http://dentedreality.com.au/2016/06/05/beauty-over-trash/ "8:36 pm") 
jQuery(document).ready(function(){
var gmap\_m15c7944827ce2f5d5b5d3df7a31f574b = {
positions : {
18 : new google.maps.LatLng( '39.763150299582', '-104.98138978175' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m15c7944827ce2f5d5b5d3df7a31f574b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.positions ) {
gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.bounds.extend( gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.positions[m] );
}
// Render markers
for ( var m in gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.positions ) {
gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.map,
position : gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.map.setCenter( gmap\_m15c7944827ce2f5d5b5d3df7a31f574b.positions[18] );
});