---
title: ''
date: '2015-10-18T20:23:06-06:00'
format: image
service: instagram
tags:
- a8cgm
latitude: '40.6861698'
longitude: '-111.5560886'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2015/10/14183204/12142556_1641250222810365_181290031_n.jpg?resize=607%2C607&ssl=1
---

[![Much excite. Such wow!](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2015/10/14183204/12142556_1641250222810365_181290031_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2015/10/18/much-excite-such-wow/) 

[![Much excite. Such wow!](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2015/10/14183204/12142556_1641250222810365_181290031_n.jpg?resize=607%2C607&ssl=1)](https://instagram.com/p/9AJRjjimA6/)

Much excite. Such wow!

40.6861698-111.5560886




* #[a8cgm](https://dentedreality.com.au/tags/a8cgm/)

Posted on [Instagram](https://instagram.com/p/9AJRjjimA6/) [8:23 pm, October 18, 2015](https://dentedreality.com.au/2015/10/18/much-excite-such-wow/ "8:23 pm") 
jQuery(document).ready(function(){
var gmap\_m27ebf7b3c082e44515199e53d8f09093 = {
positions : {
822 : new google.maps.LatLng( '40.686169773', '-111.556088621' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m27ebf7b3c082e44515199e53d8f09093' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m27ebf7b3c082e44515199e53d8f09093.positions ) {
gmap\_m27ebf7b3c082e44515199e53d8f09093.bounds.extend( gmap\_m27ebf7b3c082e44515199e53d8f09093.positions[m] );
}
// Render markers
for ( var m in gmap\_m27ebf7b3c082e44515199e53d8f09093.positions ) {
gmap\_m27ebf7b3c082e44515199e53d8f09093.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m27ebf7b3c082e44515199e53d8f09093.map,
position : gmap\_m27ebf7b3c082e44515199e53d8f09093.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m27ebf7b3c082e44515199e53d8f09093.map.setCenter( gmap\_m27ebf7b3c082e44515199e53d8f09093.positions[822] );
});