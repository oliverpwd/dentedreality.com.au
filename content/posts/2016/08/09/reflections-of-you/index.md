---
title: ''
date: '2016-08-09T12:41:04-06:00'
format: image
service: instagram
latitude: '38.0020257'
longitude: '-107.8168177'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13734237_1745999778976255_38892891_n.jpg?fit=640%2C640
---

[![Reflections of you...](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13734237_1745999778976255_38892891_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/08/09/reflections-of-you/) 

[![Reflections of you...](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13734237_1745999778976255_38892891_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BI5fshegIkf/)

Reflections of you…

38.0020257-107.8168177




Posted on [Instagram](https://www.instagram.com/p/BI5fshegIkf/) [12:41 pm, August 9, 2016](https://dentedreality.com.au/2016/08/09/reflections-of-you/ "12:41 pm") 
jQuery(document).ready(function(){
var gmap\_m84cca523224fe9c086112b0f98e9660e = {
positions : {
179 : new google.maps.LatLng( '38.002025736531', '-107.816817714' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m84cca523224fe9c086112b0f98e9660e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m84cca523224fe9c086112b0f98e9660e.positions ) {
gmap\_m84cca523224fe9c086112b0f98e9660e.bounds.extend( gmap\_m84cca523224fe9c086112b0f98e9660e.positions[m] );
}
// Render markers
for ( var m in gmap\_m84cca523224fe9c086112b0f98e9660e.positions ) {
gmap\_m84cca523224fe9c086112b0f98e9660e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m84cca523224fe9c086112b0f98e9660e.map,
position : gmap\_m84cca523224fe9c086112b0f98e9660e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m84cca523224fe9c086112b0f98e9660e.map.setCenter( gmap\_m84cca523224fe9c086112b0f98e9660e.positions[179] );
});