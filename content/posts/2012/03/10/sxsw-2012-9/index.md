---
title: SXSW 2012
date: '2012-03-10T18:38:31+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721572512_c38eed3230_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721572512_c38eed3230_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/10/sxsw-2012-9/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/10/sxsw-2012-9/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721572512/) [6:38 pm, March 10, 2012](http://dentedreality.com.au/2012/03/10/sxsw-2012-9/ "6:38 pm") 
jQuery(document).ready(function(){
var gmap\_m088510bab1e3bf379a8dab3d7329fd09 = {
positions : {
319 : new google.maps.LatLng( '30.2675', '-97.740667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m088510bab1e3bf379a8dab3d7329fd09' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m088510bab1e3bf379a8dab3d7329fd09.positions ) {
gmap\_m088510bab1e3bf379a8dab3d7329fd09.bounds.extend( gmap\_m088510bab1e3bf379a8dab3d7329fd09.positions[m] );
}
// Render markers
for ( var m in gmap\_m088510bab1e3bf379a8dab3d7329fd09.positions ) {
gmap\_m088510bab1e3bf379a8dab3d7329fd09.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m088510bab1e3bf379a8dab3d7329fd09.map,
position : gmap\_m088510bab1e3bf379a8dab3d7329fd09.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m088510bab1e3bf379a8dab3d7329fd09.map.setCenter( gmap\_m088510bab1e3bf379a8dab3d7329fd09.positions[319] );
});