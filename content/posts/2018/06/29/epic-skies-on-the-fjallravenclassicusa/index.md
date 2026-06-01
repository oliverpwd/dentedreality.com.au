---
title: ''
date: '2018-06-29T19:08:59-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.444'
longitude: '-106.326'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/35294133_648304398878122_9119983755904155648_n.jpg?resize=607%2C607&ssl=1
---

[![Epic skies on the #fjallravenclassicusa](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/35294133_648304398878122_9119983755904155648_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/epic-skies-on-the-fjallravenclassicusa/) 

[![Epic skies on the #fjallravenclassicusa](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/35294133_648304398878122_9119983755904155648_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkoTykDFfqZ/)

Epic skies on the #fjallravenclassicusa

39.444-106.326




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoTykDFfqZ/) [7:08 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/epic-skies-on-the-fjallravenclassicusa/ "7:08 pm") 
jQuery(document).ready(function(){
var gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d = {
positions : {
947 : new google.maps.LatLng( '39.444', '-106.326' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.positions ) {
gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.bounds.extend( gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.positions[m] );
}
// Render markers
for ( var m in gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.positions ) {
gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.map,
position : gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.map.setCenter( gmap\_m6e7be245ab8b6fac4cc262d5d8c0ec5d.positions[947] );
});