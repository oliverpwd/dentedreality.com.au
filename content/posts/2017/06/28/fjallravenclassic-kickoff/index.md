---
title: ''
date: '2017-06-28T07:51:24-06:00'
format: image
service: instagram
tags:
- fjallravenclassic
- fjallravenclassicusa
latitude: '39.500861'
longitude: '-106.1535167'
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19437047_144285512808700_2120774255703490560_n.jpg?fit=640%2C640&ssl=1
---

[![#fjallravenclassic kickoff!](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19437047_144285512808700_2120774255703490560_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/06/28/fjallravenclassic-kickoff/) 

[![#fjallravenclassic kickoff!](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19437047_144285512808700_2120774255703490560_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BV4rThtBRWK/)

#fjallravenclassic kickoff!

39.500861-106.1535167




* #[fjallravenclassic](https://dentedreality.com.au/tags/fjallravenclassic/)
* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BV4rThtBRWK/) [7:51 am, June 28, 2017](https://dentedreality.com.au/2017/06/28/fjallravenclassic-kickoff/ "7:51 am") 
jQuery(document).ready(function(){
var gmap\_mb3bee7b119c132c473b2d3c87ae189e8 = {
positions : {
322 : new google.maps.LatLng( '39.500861', '-106.1535167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb3bee7b119c132c473b2d3c87ae189e8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb3bee7b119c132c473b2d3c87ae189e8.positions ) {
gmap\_mb3bee7b119c132c473b2d3c87ae189e8.bounds.extend( gmap\_mb3bee7b119c132c473b2d3c87ae189e8.positions[m] );
}
// Render markers
for ( var m in gmap\_mb3bee7b119c132c473b2d3c87ae189e8.positions ) {
gmap\_mb3bee7b119c132c473b2d3c87ae189e8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb3bee7b119c132c473b2d3c87ae189e8.map,
position : gmap\_mb3bee7b119c132c473b2d3c87ae189e8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb3bee7b119c132c473b2d3c87ae189e8.map.setCenter( gmap\_mb3bee7b119c132c473b2d3c87ae189e8.positions[322] );
});