---
title: ''
date: '2019-01-26T17:35:04-07:00'
format: image
service: instagram
tags:
- cityscape
- djimavicair
- dronestagram
- nofilter
- skyline
- sunset
latitude: '39.7391'
longitude: '-104.9836'
image: https://dentedreality.com.au/wp-content/uploads/2019/01/49907441_1958528997785030_282296210611765234_n.jpg
---

[![Nice sunset Denver! #dronestagram #sunset #skyline #cityscape #djimavicair #nofilter](https://dentedreality.com.au/wp-content/uploads/2019/01/49907441_1958528997785030_282296210611765234_n.jpg)](https://dentedreality.com.au/2019/01/26/nice-sunset-denver-dronestagram-sunset-skyline-cityscape-djimavicair-nofilter/) 

[![Nice sunset Denver! #dronestagram #sunset #skyline #cityscape #djimavicair #nofilter](https://dentedreality.com.au/wp-content/uploads/2019/01/49907441_1958528997785030_282296210611765234_n.jpg)](https://www.instagram.com/p/BtHjoysg-Gm/)

Nice sunset Denver! #dronestagram #sunset #skyline #cityscape #djimavicair #nofilter

39.7391-104.9836




* #[cityscape](https://dentedreality.com.au/tags/cityscape/)
* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)
* #[nofilter](https://dentedreality.com.au/tags/nofilter/)
* #[skyline](https://dentedreality.com.au/tags/skyline/)
* #[sunset](https://dentedreality.com.au/tags/sunset/)

Posted on [Instagram](https://www.instagram.com/p/BtHjoysg-Gm/) [5:35 pm, January 26, 2019](https://dentedreality.com.au/2019/01/26/nice-sunset-denver-dronestagram-sunset-skyline-cityscape-djimavicair-nofilter/ "5:35 pm") 
jQuery(document).ready(function(){
var gmap\_m37fde60f3501632d67b049b531d34d46 = {
positions : {
416 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m37fde60f3501632d67b049b531d34d46' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m37fde60f3501632d67b049b531d34d46.positions ) {
gmap\_m37fde60f3501632d67b049b531d34d46.bounds.extend( gmap\_m37fde60f3501632d67b049b531d34d46.positions[m] );
}
// Render markers
for ( var m in gmap\_m37fde60f3501632d67b049b531d34d46.positions ) {
gmap\_m37fde60f3501632d67b049b531d34d46.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m37fde60f3501632d67b049b531d34d46.map,
position : gmap\_m37fde60f3501632d67b049b531d34d46.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m37fde60f3501632d67b049b531d34d46.map.setCenter( gmap\_m37fde60f3501632d67b049b531d34d46.positions[416] );
});