---
title: ''
date: '2015-02-01T13:23:26+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10914442_756520064428447_1725630076_n.jpg?resize=640%2C640
---

[![Crazy overnight snow. Check out the accumulations on the branches.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10914442_756520064428447_1725630076_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/01/crazy-overnight-snow-check-out-the-accumulations-on-the-branches/) 

Crazy overnight snow. Check out the accumulations on the branches.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/ykmOpuCmJI/) [1:23 pm, February 1, 2015](http://dentedreality.com.au/2015/02/01/crazy-overnight-snow-check-out-the-accumulations-on-the-branches/ "1:23 pm") 
jQuery(document).ready(function(){
var gmap\_m2d64a3463b71ea4ddc5d9836fd797682 = {
positions : {
177 : new google.maps.LatLng( '39.73465', '-104.978721667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2d64a3463b71ea4ddc5d9836fd797682' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2d64a3463b71ea4ddc5d9836fd797682.positions ) {
gmap\_m2d64a3463b71ea4ddc5d9836fd797682.bounds.extend( gmap\_m2d64a3463b71ea4ddc5d9836fd797682.positions[m] );
}
// Render markers
for ( var m in gmap\_m2d64a3463b71ea4ddc5d9836fd797682.positions ) {
gmap\_m2d64a3463b71ea4ddc5d9836fd797682.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2d64a3463b71ea4ddc5d9836fd797682.map,
position : gmap\_m2d64a3463b71ea4ddc5d9836fd797682.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2d64a3463b71ea4ddc5d9836fd797682.map.setCenter( gmap\_m2d64a3463b71ea4ddc5d9836fd797682.positions[177] );
});