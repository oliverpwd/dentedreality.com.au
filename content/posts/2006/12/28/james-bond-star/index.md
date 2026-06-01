---
title: James Bond Star
date: '2006-12-28T19:13:00+00:00'
format: image
service: flickr
tags:
- island
- jamesbond
- phuket
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348095634_2a10e59b04_o.jpg?resize=607%2C809
---

[![James Bond Star](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348095634_2a10e59b04_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/28/james-bond-star/) 
# [James Bond Star](http://dentedreality.com.au/2006/12/28/james-bond-star/)

Apparently this was featured in a James Bond movie?





* #[island](http://dentedreality.com.au/tags/island/)
* #[jamesbond](http://dentedreality.com.au/tags/jamesbond/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348095634/) [7:13 pm, December 28, 2006](http://dentedreality.com.au/2006/12/28/james-bond-star/ "7:13 pm") 
jQuery(document).ready(function(){
var gmap\_m88ad675ab7d096664f5dc3bc0dd1682a = {
positions : {
145 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m88ad675ab7d096664f5dc3bc0dd1682a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.positions ) {
gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.bounds.extend( gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.positions[m] );
}
// Render markers
for ( var m in gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.positions ) {
gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.map,
position : gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.map.setCenter( gmap\_m88ad675ab7d096664f5dc3bc0dd1682a.positions[145] );
});