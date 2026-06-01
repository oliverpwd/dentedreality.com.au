---
title: Fisheye
date: '2011-12-25T09:54:38+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- fisheye
- me
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959404659_0b104b9747_o.jpg?resize=607%2C452
---

[![Fisheye](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959404659_0b104b9747_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/25/fisheye/) 
# [Fisheye](http://dentedreality.com.au/2011/12/25/fisheye/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[fisheye](http://dentedreality.com.au/tags/fisheye/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959404659/) [9:54 am, December 25, 2011](http://dentedreality.com.au/2011/12/25/fisheye/ "9:54 am") 
jQuery(document).ready(function(){
var gmap\_m55bdf6f52e08173d8107b7a1c12298ed = {
positions : {
282 : new google.maps.LatLng( '37.736', '-122.433501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m55bdf6f52e08173d8107b7a1c12298ed' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m55bdf6f52e08173d8107b7a1c12298ed.positions ) {
gmap\_m55bdf6f52e08173d8107b7a1c12298ed.bounds.extend( gmap\_m55bdf6f52e08173d8107b7a1c12298ed.positions[m] );
}
// Render markers
for ( var m in gmap\_m55bdf6f52e08173d8107b7a1c12298ed.positions ) {
gmap\_m55bdf6f52e08173d8107b7a1c12298ed.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m55bdf6f52e08173d8107b7a1c12298ed.map,
position : gmap\_m55bdf6f52e08173d8107b7a1c12298ed.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m55bdf6f52e08173d8107b7a1c12298ed.map.setCenter( gmap\_m55bdf6f52e08173d8107b7a1c12298ed.positions[282] );
});