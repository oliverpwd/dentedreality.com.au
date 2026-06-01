---
title: ''
date: '2016-09-18T22:33:52+00:00'
format: image
service: instagram
tags:
- a8cgm
- viaferrata
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14288070_1785309675022579_3761451_n.jpg?fit=640%2C640
---

[![Just out here climbing a mountain! #viaferrata](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14288070_1785309675022579_3761451_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/18/just-out-here-climbing-a-mountain-viaferrata/) 

Just out here climbing a mountain! #viaferrata





* #[a8cgm](http://dentedreality.com.au/tags/a8cgm/)
* #[viaferrata](http://dentedreality.com.au/tags/viaferrata/)

Posted on [Instagram](https://www.instagram.com/p/BKhjVQ1gkiz/) [10:33 pm, September 18, 2016](http://dentedreality.com.au/2016/09/18/just-out-here-climbing-a-mountain-viaferrata/ "10:33 pm") 
jQuery(document).ready(function(){
var gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6 = {
positions : {
413 : new google.maps.LatLng( '50.059217094344', '-122.95837573589' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.positions ) {
gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.bounds.extend( gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.positions[m] );
}
// Render markers
for ( var m in gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.positions ) {
gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.map,
position : gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.map.setCenter( gmap\_m3fe81bb80824ca6e3963f83d5e1e2dd6.positions[413] );
});