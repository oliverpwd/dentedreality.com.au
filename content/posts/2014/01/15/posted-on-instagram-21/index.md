---
title: ''
date: '2014-01-15T19:26:47+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/dd2229fc7e4411e3a36f1229e1c1cdc1_8.jpg?resize=640%2C640
---

[![Posted on Instagram](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/dd2229fc7e4411e3a36f1229e1c1cdc1_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/15/posted-on-instagram-21/) 




* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jNaau6CmJo/) [7:26 pm, January 15, 2014](http://dentedreality.com.au/2014/01/15/posted-on-instagram-21/ "7:26 pm") 
jQuery(document).ready(function(){
var gmap\_m413e8fdd55d5cbe90cc800209c09ee30 = {
positions : {
837 : new google.maps.LatLng( '40.709307554', '-73.955932349' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m413e8fdd55d5cbe90cc800209c09ee30' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m413e8fdd55d5cbe90cc800209c09ee30.positions ) {
gmap\_m413e8fdd55d5cbe90cc800209c09ee30.bounds.extend( gmap\_m413e8fdd55d5cbe90cc800209c09ee30.positions[m] );
}
// Render markers
for ( var m in gmap\_m413e8fdd55d5cbe90cc800209c09ee30.positions ) {
gmap\_m413e8fdd55d5cbe90cc800209c09ee30.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m413e8fdd55d5cbe90cc800209c09ee30.map,
position : gmap\_m413e8fdd55d5cbe90cc800209c09ee30.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m413e8fdd55d5cbe90cc800209c09ee30.map.setCenter( gmap\_m413e8fdd55d5cbe90cc800209c09ee30.positions[837] );
});