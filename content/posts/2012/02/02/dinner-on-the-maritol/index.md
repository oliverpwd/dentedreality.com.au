---
title: Dinner on the Maritol
date: '2012-02-02T17:57:54+00:00'
format: image
service: flickr
tags:
- boat
- houseboat
- maritol
- ship
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959570547_b805941cc1_o.jpg?resize=607%2C452
---

[![Dinner on the Maritol](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959570547_b805941cc1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol/) 
# [Dinner on the Maritol](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol/)

@chexee was moving off the Maritol, so we went around for a going away dinner.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[houseboat](http://dentedreality.com.au/tags/houseboat/)
* #[maritol](http://dentedreality.com.au/tags/maritol/)
* #[ship](http://dentedreality.com.au/tags/ship/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959570547/) [5:57 pm, February 2, 2012](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol/ "5:57 pm") 
jQuery(document).ready(function(){
var gmap\_m060b5db1b2d7f0a25def3008eefc8de9 = {
positions : {
660 : new google.maps.LatLng( '37.7725', '-122.386001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m060b5db1b2d7f0a25def3008eefc8de9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m060b5db1b2d7f0a25def3008eefc8de9.positions ) {
gmap\_m060b5db1b2d7f0a25def3008eefc8de9.bounds.extend( gmap\_m060b5db1b2d7f0a25def3008eefc8de9.positions[m] );
}
// Render markers
for ( var m in gmap\_m060b5db1b2d7f0a25def3008eefc8de9.positions ) {
gmap\_m060b5db1b2d7f0a25def3008eefc8de9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m060b5db1b2d7f0a25def3008eefc8de9.map,
position : gmap\_m060b5db1b2d7f0a25def3008eefc8de9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m060b5db1b2d7f0a25def3008eefc8de9.map.setCenter( gmap\_m060b5db1b2d7f0a25def3008eefc8de9.positions[660] );
});