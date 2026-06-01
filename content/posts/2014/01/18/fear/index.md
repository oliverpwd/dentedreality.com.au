---
title: Fear
date: '2014-01-18T17:24:51+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- fear
- me
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13903833872_9822f08d25_o.jpg?resize=607%2C455
---

[![Fear](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13903833872_9822f08d25_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/18/fear/) 
# [Fear](http://dentedreality.com.au/2014/01/18/fear/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[fear](http://dentedreality.com.au/tags/fear/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13903833872/) [5:24 pm, January 18, 2014](http://dentedreality.com.au/2014/01/18/fear/ "5:24 pm") 
jQuery(document).ready(function(){
var gmap\_mf91f02c8673e0c240654b8f8a80c1d12 = {
positions : {
467 : new google.maps.LatLng( '40.686961', '-73.977662' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf91f02c8673e0c240654b8f8a80c1d12' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf91f02c8673e0c240654b8f8a80c1d12.positions ) {
gmap\_mf91f02c8673e0c240654b8f8a80c1d12.bounds.extend( gmap\_mf91f02c8673e0c240654b8f8a80c1d12.positions[m] );
}
// Render markers
for ( var m in gmap\_mf91f02c8673e0c240654b8f8a80c1d12.positions ) {
gmap\_mf91f02c8673e0c240654b8f8a80c1d12.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf91f02c8673e0c240654b8f8a80c1d12.map,
position : gmap\_mf91f02c8673e0c240654b8f8a80c1d12.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf91f02c8673e0c240654b8f8a80c1d12.map.setCenter( gmap\_mf91f02c8673e0c240654b8f8a80c1d12.positions[467] );
});