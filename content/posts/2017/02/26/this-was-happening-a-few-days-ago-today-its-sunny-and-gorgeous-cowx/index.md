---
title: 'This was happening a few days ago. Today it’s sunny and gorgeous. #cowx'
date: '2017-02-26T10:40:16+00:00'
format: video
service: instagram
tags:
- cowx
---

<http://dentedreality.com.au/wp-content/uploads/2017/02/16995142_863580967115146_6529591715857170432_n-1.mp4>

This was happening a few days ago. Today it’s sunny and gorgeous. #cowx

jQuery(document).ready(function(){
var gmap\_mea0181fac987c97c4618ad8135108d95 = {
positions : {
105 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mea0181fac987c97c4618ad8135108d95' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mea0181fac987c97c4618ad8135108d95.positions ) {
gmap\_mea0181fac987c97c4618ad8135108d95.bounds.extend( gmap\_mea0181fac987c97c4618ad8135108d95.positions[m] );
}
// Render markers
for ( var m in gmap\_mea0181fac987c97c4618ad8135108d95.positions ) {
gmap\_mea0181fac987c97c4618ad8135108d95.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mea0181fac987c97c4618ad8135108d95.map,
position : gmap\_mea0181fac987c97c4618ad8135108d95.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mea0181fac987c97c4618ad8135108d95.map.setCenter( gmap\_mea0181fac987c97c4618ad8135108d95.positions[105] );
});