---
title: Bright Coast
date: '2008-04-04T21:49:57+00:00'
format: image
service: flickr
tags:
- australia
- beach
- coast
- ocean
- renniewedding
- sunlight
- timswedding
- westernaustraliadenmark
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432613631_7832bdeda0_o.jpg?resize=607%2C455
---

[![Bright Coast](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432613631_7832bdeda0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/04/bright-coast/) 
# [Bright Coast](http://dentedreality.com.au/2008/04/04/bright-coast/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[coast](http://dentedreality.com.au/tags/coast/)
* #[ocean](http://dentedreality.com.au/tags/ocean/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[sunlight](http://dentedreality.com.au/tags/sunlight/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2432613631/) [9:49 pm, April 4, 2008](http://dentedreality.com.au/2008/04/04/bright-coast/ "9:49 pm") 
jQuery(document).ready(function(){
var gmap\_mdc785dd7b63ca285360f30b2242816e5 = {
positions : {
965 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdc785dd7b63ca285360f30b2242816e5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdc785dd7b63ca285360f30b2242816e5.positions ) {
gmap\_mdc785dd7b63ca285360f30b2242816e5.bounds.extend( gmap\_mdc785dd7b63ca285360f30b2242816e5.positions[m] );
}
// Render markers
for ( var m in gmap\_mdc785dd7b63ca285360f30b2242816e5.positions ) {
gmap\_mdc785dd7b63ca285360f30b2242816e5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdc785dd7b63ca285360f30b2242816e5.map,
position : gmap\_mdc785dd7b63ca285360f30b2242816e5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdc785dd7b63ca285360f30b2242816e5.map.setCenter( gmap\_mdc785dd7b63ca285360f30b2242816e5.positions[965] );
});