---
title: Ramsay Wedding
date: '2011-01-16T14:23:42+00:00'
format: image
service: flickr
tags:
- dunsborough
- ramsaywedding
- sheree
- todd
- wedding
- westernaustralia
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434114857_290e84ac8d_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434114857_290e84ac8d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/16/ramsay-wedding-51/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/16/ramsay-wedding-51/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434114857/) [2:23 pm, January 16, 2011](http://dentedreality.com.au/2011/01/16/ramsay-wedding-51/ "2:23 pm") 
jQuery(document).ready(function(){
var gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da = {
positions : {
646 : new google.maps.LatLng( '-33.645334', '115.031333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.positions ) {
gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.bounds.extend( gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.positions[m] );
}
// Render markers
for ( var m in gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.positions ) {
gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.map,
position : gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.map.setCenter( gmap\_m7cbe7fc783bd53a9b0cc89ea507ba1da.positions[646] );
});