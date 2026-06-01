---
title: John Wayne!
date: '2019-08-08T17:49:47-06:00'
format: video
service: instagram
latitude: '38.4547'
longitude: '-107.327'
---

https://scontent.cdninstagram.com/v/t50.2886-16/68826435\_2090959341199899\_5959889929884951687\_n.mp4?\_nc\_ht=scontent.cdninstagram.com&oe=5D4EBAC1&oh=f9f3b1cc3f12f1c797b1e34d41c3ed60

John Wayne!

38.4547-107.327
jQuery(document).ready(function(){
var gmap\_m9e58ad5f9486794c95bb98ee5464cd25 = {
positions : {
169 : new google.maps.LatLng( '38.4547', '-107.327' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9e58ad5f9486794c95bb98ee5464cd25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9e58ad5f9486794c95bb98ee5464cd25.positions ) {
gmap\_m9e58ad5f9486794c95bb98ee5464cd25.bounds.extend( gmap\_m9e58ad5f9486794c95bb98ee5464cd25.positions[m] );
}
// Render markers
for ( var m in gmap\_m9e58ad5f9486794c95bb98ee5464cd25.positions ) {
gmap\_m9e58ad5f9486794c95bb98ee5464cd25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9e58ad5f9486794c95bb98ee5464cd25.map,
position : gmap\_m9e58ad5f9486794c95bb98ee5464cd25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9e58ad5f9486794c95bb98ee5464cd25.map.setCenter( gmap\_m9e58ad5f9486794c95bb98ee5464cd25.positions[169] );
});