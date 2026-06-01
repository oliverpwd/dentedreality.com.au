---
title: ''
date: '2018-04-15T16:45:27+00:00'
format: image
service: instagram
image: https://dentedreality.com.au/wp-content/uploads/2018/04/30084038_189467341672552_474488586494803968_n.jpg
---

[![Killer day for a ride. Living this new bike!](https://dentedreality.com.au/wp-content/uploads/2018/04/30084038_189467341672552_474488586494803968_n.jpg)](https://dentedreality.com.au/2018/04/15/killer-day-for-a-ride-living-this-new-bike/) 

[![Killer day for a ride. Living this new bike!](https://dentedreality.com.au/wp-content/uploads/2018/04/30084038_189467341672552_474488586494803968_n.jpg)](https://www.instagram.com/p/Bhm7vqlFVbS/)

Killer day for a ride. Living this new bike!





Posted on [Instagram](https://www.instagram.com/p/Bhm7vqlFVbS/) [4:45 pm, April 15, 2018](https://dentedreality.com.au/2018/04/15/killer-day-for-a-ride-living-this-new-bike/ "4:45 pm") 
jQuery(document).ready(function(){
var gmap\_m6657433672f286b3dbda4729b0b65912 = {
positions : {
1000 : new google.maps.LatLng( '39.665250283333', '-105.39451766643' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6657433672f286b3dbda4729b0b65912' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6657433672f286b3dbda4729b0b65912.positions ) {
gmap\_m6657433672f286b3dbda4729b0b65912.bounds.extend( gmap\_m6657433672f286b3dbda4729b0b65912.positions[m] );
}
// Render markers
for ( var m in gmap\_m6657433672f286b3dbda4729b0b65912.positions ) {
gmap\_m6657433672f286b3dbda4729b0b65912.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6657433672f286b3dbda4729b0b65912.map,
position : gmap\_m6657433672f286b3dbda4729b0b65912.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6657433672f286b3dbda4729b0b65912.map.setCenter( gmap\_m6657433672f286b3dbda4729b0b65912.positions[1000] );
});