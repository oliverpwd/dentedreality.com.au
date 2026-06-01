---
title: The Owens’
date: '2011-05-29T13:52:26+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803432678_c755da8dc9_o.jpg?resize=607%2C452
---

[![The Owens'](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803432678_c755da8dc9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/29/the-owens-3/) 
# [The Owens’](http://dentedreality.com.au/2011/05/29/the-owens-3/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803432678/) [1:52 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/the-owens-3/ "1:52 pm") 
jQuery(document).ready(function(){
var gmap\_m7b8fe64577f5cab1c8f52f0f763707ba = {
positions : {
104 : new google.maps.LatLng( '37.776333', '-122.393834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7b8fe64577f5cab1c8f52f0f763707ba' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.positions ) {
gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.bounds.extend( gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.positions[m] );
}
// Render markers
for ( var m in gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.positions ) {
gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.map,
position : gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.map.setCenter( gmap\_m7b8fe64577f5cab1c8f52f0f763707ba.positions[104] );
});