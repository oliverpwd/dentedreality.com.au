---
title: ''
date: '2014-04-30T16:07:11+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10269027_1431312680457812_623795374_n.jpg?resize=640%2C640
---

[![This sounds like something @hugobaeta would be into.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10269027_1431312680457812_623795374_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/30/this-sounds-like-something-hugobaeta-would-be-into/) 

This sounds like something @hugobaeta would be into.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/nbbCpVCmKc/) [4:07 pm, April 30, 2014](http://dentedreality.com.au/2014/04/30/this-sounds-like-something-hugobaeta-would-be-into/ "4:07 pm") 
jQuery(document).ready(function(){
var gmap\_m2c415722d8703ac1aec8fc5b001e8dcc = {
positions : {
89 : new google.maps.LatLng( '53.34318', '-6.263625' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2c415722d8703ac1aec8fc5b001e8dcc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.positions ) {
gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.bounds.extend( gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.positions[m] );
}
// Render markers
for ( var m in gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.positions ) {
gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.map,
position : gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.map.setCenter( gmap\_m2c415722d8703ac1aec8fc5b001e8dcc.positions[89] );
});