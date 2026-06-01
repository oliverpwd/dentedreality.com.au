---
title: SXSW 2012
date: '2012-03-15T17:02:33+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721701314_a142510324_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721701314_a142510324_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/15/sxsw-2012/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/15/sxsw-2012/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721701314/) [5:02 pm, March 15, 2012](http://dentedreality.com.au/2012/03/15/sxsw-2012/ "5:02 pm") 
jQuery(document).ready(function(){
var gmap\_m1151fa67f1e6b88859d44ae4e94198a3 = {
positions : {
476 : new google.maps.LatLng( '30.2675', '-97.740667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1151fa67f1e6b88859d44ae4e94198a3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1151fa67f1e6b88859d44ae4e94198a3.positions ) {
gmap\_m1151fa67f1e6b88859d44ae4e94198a3.bounds.extend( gmap\_m1151fa67f1e6b88859d44ae4e94198a3.positions[m] );
}
// Render markers
for ( var m in gmap\_m1151fa67f1e6b88859d44ae4e94198a3.positions ) {
gmap\_m1151fa67f1e6b88859d44ae4e94198a3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1151fa67f1e6b88859d44ae4e94198a3.map,
position : gmap\_m1151fa67f1e6b88859d44ae4e94198a3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1151fa67f1e6b88859d44ae4e94198a3.map.setCenter( gmap\_m1151fa67f1e6b88859d44ae4e94198a3.positions[476] );
});