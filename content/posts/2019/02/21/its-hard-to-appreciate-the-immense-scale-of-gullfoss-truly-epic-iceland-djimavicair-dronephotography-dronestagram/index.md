---
title: ''
date: '2019-02-21T17:17:49-07:00'
format: image
service: instagram
tags:
- djimavicair
- dronephotography
- dronestagram
- iceland
latitude: '64.3259666'
longitude: '-20.1223183'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/52278919_2216005595304601_1180354604580631016_n.jpg
---

[![It's hard to appreciate the immense scale of Gullfoss. Truly epic. #iceland #djimavicair #dronephotography #dronestagram](https://dentedreality.com.au/wp-content/uploads/2019/02/52278919_2216005595304601_1180354604580631016_n.jpg)](https://dentedreality.com.au/2019/02/21/its-hard-to-appreciate-the-immense-scale-of-gullfoss-truly-epic-iceland-djimavicair-dronephotography-dronestagram/) 

[![It's hard to appreciate the immense scale of Gullfoss. Truly epic. #iceland #djimavicair #dronephotography #dronestagram](https://dentedreality.com.au/wp-content/uploads/2019/02/52278919_2216005595304601_1180354604580631016_n.jpg)](https://www.instagram.com/p/BuKeVOfHo_I/)

It’s hard to appreciate the immense scale of Gullfoss. Truly epic. #iceland #djimavicair #dronephotography #dronestagram

64.3259666-20.1223183




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)
* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKeVOfHo_I/) [5:17 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/its-hard-to-appreciate-the-immense-scale-of-gullfoss-truly-epic-iceland-djimavicair-dronephotography-dronestagram/ "5:17 pm") 
jQuery(document).ready(function(){
var gmap\_m0a05462dbdb20b8adf8267e3c66f0568 = {
positions : {
438 : new google.maps.LatLng( '64.3259666', '-20.1223183' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0a05462dbdb20b8adf8267e3c66f0568' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0a05462dbdb20b8adf8267e3c66f0568.positions ) {
gmap\_m0a05462dbdb20b8adf8267e3c66f0568.bounds.extend( gmap\_m0a05462dbdb20b8adf8267e3c66f0568.positions[m] );
}
// Render markers
for ( var m in gmap\_m0a05462dbdb20b8adf8267e3c66f0568.positions ) {
gmap\_m0a05462dbdb20b8adf8267e3c66f0568.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0a05462dbdb20b8adf8267e3c66f0568.map,
position : gmap\_m0a05462dbdb20b8adf8267e3c66f0568.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0a05462dbdb20b8adf8267e3c66f0568.map.setCenter( gmap\_m0a05462dbdb20b8adf8267e3c66f0568.positions[438] );
});