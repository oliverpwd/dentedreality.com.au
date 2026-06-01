---
title: Ramsay Wedding
date: '2011-01-15T06:44:19+00:00'
format: image
service: flickr
tags:
- beach
- dunsborough
- ramsaywedding
- sheree
- todd
- wedding
- westernaustralia
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434726774_f030d79566_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434726774_f030d79566_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/15/ramsay-wedding-57/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/15/ramsay-wedding-57/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434726774/) [6:44 am, January 15, 2011](http://dentedreality.com.au/2011/01/15/ramsay-wedding-57/ "6:44 am") 
jQuery(document).ready(function(){
var gmap\_m4125cfc251f2dc7db0b587488dd73fe8 = {
positions : {
490 : new google.maps.LatLng( '-33.573834', '115.087166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4125cfc251f2dc7db0b587488dd73fe8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4125cfc251f2dc7db0b587488dd73fe8.positions ) {
gmap\_m4125cfc251f2dc7db0b587488dd73fe8.bounds.extend( gmap\_m4125cfc251f2dc7db0b587488dd73fe8.positions[m] );
}
// Render markers
for ( var m in gmap\_m4125cfc251f2dc7db0b587488dd73fe8.positions ) {
gmap\_m4125cfc251f2dc7db0b587488dd73fe8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4125cfc251f2dc7db0b587488dd73fe8.map,
position : gmap\_m4125cfc251f2dc7db0b587488dd73fe8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4125cfc251f2dc7db0b587488dd73fe8.map.setCenter( gmap\_m4125cfc251f2dc7db0b587488dd73fe8.positions[490] );
});