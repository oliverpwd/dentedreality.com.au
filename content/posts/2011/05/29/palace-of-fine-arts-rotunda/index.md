---
title: Palace of Fine Arts Rotunda
date: '2011-05-29T07:46:50+00:00'
format: image
service: flickr
tags:
- owenswedding
- palaceoffinearts
- rotunda
- wedding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802874467_83ecc7d302_o.jpg?resize=607%2C813
---

[![Palace of Fine Arts Rotunda](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802874467_83ecc7d302_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/29/palace-of-fine-arts-rotunda/) 
# [Palace of Fine Arts Rotunda](http://dentedreality.com.au/2011/05/29/palace-of-fine-arts-rotunda/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[palaceoffinearts](http://dentedreality.com.au/tags/palaceoffinearts/)
* #[rotunda](http://dentedreality.com.au/tags/rotunda/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802874467/) [7:46 am, May 29, 2011](http://dentedreality.com.au/2011/05/29/palace-of-fine-arts-rotunda/ "7:46 am") 
jQuery(document).ready(function(){
var gmap\_m5469ca2875d3cffaa42aceabf45e53d0 = {
positions : {
267 : new google.maps.LatLng( '37.802666', '-122.447834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5469ca2875d3cffaa42aceabf45e53d0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5469ca2875d3cffaa42aceabf45e53d0.positions ) {
gmap\_m5469ca2875d3cffaa42aceabf45e53d0.bounds.extend( gmap\_m5469ca2875d3cffaa42aceabf45e53d0.positions[m] );
}
// Render markers
for ( var m in gmap\_m5469ca2875d3cffaa42aceabf45e53d0.positions ) {
gmap\_m5469ca2875d3cffaa42aceabf45e53d0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5469ca2875d3cffaa42aceabf45e53d0.map,
position : gmap\_m5469ca2875d3cffaa42aceabf45e53d0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5469ca2875d3cffaa42aceabf45e53d0.map.setCenter( gmap\_m5469ca2875d3cffaa42aceabf45e53d0.positions[267] );
});