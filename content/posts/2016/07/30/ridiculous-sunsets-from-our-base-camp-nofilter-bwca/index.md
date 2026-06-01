---
title: ''
date: '2016-07-30T09:57:32-06:00'
format: image
service: instagram
tags:
- bwca
- nofilter
latitude: '47.9637014'
longitude: '-91.5469748'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13715188_1354641291219804_2081654024_n.jpg?fit=640%2C640
---

[![Ridiculous sunsets from our base camp. #nofilter #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13715188_1354641291219804_2081654024_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/ridiculous-sunsets-from-our-base-camp-nofilter-bwca/) 

[![Ridiculous sunsets from our base camp. #nofilter #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13715188_1354641291219804_2081654024_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfdB_jgJhY/)

Ridiculous sunsets from our base camp. #nofilter #bwca

47.9637014-91.5469748




* #[bwca](https://dentedreality.com.au/tags/bwca/)
* #[nofilter](https://dentedreality.com.au/tags/nofilter/)

Posted on [Instagram](https://www.instagram.com/p/BIfdB_jgJhY/) [9:57 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/ridiculous-sunsets-from-our-base-camp-nofilter-bwca/ "9:57 am") 
jQuery(document).ready(function(){
var gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07 = {
positions : {
685 : new google.maps.LatLng( '47.963701444723', '-91.546974778261' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.positions ) {
gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.bounds.extend( gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.positions[m] );
}
// Render markers
for ( var m in gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.positions ) {
gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.map,
position : gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.map.setCenter( gmap\_m0c0e27fd602e7c4b5b7d91f7b53c9a07.positions[685] );
});