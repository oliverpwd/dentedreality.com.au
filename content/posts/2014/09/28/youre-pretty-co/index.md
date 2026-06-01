---
title: ''
date: '2014-09-28T00:12:51+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/926229_750554924994146_443470260_n.jpg?resize=640%2C640
---

[![You're pretty, CO.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/926229_750554924994146_443470260_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/28/youre-pretty-co/) 

You’re pretty, CO.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/teoukoCmPn/) [12:12 am, September 28, 2014](http://dentedreality.com.au/2014/09/28/youre-pretty-co/ "12:12 am") 
jQuery(document).ready(function(){
var gmap\_m912da56a54780ca541c92f5874e24894 = {
positions : {
231 : new google.maps.LatLng( '40.441003729', '-105.754434474' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m912da56a54780ca541c92f5874e24894' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m912da56a54780ca541c92f5874e24894.positions ) {
gmap\_m912da56a54780ca541c92f5874e24894.bounds.extend( gmap\_m912da56a54780ca541c92f5874e24894.positions[m] );
}
// Render markers
for ( var m in gmap\_m912da56a54780ca541c92f5874e24894.positions ) {
gmap\_m912da56a54780ca541c92f5874e24894.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m912da56a54780ca541c92f5874e24894.map,
position : gmap\_m912da56a54780ca541c92f5874e24894.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m912da56a54780ca541c92f5874e24894.map.setCenter( gmap\_m912da56a54780ca541c92f5874e24894.positions[231] );
});