---
title: ''
date: '2016-06-18T08:25:59-06:00'
format: image
service: instagram
latitude: '-26.8391448'
longitude: '152.9612101'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13388630_1599111547047564_1547498205_n.jpg?fit=640%2C640
---

[![Get yo nails did. 💅🏽](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13388630_1599111547047564_1547498205_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/18/get-yo-nails-did-%f0%9f%92%85%f0%9f%8f%bd/) 

[![Get yo nails did. 💅🏽](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13388630_1599111547047564_1547498205_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BGzJKwTimGZ/)

Get yo nails did. 💅🏽

-26.8391448152.9612101




Posted on [Instagram](https://www.instagram.com/p/BGzJKwTimGZ/) [8:25 am, June 18, 2016](https://dentedreality.com.au/2016/06/18/get-yo-nails-did-%f0%9f%92%85%f0%9f%8f%bd/ "8:25 am") 
jQuery(document).ready(function(){
var gmap\_m3c42f440aae37ea92ee7568e78358ab0 = {
positions : {
625 : new google.maps.LatLng( '-26.839144807334', '152.96121007777' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c42f440aae37ea92ee7568e78358ab0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c42f440aae37ea92ee7568e78358ab0.positions ) {
gmap\_m3c42f440aae37ea92ee7568e78358ab0.bounds.extend( gmap\_m3c42f440aae37ea92ee7568e78358ab0.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c42f440aae37ea92ee7568e78358ab0.positions ) {
gmap\_m3c42f440aae37ea92ee7568e78358ab0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c42f440aae37ea92ee7568e78358ab0.map,
position : gmap\_m3c42f440aae37ea92ee7568e78358ab0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c42f440aae37ea92ee7568e78358ab0.map.setCenter( gmap\_m3c42f440aae37ea92ee7568e78358ab0.positions[625] );
});