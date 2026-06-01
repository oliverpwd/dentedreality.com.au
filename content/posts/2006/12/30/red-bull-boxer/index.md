---
title: Red Bull Boxer
date: '2006-12-30T05:43:30+00:00'
format: image
service: flickr
tags:
- boxing
- fight
- muaythai
- phuket
- redbull
- thaiboxing
- thailand
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349556432_528db0baa4_o.jpg?resize=607%2C809
---

[![Red Bull Boxer](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349556432_528db0baa4_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/30/red-bull-boxer/) 
# [Red Bull Boxer](http://dentedreality.com.au/2006/12/30/red-bull-boxer/)

For Kai





* #[boxing](http://dentedreality.com.au/tags/boxing/)
* #[fight](http://dentedreality.com.au/tags/fight/)
* #[muaythai](http://dentedreality.com.au/tags/muaythai/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[redbull](http://dentedreality.com.au/tags/redbull/)
* #[thaiboxing](http://dentedreality.com.au/tags/thaiboxing/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349556432/) [5:43 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/red-bull-boxer/ "5:43 am") 
jQuery(document).ready(function(){
var gmap\_m87984982a350be521e83000962a54c99 = {
positions : {
298 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m87984982a350be521e83000962a54c99' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m87984982a350be521e83000962a54c99.positions ) {
gmap\_m87984982a350be521e83000962a54c99.bounds.extend( gmap\_m87984982a350be521e83000962a54c99.positions[m] );
}
// Render markers
for ( var m in gmap\_m87984982a350be521e83000962a54c99.positions ) {
gmap\_m87984982a350be521e83000962a54c99.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m87984982a350be521e83000962a54c99.map,
position : gmap\_m87984982a350be521e83000962a54c99.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m87984982a350be521e83000962a54c99.map.setCenter( gmap\_m87984982a350be521e83000962a54c99.positions[298] );
});