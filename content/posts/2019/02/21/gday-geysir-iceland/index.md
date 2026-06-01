---
title: ''
date: '2019-02-21T17:13:13-07:00'
format: image
service: instagram
tags:
- iceland
latitude: '64.3142117'
longitude: '-20.3009283'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/51611224_406472573459804_47267139005930775_n.jpg
---

[![G'Day Geysir! #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/51611224_406472573459804_47267139005930775_n.jpg)](https://dentedreality.com.au/2019/02/21/gday-geysir-iceland/) 

[![G'Day Geysir! #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/51611224_406472573459804_47267139005930775_n.jpg)](https://www.instagram.com/p/BuKdzcRndl0/)

G’Day Geysir! #iceland

64.3142117-20.3009283




* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKdzcRndl0/) [5:13 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/gday-geysir-iceland/ "5:13 pm") 
jQuery(document).ready(function(){
var gmap\_m4a56c9e8fd151777145d2a7f41a93407 = {
positions : {
961 : new google.maps.LatLng( '64.3142117', '-20.3009283' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4a56c9e8fd151777145d2a7f41a93407' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4a56c9e8fd151777145d2a7f41a93407.positions ) {
gmap\_m4a56c9e8fd151777145d2a7f41a93407.bounds.extend( gmap\_m4a56c9e8fd151777145d2a7f41a93407.positions[m] );
}
// Render markers
for ( var m in gmap\_m4a56c9e8fd151777145d2a7f41a93407.positions ) {
gmap\_m4a56c9e8fd151777145d2a7f41a93407.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4a56c9e8fd151777145d2a7f41a93407.map,
position : gmap\_m4a56c9e8fd151777145d2a7f41a93407.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4a56c9e8fd151777145d2a7f41a93407.map.setCenter( gmap\_m4a56c9e8fd151777145d2a7f41a93407.positions[961] );
});