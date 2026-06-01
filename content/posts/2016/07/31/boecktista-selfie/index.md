---
title: ''
date: '2016-07-31T11:00:27-06:00'
format: image
service: instagram
tags:
- boecktista
latitude: '44.9322626'
longitude: '-92.8384434'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13732202_1758203251129650_2039099696_n.jpg?fit=640%2C640
---

[![#boecktista selfie](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13732202_1758203251129650_2039099696_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/31/boecktista-selfie/) 

[![#boecktista selfie](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13732202_1758203251129650_2039099696_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIiJBqGA0A4/)

#boecktista selfie

44.9322626-92.8384434




* #[boecktista](https://dentedreality.com.au/tags/boecktista/)

Posted on [Instagram](https://www.instagram.com/p/BIiJBqGA0A4/) [11:00 am, July 31, 2016](https://dentedreality.com.au/2016/07/31/boecktista-selfie/ "11:00 am") 
jQuery(document).ready(function(){
var gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f = {
positions : {
665 : new google.maps.LatLng( '44.93226257157', '-92.838443415326' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.positions ) {
gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.bounds.extend( gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.positions[m] );
}
// Render markers
for ( var m in gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.positions ) {
gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.map,
position : gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.map.setCenter( gmap\_maa585e424dfa67ba7ab1d0d76e6ab55f.positions[665] );
});