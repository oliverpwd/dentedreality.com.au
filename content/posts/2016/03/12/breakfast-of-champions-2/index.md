---
title: ''
date: '2016-03-12T12:04:30+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/12750282_179698482411236_1843209964_n.jpg?fit=640%2C640&ssl=1
---

[![Breakfast of champions](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/12750282_179698482411236_1843209964_n.jpg?fit=640%2C640&ssl=1)](http://dentedreality.com.au/2016/03/12/breakfast-of-champions-2/) 

Breakfast of champions





Posted on [Instagram](https://www.instagram.com/p/BC3TI7FCmOD/) [12:04 pm, March 12, 2016](http://dentedreality.com.au/2016/03/12/breakfast-of-champions-2/ "12:04 pm") 
jQuery(document).ready(function(){
var gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53 = {
positions : {
733 : new google.maps.LatLng( '39.7547684', '-104.9776001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.positions ) {
gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.bounds.extend( gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.positions[m] );
}
// Render markers
for ( var m in gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.positions ) {
gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.map,
position : gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.map.setCenter( gmap\_m8e5c318d78f74f55c2ab8dc0c7487f53.positions[733] );
});