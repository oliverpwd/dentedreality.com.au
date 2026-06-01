---
title: ''
date: '2012-11-30T23:08:09+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/55b9ffc23b6411e2b85522000a9e28f2_7.jpg?resize=607%2C607
---

[![Voodoo Gumbo.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/55b9ffc23b6411e2b85522000a9e28f2_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/30/voodoo-gumbo/) 

Voodoo Gumbo.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SraLACCmKv/) [11:08 pm, November 30, 2012](http://dentedreality.com.au/2012/11/30/voodoo-gumbo/ "11:08 pm") 
jQuery(document).ready(function(){
var gmap\_mf7361de6e6c50ba4c42d3838b918c577 = {
positions : {
297 : new google.maps.LatLng( '29.95815175', '-90.06314' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf7361de6e6c50ba4c42d3838b918c577' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf7361de6e6c50ba4c42d3838b918c577.positions ) {
gmap\_mf7361de6e6c50ba4c42d3838b918c577.bounds.extend( gmap\_mf7361de6e6c50ba4c42d3838b918c577.positions[m] );
}
// Render markers
for ( var m in gmap\_mf7361de6e6c50ba4c42d3838b918c577.positions ) {
gmap\_mf7361de6e6c50ba4c42d3838b918c577.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf7361de6e6c50ba4c42d3838b918c577.map,
position : gmap\_mf7361de6e6c50ba4c42d3838b918c577.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf7361de6e6c50ba4c42d3838b918c577.map.setCenter( gmap\_mf7361de6e6c50ba4c42d3838b918c577.positions[297] );
});