---
title: ''
date: '2017-10-13T12:20:56-06:00'
format: image
service: instagram
tags:
- cafeworking
latitude: '39.76464'
longitude: '-104.95653'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/10/22352059_941179086047536_3760698051849617408_n.jpg?fit=640%2C640&ssl=1
---

[![This place is really cute, and seems to be a good spot for #cafeworking. Will try their food as well.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/10/22352059_941179086047536_3760698051849617408_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/10/13/this-place-is-really-cute-and-seems-to-be-a-good-spot-for-cafeworking-will-try-their-food-as-well/) 

[![This place is really cute, and seems to be a good spot for #cafeworking. Will try their food as well.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/10/22352059_941179086047536_3760698051849617408_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BaMrNT_BGXq/)

This place is really cute, and seems to be a good spot for #cafeworking. Will try their food as well.

39.76464-104.95653




* #[cafeworking](https://dentedreality.com.au/tags/cafeworking/)

Posted on [Instagram](https://www.instagram.com/p/BaMrNT_BGXq/) [12:20 pm, October 13, 2017](https://dentedreality.com.au/2017/10/13/this-place-is-really-cute-and-seems-to-be-a-good-spot-for-cafeworking-will-try-their-food-as-well/ "12:20 pm") 
jQuery(document).ready(function(){
var gmap\_m49bf99362a63b74961929ba691381850 = {
positions : {
272 : new google.maps.LatLng( '39.76464', '-104.95653' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m49bf99362a63b74961929ba691381850' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m49bf99362a63b74961929ba691381850.positions ) {
gmap\_m49bf99362a63b74961929ba691381850.bounds.extend( gmap\_m49bf99362a63b74961929ba691381850.positions[m] );
}
// Render markers
for ( var m in gmap\_m49bf99362a63b74961929ba691381850.positions ) {
gmap\_m49bf99362a63b74961929ba691381850.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m49bf99362a63b74961929ba691381850.map,
position : gmap\_m49bf99362a63b74961929ba691381850.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m49bf99362a63b74961929ba691381850.map.setCenter( gmap\_m49bf99362a63b74961929ba691381850.positions[272] );
});