---
title: ''
date: '2018-11-18T17:22:56-06:00'
format: image
service: instagram
tags:
- Denver
- drone
- dronephotography
- dronestagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/11/14182039/44874355_497003777375598_6297924503822475485_n.jpg?resize=607%2C607&ssl=1
---

[![Denver sunset skyline. Taken with new @djiglobal Mavic Air #drone #dronephotography #denver #dronestagram](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/11/14182039/44874355_497003777375598_6297924503822475485_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/11/18/denver-sunset-skyline-taken-with-new-djiglobal-mavic-air-drone-dronephotography-denver-dronestagram/) 

[![Denver sunset skyline. Taken with new @djiglobal Mavic Air #drone #dronephotography #denver #dronestagram](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/11/14182039/44874355_497003777375598_6297924503822475485_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BqV3ZeuAq-n/)

Denver sunset skyline. Taken with new @djiglobal Mavic Air #drone #dronephotography #denver #dronestagram

39.7391-104.9836




* #[Denver](https://dentedreality.com.au/tags/denver/)
* #[drone](https://dentedreality.com.au/tags/drone/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)

Posted on [Instagram](https://www.instagram.com/p/BqV3ZeuAq-n/) [5:22 pm, November 18, 2018](https://dentedreality.com.au/2018/11/18/denver-sunset-skyline-taken-with-new-djiglobal-mavic-air-drone-dronephotography-denver-dronestagram/ "5:22 pm") 
jQuery(document).ready(function(){
var gmap\_mc1483186d3eb2f353a34e80d726c2148 = {
positions : {
917 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc1483186d3eb2f353a34e80d726c2148' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc1483186d3eb2f353a34e80d726c2148.positions ) {
gmap\_mc1483186d3eb2f353a34e80d726c2148.bounds.extend( gmap\_mc1483186d3eb2f353a34e80d726c2148.positions[m] );
}
// Render markers
for ( var m in gmap\_mc1483186d3eb2f353a34e80d726c2148.positions ) {
gmap\_mc1483186d3eb2f353a34e80d726c2148.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc1483186d3eb2f353a34e80d726c2148.map,
position : gmap\_mc1483186d3eb2f353a34e80d726c2148.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc1483186d3eb2f353a34e80d726c2148.map.setCenter( gmap\_mc1483186d3eb2f353a34e80d726c2148.positions[917] );
});