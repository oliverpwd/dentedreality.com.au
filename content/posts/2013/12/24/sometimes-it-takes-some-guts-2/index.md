---
title: ''
date: '2013-12-24T12:27:33+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/9e0305386cc011e3ba25129d09c8e96a_8.jpg?resize=640%2C640
---

[![Sometimes it takes some guts...](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/9e0305386cc011e3ba25129d09c8e96a_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/12/24/sometimes-it-takes-some-guts-2/) 

Sometimes it takes some guts…





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/iUA862imMV/) [12:27 pm, December 24, 2013](http://dentedreality.com.au/2013/12/24/sometimes-it-takes-some-guts-2/ "12:27 pm") 
jQuery(document).ready(function(){
var gmap\_m23ad8509a43ce584b169615747c693b5 = {
positions : {
607 : new google.maps.LatLng( '40.71733038', '-73.997565465' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m23ad8509a43ce584b169615747c693b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m23ad8509a43ce584b169615747c693b5.positions ) {
gmap\_m23ad8509a43ce584b169615747c693b5.bounds.extend( gmap\_m23ad8509a43ce584b169615747c693b5.positions[m] );
}
// Render markers
for ( var m in gmap\_m23ad8509a43ce584b169615747c693b5.positions ) {
gmap\_m23ad8509a43ce584b169615747c693b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m23ad8509a43ce584b169615747c693b5.map,
position : gmap\_m23ad8509a43ce584b169615747c693b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m23ad8509a43ce584b169615747c693b5.map.setCenter( gmap\_m23ad8509a43ce584b169615747c693b5.positions[607] );
});