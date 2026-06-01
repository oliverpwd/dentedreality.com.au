---
title: Epic Australian Adventure, 2014
date: '2014-03-14T14:02:34+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904714802_2cdb3d88b4_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904714802_2cdb3d88b4_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-47/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-47/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904714802/) [2:02 pm, March 14, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-47/ "2:02 pm") 
jQuery(document).ready(function(){
var gmap\_m31f24941e88dcb949093f83d28b78539 = {
positions : {
595 : new google.maps.LatLng( '-31.9466', '115.864433' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m31f24941e88dcb949093f83d28b78539' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m31f24941e88dcb949093f83d28b78539.positions ) {
gmap\_m31f24941e88dcb949093f83d28b78539.bounds.extend( gmap\_m31f24941e88dcb949093f83d28b78539.positions[m] );
}
// Render markers
for ( var m in gmap\_m31f24941e88dcb949093f83d28b78539.positions ) {
gmap\_m31f24941e88dcb949093f83d28b78539.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m31f24941e88dcb949093f83d28b78539.map,
position : gmap\_m31f24941e88dcb949093f83d28b78539.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m31f24941e88dcb949093f83d28b78539.map.setCenter( gmap\_m31f24941e88dcb949093f83d28b78539.positions[595] );
});