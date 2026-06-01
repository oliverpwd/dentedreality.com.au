---
title: View
date: '2013-12-01T08:23:47+00:00'
format: image
service: flickr
tags:
- france
- paris
- triomphe
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923480205_cf5a2dfaf0_o.jpg?fit=1500%2C1500
---

[![View](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923480205_cf5a2dfaf0_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/view-5/) 
# [View](http://dentedreality.com.au/2013/12/01/view-5/)

From the Arc de Triomphe





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[triomphe](http://dentedreality.com.au/tags/triomphe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923480205/) [8:23 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/view-5/ "8:23 am") 
jQuery(document).ready(function(){
var gmap\_m4db83194883c72634f67349532ac59e3 = {
positions : {
959 : new google.maps.LatLng( '48.8736', '2.295302' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4db83194883c72634f67349532ac59e3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4db83194883c72634f67349532ac59e3.positions ) {
gmap\_m4db83194883c72634f67349532ac59e3.bounds.extend( gmap\_m4db83194883c72634f67349532ac59e3.positions[m] );
}
// Render markers
for ( var m in gmap\_m4db83194883c72634f67349532ac59e3.positions ) {
gmap\_m4db83194883c72634f67349532ac59e3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4db83194883c72634f67349532ac59e3.map,
position : gmap\_m4db83194883c72634f67349532ac59e3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4db83194883c72634f67349532ac59e3.map.setCenter( gmap\_m4db83194883c72634f67349532ac59e3.positions[959] );
});