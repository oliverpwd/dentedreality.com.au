---
title: Ramsay Wedding
date: '2011-01-15T09:58:10+00:00'
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
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434727208_9cb87c4c2f_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434727208_9cb87c4c2f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/15/ramsay-wedding-55/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/15/ramsay-wedding-55/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434727208/) [9:58 am, January 15, 2011](http://dentedreality.com.au/2011/01/15/ramsay-wedding-55/ "9:58 am") 
jQuery(document).ready(function(){
var gmap\_md56871b8e8aa8ad906710432d7ce0d75 = {
positions : {
754 : new google.maps.LatLng( '-33.614167', '115.111333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md56871b8e8aa8ad906710432d7ce0d75' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md56871b8e8aa8ad906710432d7ce0d75.positions ) {
gmap\_md56871b8e8aa8ad906710432d7ce0d75.bounds.extend( gmap\_md56871b8e8aa8ad906710432d7ce0d75.positions[m] );
}
// Render markers
for ( var m in gmap\_md56871b8e8aa8ad906710432d7ce0d75.positions ) {
gmap\_md56871b8e8aa8ad906710432d7ce0d75.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md56871b8e8aa8ad906710432d7ce0d75.map,
position : gmap\_md56871b8e8aa8ad906710432d7ce0d75.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md56871b8e8aa8ad906710432d7ce0d75.map.setCenter( gmap\_md56871b8e8aa8ad906710432d7ce0d75.positions[754] );
});