---
title: ''
date: '2018-07-21T23:59:27-06:00'
format: image
service: instagram
latitude: '35.6952601'
longitude: '139.7019768'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/07/14182121/37182277_1335472273252060_8699548346441793536_n.jpg
---

[![Godzilla!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/07/14182121/37182277_1335472273252060_8699548346441793536_n.jpg)](https://dentedreality.com.au/2018/07/21/godzilla/) 

[![Godzilla!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/07/14182121/37182277_1335472273252060_8699548346441793536_n.jpg)](https://www.instagram.com/p/BlhehMhF199/)

Godzilla!

35.6952601139.7019768




Posted on [Instagram](https://www.instagram.com/p/BlhehMhF199/) [11:59 pm, July 21, 2018](https://dentedreality.com.au/2018/07/21/godzilla/ "11:59 pm") 
jQuery(document).ready(function(){
var gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c = {
positions : {
794 : new google.maps.LatLng( '35.6952601', '139.7019768' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.positions ) {
gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.bounds.extend( gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.positions[m] );
}
// Render markers
for ( var m in gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.positions ) {
gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.map,
position : gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.map.setCenter( gmap\_mb86592bfe3c7c60bc98e097ff1b9e92c.positions[794] );
});