---
title: ''
date: '2015-10-12T14:08:07-06:00'
format: image
service: instagram
tags:
- a8cgm
latitude: '39.855096'
longitude: '-104.673738'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/10299894_1669424370011367_1141177395_n.jpg?resize=640%2C640
---

[![My chariot to the #a8cgm](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/10299894_1669424370011367_1141177395_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/10/12/my-chariot-to-the-a8cgm/) 

[![My chariot to the #a8cgm](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/10299894_1669424370011367_1141177395_n.jpg?resize=640%2C640)](https://instagram.com/p/8wBly8CmPj/)

My chariot to the #a8cgm

39.855096-104.673738




* #[a8cgm](https://dentedreality.com.au/tags/a8cgm/)

Posted on [Instagram](https://instagram.com/p/8wBly8CmPj/) [2:08 pm, October 12, 2015](https://dentedreality.com.au/2015/10/12/my-chariot-to-the-a8cgm/ "2:08 pm") 
jQuery(document).ready(function(){
var gmap\_mb6c58958255901810e9968130f3483cf = {
positions : {
79 : new google.maps.LatLng( '39.855096', '-104.673738' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb6c58958255901810e9968130f3483cf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb6c58958255901810e9968130f3483cf.positions ) {
gmap\_mb6c58958255901810e9968130f3483cf.bounds.extend( gmap\_mb6c58958255901810e9968130f3483cf.positions[m] );
}
// Render markers
for ( var m in gmap\_mb6c58958255901810e9968130f3483cf.positions ) {
gmap\_mb6c58958255901810e9968130f3483cf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb6c58958255901810e9968130f3483cf.map,
position : gmap\_mb6c58958255901810e9968130f3483cf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb6c58958255901810e9968130f3483cf.map.setCenter( gmap\_mb6c58958255901810e9968130f3483cf.positions[79] );
});