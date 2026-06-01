---
title: Frankenthumb
date: '2014-01-24T15:26:32+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901685071_77ea14219e_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901685071_77ea14219e_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/24/frankenthumb-7/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/24/frankenthumb-7/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901685071/) [3:26 pm, January 24, 2014](http://dentedreality.com.au/2014/01/24/frankenthumb-7/ "3:26 pm") 
jQuery(document).ready(function(){
var gmap\_m70ea3313cd3b3bb4506be013d0fc5e94 = {
positions : {
202 : new google.maps.LatLng( '40.669472', '-73.984925' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m70ea3313cd3b3bb4506be013d0fc5e94' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.positions ) {
gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.bounds.extend( gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.positions[m] );
}
// Render markers
for ( var m in gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.positions ) {
gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.map,
position : gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.map.setCenter( gmap\_m70ea3313cd3b3bb4506be013d0fc5e94.positions[202] );
});