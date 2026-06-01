---
title: ''
date: '2016-06-13T02:42:43-06:00'
format: image
service: instagram
latitude: '-37.8046399'
longitude: '144.9717918'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13355571_903238319785919_1856621720_n.jpg?fit=640%2C640
---

[![Spray](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13355571_903238319785919_1856621720_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/13/spray/) 

[![Spray](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13355571_903238319785919_1856621720_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BGlp6KFCmDm/)

Spray

-37.8046399144.9717918




Posted on [Instagram](https://www.instagram.com/p/BGlp6KFCmDm/) [2:42 am, June 13, 2016](https://dentedreality.com.au/2016/06/13/spray/ "2:42 am") 
jQuery(document).ready(function(){
var gmap\_m73f3192d78c172d0c52496426bb3162f = {
positions : {
947 : new google.maps.LatLng( '-37.804639938389', '144.97179181555' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m73f3192d78c172d0c52496426bb3162f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m73f3192d78c172d0c52496426bb3162f.positions ) {
gmap\_m73f3192d78c172d0c52496426bb3162f.bounds.extend( gmap\_m73f3192d78c172d0c52496426bb3162f.positions[m] );
}
// Render markers
for ( var m in gmap\_m73f3192d78c172d0c52496426bb3162f.positions ) {
gmap\_m73f3192d78c172d0c52496426bb3162f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m73f3192d78c172d0c52496426bb3162f.map,
position : gmap\_m73f3192d78c172d0c52496426bb3162f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m73f3192d78c172d0c52496426bb3162f.map.setCenter( gmap\_m73f3192d78c172d0c52496426bb3162f.positions[947] );
});