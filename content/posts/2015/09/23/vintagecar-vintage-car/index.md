---
title: ''
date: '2015-09-23T15:57:45+00:00'
format: image
service: instagram
tags:
- car
- vintage
- vintagecar
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11909255_160139657661467_208753305_n.jpg?resize=640%2C640
---

[![#vintagecar #vintage #car](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11909255_160139657661467_208753305_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/09/23/vintagecar-vintage-car/) 

#vintagecar #vintage #car





* #[car](http://dentedreality.com.au/tags/car/)
* #[vintage](http://dentedreality.com.au/tags/vintage/)
* #[vintagecar](http://dentedreality.com.au/tags/vintagecar/)

Posted on [Instagram](https://instagram.com/p/7_TCL3imCK/) [3:57 pm, September 23, 2015](http://dentedreality.com.au/2015/09/23/vintagecar-vintage-car/ "3:57 pm") 
jQuery(document).ready(function(){
var gmap\_m0adac7adb585056f4132b2c17bcab11c = {
positions : {
20 : new google.maps.LatLng( '39.8230705', '-105.1677094' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0adac7adb585056f4132b2c17bcab11c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0adac7adb585056f4132b2c17bcab11c.positions ) {
gmap\_m0adac7adb585056f4132b2c17bcab11c.bounds.extend( gmap\_m0adac7adb585056f4132b2c17bcab11c.positions[m] );
}
// Render markers
for ( var m in gmap\_m0adac7adb585056f4132b2c17bcab11c.positions ) {
gmap\_m0adac7adb585056f4132b2c17bcab11c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0adac7adb585056f4132b2c17bcab11c.map,
position : gmap\_m0adac7adb585056f4132b2c17bcab11c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0adac7adb585056f4132b2c17bcab11c.map.setCenter( gmap\_m0adac7adb585056f4132b2c17bcab11c.positions[20] );
});