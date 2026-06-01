---
title: ASTR
date: '2014-01-16T17:55:37+00:00'
format: image
service: flickr
tags:
- astr
- live
- music
- newyork
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13926944985_a3d90e3e6f_o.jpg?resize=607%2C455
---

[![ASTR](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13926944985_a3d90e3e6f_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/16/astr-2/) 
# [ASTR](http://dentedreality.com.au/2014/01/16/astr-2/)





* #[astr](http://dentedreality.com.au/tags/astr/)
* #[live](http://dentedreality.com.au/tags/live/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13926944985/) [5:55 pm, January 16, 2014](http://dentedreality.com.au/2014/01/16/astr-2/ "5:55 pm") 
jQuery(document).ready(function(){
var gmap\_m8ac24e79f7f600a9600f8d5b1ba88165 = {
positions : {
550 : new google.maps.LatLng( '40.72993', '-74.010095' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8ac24e79f7f600a9600f8d5b1ba88165' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.positions ) {
gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.bounds.extend( gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.positions[m] );
}
// Render markers
for ( var m in gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.positions ) {
gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.map,
position : gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.map.setCenter( gmap\_m8ac24e79f7f600a9600f8d5b1ba88165.positions[550] );
});