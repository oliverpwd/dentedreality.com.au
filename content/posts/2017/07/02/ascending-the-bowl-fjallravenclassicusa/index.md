---
title: ''
date: '2017-07-02T16:04:25-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.3973'
longitude: '-106.106'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19534573_143146559594662_8614658042958446592_n.jpg?fit=640%2C640&ssl=1
---

[![Ascending the bowl #fjallravenclassicusa](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19534573_143146559594662_8614658042958446592_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/07/02/ascending-the-bowl-fjallravenclassicusa/) 

[![Ascending the bowl #fjallravenclassicusa](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19534573_143146559594662_8614658042958446592_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BWD26A-hAVh/)

Ascending the bowl #fjallravenclassicusa

39.3973-106.106




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BWD26A-hAVh/) [4:04 pm, July 2, 2017](https://dentedreality.com.au/2017/07/02/ascending-the-bowl-fjallravenclassicusa/ "4:04 pm") 
jQuery(document).ready(function(){
var gmap\_mb3e735676a6b80d58501ff7f37208ecf = {
positions : {
721 : new google.maps.LatLng( '39.3973', '-106.106' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb3e735676a6b80d58501ff7f37208ecf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb3e735676a6b80d58501ff7f37208ecf.positions ) {
gmap\_mb3e735676a6b80d58501ff7f37208ecf.bounds.extend( gmap\_mb3e735676a6b80d58501ff7f37208ecf.positions[m] );
}
// Render markers
for ( var m in gmap\_mb3e735676a6b80d58501ff7f37208ecf.positions ) {
gmap\_mb3e735676a6b80d58501ff7f37208ecf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb3e735676a6b80d58501ff7f37208ecf.map,
position : gmap\_mb3e735676a6b80d58501ff7f37208ecf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb3e735676a6b80d58501ff7f37208ecf.map.setCenter( gmap\_mb3e735676a6b80d58501ff7f37208ecf.positions[721] );
});