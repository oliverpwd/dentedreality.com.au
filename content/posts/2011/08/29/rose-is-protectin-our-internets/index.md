---
title: Rose is protectin’ our internets
date: '2011-08-29T14:11:13+00:00'
format: image
service: flickr
tags:
- rose
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322995639_87d5aabab7_o.jpg?resize=607%2C813
---

[![Rose is protectin' our internets](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322995639_87d5aabab7_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/08/29/rose-is-protectin-our-internets/) 
# [Rose is protectin’ our internets](http://dentedreality.com.au/2011/08/29/rose-is-protectin-our-internets/)





* #[rose](http://dentedreality.com.au/tags/rose/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322995639/) [2:11 pm, August 29, 2011](http://dentedreality.com.au/2011/08/29/rose-is-protectin-our-internets/ "2:11 pm") 
jQuery(document).ready(function(){
var gmap\_m57ba868811915c310b2860ac6966c09e = {
positions : {
554 : new google.maps.LatLng( '37.782666', '-122.388167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m57ba868811915c310b2860ac6966c09e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m57ba868811915c310b2860ac6966c09e.positions ) {
gmap\_m57ba868811915c310b2860ac6966c09e.bounds.extend( gmap\_m57ba868811915c310b2860ac6966c09e.positions[m] );
}
// Render markers
for ( var m in gmap\_m57ba868811915c310b2860ac6966c09e.positions ) {
gmap\_m57ba868811915c310b2860ac6966c09e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m57ba868811915c310b2860ac6966c09e.map,
position : gmap\_m57ba868811915c310b2860ac6966c09e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m57ba868811915c310b2860ac6966c09e.map.setCenter( gmap\_m57ba868811915c310b2860ac6966c09e.positions[554] );
});