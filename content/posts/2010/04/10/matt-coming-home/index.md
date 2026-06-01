---
title: Matt Coming Home
date: '2010-04-10T08:33:56+00:00'
format: image
service: flickr
tags:
- matt
- photomatt
- tombrown
- trackerschool
- tracking
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516475332_d59ac1a349_o.jpg?resize=607%2C455
---

[![Matt Coming Home](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516475332_d59ac1a349_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/10/matt-coming-home/) 
# [Matt Coming Home](http://dentedreality.com.au/2010/04/10/matt-coming-home/)

Matt, crossing the bridge to head home from Tracker School





* #[matt](http://dentedreality.com.au/tags/matt/)
* #[photomatt](http://dentedreality.com.au/tags/photomatt/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516475332/) [8:33 am, April 10, 2010](http://dentedreality.com.au/2010/04/10/matt-coming-home/ "8:33 am") 
jQuery(document).ready(function(){
var gmap\_ma372f1fff965fe51334b1b5d73314661 = {
positions : {
140 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma372f1fff965fe51334b1b5d73314661' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma372f1fff965fe51334b1b5d73314661.positions ) {
gmap\_ma372f1fff965fe51334b1b5d73314661.bounds.extend( gmap\_ma372f1fff965fe51334b1b5d73314661.positions[m] );
}
// Render markers
for ( var m in gmap\_ma372f1fff965fe51334b1b5d73314661.positions ) {
gmap\_ma372f1fff965fe51334b1b5d73314661.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma372f1fff965fe51334b1b5d73314661.map,
position : gmap\_ma372f1fff965fe51334b1b5d73314661.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma372f1fff965fe51334b1b5d73314661.map.setCenter( gmap\_ma372f1fff965fe51334b1b5d73314661.positions[140] );
});