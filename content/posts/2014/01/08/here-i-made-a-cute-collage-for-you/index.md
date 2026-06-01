---
title: ''
date: '2014-01-08T08:31:38+00:00'
format: image
tags:
- nailedit
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/225da1c2786911e3bbfc122878962eb0_8.jpg?resize=640%2C640
---

[![Here, I made a cute collage for you!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/225da1c2786911e3bbfc122878962eb0_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/08/here-i-made-a-cute-collage-for-you/) 

Here, I made a cute collage for you!





* #[nailedit](http://dentedreality.com.au/tags/nailedit/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/i6N4HhCmO7/) [8:31 am, January 8, 2014](http://dentedreality.com.au/2014/01/08/here-i-made-a-cute-collage-for-you/ "8:31 am") 
jQuery(document).ready(function(){
var gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2 = {
positions : {
239 : new google.maps.LatLng( '40.669637659', '-73.984963736' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.positions ) {
gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.bounds.extend( gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.positions[m] );
}
// Render markers
for ( var m in gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.positions ) {
gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.map,
position : gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.map.setCenter( gmap\_m8ea3f5c8b39c8d82a348c8e17042c6f2.positions[239] );
});