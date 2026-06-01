---
title: ''
date: '2014-10-27T14:12:09+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10735249_580696792057586_275162656_n.jpg?resize=640%2C640
---

[![It's always sunny in California.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10735249_580696792057586_275162656_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/27/its-always-sunny-in-california/) 

It’s always sunny in California.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/uqz1IvCmBo/) [2:12 pm, October 27, 2014](http://dentedreality.com.au/2014/10/27/its-always-sunny-in-california/ "2:12 pm") 
jQuery(document).ready(function(){
var gmap\_m926d0e2a849015d135e258282bc0eb7a = {
positions : {
354 : new google.maps.LatLng( '37.7952', '-122.3961' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m926d0e2a849015d135e258282bc0eb7a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m926d0e2a849015d135e258282bc0eb7a.positions ) {
gmap\_m926d0e2a849015d135e258282bc0eb7a.bounds.extend( gmap\_m926d0e2a849015d135e258282bc0eb7a.positions[m] );
}
// Render markers
for ( var m in gmap\_m926d0e2a849015d135e258282bc0eb7a.positions ) {
gmap\_m926d0e2a849015d135e258282bc0eb7a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m926d0e2a849015d135e258282bc0eb7a.map,
position : gmap\_m926d0e2a849015d135e258282bc0eb7a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m926d0e2a849015d135e258282bc0eb7a.map.setCenter( gmap\_m926d0e2a849015d135e258282bc0eb7a.positions[354] );
});