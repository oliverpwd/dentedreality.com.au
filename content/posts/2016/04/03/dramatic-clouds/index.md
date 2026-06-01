---
title: ''
date: '2016-04-03T10:05:14+00:00'
format: image
service: instagram
tags:
- clouds
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12424450_511656069036145_927415799_n.jpg?fit=640%2C640
---

[![Dramatic #clouds](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12424450_511656069036145_927415799_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/04/03/dramatic-clouds/) 

Dramatic #clouds





* #[clouds](http://dentedreality.com.au/tags/clouds/)

Posted on [Instagram](https://www.instagram.com/p/BDvoHJiimCk/) [10:05 am, April 3, 2016](http://dentedreality.com.au/2016/04/03/dramatic-clouds/ "10:05 am") 
jQuery(document).ready(function(){
var gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a = {
positions : {
9 : new google.maps.LatLng( '53.015184604', '-9.404570445' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.positions ) {
gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.bounds.extend( gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.positions[m] );
}
// Render markers
for ( var m in gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.positions ) {
gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.map,
position : gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.map.setCenter( gmap\_mf7668c9eaa1d7bd419082fdf3ba2568a.positions[9] );
});