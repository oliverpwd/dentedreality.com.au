---
title: Art is a Basic Need
date: '2013-11-29T02:48:41+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900349256_6ba46e2a0b_o.jpg?resize=607%2C455
---

[![Art is a Basic Need](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900349256_6ba46e2a0b_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/29/art-is-a-basic-need/) 
# [Art is a Basic Need](http://dentedreality.com.au/2013/11/29/art-is-a-basic-need/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900349256/) [2:48 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/art-is-a-basic-need/ "2:48 am") 
jQuery(document).ready(function(){
var gmap\_m0994f33e89af14004989c1a28dc9b7a3 = {
positions : {
690 : new google.maps.LatLng( '48.885577', '2.333997' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0994f33e89af14004989c1a28dc9b7a3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0994f33e89af14004989c1a28dc9b7a3.positions ) {
gmap\_m0994f33e89af14004989c1a28dc9b7a3.bounds.extend( gmap\_m0994f33e89af14004989c1a28dc9b7a3.positions[m] );
}
// Render markers
for ( var m in gmap\_m0994f33e89af14004989c1a28dc9b7a3.positions ) {
gmap\_m0994f33e89af14004989c1a28dc9b7a3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0994f33e89af14004989c1a28dc9b7a3.map,
position : gmap\_m0994f33e89af14004989c1a28dc9b7a3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0994f33e89af14004989c1a28dc9b7a3.map.setCenter( gmap\_m0994f33e89af14004989c1a28dc9b7a3.positions[690] );
});