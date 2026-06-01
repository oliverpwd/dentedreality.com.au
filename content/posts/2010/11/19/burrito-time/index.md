---
title: Burrito Time
date: '2010-11-19T17:17:04+00:00'
format: image
service: flickr
tags:
- burrito
- burritofriday
- burritup
- taqueria
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434021329_2cdfb2eff9_o.jpg?resize=607%2C452
---

[![Burrito Time](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434021329_2cdfb2eff9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/19/burrito-time/) 
# [Burrito Time](http://dentedreality.com.au/2010/11/19/burrito-time/)





* #[burrito](http://dentedreality.com.au/tags/burrito/)
* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[burritup](http://dentedreality.com.au/tags/burritup/)
* #[taqueria](http://dentedreality.com.au/tags/taqueria/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434021329/) [5:17 pm, November 19, 2010](http://dentedreality.com.au/2010/11/19/burrito-time/ "5:17 pm") 
jQuery(document).ready(function(){
var gmap\_m3dcb5958e803a29eb13e309b4e7209be = {
positions : {
400 : new google.maps.LatLng( '37.761666', '-122.421667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3dcb5958e803a29eb13e309b4e7209be' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3dcb5958e803a29eb13e309b4e7209be.positions ) {
gmap\_m3dcb5958e803a29eb13e309b4e7209be.bounds.extend( gmap\_m3dcb5958e803a29eb13e309b4e7209be.positions[m] );
}
// Render markers
for ( var m in gmap\_m3dcb5958e803a29eb13e309b4e7209be.positions ) {
gmap\_m3dcb5958e803a29eb13e309b4e7209be.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3dcb5958e803a29eb13e309b4e7209be.map,
position : gmap\_m3dcb5958e803a29eb13e309b4e7209be.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3dcb5958e803a29eb13e309b4e7209be.map.setCenter( gmap\_m3dcb5958e803a29eb13e309b4e7209be.positions[400] );
});