---
title: ''
date: '2018-12-28T19:19:39-06:00'
format: image
service: instagram
latitude: '39.731606'
longitude: '-104.95978'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181951/47344992_2226505237616386_6659245447468400035_n.jpg?resize=607%2C607&ssl=1
---

[![Chihuly at @denverbotanic](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181951/47344992_2226505237616386_6659245447468400035_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/12/28/chihuly-at-denverbotanic/) 

[![Chihuly at @denverbotanic](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181951/47344992_2226505237616386_6659245447468400035_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Br9EjcBghiI/)

Chihuly at @denverbotanic

39.731606-104.95978




Posted on [Instagram](https://www.instagram.com/p/Br9EjcBghiI/) [7:19 pm, December 28, 2018](https://dentedreality.com.au/2018/12/28/chihuly-at-denverbotanic/ "7:19 pm") 
jQuery(document).ready(function(){
var gmap\_mba347579cb63b8edc4c9677674312d74 = {
positions : {
995 : new google.maps.LatLng( '39.731606', '-104.95978' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mba347579cb63b8edc4c9677674312d74' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mba347579cb63b8edc4c9677674312d74.positions ) {
gmap\_mba347579cb63b8edc4c9677674312d74.bounds.extend( gmap\_mba347579cb63b8edc4c9677674312d74.positions[m] );
}
// Render markers
for ( var m in gmap\_mba347579cb63b8edc4c9677674312d74.positions ) {
gmap\_mba347579cb63b8edc4c9677674312d74.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mba347579cb63b8edc4c9677674312d74.map,
position : gmap\_mba347579cb63b8edc4c9677674312d74.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mba347579cb63b8edc4c9677674312d74.map.setCenter( gmap\_mba347579cb63b8edc4c9677674312d74.positions[995] );
});