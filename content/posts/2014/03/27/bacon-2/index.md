---
title: BACON
date: '2014-03-27T04:21:27+00:00'
format: image
service: flickr
tags:
- bacon
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928317664_7e29bc33e5_o.jpg?resize=607%2C455
---

[![BACON](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928317664_7e29bc33e5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/27/bacon-2/) 
# [BACON](http://dentedreality.com.au/2014/03/27/bacon-2/)

Perth, Mooloolaba and Melbourne





* #[bacon](http://dentedreality.com.au/tags/bacon/)
* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928317664/) [4:21 am, March 27, 2014](http://dentedreality.com.au/2014/03/27/bacon-2/ "4:21 am") 
jQuery(document).ready(function(){
var gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4 = {
positions : {
842 : new google.maps.LatLng( '-37.825775', '144.956497' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.positions ) {
gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.bounds.extend( gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.positions[m] );
}
// Render markers
for ( var m in gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.positions ) {
gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.map,
position : gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.map.setCenter( gmap\_me03a2c3ef1ad4ae2ef572ed3fc8032b4.positions[842] );
});