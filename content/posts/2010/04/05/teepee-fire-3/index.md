---
title: Teepee Fire
date: '2010-04-05T06:47:49-06:00'
format: image
service: flickr
tags:
- fire
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185625/4515796483_c4e8420f8b_o-1024x768.jpg?resize=607%2C455&ssl=1
---

[![Teepee Fire](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185625/4515796483_c4e8420f8b_o-1024x768.jpg?resize=607%2C455&ssl=1)](https://dentedreality.com.au/2010/04/05/teepee-fire-3/) 
# [Teepee Fire](https://dentedreality.com.au/2010/04/05/teepee-fire-3/)

[![Teepee Fire](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185625/4515796483_c4e8420f8b_o-1024x768.jpg?resize=607%2C455&ssl=1)](http://www.flickr.com/photos/borkazoid/4515796483/)

Matt demonstrates starting a fire using the Bow Drill to get a tinder bundle started.

37.177141-122.116744




* #[fire](https://dentedreality.com.au/tags/fire/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515796483/) [6:47 am, April 5, 2010](https://dentedreality.com.au/2010/04/05/teepee-fire-3/ "6:47 am") 
jQuery(document).ready(function(){
var gmap\_m28613c61548cba5d7b8455678bf26dc1 = {
positions : {
165 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m28613c61548cba5d7b8455678bf26dc1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m28613c61548cba5d7b8455678bf26dc1.positions ) {
gmap\_m28613c61548cba5d7b8455678bf26dc1.bounds.extend( gmap\_m28613c61548cba5d7b8455678bf26dc1.positions[m] );
}
// Render markers
for ( var m in gmap\_m28613c61548cba5d7b8455678bf26dc1.positions ) {
gmap\_m28613c61548cba5d7b8455678bf26dc1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m28613c61548cba5d7b8455678bf26dc1.map,
position : gmap\_m28613c61548cba5d7b8455678bf26dc1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m28613c61548cba5d7b8455678bf26dc1.map.setCenter( gmap\_m28613c61548cba5d7b8455678bf26dc1.positions[165] );
});