---
title: Epic Australian Adventure, 2014
date: '2014-03-28T07:59:17+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927880365_bf5a68177d_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927880365_bf5a68177d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-26/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-26/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927880365/) [7:59 am, March 28, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-26/ "7:59 am") 
jQuery(document).ready(function(){
var gmap\_m2674b803b4d3fc67e79713a5f9dbd06f = {
positions : {
134 : new google.maps.LatLng( '-37.869114', '144.975327' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2674b803b4d3fc67e79713a5f9dbd06f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.positions ) {
gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.bounds.extend( gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.positions[m] );
}
// Render markers
for ( var m in gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.positions ) {
gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.map,
position : gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.map.setCenter( gmap\_m2674b803b4d3fc67e79713a5f9dbd06f.positions[134] );
});