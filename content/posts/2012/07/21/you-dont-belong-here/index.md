---
title: ''
date: '2012-07-21T17:49:55+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/01fcc3aed37e11e1b7ea22000a1cbb16_7.jpg?resize=607%2C607
---

[![You don't belong here.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/01fcc3aed37e11e1b7ea22000a1cbb16_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/07/21/you-dont-belong-here/) 

You don’t belong here.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/NW80oKCmCw/) [5:49 pm, July 21, 2012](http://dentedreality.com.au/2012/07/21/you-dont-belong-here/ "5:49 pm") 
jQuery(document).ready(function(){
var gmap\_ma8be7d3a553f93c8e9b91302a2d118af = {
positions : {
733 : new google.maps.LatLng( '40.670267552', '-73.989776373' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8be7d3a553f93c8e9b91302a2d118af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8be7d3a553f93c8e9b91302a2d118af.positions ) {
gmap\_ma8be7d3a553f93c8e9b91302a2d118af.bounds.extend( gmap\_ma8be7d3a553f93c8e9b91302a2d118af.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8be7d3a553f93c8e9b91302a2d118af.positions ) {
gmap\_ma8be7d3a553f93c8e9b91302a2d118af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8be7d3a553f93c8e9b91302a2d118af.map,
position : gmap\_ma8be7d3a553f93c8e9b91302a2d118af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8be7d3a553f93c8e9b91302a2d118af.map.setCenter( gmap\_ma8be7d3a553f93c8e9b91302a2d118af.positions[733] );
});