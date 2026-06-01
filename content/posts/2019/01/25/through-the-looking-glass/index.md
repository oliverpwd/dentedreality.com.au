---
title: ''
date: '2019-01-25T21:27:10-06:00'
format: image
service: instagram
latitude: '39.75696'
longitude: '-104.98545'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181945/49933657_286991285280806_8881693563468709366_n.jpg?resize=607%2C607&ssl=1
---

[![Through the looking glass.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181945/49933657_286991285280806_8881693563468709366_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2019/01/25/through-the-looking-glass/) 

[![Through the looking glass.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181945/49933657_286991285280806_8881693563468709366_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BtFZZ4lgraE/)

Through the looking glass.

39.75696-104.98545




Posted on [Instagram](https://www.instagram.com/p/BtFZZ4lgraE/) [9:27 pm, January 25, 2019](https://dentedreality.com.au/2019/01/25/through-the-looking-glass/ "9:27 pm") 
jQuery(document).ready(function(){
var gmap\_m2ac40a3c4f6596d2f49333142988beb4 = {
positions : {
880 : new google.maps.LatLng( '39.75696', '-104.98545' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2ac40a3c4f6596d2f49333142988beb4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2ac40a3c4f6596d2f49333142988beb4.positions ) {
gmap\_m2ac40a3c4f6596d2f49333142988beb4.bounds.extend( gmap\_m2ac40a3c4f6596d2f49333142988beb4.positions[m] );
}
// Render markers
for ( var m in gmap\_m2ac40a3c4f6596d2f49333142988beb4.positions ) {
gmap\_m2ac40a3c4f6596d2f49333142988beb4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2ac40a3c4f6596d2f49333142988beb4.map,
position : gmap\_m2ac40a3c4f6596d2f49333142988beb4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2ac40a3c4f6596d2f49333142988beb4.map.setCenter( gmap\_m2ac40a3c4f6596d2f49333142988beb4.positions[880] );
});