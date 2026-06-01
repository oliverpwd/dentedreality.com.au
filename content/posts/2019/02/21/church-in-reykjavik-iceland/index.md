---
title: ''
date: '2019-02-21T17:02:31-07:00'
format: image
service: instagram
tags:
- iceland
latitude: '64.14246'
longitude: '-21.9289'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/51393387_326840064616032_1844272302454866862_n.jpg
---

[![Church in Reykjavík. #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/51393387_326840064616032_1844272302454866862_n.jpg)](https://dentedreality.com.au/2019/02/21/church-in-reykjavik-iceland/) 

[![Church in Reykjavík. #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/51393387_326840064616032_1844272302454866862_n.jpg)](https://www.instagram.com/p/BuKclGQHKl8/)

Church in Reykjavík. #iceland

64.14246-21.9289




* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKclGQHKl8/) [5:02 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/church-in-reykjavik-iceland/ "5:02 pm") 
jQuery(document).ready(function(){
var gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601 = {
positions : {
907 : new google.maps.LatLng( '64.14246', '-21.9289' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.positions ) {
gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.bounds.extend( gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.positions[m] );
}
// Render markers
for ( var m in gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.positions ) {
gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.map,
position : gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.map.setCenter( gmap\_m1a9e0e9b5c08098043f4ebb0e4fff601.positions[907] );
});