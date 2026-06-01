---
title: ''
date: '2017-07-03T09:04:24-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.500861'
longitude: '-106.1535167'
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19624211_1951386748435372_3210812980920844288_n.jpg?fit=640%2C640&ssl=1
---

[![Finishers #fjallravenclassicusa](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19624211_1951386748435372_3210812980920844288_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/07/03/finishers-fjallravenclassicusa/) 

[![Finishers #fjallravenclassicusa](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19624211_1951386748435372_3210812980920844288_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BWFromHhwpE/)

Finishers #fjallravenclassicusa

39.500861-106.1535167




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BWFromHhwpE/) [9:04 am, July 3, 2017](https://dentedreality.com.au/2017/07/03/finishers-fjallravenclassicusa/ "9:04 am") 
jQuery(document).ready(function(){
var gmap\_m8718b15b5ec4be54d230d8f8dd405e25 = {
positions : {
242 : new google.maps.LatLng( '39.500861', '-106.1535167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8718b15b5ec4be54d230d8f8dd405e25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8718b15b5ec4be54d230d8f8dd405e25.positions ) {
gmap\_m8718b15b5ec4be54d230d8f8dd405e25.bounds.extend( gmap\_m8718b15b5ec4be54d230d8f8dd405e25.positions[m] );
}
// Render markers
for ( var m in gmap\_m8718b15b5ec4be54d230d8f8dd405e25.positions ) {
gmap\_m8718b15b5ec4be54d230d8f8dd405e25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8718b15b5ec4be54d230d8f8dd405e25.map,
position : gmap\_m8718b15b5ec4be54d230d8f8dd405e25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8718b15b5ec4be54d230d8f8dd405e25.map.setCenter( gmap\_m8718b15b5ec4be54d230d8f8dd405e25.positions[242] );
});