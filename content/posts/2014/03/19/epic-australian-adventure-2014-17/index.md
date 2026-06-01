---
title: Epic Australian Adventure, 2014
date: '2014-03-19T04:40:09+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928286154_8f7bd439e3_o.jpg?resize=607%2C194
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928286154_8f7bd439e3_o.jpg?resize=607%2C194)](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-17/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-17/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928286154/) [4:40 am, March 19, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-17/ "4:40 am") 
jQuery(document).ready(function(){
var gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62 = {
positions : {
299 : new google.maps.LatLng( '-31.997289', '115.750558' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.positions ) {
gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.bounds.extend( gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.positions[m] );
}
// Render markers
for ( var m in gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.positions ) {
gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.map,
position : gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.map.setCenter( gmap\_m4b1dd36e185b45d33a6a82f0d31a6c62.positions[299] );
});