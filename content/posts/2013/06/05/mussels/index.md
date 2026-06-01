---
title: Mussels
date: '2013-06-05T15:18:42+00:00'
format: image
service: flickr
tags:
- mussels
- seafood
- yum
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9436934801_5fe38b50b8_o.jpg?resize=607%2C452
---

[![Mussels](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9436934801_5fe38b50b8_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/06/05/mussels/) 
# [Mussels](http://dentedreality.com.au/2013/06/05/mussels/)





* #[mussels](http://dentedreality.com.au/tags/mussels/)
* #[seafood](http://dentedreality.com.au/tags/seafood/)
* #[yum](http://dentedreality.com.au/tags/yum/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436934801/) [3:18 pm, June 5, 2013](http://dentedreality.com.au/2013/06/05/mussels/ "3:18 pm") 
jQuery(document).ready(function(){
var gmap\_m62ce578f14081cdf4b75785f665c0ee9 = {
positions : {
128 : new google.maps.LatLng( '40.669333', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m62ce578f14081cdf4b75785f665c0ee9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m62ce578f14081cdf4b75785f665c0ee9.positions ) {
gmap\_m62ce578f14081cdf4b75785f665c0ee9.bounds.extend( gmap\_m62ce578f14081cdf4b75785f665c0ee9.positions[m] );
}
// Render markers
for ( var m in gmap\_m62ce578f14081cdf4b75785f665c0ee9.positions ) {
gmap\_m62ce578f14081cdf4b75785f665c0ee9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m62ce578f14081cdf4b75785f665c0ee9.map,
position : gmap\_m62ce578f14081cdf4b75785f665c0ee9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m62ce578f14081cdf4b75785f665c0ee9.map.setCenter( gmap\_m62ce578f14081cdf4b75785f665c0ee9.positions[128] );
});