---
title: Epic Australian Adventure, 2014
date: '2014-03-25T09:48:19+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904745461_094cf091e1_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904745461_094cf091e1_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-35/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-35/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904745461/) [9:48 am, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-35/ "9:48 am") 
jQuery(document).ready(function(){
var gmap\_m176700673d291eb4cdf07631f43dbeeb = {
positions : {
67 : new google.maps.LatLng( '-37.82327', '144.951797' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m176700673d291eb4cdf07631f43dbeeb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m176700673d291eb4cdf07631f43dbeeb.positions ) {
gmap\_m176700673d291eb4cdf07631f43dbeeb.bounds.extend( gmap\_m176700673d291eb4cdf07631f43dbeeb.positions[m] );
}
// Render markers
for ( var m in gmap\_m176700673d291eb4cdf07631f43dbeeb.positions ) {
gmap\_m176700673d291eb4cdf07631f43dbeeb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m176700673d291eb4cdf07631f43dbeeb.map,
position : gmap\_m176700673d291eb4cdf07631f43dbeeb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m176700673d291eb4cdf07631f43dbeeb.map.setCenter( gmap\_m176700673d291eb4cdf07631f43dbeeb.positions[67] );
});