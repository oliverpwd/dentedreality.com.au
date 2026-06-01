---
title: NERT Citywide Drill, 2011
date: '2011-04-16T08:20:52+00:00'
format: image
service: flickr
tags:
- nert
- sanfrancisco
- sffd
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802146511_be8d277e8e_o.jpg?resize=607%2C452
---

[![NERT Citywide Drill, 2011](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802146511_be8d277e8e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011/) 
# [NERT Citywide Drill, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011/)





* #[nert](http://dentedreality.com.au/tags/nert/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sffd](http://dentedreality.com.au/tags/sffd/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802146511/) [8:20 am, April 16, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011/ "8:20 am") 
jQuery(document).ready(function(){
var gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a = {
positions : {
92 : new google.maps.LatLng( '37.7595', '-122.412834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.positions ) {
gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.bounds.extend( gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.positions[m] );
}
// Render markers
for ( var m in gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.positions ) {
gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.map,
position : gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.map.setCenter( gmap\_m39343e7bd3cbd8f65c7f5aec0b05422a.positions[92] );
});