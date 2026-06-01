---
title: Ground Zero Memorial
date: '2013-06-29T10:10:02+00:00'
format: image
service: flickr
tags:
- '911'
- groundzero
- memorial
- wtc
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439836328_160f3e7888_o.jpg?resize=607%2C452
---

[![Ground Zero Memorial](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439836328_160f3e7888_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/06/29/ground-zero-memorial/) 
# [Ground Zero Memorial](http://dentedreality.com.au/2013/06/29/ground-zero-memorial/)





* #[911](http://dentedreality.com.au/tags/911/)
* #[groundzero](http://dentedreality.com.au/tags/groundzero/)
* #[memorial](http://dentedreality.com.au/tags/memorial/)
* #[wtc](http://dentedreality.com.au/tags/wtc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439836328/) [10:10 am, June 29, 2013](http://dentedreality.com.au/2013/06/29/ground-zero-memorial/ "10:10 am") 
jQuery(document).ready(function(){
var gmap\_maa38834ad411dd8a8b8334fa62231ec7 = {
positions : {
810 : new google.maps.LatLng( '40.711333', '-74.013167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maa38834ad411dd8a8b8334fa62231ec7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maa38834ad411dd8a8b8334fa62231ec7.positions ) {
gmap\_maa38834ad411dd8a8b8334fa62231ec7.bounds.extend( gmap\_maa38834ad411dd8a8b8334fa62231ec7.positions[m] );
}
// Render markers
for ( var m in gmap\_maa38834ad411dd8a8b8334fa62231ec7.positions ) {
gmap\_maa38834ad411dd8a8b8334fa62231ec7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maa38834ad411dd8a8b8334fa62231ec7.map,
position : gmap\_maa38834ad411dd8a8b8334fa62231ec7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maa38834ad411dd8a8b8334fa62231ec7.map.setCenter( gmap\_maa38834ad411dd8a8b8334fa62231ec7.positions[810] );
});