---
title: Frankenthumb
date: '2014-02-07T20:18:03+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13924814755_563b9f86f9_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13924814755_563b9f86f9_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/07/frankenthumb-3/) 
# [Frankenthumb](http://dentedreality.com.au/2014/02/07/frankenthumb-3/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924814755/) [8:18 pm, February 7, 2014](http://dentedreality.com.au/2014/02/07/frankenthumb-3/ "8:18 pm") 
jQuery(document).ready(function(){
var gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e = {
positions : {
471 : new google.maps.LatLng( '38.955433', '-77.073228' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.positions ) {
gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.bounds.extend( gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.positions[m] );
}
// Render markers
for ( var m in gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.positions ) {
gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.map,
position : gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.map.setCenter( gmap\_m08247c93158fa436fbb5f6ff9e2a8c3e.positions[471] );
});