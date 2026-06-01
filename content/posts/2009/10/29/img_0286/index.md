---
title: IMG_0286
date: '2009-10-29T17:35:08+00:00'
format: image
service: flickr
tags:
- newyork
- wcnyc
- wordcamp
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/10/4123180315_7eb4ac8e8c_o.jpg?resize=607%2C809
---

[![IMG_0286](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/10/4123180315_7eb4ac8e8c_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2009/10/29/img_0286/) 
# [IMG\_0286](http://dentedreality.com.au/2009/10/29/img_0286/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[wcnyc](http://dentedreality.com.au/tags/wcnyc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4123180315/) [5:35 pm, October 29, 2009](http://dentedreality.com.au/2009/10/29/img_0286/ "5:35 pm") 
jQuery(document).ready(function(){
var gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f = {
positions : {
961 : new google.maps.LatLng( '37.764833', '-122.422834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.positions ) {
gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.bounds.extend( gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.positions[m] );
}
// Render markers
for ( var m in gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.positions ) {
gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.map,
position : gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.map.setCenter( gmap\_m3126ecb6cfe45a9f7db1a30c9f37fb5f.positions[961] );
});