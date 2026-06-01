---
title: ''
date: '2017-01-21T11:33:30+00:00'
format: image
service: instagram
tags:
- womensmarch
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/16122457_213416562457075_6778631868347580416_n.jpg?fit=640%2C640
---

[![Denver Downtown is lit #womensmarch](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/16122457_213416562457075_6778631868347580416_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/01/21/denver-downtown-is-lit-womensmarch/) 

Denver Downtown is lit #womensmarch





* #[womensmarch](http://dentedreality.com.au/tags/womensmarch/)

Posted on [Instagram](https://www.instagram.com/p/BPiV_g_jVRJ/) [11:33 am, January 21, 2017](http://dentedreality.com.au/2017/01/21/denver-downtown-is-lit-womensmarch/ "11:33 am") 
jQuery(document).ready(function(){
var gmap\_me07140c36931067d28f13b98100cebad = {
positions : {
560 : new google.maps.LatLng( '39.7392', '-104.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me07140c36931067d28f13b98100cebad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me07140c36931067d28f13b98100cebad.positions ) {
gmap\_me07140c36931067d28f13b98100cebad.bounds.extend( gmap\_me07140c36931067d28f13b98100cebad.positions[m] );
}
// Render markers
for ( var m in gmap\_me07140c36931067d28f13b98100cebad.positions ) {
gmap\_me07140c36931067d28f13b98100cebad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me07140c36931067d28f13b98100cebad.map,
position : gmap\_me07140c36931067d28f13b98100cebad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me07140c36931067d28f13b98100cebad.map.setCenter( gmap\_me07140c36931067d28f13b98100cebad.positions[560] );
});