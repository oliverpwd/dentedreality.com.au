---
title: ''
date: '2012-08-02T17:06:20+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/e8c40548dce511e1b17a22000a1cdd10_7.jpg?resize=607%2C607
---

[![Making things better.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/e8c40548dce511e1b17a22000a1cdd10_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/02/making-things-better/) 

Making things better.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/N1xYAzimHm/) [5:06 pm, August 2, 2012](http://dentedreality.com.au/2012/08/02/making-things-better/ "5:06 pm") 
jQuery(document).ready(function(){
var gmap\_mf1e2f0630a112ce3c509c662aeec6850 = {
positions : {
762 : new google.maps.LatLng( '40.64325159', '-73.779408038' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf1e2f0630a112ce3c509c662aeec6850' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf1e2f0630a112ce3c509c662aeec6850.positions ) {
gmap\_mf1e2f0630a112ce3c509c662aeec6850.bounds.extend( gmap\_mf1e2f0630a112ce3c509c662aeec6850.positions[m] );
}
// Render markers
for ( var m in gmap\_mf1e2f0630a112ce3c509c662aeec6850.positions ) {
gmap\_mf1e2f0630a112ce3c509c662aeec6850.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf1e2f0630a112ce3c509c662aeec6850.map,
position : gmap\_mf1e2f0630a112ce3c509c662aeec6850.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf1e2f0630a112ce3c509c662aeec6850.map.setCenter( gmap\_mf1e2f0630a112ce3c509c662aeec6850.positions[762] );
});