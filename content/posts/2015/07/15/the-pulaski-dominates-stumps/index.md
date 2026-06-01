---
title: ''
date: '2015-07-15T15:33:57+00:00'
format: image
service: instagram
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/07/11325288_408474729357457_1529304383_n.jpg?resize=640%2C640
---

[![The Pulaski dominates stumps!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/07/11325288_408474729357457_1529304383_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/07/15/the-pulaski-dominates-stumps/) 

The Pulaski dominates stumps!





Posted on [Instagram](https://instagram.com/p/5LAqk4imFE/) [3:33 pm, July 15, 2015](http://dentedreality.com.au/2015/07/15/the-pulaski-dominates-stumps/ "3:33 pm") 
jQuery(document).ready(function(){
var gmap\_mce2e38597f9bf0e108f61b3e39215361 = {
positions : {
152 : new google.maps.LatLng( '39.759913333', '-104.969528333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mce2e38597f9bf0e108f61b3e39215361' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mce2e38597f9bf0e108f61b3e39215361.positions ) {
gmap\_mce2e38597f9bf0e108f61b3e39215361.bounds.extend( gmap\_mce2e38597f9bf0e108f61b3e39215361.positions[m] );
}
// Render markers
for ( var m in gmap\_mce2e38597f9bf0e108f61b3e39215361.positions ) {
gmap\_mce2e38597f9bf0e108f61b3e39215361.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mce2e38597f9bf0e108f61b3e39215361.map,
position : gmap\_mce2e38597f9bf0e108f61b3e39215361.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mce2e38597f9bf0e108f61b3e39215361.map.setCenter( gmap\_mce2e38597f9bf0e108f61b3e39215361.positions[152] );
});