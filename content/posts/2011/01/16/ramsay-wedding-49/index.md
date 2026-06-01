---
title: Ramsay Wedding
date: '2011-01-16T21:16:55+00:00'
format: image
service: flickr
tags:
- dunsborough
- kangaroos
- ramsaywedding
- sheree
- todd
- wedding
- westernaustralia
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434728728_b7a184eb64_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434728728_b7a184eb64_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/16/ramsay-wedding-49/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/16/ramsay-wedding-49/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[kangaroos](http://dentedreality.com.au/tags/kangaroos/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434728728/) [9:16 pm, January 16, 2011](http://dentedreality.com.au/2011/01/16/ramsay-wedding-49/ "9:16 pm") 
jQuery(document).ready(function(){
var gmap\_m89bbc4b7c4d53819b09d8e4f53d63328 = {
positions : {
532 : new google.maps.LatLng( '-33.694167', '115.081833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m89bbc4b7c4d53819b09d8e4f53d63328' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.positions ) {
gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.bounds.extend( gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.positions[m] );
}
// Render markers
for ( var m in gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.positions ) {
gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.map,
position : gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.map.setCenter( gmap\_m89bbc4b7c4d53819b09d8e4f53d63328.positions[532] );
});