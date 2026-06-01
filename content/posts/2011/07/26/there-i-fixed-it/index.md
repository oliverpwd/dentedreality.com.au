---
title: There I Fixed It
date: '2011-07-26T09:38:17+00:00'
format: image
service: flickr
tags:
- alarm
- fixed
- security
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322936285_157245f4ab_o.jpg?resize=607%2C452
---

[![There I Fixed It](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322936285_157245f4ab_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/07/26/there-i-fixed-it/) 
# [There I Fixed It](http://dentedreality.com.au/2011/07/26/there-i-fixed-it/)

The security alarm randomly went off… so we disconnected the audible part of it. Fixed.





* #[alarm](http://dentedreality.com.au/tags/alarm/)
* #[fixed](http://dentedreality.com.au/tags/fixed/)
* #[security](http://dentedreality.com.au/tags/security/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322936285/) [9:38 am, July 26, 2011](http://dentedreality.com.au/2011/07/26/there-i-fixed-it/ "9:38 am") 
jQuery(document).ready(function(){
var gmap\_md59c3fc67677f1b2b65f4092b3aa5c75 = {
positions : {
489 : new google.maps.LatLng( '37.782833', '-122.388167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md59c3fc67677f1b2b65f4092b3aa5c75' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.positions ) {
gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.bounds.extend( gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.positions[m] );
}
// Render markers
for ( var m in gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.positions ) {
gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.map,
position : gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.map.setCenter( gmap\_md59c3fc67677f1b2b65f4092b3aa5c75.positions[489] );
});