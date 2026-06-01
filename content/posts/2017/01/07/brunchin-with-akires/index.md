---
title: ''
date: '2017-01-07T12:01:57+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/15803818_136542310177466_846532101216927744_n.jpg?fit=640%2C640
---

[![Brunchin with @akires](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/15803818_136542310177466_846532101216927744_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/01/07/brunchin-with-akires/) 

Brunchin with @akires





Posted on [Instagram](https://www.instagram.com/p/BO-WHlyDUL0/) [12:01 pm, January 7, 2017](http://dentedreality.com.au/2017/01/07/brunchin-with-akires/ "12:01 pm") 
jQuery(document).ready(function(){
var gmap\_mde3d160889ac85f0fbbb3f8aff431400 = {
positions : {
805 : new google.maps.LatLng( '39.75949', '-104.98465' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mde3d160889ac85f0fbbb3f8aff431400' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mde3d160889ac85f0fbbb3f8aff431400.positions ) {
gmap\_mde3d160889ac85f0fbbb3f8aff431400.bounds.extend( gmap\_mde3d160889ac85f0fbbb3f8aff431400.positions[m] );
}
// Render markers
for ( var m in gmap\_mde3d160889ac85f0fbbb3f8aff431400.positions ) {
gmap\_mde3d160889ac85f0fbbb3f8aff431400.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mde3d160889ac85f0fbbb3f8aff431400.map,
position : gmap\_mde3d160889ac85f0fbbb3f8aff431400.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mde3d160889ac85f0fbbb3f8aff431400.map.setCenter( gmap\_mde3d160889ac85f0fbbb3f8aff431400.positions[805] );
});