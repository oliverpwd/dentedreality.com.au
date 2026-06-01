---
title: Epic Australian Adventure, 2014
date: '2014-03-25T07:34:20+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904745876_21c7d61c79_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904745876_21c7d61c79_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-37/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-37/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904745876/) [7:34 am, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-37/ "7:34 am") 
jQuery(document).ready(function(){
var gmap\_m9ba9084d5bd890ebfda777570bf3298e = {
positions : {
977 : new google.maps.LatLng( '-37.81542', '144.94165' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9ba9084d5bd890ebfda777570bf3298e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9ba9084d5bd890ebfda777570bf3298e.positions ) {
gmap\_m9ba9084d5bd890ebfda777570bf3298e.bounds.extend( gmap\_m9ba9084d5bd890ebfda777570bf3298e.positions[m] );
}
// Render markers
for ( var m in gmap\_m9ba9084d5bd890ebfda777570bf3298e.positions ) {
gmap\_m9ba9084d5bd890ebfda777570bf3298e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9ba9084d5bd890ebfda777570bf3298e.map,
position : gmap\_m9ba9084d5bd890ebfda777570bf3298e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9ba9084d5bd890ebfda777570bf3298e.map.setCenter( gmap\_m9ba9084d5bd890ebfda777570bf3298e.positions[977] );
});