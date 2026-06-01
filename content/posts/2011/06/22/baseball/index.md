---
title: Baseball
date: '2011-06-22T16:30:23+00:00'
format: image
service: flickr
tags:
- attpark
- baseball
- minnesotatwins
- sfgiants
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/6323452100_67bc632575_o.jpg?resize=607%2C452
---

[![Baseball](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/6323452100_67bc632575_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/06/22/baseball/) 
# [Baseball](http://dentedreality.com.au/2011/06/22/baseball/)

Giants v Twins





* #[attpark](http://dentedreality.com.au/tags/attpark/)
* #[baseball](http://dentedreality.com.au/tags/baseball/)
* #[minnesotatwins](http://dentedreality.com.au/tags/minnesotatwins/)
* #[sfgiants](http://dentedreality.com.au/tags/sfgiants/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323452100/) [4:30 pm, June 22, 2011](http://dentedreality.com.au/2011/06/22/baseball/ "4:30 pm") 
jQuery(document).ready(function(){
var gmap\_m3fc69d548eea8d8a8f704f1cd41c8592 = {
positions : {
129 : new google.maps.LatLng( '37.779', '-122.389667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3fc69d548eea8d8a8f704f1cd41c8592' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.positions ) {
gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.bounds.extend( gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.positions[m] );
}
// Render markers
for ( var m in gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.positions ) {
gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.map,
position : gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.map.setCenter( gmap\_m3fc69d548eea8d8a8f704f1cd41c8592.positions[129] );
});