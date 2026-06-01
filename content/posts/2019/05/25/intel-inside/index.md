---
title: ''
date: '2019-05-25T12:43:29-06:00'
format: image
service: instagram
latitude: '39.6905332'
longitude: '-105.1521218'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/05/25142514/59575512_305445573696532_4685288855555767108_n.jpg?fit=640%2C640&ssl=1
---

[![Intel inside](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/05/25142514/59575512_305445573696532_4685288855555767108_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/05/25/intel-inside/) 

[![Intel inside](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/05/25142514/59575512_305445573696532_4685288855555767108_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/Bx5V_0OJVOw/)

Intel inside

39.6905332-105.1521218




Posted on [Instagram](https://www.instagram.com/p/Bx5V_0OJVOw/) [12:43 pm, May 25, 2019](https://dentedreality.com.au/2019/05/25/intel-inside/ "12:43 pm") 
jQuery(document).ready(function(){
var gmap\_m3b6e85966dc10da4b49048cae9c17c45 = {
positions : {
756 : new google.maps.LatLng( '39.6905332', '-105.1521218' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3b6e85966dc10da4b49048cae9c17c45' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3b6e85966dc10da4b49048cae9c17c45.positions ) {
gmap\_m3b6e85966dc10da4b49048cae9c17c45.bounds.extend( gmap\_m3b6e85966dc10da4b49048cae9c17c45.positions[m] );
}
// Render markers
for ( var m in gmap\_m3b6e85966dc10da4b49048cae9c17c45.positions ) {
gmap\_m3b6e85966dc10da4b49048cae9c17c45.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3b6e85966dc10da4b49048cae9c17c45.map,
position : gmap\_m3b6e85966dc10da4b49048cae9c17c45.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3b6e85966dc10da4b49048cae9c17c45.map.setCenter( gmap\_m3b6e85966dc10da4b49048cae9c17c45.positions[756] );
});