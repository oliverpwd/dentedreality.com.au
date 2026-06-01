---
title: Epic Australian Adventure, 2014
date: '2014-03-10T03:54:55+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928263244_1c1fc96f9c_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928263244_1c1fc96f9c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/10/epic-australian-adventure-2014-56/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/10/epic-australian-adventure-2014-56/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928263244/) [3:54 am, March 10, 2014](http://dentedreality.com.au/2014/03/10/epic-australian-adventure-2014-56/ "3:54 am") 
jQuery(document).ready(function(){
var gmap\_mb32dd304571859fe678bf151f1b4c8ab = {
positions : {
575 : new google.maps.LatLng( '-32.053123', '115.846336' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb32dd304571859fe678bf151f1b4c8ab' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb32dd304571859fe678bf151f1b4c8ab.positions ) {
gmap\_mb32dd304571859fe678bf151f1b4c8ab.bounds.extend( gmap\_mb32dd304571859fe678bf151f1b4c8ab.positions[m] );
}
// Render markers
for ( var m in gmap\_mb32dd304571859fe678bf151f1b4c8ab.positions ) {
gmap\_mb32dd304571859fe678bf151f1b4c8ab.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb32dd304571859fe678bf151f1b4c8ab.map,
position : gmap\_mb32dd304571859fe678bf151f1b4c8ab.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb32dd304571859fe678bf151f1b4c8ab.map.setCenter( gmap\_mb32dd304571859fe678bf151f1b4c8ab.positions[575] );
});