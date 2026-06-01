---
title: WordPress Pancakes!
date: '2013-06-09T06:44:45+00:00'
format: image
tags:
- jmdodd
- pancakes
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437042989_a3ca711791_o.jpg?resize=607%2C813
---

[![WordPress Pancakes!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437042989_a3ca711791_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/06/09/wordpress-pancakes/) 
# [WordPress Pancakes!](http://dentedreality.com.au/2013/06/09/wordpress-pancakes/)

Care of the talented Jennifer.





* #[jmdodd](http://dentedreality.com.au/tags/jmdodd/)
* #[pancakes](http://dentedreality.com.au/tags/pancakes/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437042989/) [6:44 am, June 9, 2013](http://dentedreality.com.au/2013/06/09/wordpress-pancakes/ "6:44 am") 
jQuery(document).ready(function(){
var gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42 = {
positions : {
680 : new google.maps.LatLng( '45.5165', '-122.6185' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.positions ) {
gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.bounds.extend( gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.positions[m] );
}
// Render markers
for ( var m in gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.positions ) {
gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.map,
position : gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.map.setCenter( gmap\_mbaaedd9fffd6b950549da5c1aa6c5d42.positions[680] );
});