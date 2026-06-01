---
title: ''
date: '2015-11-24T21:01:55-07:00'
format: image
service: instagram
latitude: '39.7641434'
longitude: '-104.9783539'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/11/12237510_1496304804032194_1423590146_n.jpg?resize=640%2C640
---

[![Fancy cocktails with dinner.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/11/12237510_1496304804032194_1423590146_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/11/24/fancy-cocktails-with-dinner/) 

[![Fancy cocktails with dinner.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/11/12237510_1496304804032194_1423590146_n.jpg?resize=640%2C640)](https://instagram.com/p/-fl_ujimCH/)

Fancy cocktails with dinner.

39.7641434-104.9783539




Posted on [Instagram](https://instagram.com/p/-fl_ujimCH/) [9:01 pm, November 24, 2015](https://dentedreality.com.au/2015/11/24/fancy-cocktails-with-dinner/ "9:01 pm") 
jQuery(document).ready(function(){
var gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1 = {
positions : {
175 : new google.maps.LatLng( '39.76414337', '-104.978353864' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.positions ) {
gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.bounds.extend( gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.positions[m] );
}
// Render markers
for ( var m in gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.positions ) {
gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.map,
position : gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.map.setCenter( gmap\_m4cf4f7f2b7cda7f21c84cfe5937be2c1.positions[175] );
});