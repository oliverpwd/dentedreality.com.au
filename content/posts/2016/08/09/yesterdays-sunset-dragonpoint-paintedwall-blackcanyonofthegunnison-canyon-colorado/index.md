---
title: ''
date: '2016-08-09T12:33:02+00:00'
format: image
service: instagram
tags:
- blackcanyonofthegunnison
- canyon
- colorado
- dragonpoint
- paintedwall
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13768117_278534052527807_344588635_n.jpg?fit=640%2C640
---

[![Yesterday's sunset. #dragonpoint #paintedwall #blackcanyonofthegunnison #canyon #colorado](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13768117_278534052527807_344588635_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/09/yesterdays-sunset-dragonpoint-paintedwall-blackcanyonofthegunnison-canyon-colorado/) 

Yesterday’s sunset. #dragonpoint #paintedwall #blackcanyonofthegunnison #canyon #colorado





* #[blackcanyonofthegunnison](http://dentedreality.com.au/tags/blackcanyonofthegunnison/)
* #[canyon](http://dentedreality.com.au/tags/canyon/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[dragonpoint](http://dentedreality.com.au/tags/dragonpoint/)
* #[paintedwall](http://dentedreality.com.au/tags/paintedwall/)

Posted on [Instagram](https://www.instagram.com/p/BI5exnqgY0x/) [12:33 pm, August 9, 2016](http://dentedreality.com.au/2016/08/09/yesterdays-sunset-dragonpoint-paintedwall-blackcanyonofthegunnison-canyon-colorado/ "12:33 pm") 
jQuery(document).ready(function(){
var gmap\_m7dcdf7bb405cdb6e880061efa247ba76 = {
positions : {
399 : new google.maps.LatLng( '38.488869182295', '-107.74033621979' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7dcdf7bb405cdb6e880061efa247ba76' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7dcdf7bb405cdb6e880061efa247ba76.positions ) {
gmap\_m7dcdf7bb405cdb6e880061efa247ba76.bounds.extend( gmap\_m7dcdf7bb405cdb6e880061efa247ba76.positions[m] );
}
// Render markers
for ( var m in gmap\_m7dcdf7bb405cdb6e880061efa247ba76.positions ) {
gmap\_m7dcdf7bb405cdb6e880061efa247ba76.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7dcdf7bb405cdb6e880061efa247ba76.map,
position : gmap\_m7dcdf7bb405cdb6e880061efa247ba76.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7dcdf7bb405cdb6e880061efa247ba76.map.setCenter( gmap\_m7dcdf7bb405cdb6e880061efa247ba76.positions[399] );
});