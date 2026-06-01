---
title: ''
date: '2019-02-21T17:10:13-07:00'
format: image
service: instagram
tags:
- iceland
latitude: '64.2156056'
longitude: '-21.0756892'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/52848285_789230101457572_6587844718584229605_n.jpg
---

[![#iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/52848285_789230101457572_6587844718584229605_n.jpg)](https://dentedreality.com.au/2019/02/21/iceland/) 

[![#iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/52848285_789230101457572_6587844718584229605_n.jpg)](https://www.instagram.com/p/BuKddkDnYXE/)

#iceland

64.2156056-21.0756892




* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKddkDnYXE/) [5:10 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/iceland/ "5:10 pm") 
jQuery(document).ready(function(){
var gmap\_m6de081ea74deefd429d3c8a286384bc5 = {
positions : {
117 : new google.maps.LatLng( '64.2156056', '-21.0756892' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6de081ea74deefd429d3c8a286384bc5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6de081ea74deefd429d3c8a286384bc5.positions ) {
gmap\_m6de081ea74deefd429d3c8a286384bc5.bounds.extend( gmap\_m6de081ea74deefd429d3c8a286384bc5.positions[m] );
}
// Render markers
for ( var m in gmap\_m6de081ea74deefd429d3c8a286384bc5.positions ) {
gmap\_m6de081ea74deefd429d3c8a286384bc5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6de081ea74deefd429d3c8a286384bc5.map,
position : gmap\_m6de081ea74deefd429d3c8a286384bc5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6de081ea74deefd429d3c8a286384bc5.map.setCenter( gmap\_m6de081ea74deefd429d3c8a286384bc5.positions[117] );
});