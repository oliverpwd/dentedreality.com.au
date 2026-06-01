---
title: San Francisco
date: '2011-12-18T12:13:23+00:00'
format: image
service: flickr
tags:
- california
- sanfrancisco
- skyline
- view
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959402147_5052581cfc_o.jpg?resize=607%2C452
---

[![San Francisco](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959402147_5052581cfc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/18/san-francisco/) 
# [San Francisco](http://dentedreality.com.au/2011/12/18/san-francisco/)

From the South





* #[california](http://dentedreality.com.au/tags/california/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959402147/) [12:13 pm, December 18, 2011](http://dentedreality.com.au/2011/12/18/san-francisco/ "12:13 pm") 
jQuery(document).ready(function(){
var gmap\_m0d763039a6c2bbd28bca039d8cd7600e = {
positions : {
753 : new google.maps.LatLng( '37.7385', '-122.453167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0d763039a6c2bbd28bca039d8cd7600e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0d763039a6c2bbd28bca039d8cd7600e.positions ) {
gmap\_m0d763039a6c2bbd28bca039d8cd7600e.bounds.extend( gmap\_m0d763039a6c2bbd28bca039d8cd7600e.positions[m] );
}
// Render markers
for ( var m in gmap\_m0d763039a6c2bbd28bca039d8cd7600e.positions ) {
gmap\_m0d763039a6c2bbd28bca039d8cd7600e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0d763039a6c2bbd28bca039d8cd7600e.map,
position : gmap\_m0d763039a6c2bbd28bca039d8cd7600e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0d763039a6c2bbd28bca039d8cd7600e.map.setCenter( gmap\_m0d763039a6c2bbd28bca039d8cd7600e.positions[753] );
});