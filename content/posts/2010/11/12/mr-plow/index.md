---
title: Mr Plow!
date: '2010-11-12T07:09:48+00:00'
format: image
service: flickr
tags:
- awesome
- minnesota
- snowplow
- truck
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183208435_cbe448b396_o.jpg?resize=607%2C452
---

[![Mr Plow!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183208435_cbe448b396_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/12/mr-plow/) 
# [Mr Plow!](http://dentedreality.com.au/2010/11/12/mr-plow/)





* #[awesome](http://dentedreality.com.au/tags/awesome/)
* #[minnesota](http://dentedreality.com.au/tags/minnesota/)
* #[snowplow](http://dentedreality.com.au/tags/snowplow/)
* #[truck](http://dentedreality.com.au/tags/truck/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183208435/) [7:09 am, November 12, 2010](http://dentedreality.com.au/2010/11/12/mr-plow/ "7:09 am") 
jQuery(document).ready(function(){
var gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1 = {
positions : {
570 : new google.maps.LatLng( '44.978', '-93.257834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.positions ) {
gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.bounds.extend( gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.positions[m] );
}
// Render markers
for ( var m in gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.positions ) {
gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.map,
position : gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.map.setCenter( gmap\_m6a5f9bded0562f9a79d220c6bd77c8a1.positions[570] );
});