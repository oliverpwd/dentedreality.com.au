---
title: ''
date: '2016-01-13T22:12:55+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12534351_1193860647310394_645743033_n.jpg?resize=607%2C607
---

[![Dry Dock](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12534351_1193860647310394_645743033_n.jpg?resize=607%2C607)](http://dentedreality.com.au/2016/01/13/dry-dock/) 

Dry Dock





Posted on [Instagram](https://www.instagram.com/p/BAgd3a6imAS/) [10:12 pm, January 13, 2016](http://dentedreality.com.au/2016/01/13/dry-dock/ "10:12 pm") 
jQuery(document).ready(function(){
var gmap\_maa01f74f9f78c7d1d2bc925fb7101e38 = {
positions : {
903 : new google.maps.LatLng( '-33.905069136', '18.420180163' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maa01f74f9f78c7d1d2bc925fb7101e38' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.positions ) {
gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.bounds.extend( gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.positions[m] );
}
// Render markers
for ( var m in gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.positions ) {
gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.map,
position : gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.map.setCenter( gmap\_maa01f74f9f78c7d1d2bc925fb7101e38.positions[903] );
});