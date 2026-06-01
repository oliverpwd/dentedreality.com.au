---
title: ''
date: '2014-10-23T21:28:28+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10724672_1485263651756579_2067894540_n.jpg?resize=640%2C640
---

[![DEN is a ghost town on a Thursday night apparently.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10724672_1485263651756579_2067894540_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/23/den-is-a-ghost-town-on-a-thursday-night-apparently/) 

DEN is a ghost town on a Thursday night apparently.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/uhSlTXCmLv/) [9:28 pm, October 23, 2014](http://dentedreality.com.au/2014/10/23/den-is-a-ghost-town-on-a-thursday-night-apparently/ "9:28 pm") 
jQuery(document).ready(function(){
var gmap\_mc040b85cd3cae8318ab2d0dbba27221c = {
positions : {
631 : new google.maps.LatLng( '39.858625236', '-104.672347132' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc040b85cd3cae8318ab2d0dbba27221c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc040b85cd3cae8318ab2d0dbba27221c.positions ) {
gmap\_mc040b85cd3cae8318ab2d0dbba27221c.bounds.extend( gmap\_mc040b85cd3cae8318ab2d0dbba27221c.positions[m] );
}
// Render markers
for ( var m in gmap\_mc040b85cd3cae8318ab2d0dbba27221c.positions ) {
gmap\_mc040b85cd3cae8318ab2d0dbba27221c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc040b85cd3cae8318ab2d0dbba27221c.map,
position : gmap\_mc040b85cd3cae8318ab2d0dbba27221c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc040b85cd3cae8318ab2d0dbba27221c.map.setCenter( gmap\_mc040b85cd3cae8318ab2d0dbba27221c.positions[631] );
});