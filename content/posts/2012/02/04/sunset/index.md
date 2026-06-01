---
title: Sunset
date: '2012-02-04T13:17:04+00:00'
format: image
service: flickr
tags:
- sky
- sunset
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813458504_3f0c93b896_o.jpg?resize=607%2C813
---

[![Sunset](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813458504_3f0c93b896_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/02/04/sunset/) 
# [Sunset](http://dentedreality.com.au/2012/02/04/sunset/)

I think





* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813458504/) [1:17 pm, February 4, 2012](http://dentedreality.com.au/2012/02/04/sunset/ "1:17 pm") 
jQuery(document).ready(function(){
var gmap\_mfff89ab6411a5f35455106c9de854487 = {
positions : {
975 : new google.maps.LatLng( '37.878', '-122.062667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfff89ab6411a5f35455106c9de854487' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfff89ab6411a5f35455106c9de854487.positions ) {
gmap\_mfff89ab6411a5f35455106c9de854487.bounds.extend( gmap\_mfff89ab6411a5f35455106c9de854487.positions[m] );
}
// Render markers
for ( var m in gmap\_mfff89ab6411a5f35455106c9de854487.positions ) {
gmap\_mfff89ab6411a5f35455106c9de854487.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfff89ab6411a5f35455106c9de854487.map,
position : gmap\_mfff89ab6411a5f35455106c9de854487.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfff89ab6411a5f35455106c9de854487.map.setCenter( gmap\_mfff89ab6411a5f35455106c9de854487.positions[975] );
});