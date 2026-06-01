---
title: Epic Australian Adventure, 2014
date: '2014-03-28T08:40:14+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927880925_ff601f6162_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927880925_ff601f6162_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-25/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-25/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927880925/) [8:40 am, March 28, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-25/ "8:40 am") 
jQuery(document).ready(function(){
var gmap\_m7e1ff29337069f91a01c2a3279ebd322 = {
positions : {
658 : new google.maps.LatLng( '-37.86472', '144.965727' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7e1ff29337069f91a01c2a3279ebd322' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7e1ff29337069f91a01c2a3279ebd322.positions ) {
gmap\_m7e1ff29337069f91a01c2a3279ebd322.bounds.extend( gmap\_m7e1ff29337069f91a01c2a3279ebd322.positions[m] );
}
// Render markers
for ( var m in gmap\_m7e1ff29337069f91a01c2a3279ebd322.positions ) {
gmap\_m7e1ff29337069f91a01c2a3279ebd322.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7e1ff29337069f91a01c2a3279ebd322.map,
position : gmap\_m7e1ff29337069f91a01c2a3279ebd322.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7e1ff29337069f91a01c2a3279ebd322.map.setCenter( gmap\_m7e1ff29337069f91a01c2a3279ebd322.positions[658] );
});