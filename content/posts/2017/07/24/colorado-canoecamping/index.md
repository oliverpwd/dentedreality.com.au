---
title: ''
date: '2017-07-24T13:38:17+00:00'
format: image
service: instagram
tags:
- canoecamping
- colorado
image: https://dentedreality.com.au/wp-content/uploads/2017/07/20225575_247136262458451_2412165753554862080_n.jpg
---

[![#colorado #canoecamping](https://dentedreality.com.au/wp-content/uploads/2017/07/20225575_247136262458451_2412165753554862080_n.jpg)](https://dentedreality.com.au/2017/07/24/colorado-canoecamping/) 

[![#colorado #canoecamping](https://dentedreality.com.au/wp-content/uploads/2017/07/20225575_247136262458451_2412165753554862080_n.jpg)](https://www.instagram.com/p/BW8Pq5aBNb4/)

#colorado #canoecamping





* #[canoecamping](https://dentedreality.com.au/tags/canoecamping/)
* #[colorado](https://dentedreality.com.au/tags/colorado/)

Posted on [Instagram](https://www.instagram.com/p/BW8Pq5aBNb4/) [1:38 pm, July 24, 2017](https://dentedreality.com.au/2017/07/24/colorado-canoecamping/ "1:38 pm") 
jQuery(document).ready(function(){
var gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a = {
positions : {
285 : new google.maps.LatLng( '39.862997046629', '-105.08438988874' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.positions ) {
gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.bounds.extend( gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.positions[m] );
}
// Render markers
for ( var m in gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.positions ) {
gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.map,
position : gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.map.setCenter( gmap\_m2f5f15c3d51a7676ffde46a6e97dd50a.positions[285] );
});