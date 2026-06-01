---
title: ''
date: '2019-02-21T17:05:18-07:00'
format: image
service: instagram
tags:
- iceland
latitude: '64.14246'
longitude: '-21.9289'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/51772991_146328366376758_2968694170022927835_n.jpg
---

[![Classic Reykjavík view. #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/51772991_146328366376758_2968694170022927835_n.jpg)](https://dentedreality.com.au/2019/02/21/classic-reykjavik-view-iceland/) 

[![Classic Reykjavík view. #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/51772991_146328366376758_2968694170022927835_n.jpg)](https://www.instagram.com/p/BuKc5jhHn2x/)

Classic Reykjavík view. #iceland

64.14246-21.9289




* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKc5jhHn2x/) [5:05 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/classic-reykjavik-view-iceland/ "5:05 pm") 
jQuery(document).ready(function(){
var gmap\_mb4d9906a24765fb8e784fb0ffadd2e98 = {
positions : {
233 : new google.maps.LatLng( '64.14246', '-21.9289' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb4d9906a24765fb8e784fb0ffadd2e98' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.positions ) {
gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.bounds.extend( gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.positions[m] );
}
// Render markers
for ( var m in gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.positions ) {
gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.map,
position : gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.map.setCenter( gmap\_mb4d9906a24765fb8e784fb0ffadd2e98.positions[233] );
});