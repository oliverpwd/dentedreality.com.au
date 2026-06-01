---
title: Night, Bridge
date: '2013-12-01T12:37:43+00:00'
format: image
service: flickr
tags:
- bridge
- france
- lights
- night
- paris
- seine
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923544993_d9bb07bfbe_o.jpg?fit=1500%2C1500
---

[![Night, Bridge](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923544993_d9bb07bfbe_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/night-bridge/) 
# [Night, Bridge](http://dentedreality.com.au/2013/12/01/night-bridge/)





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[lights](http://dentedreality.com.au/tags/lights/)
* #[night](http://dentedreality.com.au/tags/night/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[seine](http://dentedreality.com.au/tags/seine/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923544993/) [12:37 pm, December 1, 2013](http://dentedreality.com.au/2013/12/01/night-bridge/ "12:37 pm") 
jQuery(document).ready(function(){
var gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180 = {
positions : {
343 : new google.maps.LatLng( '48.85545', '2.349683' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.positions ) {
gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.bounds.extend( gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.positions[m] );
}
// Render markers
for ( var m in gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.positions ) {
gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.map,
position : gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.map.setCenter( gmap\_mc1e697dbb969a2efd0fc2e0fbb19e180.positions[343] );
});