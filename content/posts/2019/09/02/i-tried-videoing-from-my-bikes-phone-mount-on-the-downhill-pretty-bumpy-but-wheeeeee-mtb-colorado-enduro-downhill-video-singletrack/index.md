---
title: 'I tried videoing from my bike’s phone mount on the downhill. Pretty bumpy,
  but — wheeeeee! #mtb #colorado #enduro #downhill #video #singletrack'
date: '2019-09-02T16:33:36-06:00'
format: video
service: instagram
tags:
- colorado
- downhill
- enduro
- mtb
- singletrack
- video
latitude: '39.4078'
longitude: '-105.171'
---

https://scontent.cdninstagram.com/v/t50.2886-16/70062041\_376896642956518\_8456465293877072941\_n.mp4?\_nc\_ht=scontent.cdninstagram.com&oe=5D70483E&oh=852797f0f0db0e97f60dd36215dc4ce4

I tried videoing from my bike’s phone mount on the downhill. Pretty bumpy, but — wheeeeee! #mtb #colorado #enduro #downhill #video #singletrack

39.4078-105.171
jQuery(document).ready(function(){
var gmap\_m17c033b47358098c7edc1e1bd117eb30 = {
positions : {
826 : new google.maps.LatLng( '39.4078', '-105.171' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m17c033b47358098c7edc1e1bd117eb30' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m17c033b47358098c7edc1e1bd117eb30.positions ) {
gmap\_m17c033b47358098c7edc1e1bd117eb30.bounds.extend( gmap\_m17c033b47358098c7edc1e1bd117eb30.positions[m] );
}
// Render markers
for ( var m in gmap\_m17c033b47358098c7edc1e1bd117eb30.positions ) {
gmap\_m17c033b47358098c7edc1e1bd117eb30.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m17c033b47358098c7edc1e1bd117eb30.map,
position : gmap\_m17c033b47358098c7edc1e1bd117eb30.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m17c033b47358098c7edc1e1bd117eb30.map.setCenter( gmap\_m17c033b47358098c7edc1e1bd117eb30.positions[826] );
});