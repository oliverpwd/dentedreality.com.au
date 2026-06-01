---
title: Quarantine project complete. New pergola for the patio area. @tojagrid frame
  with custom diagonal slats.
date: '2020-04-01T14:09:53-06:00'
format: video
service: instagram
latitude: '39.7391'
longitude: '-104.9836'
---

<https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/04/03122829/91332028_652674875482255_8824208381062844614_n.mp4>

Quarantine project complete. New pergola for the patio area. @tojagrid frame with custom diagonal slats.

39.7391-104.9836
jQuery(document).ready(function(){
var gmap\_m56034dcc68fbe51266baca3eefe54b04 = {
positions : {
215 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m56034dcc68fbe51266baca3eefe54b04' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m56034dcc68fbe51266baca3eefe54b04.positions ) {
gmap\_m56034dcc68fbe51266baca3eefe54b04.bounds.extend( gmap\_m56034dcc68fbe51266baca3eefe54b04.positions[m] );
}
// Render markers
for ( var m in gmap\_m56034dcc68fbe51266baca3eefe54b04.positions ) {
gmap\_m56034dcc68fbe51266baca3eefe54b04.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m56034dcc68fbe51266baca3eefe54b04.map,
position : gmap\_m56034dcc68fbe51266baca3eefe54b04.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m56034dcc68fbe51266baca3eefe54b04.map.setCenter( gmap\_m56034dcc68fbe51266baca3eefe54b04.positions[215] );
});