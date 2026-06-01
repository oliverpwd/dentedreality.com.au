---
title: ''
date: '2017-04-09T16:27:39-06:00'
format: image
service: instagram
latitude: '39.7572'
longitude: '-104.967'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/17663820_290046178092351_7816564200653717504_n.jpg?fit=640%2C640
---

[![Got all the cooler season things planted finally. Even though it's pretty warm already, and forecast for more of the same.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/17663820_290046178092351_7816564200653717504_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/04/09/got-all-the-cooler-season-things-planted-finally-even-though-its-pretty-warm-already-and-forecast-for-more-of-the-same/) 

[![Got all the cooler season things planted finally. Even though it's pretty warm already, and forecast for more of the same.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/17663820_290046178092351_7816564200653717504_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BSrmysTB19C/)

Got all the cooler season things planted finally. Even though it’s pretty warm already, and forecast for more of the same.

39.7572-104.967




Posted on [Instagram](https://www.instagram.com/p/BSrmysTB19C/) [4:27 pm, April 9, 2017](https://dentedreality.com.au/2017/04/09/got-all-the-cooler-season-things-planted-finally-even-though-its-pretty-warm-already-and-forecast-for-more-of-the-same/ "4:27 pm") 
jQuery(document).ready(function(){
var gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f = {
positions : {
184 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.positions ) {
gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.bounds.extend( gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.positions[m] );
}
// Render markers
for ( var m in gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.positions ) {
gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.map,
position : gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.map.setCenter( gmap\_mbfbfe6a153079cb2a2d0fe39cb79bb1f.positions[184] );
});