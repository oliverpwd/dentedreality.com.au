---
title: ''
date: '2014-06-06T13:00:32+00:00'
format: image
service: instagram
tags:
- burritofriday
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10449058_288901831288335_1413897187_n.jpg?resize=640%2C640
---

[![Getting my #burritofriday on.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10449058_288901831288335_1413897187_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/06/06/getting-my-burritofriday-on-3/) 

Getting my #burritofriday on.





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/o6XGDyimP5/) [1:00 pm, June 6, 2014](http://dentedreality.com.au/2014/06/06/getting-my-burritofriday-on-3/ "1:00 pm") 
jQuery(document).ready(function(){
var gmap\_me51ce47a580d8e3cbf3487a53722101e = {
positions : {
127 : new google.maps.LatLng( '40.674235418', '-73.982220724' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me51ce47a580d8e3cbf3487a53722101e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me51ce47a580d8e3cbf3487a53722101e.positions ) {
gmap\_me51ce47a580d8e3cbf3487a53722101e.bounds.extend( gmap\_me51ce47a580d8e3cbf3487a53722101e.positions[m] );
}
// Render markers
for ( var m in gmap\_me51ce47a580d8e3cbf3487a53722101e.positions ) {
gmap\_me51ce47a580d8e3cbf3487a53722101e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me51ce47a580d8e3cbf3487a53722101e.map,
position : gmap\_me51ce47a580d8e3cbf3487a53722101e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me51ce47a580d8e3cbf3487a53722101e.map.setCenter( gmap\_me51ce47a580d8e3cbf3487a53722101e.positions[127] );
});