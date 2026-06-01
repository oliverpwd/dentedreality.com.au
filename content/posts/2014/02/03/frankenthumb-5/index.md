---
title: Frankenthumb
date: '2014-02-03T05:51:43+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13924812805_cfe0249790_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13924812805_cfe0249790_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/03/frankenthumb-5/) 
# [Frankenthumb](http://dentedreality.com.au/2014/02/03/frankenthumb-5/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924812805/) [5:51 am, February 3, 2014](http://dentedreality.com.au/2014/02/03/frankenthumb-5/ "5:51 am") 
jQuery(document).ready(function(){
var gmap\_m3b5e9f2f712f1f133702b6438f7cf302 = {
positions : {
656 : new google.maps.LatLng( '40.669363', '-73.985031' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3b5e9f2f712f1f133702b6438f7cf302' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3b5e9f2f712f1f133702b6438f7cf302.positions ) {
gmap\_m3b5e9f2f712f1f133702b6438f7cf302.bounds.extend( gmap\_m3b5e9f2f712f1f133702b6438f7cf302.positions[m] );
}
// Render markers
for ( var m in gmap\_m3b5e9f2f712f1f133702b6438f7cf302.positions ) {
gmap\_m3b5e9f2f712f1f133702b6438f7cf302.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3b5e9f2f712f1f133702b6438f7cf302.map,
position : gmap\_m3b5e9f2f712f1f133702b6438f7cf302.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3b5e9f2f712f1f133702b6438f7cf302.map.setCenter( gmap\_m3b5e9f2f712f1f133702b6438f7cf302.positions[656] );
});