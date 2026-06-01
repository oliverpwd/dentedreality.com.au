---
title: Mass production pizza.
date: '2016-12-30T15:54:13+00:00'
format: video
service: instagram
---

<http://dentedreality.com.au/wp-content/uploads/2016/12/15819813_1218393051588528_7932294641360044032_n.mp4>

Mass production pizza.

jQuery(document).ready(function(){
var gmap\_me2694524a39df5c45074447e4f573d4c = {
positions : {
671 : new google.maps.LatLng( '39.78939', '-105.0826699' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me2694524a39df5c45074447e4f573d4c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me2694524a39df5c45074447e4f573d4c.positions ) {
gmap\_me2694524a39df5c45074447e4f573d4c.bounds.extend( gmap\_me2694524a39df5c45074447e4f573d4c.positions[m] );
}
// Render markers
for ( var m in gmap\_me2694524a39df5c45074447e4f573d4c.positions ) {
gmap\_me2694524a39df5c45074447e4f573d4c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me2694524a39df5c45074447e4f573d4c.map,
position : gmap\_me2694524a39df5c45074447e4f573d4c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me2694524a39df5c45074447e4f573d4c.map.setCenter( gmap\_me2694524a39df5c45074447e4f573d4c.positions[671] );
});