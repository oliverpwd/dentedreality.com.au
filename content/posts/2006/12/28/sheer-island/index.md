---
title: Sheer Island
date: '2006-12-28T23:14:22+00:00'
format: image
service: flickr
tags:
- island
- phuket
- steep
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348092772_72173ce2e8_o.jpg?resize=607%2C455
---

[![Sheer Island](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348092772_72173ce2e8_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/28/sheer-island/) 
# [Sheer Island](http://dentedreality.com.au/2006/12/28/sheer-island/)





* #[island](http://dentedreality.com.au/tags/island/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[steep](http://dentedreality.com.au/tags/steep/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348092772/) [11:14 pm, December 28, 2006](http://dentedreality.com.au/2006/12/28/sheer-island/ "11:14 pm") 
jQuery(document).ready(function(){
var gmap\_m5616e9eeaca4744d82149a6c4315d88a = {
positions : {
293 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5616e9eeaca4744d82149a6c4315d88a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5616e9eeaca4744d82149a6c4315d88a.positions ) {
gmap\_m5616e9eeaca4744d82149a6c4315d88a.bounds.extend( gmap\_m5616e9eeaca4744d82149a6c4315d88a.positions[m] );
}
// Render markers
for ( var m in gmap\_m5616e9eeaca4744d82149a6c4315d88a.positions ) {
gmap\_m5616e9eeaca4744d82149a6c4315d88a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5616e9eeaca4744d82149a6c4315d88a.map,
position : gmap\_m5616e9eeaca4744d82149a6c4315d88a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5616e9eeaca4744d82149a6c4315d88a.map.setCenter( gmap\_m5616e9eeaca4744d82149a6c4315d88a.positions[293] );
});