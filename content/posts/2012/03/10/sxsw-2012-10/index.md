---
title: SXSW 2012
date: '2012-03-10T16:25:47+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721571558_fba1dfdc3d_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721571558_fba1dfdc3d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/10/sxsw-2012-10/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/10/sxsw-2012-10/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721571558/) [4:25 pm, March 10, 2012](http://dentedreality.com.au/2012/03/10/sxsw-2012-10/ "4:25 pm") 
jQuery(document).ready(function(){
var gmap\_m3fa6fe9b497acbfe8276949156707125 = {
positions : {
945 : new google.maps.LatLng( '30.267', '-97.740667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3fa6fe9b497acbfe8276949156707125' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3fa6fe9b497acbfe8276949156707125.positions ) {
gmap\_m3fa6fe9b497acbfe8276949156707125.bounds.extend( gmap\_m3fa6fe9b497acbfe8276949156707125.positions[m] );
}
// Render markers
for ( var m in gmap\_m3fa6fe9b497acbfe8276949156707125.positions ) {
gmap\_m3fa6fe9b497acbfe8276949156707125.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3fa6fe9b497acbfe8276949156707125.map,
position : gmap\_m3fa6fe9b497acbfe8276949156707125.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3fa6fe9b497acbfe8276949156707125.map.setCenter( gmap\_m3fa6fe9b497acbfe8276949156707125.positions[945] );
});