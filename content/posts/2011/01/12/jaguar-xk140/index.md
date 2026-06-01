---
title: Jaguar XK140
date: '2011-01-12T13:02:52+00:00'
format: image
service: flickr
tags:
- jaguar
- xk140
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434110409_6e6d193931_o.jpg?resize=607%2C452
---

[![Jaguar XK140](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434110409_6e6d193931_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/12/jaguar-xk140/) 
# [Jaguar XK140](http://dentedreality.com.au/2011/01/12/jaguar-xk140/)





* #[jaguar](http://dentedreality.com.au/tags/jaguar/)
* #[xk140](http://dentedreality.com.au/tags/xk140/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434110409/) [1:02 pm, January 12, 2011](http://dentedreality.com.au/2011/01/12/jaguar-xk140/ "1:02 pm") 
jQuery(document).ready(function(){
var gmap\_m0cfe900ab5aeddab7d14baa93537f128 = {
positions : {
778 : new google.maps.LatLng( '-32.0535', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0cfe900ab5aeddab7d14baa93537f128' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0cfe900ab5aeddab7d14baa93537f128.positions ) {
gmap\_m0cfe900ab5aeddab7d14baa93537f128.bounds.extend( gmap\_m0cfe900ab5aeddab7d14baa93537f128.positions[m] );
}
// Render markers
for ( var m in gmap\_m0cfe900ab5aeddab7d14baa93537f128.positions ) {
gmap\_m0cfe900ab5aeddab7d14baa93537f128.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0cfe900ab5aeddab7d14baa93537f128.map,
position : gmap\_m0cfe900ab5aeddab7d14baa93537f128.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0cfe900ab5aeddab7d14baa93537f128.map.setCenter( gmap\_m0cfe900ab5aeddab7d14baa93537f128.positions[778] );
});