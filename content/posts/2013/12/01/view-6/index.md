---
title: View
date: '2013-12-01T08:20:17+00:00'
format: image
service: flickr
tags:
- france
- paris
- triomphe
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923535313_7297519e45_o.jpg?fit=1500%2C1500
---

[![View](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923535313_7297519e45_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/view-6/) 
# [View](http://dentedreality.com.au/2013/12/01/view-6/)

From the Arc de Triomphe





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[triomphe](http://dentedreality.com.au/tags/triomphe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923535313/) [8:20 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/view-6/ "8:20 am") 
jQuery(document).ready(function(){
var gmap\_m573012046d0f74ea6796eeffba6bc6b1 = {
positions : {
234 : new google.maps.LatLng( '48.873536', '2.295622' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m573012046d0f74ea6796eeffba6bc6b1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m573012046d0f74ea6796eeffba6bc6b1.positions ) {
gmap\_m573012046d0f74ea6796eeffba6bc6b1.bounds.extend( gmap\_m573012046d0f74ea6796eeffba6bc6b1.positions[m] );
}
// Render markers
for ( var m in gmap\_m573012046d0f74ea6796eeffba6bc6b1.positions ) {
gmap\_m573012046d0f74ea6796eeffba6bc6b1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m573012046d0f74ea6796eeffba6bc6b1.map,
position : gmap\_m573012046d0f74ea6796eeffba6bc6b1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m573012046d0f74ea6796eeffba6bc6b1.map.setCenter( gmap\_m573012046d0f74ea6796eeffba6bc6b1.positions[234] );
});