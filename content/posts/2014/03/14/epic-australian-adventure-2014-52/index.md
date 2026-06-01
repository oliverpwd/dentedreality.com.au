---
title: Epic Australian Adventure, 2014
date: '2014-03-14T08:24:25+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928268024_253961f226_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928268024_253961f226_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-52/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-52/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928268024/) [8:24 am, March 14, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-52/ "8:24 am") 
jQuery(document).ready(function(){
var gmap\_mfeaff48342324a9c531b523fcc36d9ab = {
positions : {
736 : new google.maps.LatLng( '-31.994092', '115.858969' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfeaff48342324a9c531b523fcc36d9ab' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfeaff48342324a9c531b523fcc36d9ab.positions ) {
gmap\_mfeaff48342324a9c531b523fcc36d9ab.bounds.extend( gmap\_mfeaff48342324a9c531b523fcc36d9ab.positions[m] );
}
// Render markers
for ( var m in gmap\_mfeaff48342324a9c531b523fcc36d9ab.positions ) {
gmap\_mfeaff48342324a9c531b523fcc36d9ab.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfeaff48342324a9c531b523fcc36d9ab.map,
position : gmap\_mfeaff48342324a9c531b523fcc36d9ab.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfeaff48342324a9c531b523fcc36d9ab.map.setCenter( gmap\_mfeaff48342324a9c531b523fcc36d9ab.positions[736] );
});