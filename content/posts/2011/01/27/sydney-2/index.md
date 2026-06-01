---
title: Sydney
date: '2011-01-27T11:31:27+00:00'
format: image
service: flickr
tags:
- australia
- sydney
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434808036_c66e248387_o.jpg?resize=607%2C452
---

[![Sydney](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434808036_c66e248387_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/27/sydney-2/) 
# [Sydney](http://dentedreality.com.au/2011/01/27/sydney-2/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434808036/) [11:31 am, January 27, 2011](http://dentedreality.com.au/2011/01/27/sydney-2/ "11:31 am") 
jQuery(document).ready(function(){
var gmap\_ma75e00517e39c2e5840db24810066d08 = {
positions : {
59 : new google.maps.LatLng( '-33.860334', '151.209666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma75e00517e39c2e5840db24810066d08' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma75e00517e39c2e5840db24810066d08.positions ) {
gmap\_ma75e00517e39c2e5840db24810066d08.bounds.extend( gmap\_ma75e00517e39c2e5840db24810066d08.positions[m] );
}
// Render markers
for ( var m in gmap\_ma75e00517e39c2e5840db24810066d08.positions ) {
gmap\_ma75e00517e39c2e5840db24810066d08.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma75e00517e39c2e5840db24810066d08.map,
position : gmap\_ma75e00517e39c2e5840db24810066d08.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma75e00517e39c2e5840db24810066d08.map.setCenter( gmap\_ma75e00517e39c2e5840db24810066d08.positions[59] );
});