---
title: 4th of July, 2013
date: '2013-07-04T17:21:32+00:00'
format: image
service: flickr
tags:
- '20130704'
- 4thofjuly
- fireworks
- sparklers
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9439838924_d98ca9b2ae_o.jpg?resize=607%2C452
---

[![4th of July, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9439838924_d98ca9b2ae_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-5/) 
# [4th of July, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-5/)





* #[20130704](http://dentedreality.com.au/tags/20130704/)
* #[4thofjuly](http://dentedreality.com.au/tags/4thofjuly/)
* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[sparklers](http://dentedreality.com.au/tags/sparklers/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439838924/) [5:21 pm, July 4, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-5/ "5:21 pm") 
jQuery(document).ready(function(){
var gmap\_m280fbcd31ad5b7a1720113811eac5b20 = {
positions : {
993 : new google.maps.LatLng( '40.716666', '-73.946' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m280fbcd31ad5b7a1720113811eac5b20' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m280fbcd31ad5b7a1720113811eac5b20.positions ) {
gmap\_m280fbcd31ad5b7a1720113811eac5b20.bounds.extend( gmap\_m280fbcd31ad5b7a1720113811eac5b20.positions[m] );
}
// Render markers
for ( var m in gmap\_m280fbcd31ad5b7a1720113811eac5b20.positions ) {
gmap\_m280fbcd31ad5b7a1720113811eac5b20.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m280fbcd31ad5b7a1720113811eac5b20.map,
position : gmap\_m280fbcd31ad5b7a1720113811eac5b20.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m280fbcd31ad5b7a1720113811eac5b20.map.setCenter( gmap\_m280fbcd31ad5b7a1720113811eac5b20.positions[993] );
});