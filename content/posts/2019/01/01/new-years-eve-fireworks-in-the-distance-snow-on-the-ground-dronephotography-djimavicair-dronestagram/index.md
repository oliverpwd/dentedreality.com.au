---
title: ''
date: '2019-01-01T02:15:32-06:00'
format: image
service: instagram
tags:
- djimavicair
- dronephotography
- dronestagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181949/47433966_312461889392861_6848820838684600467_n.jpg?resize=607%2C607&ssl=1
---

[![New Year's Eve fireworks in the distance. Snow on the ground. #dronephotography #djimavicair #dronestagram](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181949/47433966_312461889392861_6848820838684600467_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2019/01/01/new-years-eve-fireworks-in-the-distance-snow-on-the-ground-dronephotography-djimavicair-dronestagram/) 

[![New Year's Eve fireworks in the distance. Snow on the ground. #dronephotography #djimavicair #dronestagram](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181949/47433966_312461889392861_6848820838684600467_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BsFiiFBg58R/)

New Year’s Eve fireworks in the distance. Snow on the ground. #dronephotography #djimavicair #dronestagram

39.7391-104.9836




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)

Posted on [Instagram](https://www.instagram.com/p/BsFiiFBg58R/) [2:15 am, January 1, 2019](https://dentedreality.com.au/2019/01/01/new-years-eve-fireworks-in-the-distance-snow-on-the-ground-dronephotography-djimavicair-dronestagram/ "2:15 am") 
jQuery(document).ready(function(){
var gmap\_m6fce2ab06094df377ea846ae568d826e = {
positions : {
523 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6fce2ab06094df377ea846ae568d826e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6fce2ab06094df377ea846ae568d826e.positions ) {
gmap\_m6fce2ab06094df377ea846ae568d826e.bounds.extend( gmap\_m6fce2ab06094df377ea846ae568d826e.positions[m] );
}
// Render markers
for ( var m in gmap\_m6fce2ab06094df377ea846ae568d826e.positions ) {
gmap\_m6fce2ab06094df377ea846ae568d826e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6fce2ab06094df377ea846ae568d826e.map,
position : gmap\_m6fce2ab06094df377ea846ae568d826e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6fce2ab06094df377ea846ae568d826e.map.setCenter( gmap\_m6fce2ab06094df377ea846ae568d826e.positions[523] );
});