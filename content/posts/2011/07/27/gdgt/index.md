---
title: gdgt
date: '2011-07-27T09:27:09+00:00'
format: image
service: flickr
tags:
- gdgt
- sign
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6323462950_5f1d6a0c56_o.jpg?resize=607%2C452
---

[![gdgt](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6323462950_5f1d6a0c56_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/07/27/gdgt/) 
# [gdgt](http://dentedreality.com.au/2011/07/27/gdgt/)

Sign at the gdgt offices





* #[gdgt](http://dentedreality.com.au/tags/gdgt/)
* #[sign](http://dentedreality.com.au/tags/sign/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323462950/) [9:27 am, July 27, 2011](http://dentedreality.com.au/2011/07/27/gdgt/ "9:27 am") 
jQuery(document).ready(function(){
var gmap\_mffef9f1347392eb4ed4a510dbb043a87 = {
positions : {
596 : new google.maps.LatLng( '37.782666', '-122.406667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mffef9f1347392eb4ed4a510dbb043a87' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mffef9f1347392eb4ed4a510dbb043a87.positions ) {
gmap\_mffef9f1347392eb4ed4a510dbb043a87.bounds.extend( gmap\_mffef9f1347392eb4ed4a510dbb043a87.positions[m] );
}
// Render markers
for ( var m in gmap\_mffef9f1347392eb4ed4a510dbb043a87.positions ) {
gmap\_mffef9f1347392eb4ed4a510dbb043a87.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mffef9f1347392eb4ed4a510dbb043a87.map,
position : gmap\_mffef9f1347392eb4ed4a510dbb043a87.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mffef9f1347392eb4ed4a510dbb043a87.map.setCenter( gmap\_mffef9f1347392eb4ed4a510dbb043a87.positions[596] );
});