---
title: 'To the stars. #stars #space #art'
date: '2016-11-22T12:37:25-07:00'
format: video
service: instagram
tags:
- art
- space
- stars
latitude: '38.8913594'
longitude: '-77.0199482'
---

<https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2016/11/14182415/15192397_210204466093374_3897248733070360576_n-1.mp4>

To the stars. #stars #space #art

38.8913594-77.0199482
jQuery(document).ready(function(){
var gmap\_md2cbbe32f71092c57565094595b8ff01 = {
positions : {
717 : new google.maps.LatLng( '38.891359415', '-77.019948174347' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md2cbbe32f71092c57565094595b8ff01' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md2cbbe32f71092c57565094595b8ff01.positions ) {
gmap\_md2cbbe32f71092c57565094595b8ff01.bounds.extend( gmap\_md2cbbe32f71092c57565094595b8ff01.positions[m] );
}
// Render markers
for ( var m in gmap\_md2cbbe32f71092c57565094595b8ff01.positions ) {
gmap\_md2cbbe32f71092c57565094595b8ff01.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md2cbbe32f71092c57565094595b8ff01.map,
position : gmap\_md2cbbe32f71092c57565094595b8ff01.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md2cbbe32f71092c57565094595b8ff01.map.setCenter( gmap\_md2cbbe32f71092c57565094595b8ff01.positions[717] );
});