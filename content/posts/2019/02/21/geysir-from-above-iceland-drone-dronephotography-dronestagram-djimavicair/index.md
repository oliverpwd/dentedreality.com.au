---
title: ''
date: '2019-02-21T17:15:41-07:00'
format: image
service: instagram
tags:
- djimavicair
- drone
- dronephotography
- dronestagram
- iceland
latitude: '64.3142117'
longitude: '-20.3009283'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/52846316_694753760940762_3379162997796781629_n.jpg
---

[![Geysir from above. #iceland #drone #dronephotography #dronestagram #djimavicair](https://dentedreality.com.au/wp-content/uploads/2019/02/52846316_694753760940762_3379162997796781629_n.jpg)](https://dentedreality.com.au/2019/02/21/geysir-from-above-iceland-drone-dronephotography-dronestagram-djimavicair/) 

[![Geysir from above. #iceland #drone #dronephotography #dronestagram #djimavicair](https://dentedreality.com.au/wp-content/uploads/2019/02/52846316_694753760940762_3379162997796781629_n.jpg)](https://www.instagram.com/p/BuKeFk0nP49/)

Geysir from above. #iceland #drone #dronephotography #dronestagram #djimavicair

64.3142117-20.3009283




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[drone](https://dentedreality.com.au/tags/drone/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)
* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKeFk0nP49/) [5:15 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/geysir-from-above-iceland-drone-dronephotography-dronestagram-djimavicair/ "5:15 pm") 
jQuery(document).ready(function(){
var gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654 = {
positions : {
310 : new google.maps.LatLng( '64.3142117', '-20.3009283' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.positions ) {
gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.bounds.extend( gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.positions[m] );
}
// Render markers
for ( var m in gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.positions ) {
gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.map,
position : gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.map.setCenter( gmap\_m54e8f5ec8dbc2c402804fb13cbe6e654.positions[310] );
});