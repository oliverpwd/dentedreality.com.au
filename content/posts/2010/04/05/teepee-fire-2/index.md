---
title: Teepee Fire
date: '2010-04-05T06:55:38-06:00'
format: image
service: flickr
tags:
- fire
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185625/4515797391_26aca37fa0_o-1024x768.jpg?resize=607%2C455&ssl=1
---

[![Teepee Fire](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185625/4515797391_26aca37fa0_o-1024x768.jpg?resize=607%2C455&ssl=1)](https://dentedreality.com.au/2010/04/05/teepee-fire-2/) 
# [Teepee Fire](https://dentedreality.com.au/2010/04/05/teepee-fire-2/)

[![Teepee Fire](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/04/14185625/4515797391_26aca37fa0_o-1024x768.jpg?resize=607%2C455&ssl=1)](http://www.flickr.com/photos/borkazoid/4515797391/)

Matt demonstrates starting a fire using the Bow Drill to get a tinder bundle started.

37.177141-122.116744




* #[fire](https://dentedreality.com.au/tags/fire/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515797391/) [6:55 am, April 5, 2010](https://dentedreality.com.au/2010/04/05/teepee-fire-2/ "6:55 am") 
jQuery(document).ready(function(){
var gmap\_m2540c936e043f27dbe11b63ef9fbae7a = {
positions : {
183 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2540c936e043f27dbe11b63ef9fbae7a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2540c936e043f27dbe11b63ef9fbae7a.positions ) {
gmap\_m2540c936e043f27dbe11b63ef9fbae7a.bounds.extend( gmap\_m2540c936e043f27dbe11b63ef9fbae7a.positions[m] );
}
// Render markers
for ( var m in gmap\_m2540c936e043f27dbe11b63ef9fbae7a.positions ) {
gmap\_m2540c936e043f27dbe11b63ef9fbae7a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2540c936e043f27dbe11b63ef9fbae7a.map,
position : gmap\_m2540c936e043f27dbe11b63ef9fbae7a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2540c936e043f27dbe11b63ef9fbae7a.map.setCenter( gmap\_m2540c936e043f27dbe11b63ef9fbae7a.positions[183] );
});