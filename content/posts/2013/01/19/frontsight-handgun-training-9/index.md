---
title: Frontsight Handgun Training
date: '2013-01-19T11:27:35+00:00'
format: image
service: flickr
tags:
- frontsight
- gun
- gunrange
- handgun
- pistol
- shooting
- training
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8459084337_098644effb_o.jpg?resize=607%2C813
---

[![Frontsight Handgun Training](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8459084337_098644effb_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/01/19/frontsight-handgun-training-9/) 
# [Frontsight Handgun Training](http://dentedreality.com.au/2013/01/19/frontsight-handgun-training-9/)





* #[frontsight](http://dentedreality.com.au/tags/frontsight/)
* #[gun](http://dentedreality.com.au/tags/gun/)
* #[gunrange](http://dentedreality.com.au/tags/gunrange/)
* #[handgun](http://dentedreality.com.au/tags/handgun/)
* #[pistol](http://dentedreality.com.au/tags/pistol/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)
* #[training](http://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459084337/) [11:27 am, January 19, 2013](http://dentedreality.com.au/2013/01/19/frontsight-handgun-training-9/ "11:27 am") 
jQuery(document).ready(function(){
var gmap\_m46ad71f469f1b78a9d453e6a93208fa0 = {
positions : {
475 : new google.maps.LatLng( '36.031333', '-115.883334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m46ad71f469f1b78a9d453e6a93208fa0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m46ad71f469f1b78a9d453e6a93208fa0.positions ) {
gmap\_m46ad71f469f1b78a9d453e6a93208fa0.bounds.extend( gmap\_m46ad71f469f1b78a9d453e6a93208fa0.positions[m] );
}
// Render markers
for ( var m in gmap\_m46ad71f469f1b78a9d453e6a93208fa0.positions ) {
gmap\_m46ad71f469f1b78a9d453e6a93208fa0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m46ad71f469f1b78a9d453e6a93208fa0.map,
position : gmap\_m46ad71f469f1b78a9d453e6a93208fa0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m46ad71f469f1b78a9d453e6a93208fa0.map.setCenter( gmap\_m46ad71f469f1b78a9d453e6a93208fa0.positions[475] );
});