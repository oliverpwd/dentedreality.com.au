---
title: ''
date: '2016-08-07T14:42:21+00:00'
format: image
service: instagram
tags:
- blackcanyon
- canyon
- colorado
- gunnisonriver
- river
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13704247_319503361715991_1731681336_n.jpg?fit=640%2C640
---

[![Absolutely ridiculously gorgeous canyon. Colorado is good at this. #colorado #canyon #blackcanyon #gunnisonriver #river](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13704247_319503361715991_1731681336_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/07/absolutely-ridiculously-gorgeous-canyon-colorado-is-good-at-this-colorado-canyon-blackcanyon-gunnisonriver-river/) 

Absolutely ridiculously gorgeous canyon. Colorado is good at this. #colorado #canyon #blackcanyon #gunnisonriver #river





* #[blackcanyon](http://dentedreality.com.au/tags/blackcanyon/)
* #[canyon](http://dentedreality.com.au/tags/canyon/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[gunnisonriver](http://dentedreality.com.au/tags/gunnisonriver/)
* #[river](http://dentedreality.com.au/tags/river/)

Posted on [Instagram](https://www.instagram.com/p/BI0j_DngQtK/) [2:42 pm, August 7, 2016](http://dentedreality.com.au/2016/08/07/absolutely-ridiculously-gorgeous-canyon-colorado-is-good-at-this-colorado-canyon-blackcanyon-gunnisonriver-river/ "2:42 pm") 
jQuery(document).ready(function(){
var gmap\_m8c43abdb85d024f1f29a08d508f91ee2 = {
positions : {
520 : new google.maps.LatLng( '38.4425', '-107.556' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8c43abdb85d024f1f29a08d508f91ee2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8c43abdb85d024f1f29a08d508f91ee2.positions ) {
gmap\_m8c43abdb85d024f1f29a08d508f91ee2.bounds.extend( gmap\_m8c43abdb85d024f1f29a08d508f91ee2.positions[m] );
}
// Render markers
for ( var m in gmap\_m8c43abdb85d024f1f29a08d508f91ee2.positions ) {
gmap\_m8c43abdb85d024f1f29a08d508f91ee2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8c43abdb85d024f1f29a08d508f91ee2.map,
position : gmap\_m8c43abdb85d024f1f29a08d508f91ee2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8c43abdb85d024f1f29a08d508f91ee2.map.setCenter( gmap\_m8c43abdb85d024f1f29a08d508f91ee2.positions[520] );
});