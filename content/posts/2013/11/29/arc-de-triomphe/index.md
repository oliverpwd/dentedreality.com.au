---
title: Arc de Triomphe
date: '2013-11-29T07:19:42+00:00'
format: image
service: flickr
tags:
- france
- paris
- triomphe
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900369432_253b53c585_o.jpg?fit=1500%2C1500
---

[![Arc de Triomphe](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900369432_253b53c585_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/11/29/arc-de-triomphe/) 
# [Arc de Triomphe](http://dentedreality.com.au/2013/11/29/arc-de-triomphe/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[triomphe](http://dentedreality.com.au/tags/triomphe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900369432/) [7:19 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/arc-de-triomphe/ "7:19 am") 
jQuery(document).ready(function(){
var gmap\_md4c5ee308181124e87b25fcbf9813a4b = {
positions : {
936 : new google.maps.LatLng( '48.873725', '2.296544' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md4c5ee308181124e87b25fcbf9813a4b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md4c5ee308181124e87b25fcbf9813a4b.positions ) {
gmap\_md4c5ee308181124e87b25fcbf9813a4b.bounds.extend( gmap\_md4c5ee308181124e87b25fcbf9813a4b.positions[m] );
}
// Render markers
for ( var m in gmap\_md4c5ee308181124e87b25fcbf9813a4b.positions ) {
gmap\_md4c5ee308181124e87b25fcbf9813a4b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md4c5ee308181124e87b25fcbf9813a4b.map,
position : gmap\_md4c5ee308181124e87b25fcbf9813a4b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md4c5ee308181124e87b25fcbf9813a4b.map.setCenter( gmap\_md4c5ee308181124e87b25fcbf9813a4b.positions[936] );
});