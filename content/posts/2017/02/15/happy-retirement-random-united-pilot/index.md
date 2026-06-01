---
title: ''
date: '2017-02-15T12:30:25+00:00'
format: image
service: instagram
tags:
- united
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16790328_385898385113901_7482312708759486464_n.jpg?fit=640%2C640
---

[![Happy Retirement, random United pilot.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16790328_385898385113901_7482312708759486464_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/15/happy-retirement-random-united-pilot/) 

Happy Retirement, random United pilot.





* #[united](http://dentedreality.com.au/tags/united/)

Posted on [Instagram](https://www.instagram.com/p/BQi0YQMD8K5/) [12:30 pm, February 15, 2017](http://dentedreality.com.au/2017/02/15/happy-retirement-random-united-pilot/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_m99bb98e9d3d014968e84be962a63a727 = {
positions : {
878 : new google.maps.LatLng( '29.984444444444', '-95.341388888889' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m99bb98e9d3d014968e84be962a63a727' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m99bb98e9d3d014968e84be962a63a727.positions ) {
gmap\_m99bb98e9d3d014968e84be962a63a727.bounds.extend( gmap\_m99bb98e9d3d014968e84be962a63a727.positions[m] );
}
// Render markers
for ( var m in gmap\_m99bb98e9d3d014968e84be962a63a727.positions ) {
gmap\_m99bb98e9d3d014968e84be962a63a727.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m99bb98e9d3d014968e84be962a63a727.map,
position : gmap\_m99bb98e9d3d014968e84be962a63a727.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m99bb98e9d3d014968e84be962a63a727.map.setCenter( gmap\_m99bb98e9d3d014968e84be962a63a727.positions[878] );
});