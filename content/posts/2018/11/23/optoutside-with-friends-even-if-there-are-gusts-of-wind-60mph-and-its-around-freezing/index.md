---
title: ''
date: '2018-11-23T20:11:25-06:00'
format: image
service: instagram
tags:
- optoutside
latitude: '39.6353549'
longitude: '-105.2792674'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/11/14182039/46014668_1914790748636227_3867284083068002512_n-1.jpg?resize=607%2C604&ssl=1
---

[![#optoutside with friends, even if there are gusts of wind 60mph and it's around freezing!](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/11/14182039/46014668_1914790748636227_3867284083068002512_n-1.jpg?resize=607%2C604&ssl=1)](https://dentedreality.com.au/2018/11/23/optoutside-with-friends-even-if-there-are-gusts-of-wind-60mph-and-its-around-freezing/) 

[![#optoutside with friends, even if there are gusts of wind 60mph and it's around freezing!](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/11/14182039/46014668_1914790748636227_3867284083068002512_n-1.jpg?resize=607%2C604&ssl=1)](https://www.instagram.com/p/BqjCp9GA5Vx/)

#optoutside with friends, even if there are gusts of wind 60mph and it’s around freezing!

39.6353549-105.2792674




* #[optoutside](https://dentedreality.com.au/tags/optoutside/)

Posted on [Instagram](https://www.instagram.com/p/BqjCp9GA5Vx/) [8:11 pm, November 23, 2018](https://dentedreality.com.au/2018/11/23/optoutside-with-friends-even-if-there-are-gusts-of-wind-60mph-and-its-around-freezing/ "8:11 pm") 
jQuery(document).ready(function(){
var gmap\_m66bc6bbd297ecf3319d1cbd79f50784c = {
positions : {
28 : new google.maps.LatLng( '39.6353549', '-105.2792674' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m66bc6bbd297ecf3319d1cbd79f50784c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.positions ) {
gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.bounds.extend( gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.positions[m] );
}
// Render markers
for ( var m in gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.positions ) {
gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.map,
position : gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.map.setCenter( gmap\_m66bc6bbd297ecf3319d1cbd79f50784c.positions[28] );
});