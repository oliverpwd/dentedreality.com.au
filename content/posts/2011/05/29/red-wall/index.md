---
title: Red Wall
date: '2011-05-29T16:27:32+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- owenswedding
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433452_d300b945c9_o.jpg?resize=607%2C813
---

[![Red Wall](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433452_d300b945c9_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/29/red-wall/) 
# [Red Wall](http://dentedreality.com.au/2011/05/29/red-wall/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803433452/) [4:27 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/red-wall/ "4:27 pm") 
jQuery(document).ready(function(){
var gmap\_m05afc3bc62bee85967cc97933d47222d = {
positions : {
947 : new google.maps.LatLng( '37.791', '-122.42' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m05afc3bc62bee85967cc97933d47222d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m05afc3bc62bee85967cc97933d47222d.positions ) {
gmap\_m05afc3bc62bee85967cc97933d47222d.bounds.extend( gmap\_m05afc3bc62bee85967cc97933d47222d.positions[m] );
}
// Render markers
for ( var m in gmap\_m05afc3bc62bee85967cc97933d47222d.positions ) {
gmap\_m05afc3bc62bee85967cc97933d47222d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m05afc3bc62bee85967cc97933d47222d.map,
position : gmap\_m05afc3bc62bee85967cc97933d47222d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m05afc3bc62bee85967cc97933d47222d.map.setCenter( gmap\_m05afc3bc62bee85967cc97933d47222d.positions[947] );
});