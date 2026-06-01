---
title: Monkeys Ahoy!
date: '2006-12-28T21:34:35+00:00'
format: image
service: flickr
tags:
- island
- monkeys
- phuket
- thailand
- thailand06
- tourists
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348093900_80da03dab5_o.jpg?resize=607%2C455
---

[![Monkeys Ahoy!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348093900_80da03dab5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/28/monkeys-ahoy/) 
# [Monkeys Ahoy!](http://dentedreality.com.au/2006/12/28/monkeys-ahoy/)





* #[island](http://dentedreality.com.au/tags/island/)
* #[monkeys](http://dentedreality.com.au/tags/monkeys/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)
* #[tourists](http://dentedreality.com.au/tags/tourists/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348093900/) [9:34 pm, December 28, 2006](http://dentedreality.com.au/2006/12/28/monkeys-ahoy/ "9:34 pm") 
jQuery(document).ready(function(){
var gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0 = {
positions : {
891 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.positions ) {
gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.bounds.extend( gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.positions[m] );
}
// Render markers
for ( var m in gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.positions ) {
gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.map,
position : gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.map.setCenter( gmap\_m9d459aa8531eae3ef80c4fc81eeaa2f0.positions[891] );
});