---
title: Jackolanterns!
date: '2010-10-24T13:56:05+00:00'
format: image
service: flickr
tags:
- halloween
- jackolantern
- pumpkin
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183767372_fcb638c838_o.jpg?resize=607%2C452
---

[![Jackolanterns!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183767372_fcb638c838_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/10/24/jackolanterns-2/) 
# [Jackolanterns!](http://dentedreality.com.au/2010/10/24/jackolanterns-2/)





* #[halloween](http://dentedreality.com.au/tags/halloween/)
* #[jackolantern](http://dentedreality.com.au/tags/jackolantern/)
* #[pumpkin](http://dentedreality.com.au/tags/pumpkin/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183767372/) [1:56 pm, October 24, 2010](http://dentedreality.com.au/2010/10/24/jackolanterns-2/ "1:56 pm") 
jQuery(document).ready(function(){
var gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c = {
positions : {
680 : new google.maps.LatLng( '37.795666', '-122.425167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.positions ) {
gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.bounds.extend( gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.positions[m] );
}
// Render markers
for ( var m in gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.positions ) {
gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.map,
position : gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.map.setCenter( gmap\_mb3bb0847ef1e33566e6cf5a84f9d744c.positions[680] );
});