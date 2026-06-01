---
title: ''
date: '2014-09-15T12:30:07+00:00'
format: image
service: instagram
tags:
- a8cmeetup
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10683782_324928311001543_132266627_n.jpg?resize=640%2C640
---

[![Road trip to #a8cmeetup with @alternatekev and @michaelarestad.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10683782_324928311001543_132266627_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/15/road-trip-to-a8cmeetup-with-alternatekev-and-michaelarestad/) 

Road trip to #a8cmeetup with @alternatekev and @michaelarestad.





* #[a8cmeetup](http://dentedreality.com.au/tags/a8cmeetup/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/s-exHJCmJM/) [12:30 pm, September 15, 2014](http://dentedreality.com.au/2014/09/15/road-trip-to-a8cmeetup-with-alternatekev-and-michaelarestad/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_m9c0dfe270965ea33bba310c993ad47d0 = {
positions : {
352 : new google.maps.LatLng( '39.744013333', '-105.44297' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9c0dfe270965ea33bba310c993ad47d0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9c0dfe270965ea33bba310c993ad47d0.positions ) {
gmap\_m9c0dfe270965ea33bba310c993ad47d0.bounds.extend( gmap\_m9c0dfe270965ea33bba310c993ad47d0.positions[m] );
}
// Render markers
for ( var m in gmap\_m9c0dfe270965ea33bba310c993ad47d0.positions ) {
gmap\_m9c0dfe270965ea33bba310c993ad47d0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9c0dfe270965ea33bba310c993ad47d0.map,
position : gmap\_m9c0dfe270965ea33bba310c993ad47d0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9c0dfe270965ea33bba310c993ad47d0.map.setCenter( gmap\_m9c0dfe270965ea33bba310c993ad47d0.positions[352] );
});