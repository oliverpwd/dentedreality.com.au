---
title: Jackolanterns!
date: '2010-10-24T13:55:38-06:00'
format: image
service: flickr
tags:
- halloween
- jackolantern
- pumpkin
- wordpress
latitude: '37.795666'
longitude: '-122.425334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/10/14185838/5183168681_6ecae89e8f_o.jpg
---

[![Jackolanterns!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/10/14185838/5183168681_6ecae89e8f_o.jpg)](https://dentedreality.com.au/2010/10/24/jackolanterns-3/) 
# [Jackolanterns!](https://dentedreality.com.au/2010/10/24/jackolanterns-3/)

[![Jackolanterns!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/10/14185838/5183168681_6ecae89e8f_o.jpg)](http://www.flickr.com/photos/borkazoid/5183168681/)

37.795666-122.425334




* #[halloween](https://dentedreality.com.au/tags/halloween/)
* #[jackolantern](https://dentedreality.com.au/tags/jackolantern/)
* #[pumpkin](https://dentedreality.com.au/tags/pumpkin/)
* #[wordpress](https://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183168681/) [1:55 pm, October 24, 2010](https://dentedreality.com.au/2010/10/24/jackolanterns-3/ "1:55 pm") 
jQuery(document).ready(function(){
var gmap\_m025e617703e14829ac898f68d0b2f395 = {
positions : {
433 : new google.maps.LatLng( '37.795666', '-122.425334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m025e617703e14829ac898f68d0b2f395' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m025e617703e14829ac898f68d0b2f395.positions ) {
gmap\_m025e617703e14829ac898f68d0b2f395.bounds.extend( gmap\_m025e617703e14829ac898f68d0b2f395.positions[m] );
}
// Render markers
for ( var m in gmap\_m025e617703e14829ac898f68d0b2f395.positions ) {
gmap\_m025e617703e14829ac898f68d0b2f395.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m025e617703e14829ac898f68d0b2f395.map,
position : gmap\_m025e617703e14829ac898f68d0b2f395.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m025e617703e14829ac898f68d0b2f395.map.setCenter( gmap\_m025e617703e14829ac898f68d0b2f395.positions[433] );
});