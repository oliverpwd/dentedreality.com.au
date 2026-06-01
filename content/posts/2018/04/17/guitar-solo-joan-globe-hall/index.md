---
title: Guitar Solo! Joan @ Globe Hall
date: '2018-04-17T23:58:11+00:00'
format: video
service: instagram
---

<https://scontent.cdninstagram.com/vp/b257653cb004377f4bca46b2cb38eb4f/5AD965EF/t50.2886-16/30210065_163108794377169_2904808144607641600_n.mp4>

Guitar Solo! Joan @ Globe Hall

jQuery(document).ready(function(){
var gmap\_m2a99d0c3f29474d990e5fb2d81926907 = {
positions : {
321 : new google.maps.LatLng( '39.7780113', '-104.9825363' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2a99d0c3f29474d990e5fb2d81926907' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2a99d0c3f29474d990e5fb2d81926907.positions ) {
gmap\_m2a99d0c3f29474d990e5fb2d81926907.bounds.extend( gmap\_m2a99d0c3f29474d990e5fb2d81926907.positions[m] );
}
// Render markers
for ( var m in gmap\_m2a99d0c3f29474d990e5fb2d81926907.positions ) {
gmap\_m2a99d0c3f29474d990e5fb2d81926907.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2a99d0c3f29474d990e5fb2d81926907.map,
position : gmap\_m2a99d0c3f29474d990e5fb2d81926907.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2a99d0c3f29474d990e5fb2d81926907.map.setCenter( gmap\_m2a99d0c3f29474d990e5fb2d81926907.positions[321] );
});