---
title: Ramsay Wedding
date: '2011-01-15T07:21:48+00:00'
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
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434726992_71c98a9d1d_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434726992_71c98a9d1d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/15/ramsay-wedding-56/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/15/ramsay-wedding-56/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434726992/) [7:21 am, January 15, 2011](http://dentedreality.com.au/2011/01/15/ramsay-wedding-56/ "7:21 am") 
jQuery(document).ready(function(){
var gmap\_m0f851f0f2291af5caaa3521a0854e641 = {
positions : {
517 : new google.maps.LatLng( '-33.573334', '115.087499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0f851f0f2291af5caaa3521a0854e641' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0f851f0f2291af5caaa3521a0854e641.positions ) {
gmap\_m0f851f0f2291af5caaa3521a0854e641.bounds.extend( gmap\_m0f851f0f2291af5caaa3521a0854e641.positions[m] );
}
// Render markers
for ( var m in gmap\_m0f851f0f2291af5caaa3521a0854e641.positions ) {
gmap\_m0f851f0f2291af5caaa3521a0854e641.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0f851f0f2291af5caaa3521a0854e641.map,
position : gmap\_m0f851f0f2291af5caaa3521a0854e641.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0f851f0f2291af5caaa3521a0854e641.map.setCenter( gmap\_m0f851f0f2291af5caaa3521a0854e641.positions[517] );
});