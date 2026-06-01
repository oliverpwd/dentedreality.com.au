---
title: Frontsight Handgun Training
date: '2013-01-20T04:46:49+00:00'
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
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460187292_1a029e8224_o.jpg?resize=607%2C452
---

[![Frontsight Handgun Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460187292_1a029e8224_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/01/20/frontsight-handgun-training-4/) 
# [Frontsight Handgun Training](http://dentedreality.com.au/2013/01/20/frontsight-handgun-training-4/)





* #[frontsight](http://dentedreality.com.au/tags/frontsight/)
* #[gun](http://dentedreality.com.au/tags/gun/)
* #[gunrange](http://dentedreality.com.au/tags/gunrange/)
* #[handgun](http://dentedreality.com.au/tags/handgun/)
* #[pistol](http://dentedreality.com.au/tags/pistol/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)
* #[training](http://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460187292/) [4:46 am, January 20, 2013](http://dentedreality.com.au/2013/01/20/frontsight-handgun-training-4/ "4:46 am") 
jQuery(document).ready(function(){
var gmap\_med13927d2b128ed90d5b4322057174ed = {
positions : {
628 : new google.maps.LatLng( '36.042333', '-115.890667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_med13927d2b128ed90d5b4322057174ed' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_med13927d2b128ed90d5b4322057174ed.positions ) {
gmap\_med13927d2b128ed90d5b4322057174ed.bounds.extend( gmap\_med13927d2b128ed90d5b4322057174ed.positions[m] );
}
// Render markers
for ( var m in gmap\_med13927d2b128ed90d5b4322057174ed.positions ) {
gmap\_med13927d2b128ed90d5b4322057174ed.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_med13927d2b128ed90d5b4322057174ed.map,
position : gmap\_med13927d2b128ed90d5b4322057174ed.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_med13927d2b128ed90d5b4322057174ed.map.setCenter( gmap\_med13927d2b128ed90d5b4322057174ed.positions[628] );
});