---
title: Epic Australian Adventure, 2014
date: '2014-03-25T09:47:46+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904752682_558c427af6_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904752682_558c427af6_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-36/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-36/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904752682/) [9:47 am, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-36/ "9:47 am") 
jQuery(document).ready(function(){
var gmap\_mba345a864326ec6919b497a8dff2bc77 = {
positions : {
759 : new google.maps.LatLng( '-37.823178', '144.951736' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mba345a864326ec6919b497a8dff2bc77' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mba345a864326ec6919b497a8dff2bc77.positions ) {
gmap\_mba345a864326ec6919b497a8dff2bc77.bounds.extend( gmap\_mba345a864326ec6919b497a8dff2bc77.positions[m] );
}
// Render markers
for ( var m in gmap\_mba345a864326ec6919b497a8dff2bc77.positions ) {
gmap\_mba345a864326ec6919b497a8dff2bc77.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mba345a864326ec6919b497a8dff2bc77.map,
position : gmap\_mba345a864326ec6919b497a8dff2bc77.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mba345a864326ec6919b497a8dff2bc77.map.setCenter( gmap\_mba345a864326ec6919b497a8dff2bc77.positions[759] );
});