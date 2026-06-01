---
title: Glimpse of the View
date: '2006-11-25T08:48:06+00:00'
format: image
service: flickr
tags:
- bigsur
- bottchersgap
- california
- landscape
- lospadresnationalpark
- ridgeline
- valley
- view
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308099213_828ac3ac2d_o.jpg?resize=607%2C455
---

[![Glimpse of the View](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308099213_828ac3ac2d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/11/25/glimpse-of-the-view/) 
# [Glimpse of the View](http://dentedreality.com.au/2006/11/25/glimpse-of-the-view/)

One of many amazing valley views in the area.





* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[landscape](http://dentedreality.com.au/tags/landscape/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[ridgeline](http://dentedreality.com.au/tags/ridgeline/)
* #[valley](http://dentedreality.com.au/tags/valley/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308099213/) [8:48 am, November 25, 2006](http://dentedreality.com.au/2006/11/25/glimpse-of-the-view/ "8:48 am") 
jQuery(document).ready(function(){
var gmap\_me55db0f223934c0b1397c5cc8c8b0571 = {
positions : {
527 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me55db0f223934c0b1397c5cc8c8b0571' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me55db0f223934c0b1397c5cc8c8b0571.positions ) {
gmap\_me55db0f223934c0b1397c5cc8c8b0571.bounds.extend( gmap\_me55db0f223934c0b1397c5cc8c8b0571.positions[m] );
}
// Render markers
for ( var m in gmap\_me55db0f223934c0b1397c5cc8c8b0571.positions ) {
gmap\_me55db0f223934c0b1397c5cc8c8b0571.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me55db0f223934c0b1397c5cc8c8b0571.map,
position : gmap\_me55db0f223934c0b1397c5cc8c8b0571.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me55db0f223934c0b1397c5cc8c8b0571.map.setCenter( gmap\_me55db0f223934c0b1397c5cc8c8b0571.positions[527] );
});