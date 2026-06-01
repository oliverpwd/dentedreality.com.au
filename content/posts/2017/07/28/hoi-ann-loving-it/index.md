---
title: Hoi Ann. Loving it.
date: '2017-07-28T22:08:58-06:00'
format: video
service: instagram
latitude: '39.76985'
longitude: '-104.97295'
---

<https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2017/07/14182411/20271362_1835203006809425_2866936750784118784_n.mp4>

Hoi Ann. Loving it.

39.76985-104.97295
jQuery(document).ready(function(){
var gmap\_m629268bd9c1d15b4b249ffcb6e477be6 = {
positions : {
175 : new google.maps.LatLng( '39.76985', '-104.97295' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m629268bd9c1d15b4b249ffcb6e477be6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m629268bd9c1d15b4b249ffcb6e477be6.positions ) {
gmap\_m629268bd9c1d15b4b249ffcb6e477be6.bounds.extend( gmap\_m629268bd9c1d15b4b249ffcb6e477be6.positions[m] );
}
// Render markers
for ( var m in gmap\_m629268bd9c1d15b4b249ffcb6e477be6.positions ) {
gmap\_m629268bd9c1d15b4b249ffcb6e477be6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m629268bd9c1d15b4b249ffcb6e477be6.map,
position : gmap\_m629268bd9c1d15b4b249ffcb6e477be6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m629268bd9c1d15b4b249ffcb6e477be6.map.setCenter( gmap\_m629268bd9c1d15b4b249ffcb6e477be6.positions[175] );
});