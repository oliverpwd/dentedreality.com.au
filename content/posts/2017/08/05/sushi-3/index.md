---
title: ''
date: '2017-08-05T05:30:47+00:00'
format: image
service: instagram
image: https://dentedreality.com.au/wp-content/uploads/2017/08/20635113_159259267973842_4263618407015907328_n.jpg
---

[![Sushi](https://dentedreality.com.au/wp-content/uploads/2017/08/20635113_159259267973842_4263618407015907328_n.jpg)](https://dentedreality.com.au/2017/08/05/sushi-3/) 

[![Sushi](https://dentedreality.com.au/wp-content/uploads/2017/08/20635113_159259267973842_4263618407015907328_n.jpg)](https://www.instagram.com/p/BXaRa8Ohzwg/)

Sushi





Posted on [Instagram](https://www.instagram.com/p/BXaRa8Ohzwg/) [5:30 am, August 5, 2017](https://dentedreality.com.au/2017/08/05/sushi-3/ "5:30 am") 
jQuery(document).ready(function(){
var gmap\_mbbbc39360fd29bd0999880b0fca2bb24 = {
positions : {
750 : new google.maps.LatLng( '52.361659686179', '4.8825574754137' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbbbc39360fd29bd0999880b0fca2bb24' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbbbc39360fd29bd0999880b0fca2bb24.positions ) {
gmap\_mbbbc39360fd29bd0999880b0fca2bb24.bounds.extend( gmap\_mbbbc39360fd29bd0999880b0fca2bb24.positions[m] );
}
// Render markers
for ( var m in gmap\_mbbbc39360fd29bd0999880b0fca2bb24.positions ) {
gmap\_mbbbc39360fd29bd0999880b0fca2bb24.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbbbc39360fd29bd0999880b0fca2bb24.map,
position : gmap\_mbbbc39360fd29bd0999880b0fca2bb24.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbbbc39360fd29bd0999880b0fca2bb24.map.setCenter( gmap\_mbbbc39360fd29bd0999880b0fca2bb24.positions[750] );
});