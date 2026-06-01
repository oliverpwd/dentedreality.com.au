---
title: ''
date: '2016-07-30T09:52:55-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '47.7511285'
longitude: '-90.3314226'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13827233_1389289221087699_840750034_n.jpg?fit=640%2C640
---

[![Sunset canoes #bwca](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13827233_1389289221087699_840750034_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/sunset-canoes-bwca/) 

[![Sunset canoes #bwca](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13827233_1389289221087699_840750034_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfcgJegmR5/)

Sunset canoes #bwca

47.7511285-90.3314226




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIfcgJegmR5/) [9:52 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/sunset-canoes-bwca/ "9:52 am") 
jQuery(document).ready(function(){
var gmap\_m391d4616e0d984e1eda0fad1da41697a = {
positions : {
448 : new google.maps.LatLng( '47.751128501303', '-90.331422630782' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m391d4616e0d984e1eda0fad1da41697a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m391d4616e0d984e1eda0fad1da41697a.positions ) {
gmap\_m391d4616e0d984e1eda0fad1da41697a.bounds.extend( gmap\_m391d4616e0d984e1eda0fad1da41697a.positions[m] );
}
// Render markers
for ( var m in gmap\_m391d4616e0d984e1eda0fad1da41697a.positions ) {
gmap\_m391d4616e0d984e1eda0fad1da41697a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m391d4616e0d984e1eda0fad1da41697a.map,
position : gmap\_m391d4616e0d984e1eda0fad1da41697a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m391d4616e0d984e1eda0fad1da41697a.map.setCenter( gmap\_m391d4616e0d984e1eda0fad1da41697a.positions[448] );
});