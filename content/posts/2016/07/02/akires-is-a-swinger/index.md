---
title: '@akires is a swinger'
date: '2016-07-02T06:16:38-06:00'
format: video
service: instagram
latitude: '-33.7193504'
longitude: '150.3223934'
---

<https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2016/07/14182417/13593308_1124652860891109_854070849_n-1.mp4>

@akires is a swinger

-33.7193504150.3223934
jQuery(document).ready(function(){
var gmap\_m0445bc813461f09d4b4653774a2d27bf = {
positions : {
1000 : new google.maps.LatLng( '-33.719350413941', '150.32239338759' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0445bc813461f09d4b4653774a2d27bf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0445bc813461f09d4b4653774a2d27bf.positions ) {
gmap\_m0445bc813461f09d4b4653774a2d27bf.bounds.extend( gmap\_m0445bc813461f09d4b4653774a2d27bf.positions[m] );
}
// Render markers
for ( var m in gmap\_m0445bc813461f09d4b4653774a2d27bf.positions ) {
gmap\_m0445bc813461f09d4b4653774a2d27bf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0445bc813461f09d4b4653774a2d27bf.map,
position : gmap\_m0445bc813461f09d4b4653774a2d27bf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0445bc813461f09d4b4653774a2d27bf.map.setCenter( gmap\_m0445bc813461f09d4b4653774a2d27bf.positions[1000] );
});