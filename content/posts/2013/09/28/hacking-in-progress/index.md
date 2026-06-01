---
title: ''
date: '2013-09-28T14:39:19+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/49586aec286d11e385a622000a1f9e5b_8.jpg?resize=640%2C640
---

[![Hacking in progress.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/49586aec286d11e385a622000a1f9e5b_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/09/28/hacking-in-progress/) 

Hacking in progress.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/e0IAehimPB/) [2:39 pm, September 28, 2013](http://dentedreality.com.au/2013/09/28/hacking-in-progress/ "2:39 pm") 
jQuery(document).ready(function(){
var gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659 = {
positions : {
838 : new google.maps.LatLng( '37.784147778', '-122.397345208' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.positions ) {
gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.bounds.extend( gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.positions[m] );
}
// Render markers
for ( var m in gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.positions ) {
gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.map,
position : gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.map.setCenter( gmap\_m1b3fdfa8be68f5b6b8f141579e0f0659.positions[838] );
});