---
title: ''
date: '2018-12-01T14:02:40-06:00'
format: image
service: instagram
tags:
- dji
- drone
- mavicair
latitude: '39.7604294'
longitude: '-104.9768295'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14182037/46332104_210962939695834_2457103594997108781_n.jpg?resize=607%2C607&ssl=1
---

[![It me. Taken on a @dji_mavic_air_photography #dji #drone #mavicair](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14182037/46332104_210962939695834_2457103594997108781_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/12/01/it-me-taken-on-a-dji_mavic_air_photography-dji-drone-mavicair/) 

[![It me. Taken on a @dji_mavic_air_photography #dji #drone #mavicair](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14182037/46332104_210962939695834_2457103594997108781_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bq2-0GmgT14/)

It me. Taken on a @dji\_mavic\_air\_photography #dji #drone #mavicair

39.7604294-104.9768295




* #[dji](https://dentedreality.com.au/tags/dji/)
* #[drone](https://dentedreality.com.au/tags/drone/)
* #[mavicair](https://dentedreality.com.au/tags/mavicair/)

Posted on [Instagram](https://www.instagram.com/p/Bq2-0GmgT14/) [2:02 pm, December 1, 2018](https://dentedreality.com.au/2018/12/01/it-me-taken-on-a-dji_mavic_air_photography-dji-drone-mavicair/ "2:02 pm") 
jQuery(document).ready(function(){
var gmap\_mc13314c9c8761852abe3d0b26cfdbe07 = {
positions : {
512 : new google.maps.LatLng( '39.7604294', '-104.9768295' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc13314c9c8761852abe3d0b26cfdbe07' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc13314c9c8761852abe3d0b26cfdbe07.positions ) {
gmap\_mc13314c9c8761852abe3d0b26cfdbe07.bounds.extend( gmap\_mc13314c9c8761852abe3d0b26cfdbe07.positions[m] );
}
// Render markers
for ( var m in gmap\_mc13314c9c8761852abe3d0b26cfdbe07.positions ) {
gmap\_mc13314c9c8761852abe3d0b26cfdbe07.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc13314c9c8761852abe3d0b26cfdbe07.map,
position : gmap\_mc13314c9c8761852abe3d0b26cfdbe07.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc13314c9c8761852abe3d0b26cfdbe07.map.setCenter( gmap\_mc13314c9c8761852abe3d0b26cfdbe07.positions[512] );
});