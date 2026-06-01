---
title: 'Droning inside for new year’s. Seems like a good idea. #dronephotography #djimavicair'
date: '2019-01-01T00:24:41-06:00'
format: video
service: instagram
tags:
- djimavicair
- dronephotography
latitude: '39.7572'
longitude: '-104.967'
---

https://scontent.cdninstagram.com/vp/2adc89cf370a7dc223c65cddf432a0cf/5C2DE589/t50.2886-16/49548580\_2206310036253594\_5089281214896930816\_n.mp4?\_nc\_ht=scontent.cdninstagram.com

Droning inside for new year’s. Seems like a good idea. #dronephotography #djimavicair

39.7572-104.967
jQuery(document).ready(function(){
var gmap\_m1a293357e62c53ba8a787a140e61a778 = {
positions : {
885 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1a293357e62c53ba8a787a140e61a778' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1a293357e62c53ba8a787a140e61a778.positions ) {
gmap\_m1a293357e62c53ba8a787a140e61a778.bounds.extend( gmap\_m1a293357e62c53ba8a787a140e61a778.positions[m] );
}
// Render markers
for ( var m in gmap\_m1a293357e62c53ba8a787a140e61a778.positions ) {
gmap\_m1a293357e62c53ba8a787a140e61a778.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1a293357e62c53ba8a787a140e61a778.map,
position : gmap\_m1a293357e62c53ba8a787a140e61a778.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1a293357e62c53ba8a787a140e61a778.map.setCenter( gmap\_m1a293357e62c53ba8a787a140e61a778.positions[885] );
});