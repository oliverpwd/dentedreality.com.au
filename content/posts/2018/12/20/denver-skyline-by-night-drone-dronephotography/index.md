---
title: ''
date: '2018-12-20T18:57:52-06:00'
format: image
service: instagram
tags:
- drone
- dronephotography
latitude: '39.7604294'
longitude: '-104.9768295'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181955/46928541_130199991327211_4679327903939870931_n.jpg?resize=607%2C607&ssl=1
---

[![Denver skyline by night #drone #dronephotography](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181955/46928541_130199991327211_4679327903939870931_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/12/20/denver-skyline-by-night-drone-dronephotography/) 

[![Denver skyline by night #drone #dronephotography](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181955/46928541_130199991327211_4679327903939870931_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Brobs2AAKFV/)

Denver skyline by night #drone #dronephotography

39.7604294-104.9768295




* #[drone](https://dentedreality.com.au/tags/drone/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)

Posted on [Instagram](https://www.instagram.com/p/Brobs2AAKFV/) [6:57 pm, December 20, 2018](https://dentedreality.com.au/2018/12/20/denver-skyline-by-night-drone-dronephotography/ "6:57 pm") 
jQuery(document).ready(function(){
var gmap\_m179475942a08029d89d94a34dc96e0e9 = {
positions : {
136 : new google.maps.LatLng( '39.7604294', '-104.9768295' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m179475942a08029d89d94a34dc96e0e9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m179475942a08029d89d94a34dc96e0e9.positions ) {
gmap\_m179475942a08029d89d94a34dc96e0e9.bounds.extend( gmap\_m179475942a08029d89d94a34dc96e0e9.positions[m] );
}
// Render markers
for ( var m in gmap\_m179475942a08029d89d94a34dc96e0e9.positions ) {
gmap\_m179475942a08029d89d94a34dc96e0e9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m179475942a08029d89d94a34dc96e0e9.map,
position : gmap\_m179475942a08029d89d94a34dc96e0e9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m179475942a08029d89d94a34dc96e0e9.map.setCenter( gmap\_m179475942a08029d89d94a34dc96e0e9.positions[136] );
});