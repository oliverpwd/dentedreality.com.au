---
title: ''
date: '2014-01-17T21:45:43+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/8b3ef76c7fea11e38fd012680049e3b3_8.jpg?resize=640%2C640
---

[![Lovecraft in Brooklyn. Cthulhu garnish.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/8b3ef76c7fea11e38fd012680049e3b3_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/17/lovecraft-in-brooklyn-cthulhu-garnish-2/) 

Lovecraft in Brooklyn. Cthulhu garnish.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jSz6DLimA8/) [9:45 pm, January 17, 2014](http://dentedreality.com.au/2014/01/17/lovecraft-in-brooklyn-cthulhu-garnish-2/ "9:45 pm") 
jQuery(document).ready(function(){
var gmap\_m3dc87212b43735262a46517734df5d32 = {
positions : {
881 : new google.maps.LatLng( '40.709307554', '-73.955932349' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3dc87212b43735262a46517734df5d32' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3dc87212b43735262a46517734df5d32.positions ) {
gmap\_m3dc87212b43735262a46517734df5d32.bounds.extend( gmap\_m3dc87212b43735262a46517734df5d32.positions[m] );
}
// Render markers
for ( var m in gmap\_m3dc87212b43735262a46517734df5d32.positions ) {
gmap\_m3dc87212b43735262a46517734df5d32.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3dc87212b43735262a46517734df5d32.map,
position : gmap\_m3dc87212b43735262a46517734df5d32.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3dc87212b43735262a46517734df5d32.map.setCenter( gmap\_m3dc87212b43735262a46517734df5d32.positions[881] );
});