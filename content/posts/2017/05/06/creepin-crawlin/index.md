---
title: Creepin. Crawlin.
date: '2017-05-06T12:38:29+00:00'
format: video
service: instagram
---

<https://scontent.cdninstagram.com/t50.2886-16/18343728_1956926234529666_5319050291511820288_n.mp4>

Creepin. Crawlin.

jQuery(document).ready(function(){
var gmap\_m7ed7c539a2216bcd080ac7ef47084cbe = {
positions : {
475 : new google.maps.LatLng( '39.710432295834', '-105.01383279153' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7ed7c539a2216bcd080ac7ef47084cbe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.positions ) {
gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.bounds.extend( gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.positions[m] );
}
// Render markers
for ( var m in gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.positions ) {
gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.map,
position : gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.map.setCenter( gmap\_m7ed7c539a2216bcd080ac7ef47084cbe.positions[475] );
});