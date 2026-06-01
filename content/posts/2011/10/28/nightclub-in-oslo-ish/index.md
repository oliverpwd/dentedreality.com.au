---
title: Nightclub in Oslo – “ish”
date: '2011-10-28T21:30:04+00:00'
format: image
service: flickr
tags:
- club
- ish
- norway
- Oslo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812168456_e74fcbdc0b_o.jpg?resize=607%2C452
---

[![Nightclub in Oslo - "ish"](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812168456_e74fcbdc0b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/28/nightclub-in-oslo-ish/) 
# [Nightclub in Oslo – “ish”](http://dentedreality.com.au/2011/10/28/nightclub-in-oslo-ish/)





* #[club](http://dentedreality.com.au/tags/club/)
* #[ish](http://dentedreality.com.au/tags/ish/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812168456/) [9:30 pm, October 28, 2011](http://dentedreality.com.au/2011/10/28/nightclub-in-oslo-ish/ "9:30 pm") 
jQuery(document).ready(function(){
var gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee = {
positions : {
497 : new google.maps.LatLng( '59.914833', '10.734333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.positions ) {
gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.bounds.extend( gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.positions[m] );
}
// Render markers
for ( var m in gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.positions ) {
gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.map,
position : gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.map.setCenter( gmap\_m4424611b4a2e1b825aba1b7a38a7e6ee.positions[497] );
});