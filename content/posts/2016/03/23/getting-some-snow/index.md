---
title: ''
date: '2016-03-23T15:45:32+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/1169286_1344591708889928_1657764280_n.jpg?fit=640%2C640
---

[![Getting some snow.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/1169286_1344591708889928_1657764280_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/03/23/getting-some-snow/) 

Getting some snow.





Posted on [Instagram](https://www.instagram.com/p/BDT6T5wCmB9/) [3:45 pm, March 23, 2016](http://dentedreality.com.au/2016/03/23/getting-some-snow/ "3:45 pm") 
jQuery(document).ready(function(){
var gmap\_m4a07bacc5123930a2cad383a326ee220 = {
positions : {
721 : new google.maps.LatLng( '39.7392', '-104.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4a07bacc5123930a2cad383a326ee220' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4a07bacc5123930a2cad383a326ee220.positions ) {
gmap\_m4a07bacc5123930a2cad383a326ee220.bounds.extend( gmap\_m4a07bacc5123930a2cad383a326ee220.positions[m] );
}
// Render markers
for ( var m in gmap\_m4a07bacc5123930a2cad383a326ee220.positions ) {
gmap\_m4a07bacc5123930a2cad383a326ee220.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4a07bacc5123930a2cad383a326ee220.map,
position : gmap\_m4a07bacc5123930a2cad383a326ee220.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4a07bacc5123930a2cad383a326ee220.map.setCenter( gmap\_m4a07bacc5123930a2cad383a326ee220.positions[721] );
});