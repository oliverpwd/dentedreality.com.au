---
title: ''
date: '2015-12-15T19:20:31+00:00'
format: image
service: instagram
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/12346274_1711798745732096_641164456_n.jpg?fit=640%2C640
---

[![All of the snows.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/12346274_1711798745732096_641164456_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2015/12/15/all-of-the-snows/) 

All of the snows.





Posted on [Instagram](https://www.instagram.com/p/_VfFZMCmOc/) [7:20 pm, December 15, 2015](http://dentedreality.com.au/2015/12/15/all-of-the-snows/ "7:20 pm") 
jQuery(document).ready(function(){
var gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3 = {
positions : {
580 : new google.maps.LatLng( '39.7392', '-104.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.positions ) {
gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.bounds.extend( gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.positions[m] );
}
// Render markers
for ( var m in gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.positions ) {
gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.map,
position : gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.map.setCenter( gmap\_m6b59f31b792bcc31f9bd8d6f6939a3c3.positions[580] );
});