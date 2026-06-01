---
title: ''
date: '2014-09-28T00:14:50+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10691661_328575950647399_1293447946_n.jpg?resize=640%2C640
---

[![Elk are not small animals.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10691661_328575950647399_1293447946_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/28/elk-are-not-small-animals/) 

Elk are not small animals.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/teo9A9CmP2/) [12:14 am, September 28, 2014](http://dentedreality.com.au/2014/09/28/elk-are-not-small-animals/ "12:14 am") 
jQuery(document).ready(function(){
var gmap\_m6037afb5eb19373a58246a2d78b3b960 = {
positions : {
912 : new google.maps.LatLng( '40.366461229', '-105.560970449' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6037afb5eb19373a58246a2d78b3b960' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6037afb5eb19373a58246a2d78b3b960.positions ) {
gmap\_m6037afb5eb19373a58246a2d78b3b960.bounds.extend( gmap\_m6037afb5eb19373a58246a2d78b3b960.positions[m] );
}
// Render markers
for ( var m in gmap\_m6037afb5eb19373a58246a2d78b3b960.positions ) {
gmap\_m6037afb5eb19373a58246a2d78b3b960.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6037afb5eb19373a58246a2d78b3b960.map,
position : gmap\_m6037afb5eb19373a58246a2d78b3b960.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6037afb5eb19373a58246a2d78b3b960.map.setCenter( gmap\_m6037afb5eb19373a58246a2d78b3b960.positions[912] );
});