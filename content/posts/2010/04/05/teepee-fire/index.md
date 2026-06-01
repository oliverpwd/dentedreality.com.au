---
title: Teepee Fire
date: '2010-04-05T06:55:21-06:00'
format: image
service: flickr
tags:
- fire
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185626/4516433986_72c4c4fe96_o-1024x768.jpg?resize=607%2C455&ssl=1
---

[![Teepee Fire](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185626/4516433986_72c4c4fe96_o-1024x768.jpg?resize=607%2C455&ssl=1)](https://dentedreality.com.au/2010/04/05/teepee-fire/) 
# [Teepee Fire](https://dentedreality.com.au/2010/04/05/teepee-fire/)

[![Teepee Fire](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185626/4516433986_72c4c4fe96_o-1024x768.jpg?resize=607%2C455&ssl=1)](http://www.flickr.com/photos/borkazoid/4516433986/)

Matt demonstrates starting a fire using the Bow Drill to get a tinder bundle started.

37.177141-122.116744




* #[fire](https://dentedreality.com.au/tags/fire/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516433986/) [6:55 am, April 5, 2010](https://dentedreality.com.au/2010/04/05/teepee-fire/ "6:55 am") 
jQuery(document).ready(function(){
var gmap\_m3b5cc5b7d4ec01af69be040971c2c865 = {
positions : {
564 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3b5cc5b7d4ec01af69be040971c2c865' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3b5cc5b7d4ec01af69be040971c2c865.positions ) {
gmap\_m3b5cc5b7d4ec01af69be040971c2c865.bounds.extend( gmap\_m3b5cc5b7d4ec01af69be040971c2c865.positions[m] );
}
// Render markers
for ( var m in gmap\_m3b5cc5b7d4ec01af69be040971c2c865.positions ) {
gmap\_m3b5cc5b7d4ec01af69be040971c2c865.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3b5cc5b7d4ec01af69be040971c2c865.map,
position : gmap\_m3b5cc5b7d4ec01af69be040971c2c865.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3b5cc5b7d4ec01af69be040971c2c865.map.setCenter( gmap\_m3b5cc5b7d4ec01af69be040971c2c865.positions[564] );
});