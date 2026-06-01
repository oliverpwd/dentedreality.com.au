---
title: ''
date: '2018-10-27T15:34:41-06:00'
format: image
service: instagram
latitude: '39.7572'
longitude: '-104.967'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/10/14182049/43820763_577973712660053_3104604540515835135_n.jpg?resize=607%2C607&ssl=1
---

[![Halloweenies. The butternut is a reject from our garden.](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/10/14182049/43820763_577973712660053_3104604540515835135_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/10/27/halloweenies-the-butternut-is-a-reject-from-our-garden/) 

[![Halloweenies. The butternut is a reject from our garden.](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/10/14182049/43820763_577973712660053_3104604540515835135_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bpc6p8HALLx/)

Halloweenies. The butternut is a reject from our garden.

39.7572-104.967




Posted on [Instagram](https://www.instagram.com/p/Bpc6p8HALLx/) [3:34 pm, October 27, 2018](https://dentedreality.com.au/2018/10/27/halloweenies-the-butternut-is-a-reject-from-our-garden/ "3:34 pm") 
jQuery(document).ready(function(){
var gmap\_mc53658ab7cdb013bafb3018d5d5c6b75 = {
positions : {
126 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc53658ab7cdb013bafb3018d5d5c6b75' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.positions ) {
gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.bounds.extend( gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.positions[m] );
}
// Render markers
for ( var m in gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.positions ) {
gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.map,
position : gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.map.setCenter( gmap\_mc53658ab7cdb013bafb3018d5d5c6b75.positions[126] );
});