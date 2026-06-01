---
title: ''
date: '2018-04-22T15:31:07+00:00'
format: image
service: instagram
tags:
- earthday
- optoutside
image: https://dentedreality.com.au/wp-content/uploads/2018/04/30589866_145720049605397_2754329666130018304_n.jpg
---

[![Hiking the Table. 9.1 miles.](https://dentedreality.com.au/wp-content/uploads/2018/04/30589866_145720049605397_2754329666130018304_n.jpg)](https://dentedreality.com.au/2018/04/22/hiking-the-table-9-1-miles/) 

[![Hiking the Table. 9.1 miles.](https://dentedreality.com.au/wp-content/uploads/2018/04/30589866_145720049605397_2754329666130018304_n.jpg)](https://www.instagram.com/p/Bh40zWPlVXl/)

Hiking the Table. 9.1 miles.





* #[earthday](https://dentedreality.com.au/tags/earthday/)
* #[optoutside](https://dentedreality.com.au/tags/optoutside/)

Posted on [Instagram](https://www.instagram.com/p/Bh40zWPlVXl/) [3:31 pm, April 22, 2018](https://dentedreality.com.au/2018/04/22/hiking-the-table-9-1-miles/ "3:31 pm") 
jQuery(document).ready(function(){
var gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33 = {
positions : {
438 : new google.maps.LatLng( '39.781102777778', '-105.22058611111' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.positions ) {
gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.bounds.extend( gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.positions[m] );
}
// Render markers
for ( var m in gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.positions ) {
gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.map,
position : gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.map.setCenter( gmap\_mb1d10e34e9fe70ffa5bccca2cee40e33.positions[438] );
});