---
title: ''
date: '2011-12-24T03:31:34+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/4e6d44de2e0111e1a87612313804ec91_7.jpg?resize=607%2C607
---

[![Christmas Loot](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/4e6d44de2e0111e1a87612313804ec91_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/12/24/christmas-loot/) 

Christmas Loot





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/bHN4f/) [3:31 am, December 24, 2011](http://dentedreality.com.au/2011/12/24/christmas-loot/ "3:31 am") 
jQuery(document).ready(function(){
var gmap\_m0851ee15e6a08c03ecc118f85745cfd5 = {
positions : {
53 : new google.maps.LatLng( '37.73583', '-122.4338' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0851ee15e6a08c03ecc118f85745cfd5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0851ee15e6a08c03ecc118f85745cfd5.positions ) {
gmap\_m0851ee15e6a08c03ecc118f85745cfd5.bounds.extend( gmap\_m0851ee15e6a08c03ecc118f85745cfd5.positions[m] );
}
// Render markers
for ( var m in gmap\_m0851ee15e6a08c03ecc118f85745cfd5.positions ) {
gmap\_m0851ee15e6a08c03ecc118f85745cfd5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0851ee15e6a08c03ecc118f85745cfd5.map,
position : gmap\_m0851ee15e6a08c03ecc118f85745cfd5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0851ee15e6a08c03ecc118f85745cfd5.map.setCenter( gmap\_m0851ee15e6a08c03ecc118f85745cfd5.positions[53] );
});