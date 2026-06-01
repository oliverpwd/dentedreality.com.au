---
title: Matt’s Interview
date: '2011-03-11T11:28:32+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802095563_fa5c84b9a8_o.jpg?resize=607%2C452
---

[![Matt's Interview](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802095563_fa5c84b9a8_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/11/matts-interview/) 
# [Matt’s Interview](http://dentedreality.com.au/2011/03/11/matts-interview/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802095563/) [11:28 am, March 11, 2011](http://dentedreality.com.au/2011/03/11/matts-interview/ "11:28 am") 
jQuery(document).ready(function(){
var gmap\_m32b603c7a67482682869268f8a3496f4 = {
positions : {
556 : new google.maps.LatLng( '30.2625', '-97.7395' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m32b603c7a67482682869268f8a3496f4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m32b603c7a67482682869268f8a3496f4.positions ) {
gmap\_m32b603c7a67482682869268f8a3496f4.bounds.extend( gmap\_m32b603c7a67482682869268f8a3496f4.positions[m] );
}
// Render markers
for ( var m in gmap\_m32b603c7a67482682869268f8a3496f4.positions ) {
gmap\_m32b603c7a67482682869268f8a3496f4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m32b603c7a67482682869268f8a3496f4.map,
position : gmap\_m32b603c7a67482682869268f8a3496f4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m32b603c7a67482682869268f8a3496f4.map.setCenter( gmap\_m32b603c7a67482682869268f8a3496f4.positions[556] );
});