---
title: SXSW 2012
date: '2012-03-13T16:50:52+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721698814_c74fde557a_o.jpg?resize=607%2C453
---

[![SXSW 2012](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721698814_c74fde557a_o.jpg?resize=607%2C453)](http://dentedreality.com.au/2012/03/13/sxsw-2012-11/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/13/sxsw-2012-11/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721698814/) [4:50 pm, March 13, 2012](http://dentedreality.com.au/2012/03/13/sxsw-2012-11/ "4:50 pm") 
jQuery(document).ready(function(){
var gmap\_m68b629e305d80b9ebbf35c519dc007e8 = {
positions : {
543 : new google.maps.LatLng( '30.266333', '-97.737667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m68b629e305d80b9ebbf35c519dc007e8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m68b629e305d80b9ebbf35c519dc007e8.positions ) {
gmap\_m68b629e305d80b9ebbf35c519dc007e8.bounds.extend( gmap\_m68b629e305d80b9ebbf35c519dc007e8.positions[m] );
}
// Render markers
for ( var m in gmap\_m68b629e305d80b9ebbf35c519dc007e8.positions ) {
gmap\_m68b629e305d80b9ebbf35c519dc007e8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m68b629e305d80b9ebbf35c519dc007e8.map,
position : gmap\_m68b629e305d80b9ebbf35c519dc007e8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m68b629e305d80b9ebbf35c519dc007e8.map.setCenter( gmap\_m68b629e305d80b9ebbf35c519dc007e8.positions[543] );
});