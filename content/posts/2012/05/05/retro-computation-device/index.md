---
title: ''
date: '2012-05-05T16:50:52+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/00ef6f9696f411e1b10e123138105d6b_7.jpg?resize=607%2C607
---

[![Retro Computation Device.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/00ef6f9696f411e1b10e123138105d6b_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/05/05/retro-computation-device/) 

Retro Computation Device.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/KQk23vimKc/) [4:50 pm, May 5, 2012](http://dentedreality.com.au/2012/05/05/retro-computation-device/ "4:50 pm") 
jQuery(document).ready(function(){
var gmap\_mdeb7b9771edd0e7909e48f46bc6061ff = {
positions : {
913 : new google.maps.LatLng( '37.755332946', '-122.420669555' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdeb7b9771edd0e7909e48f46bc6061ff' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.positions ) {
gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.bounds.extend( gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.positions[m] );
}
// Render markers
for ( var m in gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.positions ) {
gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.map,
position : gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.map.setCenter( gmap\_mdeb7b9771edd0e7909e48f46bc6061ff.positions[913] );
});