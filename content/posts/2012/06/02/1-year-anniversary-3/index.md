---
title: 1 year Anniversary
date: '2012-06-02T17:18:44+00:00'
format: image
service: flickr
tags:
- anniversary
- erika
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7770964372_f3240acbf2_o.jpg?resize=607%2C813
---

[![1 year Anniversary](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7770964372_f3240acbf2_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/06/02/1-year-anniversary-3/) 
# [1 year Anniversary](http://dentedreality.com.au/2012/06/02/1-year-anniversary-3/)





* #[anniversary](http://dentedreality.com.au/tags/anniversary/)
* #[erika](http://dentedreality.com.au/tags/erika/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770964372/) [5:18 pm, June 2, 2012](http://dentedreality.com.au/2012/06/02/1-year-anniversary-3/ "5:18 pm") 
jQuery(document).ready(function(){
var gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b = {
positions : {
504 : new google.maps.LatLng( '37.773333', '-122.421501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.positions ) {
gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.bounds.extend( gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.positions[m] );
}
// Render markers
for ( var m in gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.positions ) {
gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.map,
position : gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.map.setCenter( gmap\_m733c2c4bdeb7efc4e2f00e394ceb6c4b.positions[504] );
});