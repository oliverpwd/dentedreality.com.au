---
title: ''
date: '2014-11-09T14:23:58+00:00'
format: image
service: instagram
tags:
- latergram
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10735304_744647192277533_1909358408_n.jpg?resize=640%2C640
---

[![Beautiful CO sunset #latergram](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10735304_744647192277533_1909358408_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/09/beautiful-co-sunset-latergram/) 

Beautiful CO sunset #latergram





* #[latergram](http://dentedreality.com.au/tags/latergram/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/vMaYfkimP4/) [2:23 pm, November 9, 2014](http://dentedreality.com.au/2014/11/09/beautiful-co-sunset-latergram/ "2:23 pm") 
jQuery(document).ready(function(){
var gmap\_m04d31817d3657ec5337453ef9d1a121a = {
positions : {
271 : new google.maps.LatLng( '39.8185745', '-105.286428802' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m04d31817d3657ec5337453ef9d1a121a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m04d31817d3657ec5337453ef9d1a121a.positions ) {
gmap\_m04d31817d3657ec5337453ef9d1a121a.bounds.extend( gmap\_m04d31817d3657ec5337453ef9d1a121a.positions[m] );
}
// Render markers
for ( var m in gmap\_m04d31817d3657ec5337453ef9d1a121a.positions ) {
gmap\_m04d31817d3657ec5337453ef9d1a121a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m04d31817d3657ec5337453ef9d1a121a.map,
position : gmap\_m04d31817d3657ec5337453ef9d1a121a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m04d31817d3657ec5337453ef9d1a121a.map.setCenter( gmap\_m04d31817d3657ec5337453ef9d1a121a.positions[271] );
});