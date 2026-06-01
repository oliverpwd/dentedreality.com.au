---
title: 'Epic Giant Slide Races #jillandkai16616'
date: '2016-06-18T08:28:21-06:00'
format: video
service: instagram
tags:
- jillandkai16616
latitude: '-26.74924'
longitude: '153.04596'
---

<https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2016/06/14182417/13475386_584338951746197_191581269_n-1.mp4>

Epic Giant Slide Races #jillandkai16616

-26.74924153.04596
jQuery(document).ready(function(){
var gmap\_meca062a1b0eae8d326d86c3a84f061b2 = {
positions : {
102 : new google.maps.LatLng( '-26.74924', '153.04596' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meca062a1b0eae8d326d86c3a84f061b2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meca062a1b0eae8d326d86c3a84f061b2.positions ) {
gmap\_meca062a1b0eae8d326d86c3a84f061b2.bounds.extend( gmap\_meca062a1b0eae8d326d86c3a84f061b2.positions[m] );
}
// Render markers
for ( var m in gmap\_meca062a1b0eae8d326d86c3a84f061b2.positions ) {
gmap\_meca062a1b0eae8d326d86c3a84f061b2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meca062a1b0eae8d326d86c3a84f061b2.map,
position : gmap\_meca062a1b0eae8d326d86c3a84f061b2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meca062a1b0eae8d326d86c3a84f061b2.map.setCenter( gmap\_meca062a1b0eae8d326d86c3a84f061b2.positions[102] );
});