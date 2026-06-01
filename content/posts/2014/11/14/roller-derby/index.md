---
title: ''
date: '2014-11-14T19:31:46+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/917207_597056140419887_1937253306_n.jpg?resize=640%2C640
---

[![Roller Derby!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/917207_597056140419887_1937253306_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/14/roller-derby/) 

Roller Derby!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/vZ1lSsimAj/) [7:31 pm, November 14, 2014](http://dentedreality.com.au/2014/11/14/roller-derby/ "7:31 pm") 
jQuery(document).ready(function(){
var gmap\_mdf173d87a028472bc9df565f6967de13 = {
positions : {
434 : new google.maps.LatLng( '39.740619155', '-104.977246694' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdf173d87a028472bc9df565f6967de13' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdf173d87a028472bc9df565f6967de13.positions ) {
gmap\_mdf173d87a028472bc9df565f6967de13.bounds.extend( gmap\_mdf173d87a028472bc9df565f6967de13.positions[m] );
}
// Render markers
for ( var m in gmap\_mdf173d87a028472bc9df565f6967de13.positions ) {
gmap\_mdf173d87a028472bc9df565f6967de13.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdf173d87a028472bc9df565f6967de13.map,
position : gmap\_mdf173d87a028472bc9df565f6967de13.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdf173d87a028472bc9df565f6967de13.map.setCenter( gmap\_mdf173d87a028472bc9df565f6967de13.positions[434] );
});