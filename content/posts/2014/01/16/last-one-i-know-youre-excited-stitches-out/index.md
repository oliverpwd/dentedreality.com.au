---
title: ''
date: '2014-01-16T09:57:51+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/7dee89d87ebe11e3bf250ee929a7ce16_8.jpg?resize=640%2C640
---

[![Last one, I know you're excited. Stitches out!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/7dee89d87ebe11e3bf250ee929a7ce16_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/16/last-one-i-know-youre-excited-stitches-out/) 

Last one, I know you’re excited. Stitches out!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jO-GpSCmM6/) [9:57 am, January 16, 2014](http://dentedreality.com.au/2014/01/16/last-one-i-know-youre-excited-stitches-out/ "9:57 am") 
jQuery(document).ready(function(){
var gmap\_mccb04680e2d0bf141efc4a9a6df8cadd = {
positions : {
649 : new google.maps.LatLng( '40.669436667', '-73.984946667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mccb04680e2d0bf141efc4a9a6df8cadd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.positions ) {
gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.bounds.extend( gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.positions[m] );
}
// Render markers
for ( var m in gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.positions ) {
gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.map,
position : gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.map.setCenter( gmap\_mccb04680e2d0bf141efc4a9a6df8cadd.positions[649] );
});