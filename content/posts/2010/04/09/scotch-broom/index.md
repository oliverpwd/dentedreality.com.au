---
title: Scotch Broom
date: '2010-04-09T10:51:25+00:00'
format: image
service: flickr
tags:
- scotchbroom
- tombrown
- trackerschool
- tracking
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516466448_dd3125646a_o.jpg?resize=607%2C455
---

[![Scotch Broom](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516466448_dd3125646a_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/scotch-broom/) 
# [Scotch Broom](http://dentedreality.com.au/2010/04/09/scotch-broom/)

As seen during our edible/medicinal plant walk.





* #[scotchbroom](http://dentedreality.com.au/tags/scotchbroom/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516466448/) [10:51 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/scotch-broom/ "10:51 am") 
jQuery(document).ready(function(){
var gmap\_me923bffaba61fb0f28b2a78aa26dac2a = {
positions : {
462 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me923bffaba61fb0f28b2a78aa26dac2a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me923bffaba61fb0f28b2a78aa26dac2a.positions ) {
gmap\_me923bffaba61fb0f28b2a78aa26dac2a.bounds.extend( gmap\_me923bffaba61fb0f28b2a78aa26dac2a.positions[m] );
}
// Render markers
for ( var m in gmap\_me923bffaba61fb0f28b2a78aa26dac2a.positions ) {
gmap\_me923bffaba61fb0f28b2a78aa26dac2a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me923bffaba61fb0f28b2a78aa26dac2a.map,
position : gmap\_me923bffaba61fb0f28b2a78aa26dac2a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me923bffaba61fb0f28b2a78aa26dac2a.map.setCenter( gmap\_me923bffaba61fb0f28b2a78aa26dac2a.positions[462] );
});