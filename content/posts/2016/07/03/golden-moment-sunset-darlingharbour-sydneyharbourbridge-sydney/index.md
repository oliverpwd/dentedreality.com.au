---
title: ''
date: '2016-07-03T02:22:39-06:00'
format: image
service: instagram
tags:
- darlingharbour
- sunset
- sydney
- sydneyharbourbridge
latitude: '-33.8553807'
longitude: '151.2497171'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13534531_726783487461105_1631239780_n.jpg?fit=640%2C640
---

[![Golden moment. #sunset #darlingharbour #sydneyharbourbridge #sydney](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13534531_726783487461105_1631239780_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/03/golden-moment-sunset-darlingharbour-sydneyharbourbridge-sydney/) 

[![Golden moment. #sunset #darlingharbour #sydneyharbourbridge #sydney](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13534531_726783487461105_1631239780_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BHZHgrygjt5/)

Golden moment. #sunset #darlingharbour #sydneyharbourbridge #sydney

-33.8553807151.2497171




* #[darlingharbour](https://dentedreality.com.au/tags/darlingharbour/)
* #[sunset](https://dentedreality.com.au/tags/sunset/)
* #[sydney](https://dentedreality.com.au/tags/sydney/)
* #[sydneyharbourbridge](https://dentedreality.com.au/tags/sydneyharbourbridge/)

Posted on [Instagram](https://www.instagram.com/p/BHZHgrygjt5/) [2:22 am, July 3, 2016](https://dentedreality.com.au/2016/07/03/golden-moment-sunset-darlingharbour-sydneyharbourbridge-sydney/ "2:22 am") 
jQuery(document).ready(function(){
var gmap\_md0cc150869e63810a8703a37bbcd95cf = {
positions : {
652 : new google.maps.LatLng( '-33.855380695714', '151.24971706434' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md0cc150869e63810a8703a37bbcd95cf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md0cc150869e63810a8703a37bbcd95cf.positions ) {
gmap\_md0cc150869e63810a8703a37bbcd95cf.bounds.extend( gmap\_md0cc150869e63810a8703a37bbcd95cf.positions[m] );
}
// Render markers
for ( var m in gmap\_md0cc150869e63810a8703a37bbcd95cf.positions ) {
gmap\_md0cc150869e63810a8703a37bbcd95cf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md0cc150869e63810a8703a37bbcd95cf.map,
position : gmap\_md0cc150869e63810a8703a37bbcd95cf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md0cc150869e63810a8703a37bbcd95cf.map.setCenter( gmap\_md0cc150869e63810a8703a37bbcd95cf.positions[652] );
});