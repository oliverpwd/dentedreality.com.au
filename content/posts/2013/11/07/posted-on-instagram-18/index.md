---
title: ''
date: '2013-11-07T21:08:49+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/1171669_646176945403584_1911190040_n.jpg?resize=640%2C640
---

[![Posted on Instagram](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/1171669_646176945403584_1911190040_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/11/07/posted-on-instagram-18/) 




* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/gb0YLMCmDg/) [9:08 pm, November 7, 2013](http://dentedreality.com.au/2013/11/07/posted-on-instagram-18/ "9:08 pm") 
jQuery(document).ready(function(){
var gmap\_ma06e1ecafc4a67c08d79fee119d4a98f = {
positions : {
268 : new google.maps.LatLng( '40.765952379', '-73.986971513' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma06e1ecafc4a67c08d79fee119d4a98f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.positions ) {
gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.bounds.extend( gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.positions[m] );
}
// Render markers
for ( var m in gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.positions ) {
gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.map,
position : gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.map.setCenter( gmap\_ma06e1ecafc4a67c08d79fee119d4a98f.positions[268] );
});