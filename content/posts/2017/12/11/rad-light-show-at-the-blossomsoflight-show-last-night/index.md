---
title: 'Rad light show at the #blossomsoflight show last night.'
date: '2017-12-11T21:31:50+00:00'
format: video
service: instagram
tags:
- blossomsoflight
---

<https://dentedreality.com.au/wp-content/uploads/2017/12/25027416_115323165924366_7861851547003518976_n.mp4>

Rad light show at the #blossomsoflight show last night.

jQuery(document).ready(function(){
var gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323 = {
positions : {
962 : new google.maps.LatLng( '39.73214416473', '-104.9607721189' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.positions ) {
gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.bounds.extend( gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.positions[m] );
}
// Render markers
for ( var m in gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.positions ) {
gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.map,
position : gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.map.setCenter( gmap\_m2d4fc2c2ea49f14f154e89ddd2c7d323.positions[962] );
});