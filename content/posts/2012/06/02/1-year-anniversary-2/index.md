---
title: 1 year Anniversary
date: '2012-06-02T17:20:43+00:00'
format: image
service: flickr
tags:
- anniversary
- champagne
- prosecco
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7770964474_1b4f67580b_o.jpg?resize=607%2C813
---

[![1 year Anniversary](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7770964474_1b4f67580b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/06/02/1-year-anniversary-2/) 
# [1 year Anniversary](http://dentedreality.com.au/2012/06/02/1-year-anniversary-2/)





* #[anniversary](http://dentedreality.com.au/tags/anniversary/)
* #[champagne](http://dentedreality.com.au/tags/champagne/)
* #[prosecco](http://dentedreality.com.au/tags/prosecco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770964474/) [5:20 pm, June 2, 2012](http://dentedreality.com.au/2012/06/02/1-year-anniversary-2/ "5:20 pm") 
jQuery(document).ready(function(){
var gmap\_me3302e53e6be176209f5c739b5ab5f8c = {
positions : {
411 : new google.maps.LatLng( '37.773333', '-122.421334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me3302e53e6be176209f5c739b5ab5f8c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me3302e53e6be176209f5c739b5ab5f8c.positions ) {
gmap\_me3302e53e6be176209f5c739b5ab5f8c.bounds.extend( gmap\_me3302e53e6be176209f5c739b5ab5f8c.positions[m] );
}
// Render markers
for ( var m in gmap\_me3302e53e6be176209f5c739b5ab5f8c.positions ) {
gmap\_me3302e53e6be176209f5c739b5ab5f8c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me3302e53e6be176209f5c739b5ab5f8c.map,
position : gmap\_me3302e53e6be176209f5c739b5ab5f8c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me3302e53e6be176209f5c739b5ab5f8c.map.setCenter( gmap\_me3302e53e6be176209f5c739b5ab5f8c.positions[411] );
});