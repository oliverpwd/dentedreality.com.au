---
title: ''
date: '2017-08-05T07:00:30+00:00'
format: image
service: instagram
image: https://dentedreality.com.au/wp-content/uploads/2017/08/20590118_1743041719069591_5216157512348205056_n.jpg
---

[![Our doorstep canal.](https://dentedreality.com.au/wp-content/uploads/2017/08/20590118_1743041719069591_5216157512348205056_n.jpg)](https://dentedreality.com.au/2017/08/05/our-doorstep-canal/) 

[![Our doorstep canal.](https://dentedreality.com.au/wp-content/uploads/2017/08/20590118_1743041719069591_5216157512348205056_n.jpg)](https://www.instagram.com/p/BXabr7rhWaz/)

Our doorstep canal.





Posted on [Instagram](https://www.instagram.com/p/BXabr7rhWaz/) [7:00 am, August 5, 2017](https://dentedreality.com.au/2017/08/05/our-doorstep-canal/ "7:00 am") 
jQuery(document).ready(function(){
var gmap\_m3486e39b179685cb00eea8ba435ef2be = {
positions : {
383 : new google.maps.LatLng( '52.0833', '5.13333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3486e39b179685cb00eea8ba435ef2be' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3486e39b179685cb00eea8ba435ef2be.positions ) {
gmap\_m3486e39b179685cb00eea8ba435ef2be.bounds.extend( gmap\_m3486e39b179685cb00eea8ba435ef2be.positions[m] );
}
// Render markers
for ( var m in gmap\_m3486e39b179685cb00eea8ba435ef2be.positions ) {
gmap\_m3486e39b179685cb00eea8ba435ef2be.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3486e39b179685cb00eea8ba435ef2be.map,
position : gmap\_m3486e39b179685cb00eea8ba435ef2be.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3486e39b179685cb00eea8ba435ef2be.map.setCenter( gmap\_m3486e39b179685cb00eea8ba435ef2be.positions[383] );
});