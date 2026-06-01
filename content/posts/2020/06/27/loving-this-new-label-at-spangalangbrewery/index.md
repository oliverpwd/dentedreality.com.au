---
title: Loving this new label at @spangalangbrewery !
date: '2020-06-27T19:29:15-06:00'
format: video
service: instagram
latitude: '39.7552419'
longitude: '-104.9770576'
---

https://scontent.cdninstagram.com/v/t50.2886-16/105330423\_579297246107529\_8734484796582320243\_n.mp4?\_nc\_ht=scontent.cdninstagram.com&\_nc\_ohc=l7Kkkm21wM0AX\_6gTq4&oe=5EFA241F&oh=71a22a01cef7187805081caaf699bad3

Loving this new label at @spangalangbrewery !

39.7552419-104.9770576
jQuery(document).ready(function(){
var gmap\_me553738f6e4f375e658824a787ada88b = {
positions : {
570 : new google.maps.LatLng( '39.7552419', '-104.9770576' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me553738f6e4f375e658824a787ada88b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me553738f6e4f375e658824a787ada88b.positions ) {
gmap\_me553738f6e4f375e658824a787ada88b.bounds.extend( gmap\_me553738f6e4f375e658824a787ada88b.positions[m] );
}
// Render markers
for ( var m in gmap\_me553738f6e4f375e658824a787ada88b.positions ) {
gmap\_me553738f6e4f375e658824a787ada88b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me553738f6e4f375e658824a787ada88b.map,
position : gmap\_me553738f6e4f375e658824a787ada88b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me553738f6e4f375e658824a787ada88b.map.setCenter( gmap\_me553738f6e4f375e658824a787ada88b.positions[570] );
});