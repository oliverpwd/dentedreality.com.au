---
title: ''
date: '2018-08-11T11:14:05-06:00'
format: image
service: instagram
tags:
- beets
- carrots
- gardening
- inmygarden
- veggiegarden
latitude: '39.7572'
longitude: '-104.967'
image: https://dentedreality.com.au/wp-content/uploads/2018/08/37959258_266152534200573_2186657452001329152_n.jpg
---

[![Today's harvest! #carrots #beets #veggiegarden #gardening #inmygarden](https://dentedreality.com.au/wp-content/uploads/2018/08/37959258_266152534200573_2186657452001329152_n.jpg)](https://dentedreality.com.au/2018/08/11/todays-harvest-carrots-beets-veggiegarden-gardening-inmygarden/) 

[![Today's harvest! #carrots #beets #veggiegarden #gardening #inmygarden](https://dentedreality.com.au/wp-content/uploads/2018/08/37959258_266152534200573_2186657452001329152_n.jpg)](https://www.instagram.com/p/BmWLn3iFZGG/)

Today’s harvest! #carrots #beets #veggiegarden #gardening #inmygarden

39.7572-104.967




* #[beets](https://dentedreality.com.au/tags/beets/)
* #[carrots](https://dentedreality.com.au/tags/carrots/)
* #[gardening](https://dentedreality.com.au/tags/gardening/)
* #[inmygarden](https://dentedreality.com.au/tags/inmygarden/)
* #[veggiegarden](https://dentedreality.com.au/tags/veggiegarden/)

Posted on [Instagram](https://www.instagram.com/p/BmWLn3iFZGG/) [11:14 am, August 11, 2018](https://dentedreality.com.au/2018/08/11/todays-harvest-carrots-beets-veggiegarden-gardening-inmygarden/ "11:14 am") 
jQuery(document).ready(function(){
var gmap\_mdd5d03c1392898475a4a358217896a20 = {
positions : {
206 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdd5d03c1392898475a4a358217896a20' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdd5d03c1392898475a4a358217896a20.positions ) {
gmap\_mdd5d03c1392898475a4a358217896a20.bounds.extend( gmap\_mdd5d03c1392898475a4a358217896a20.positions[m] );
}
// Render markers
for ( var m in gmap\_mdd5d03c1392898475a4a358217896a20.positions ) {
gmap\_mdd5d03c1392898475a4a358217896a20.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdd5d03c1392898475a4a358217896a20.map,
position : gmap\_mdd5d03c1392898475a4a358217896a20.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdd5d03c1392898475a4a358217896a20.map.setCenter( gmap\_mdd5d03c1392898475a4a358217896a20.positions[206] );
});