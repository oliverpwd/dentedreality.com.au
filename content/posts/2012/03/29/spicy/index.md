---
title: Spicy
date: '2012-03-29T08:53:18+00:00'
format: image
service: flickr
tags:
- shelves
- spices
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770426564_a646a924e0_o.jpg?resize=607%2C813
---

[![Spicy](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770426564_a646a924e0_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/03/29/spicy/) 
# [Spicy](http://dentedreality.com.au/2012/03/29/spicy/)





* #[shelves](http://dentedreality.com.au/tags/shelves/)
* #[spices](http://dentedreality.com.au/tags/spices/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770426564/) [8:53 am, March 29, 2012](http://dentedreality.com.au/2012/03/29/spicy/ "8:53 am") 
jQuery(document).ready(function(){
var gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6 = {
positions : {
730 : new google.maps.LatLng( '38.301666', '-122.2815' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.positions ) {
gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.bounds.extend( gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.positions[m] );
}
// Render markers
for ( var m in gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.positions ) {
gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.map,
position : gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.map.setCenter( gmap\_mc58ece79a9de0ffd0eeefd9e40c911a6.positions[730] );
});