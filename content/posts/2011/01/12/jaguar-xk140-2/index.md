---
title: Jaguar XK140
date: '2011-01-12T13:00:22-07:00'
format: image
service: flickr
tags:
- jaguar
- xk140
latitude: '-32.0535'
longitude: '115.846333'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14190002/5434723628_a2ff55e575_o.jpg
---

[![Jaguar XK140](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14190002/5434723628_a2ff55e575_o.jpg)](https://dentedreality.com.au/2011/01/12/jaguar-xk140-2/) 
# [Jaguar XK140](https://dentedreality.com.au/2011/01/12/jaguar-xk140-2/)

[![Jaguar XK140](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14190002/5434723628_a2ff55e575_o.jpg)](http://www.flickr.com/photos/borkazoid/5434723628/)

-32.0535115.846333




* #[jaguar](https://dentedreality.com.au/tags/jaguar/)
* #[xk140](https://dentedreality.com.au/tags/xk140/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434723628/) [1:00 pm, January 12, 2011](https://dentedreality.com.au/2011/01/12/jaguar-xk140-2/ "1:00 pm") 
jQuery(document).ready(function(){
var gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1 = {
positions : {
294 : new google.maps.LatLng( '-32.0535', '115.846333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.positions ) {
gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.bounds.extend( gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.positions[m] );
}
// Render markers
for ( var m in gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.positions ) {
gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.map,
position : gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.map.setCenter( gmap\_mac2ce1bf2bf29a8ab06214c778afa9d1.positions[294] );
});