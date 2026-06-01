---
title: ''
date: '2014-04-27T03:14:27+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/e7a4e06acde311e39e620002c9ceffec_8.jpg?resize=640%2C640
---

[![Full Irish](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/e7a4e06acde311e39e620002c9ceffec_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/27/full-irish/) 

Full Irish





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/nSUOZdimJO/) [3:14 am, April 27, 2014](http://dentedreality.com.au/2014/04/27/full-irish/ "3:14 am") 
jQuery(document).ready(function(){
var gmap\_m7a8663fb96e3cafd05386810ff9439b5 = {
positions : {
574 : new google.maps.LatLng( '53.344027568', '-6.268191376' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7a8663fb96e3cafd05386810ff9439b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7a8663fb96e3cafd05386810ff9439b5.positions ) {
gmap\_m7a8663fb96e3cafd05386810ff9439b5.bounds.extend( gmap\_m7a8663fb96e3cafd05386810ff9439b5.positions[m] );
}
// Render markers
for ( var m in gmap\_m7a8663fb96e3cafd05386810ff9439b5.positions ) {
gmap\_m7a8663fb96e3cafd05386810ff9439b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7a8663fb96e3cafd05386810ff9439b5.map,
position : gmap\_m7a8663fb96e3cafd05386810ff9439b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7a8663fb96e3cafd05386810ff9439b5.map.setCenter( gmap\_m7a8663fb96e3cafd05386810ff9439b5.positions[574] );
});