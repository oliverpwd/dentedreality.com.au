---
title: ''
date: '2015-10-18T21:08:16-06:00'
format: image
service: instagram
tags:
- a8cgm
latitude: '40.6861698'
longitude: '-111.5560886'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/12132856_928744777163144_1932698572_n.jpg?resize=640%2C640
---

[![Our company's in-house band(s) slay! #a8cgm @automattic](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/12132856_928744777163144_1932698572_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/10/18/our-companys-in-house-bands-slay-a8cgm-automattic/) 

[![Our company's in-house band(s) slay! #a8cgm @automattic](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/12132856_928744777163144_1932698572_n.jpg?resize=640%2C640)](https://instagram.com/p/9AOcUfCmI9/)

Our company’s in-house band(s) slay! #a8cgm @automattic

40.6861698-111.5560886




* #[a8cgm](https://dentedreality.com.au/tags/a8cgm/)

Posted on [Instagram](https://instagram.com/p/9AOcUfCmI9/) [9:08 pm, October 18, 2015](https://dentedreality.com.au/2015/10/18/our-companys-in-house-bands-slay-a8cgm-automattic/ "9:08 pm") 
jQuery(document).ready(function(){
var gmap\_m3d93deb90212ad424468dc41bb9d52ad = {
positions : {
405 : new google.maps.LatLng( '40.686169773', '-111.556088621' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3d93deb90212ad424468dc41bb9d52ad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3d93deb90212ad424468dc41bb9d52ad.positions ) {
gmap\_m3d93deb90212ad424468dc41bb9d52ad.bounds.extend( gmap\_m3d93deb90212ad424468dc41bb9d52ad.positions[m] );
}
// Render markers
for ( var m in gmap\_m3d93deb90212ad424468dc41bb9d52ad.positions ) {
gmap\_m3d93deb90212ad424468dc41bb9d52ad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3d93deb90212ad424468dc41bb9d52ad.map,
position : gmap\_m3d93deb90212ad424468dc41bb9d52ad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3d93deb90212ad424468dc41bb9d52ad.map.setCenter( gmap\_m3d93deb90212ad424468dc41bb9d52ad.positions[405] );
});