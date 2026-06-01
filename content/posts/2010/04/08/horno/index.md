---
title: Horno
date: '2010-04-08T10:17:55+00:00'
format: image
service: flickr
tags:
- horno
- tombrown
- trackerschool
- tracking
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516453382_bd7d0e2517_o.jpg?resize=607%2C455
---

[![Horno](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516453382_bd7d0e2517_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/horno/) 
# [Horno](http://dentedreality.com.au/2010/04/08/horno/)

Earth oven, pronounced "orno".





* #[horno](http://dentedreality.com.au/tags/horno/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516453382/) [10:17 am, April 8, 2010](http://dentedreality.com.au/2010/04/08/horno/ "10:17 am") 
jQuery(document).ready(function(){
var gmap\_mbd3b86a8a430519ee0709a37158c33c4 = {
positions : {
203 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbd3b86a8a430519ee0709a37158c33c4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbd3b86a8a430519ee0709a37158c33c4.positions ) {
gmap\_mbd3b86a8a430519ee0709a37158c33c4.bounds.extend( gmap\_mbd3b86a8a430519ee0709a37158c33c4.positions[m] );
}
// Render markers
for ( var m in gmap\_mbd3b86a8a430519ee0709a37158c33c4.positions ) {
gmap\_mbd3b86a8a430519ee0709a37158c33c4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbd3b86a8a430519ee0709a37158c33c4.map,
position : gmap\_mbd3b86a8a430519ee0709a37158c33c4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbd3b86a8a430519ee0709a37158c33c4.map.setCenter( gmap\_mbd3b86a8a430519ee0709a37158c33c4.positions[203] );
});