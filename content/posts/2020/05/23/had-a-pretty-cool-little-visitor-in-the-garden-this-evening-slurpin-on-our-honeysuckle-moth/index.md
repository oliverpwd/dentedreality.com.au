---
title: 'Had a pretty cool little visitor in the garden this evening, slurpin’ on our
  honeysuckle. #moth'
date: '2020-05-23T20:11:53-06:00'
format: video
service: instagram
tags:
- moth
latitude: '39.7572'
longitude: '-104.967'
---

https://scontent.cdninstagram.com/v/t50.2886-16/98176221\_1185865921779341\_1219548950954559011\_n.mp4?\_nc\_ht=scontent.cdninstagram.com&\_nc\_ohc=qHlN50Nhlc8AX\_jsZvA&oe=5ECBD798&oh=258bb8055963c8a939791ec353d0ccea

Had a pretty cool little visitor in the garden this evening, slurpin’ on our honeysuckle. #moth

39.7572-104.967
jQuery(document).ready(function(){
var gmap\_m45197d8dbea7668015202ae7c29df75b = {
positions : {
858 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m45197d8dbea7668015202ae7c29df75b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m45197d8dbea7668015202ae7c29df75b.positions ) {
gmap\_m45197d8dbea7668015202ae7c29df75b.bounds.extend( gmap\_m45197d8dbea7668015202ae7c29df75b.positions[m] );
}
// Render markers
for ( var m in gmap\_m45197d8dbea7668015202ae7c29df75b.positions ) {
gmap\_m45197d8dbea7668015202ae7c29df75b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m45197d8dbea7668015202ae7c29df75b.map,
position : gmap\_m45197d8dbea7668015202ae7c29df75b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m45197d8dbea7668015202ae7c29df75b.map.setCenter( gmap\_m45197d8dbea7668015202ae7c29df75b.positions[858] );
});