---
title: Harriman State Park
date: '2013-08-31T07:29:21+00:00'
format: image
tags:
- backpacking
- harriman
- harrimanstatepark
- hiking
- newyork
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767989443_3b13d82be9_o.jpg?resize=607%2C452
---

[![Harriman State Park](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767989443_3b13d82be9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/31/harriman-state-park-5/) 
# [Harriman State Park](http://dentedreality.com.au/2013/08/31/harriman-state-park-5/)





* #[backpacking](http://dentedreality.com.au/tags/backpacking/)
* #[harriman](http://dentedreality.com.au/tags/harriman/)
* #[harrimanstatepark](http://dentedreality.com.au/tags/harrimanstatepark/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767989443/) [7:29 am, August 31, 2013](http://dentedreality.com.au/2013/08/31/harriman-state-park-5/ "7:29 am") 
jQuery(document).ready(function(){
var gmap\_m465c3789ee7d9c16cb4f22a12bce116b = {
positions : {
300 : new google.maps.LatLng( '41.193833', '-74.1815' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m465c3789ee7d9c16cb4f22a12bce116b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m465c3789ee7d9c16cb4f22a12bce116b.positions ) {
gmap\_m465c3789ee7d9c16cb4f22a12bce116b.bounds.extend( gmap\_m465c3789ee7d9c16cb4f22a12bce116b.positions[m] );
}
// Render markers
for ( var m in gmap\_m465c3789ee7d9c16cb4f22a12bce116b.positions ) {
gmap\_m465c3789ee7d9c16cb4f22a12bce116b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m465c3789ee7d9c16cb4f22a12bce116b.map,
position : gmap\_m465c3789ee7d9c16cb4f22a12bce116b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m465c3789ee7d9c16cb4f22a12bce116b.map.setCenter( gmap\_m465c3789ee7d9c16cb4f22a12bce116b.positions[300] );
});