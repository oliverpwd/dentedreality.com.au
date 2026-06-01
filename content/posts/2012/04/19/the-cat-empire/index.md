---
title: The Cat Empire
date: '2012-04-19T19:57:03+00:00'
format: image
service: flickr
tags:
- catempire
- livemusic
- sanfrancisco
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/04/7770706876_35f0d4c0d4_o.jpg?resize=607%2C452
---

[![The Cat Empire](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/04/7770706876_35f0d4c0d4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/04/19/the-cat-empire/) 
# [The Cat Empire](http://dentedreality.com.au/2012/04/19/the-cat-empire/)





* #[catempire](http://dentedreality.com.au/tags/catempire/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770706876/) [7:57 pm, April 19, 2012](http://dentedreality.com.au/2012/04/19/the-cat-empire/ "7:57 pm") 
jQuery(document).ready(function(){
var gmap\_m4bf22c1f8bed0f633cbe2804e7c75486 = {
positions : {
498 : new google.maps.LatLng( '37.771499', '-122.413334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4bf22c1f8bed0f633cbe2804e7c75486' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.positions ) {
gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.bounds.extend( gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.positions[m] );
}
// Render markers
for ( var m in gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.positions ) {
gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.map,
position : gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.map.setCenter( gmap\_m4bf22c1f8bed0f633cbe2804e7c75486.positions[498] );
});