---
title: Tunnel
date: '2013-11-29T07:26:53+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923530373_751049cd92_o.jpg?fit=1500%2C1500
---

[![Tunnel](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923530373_751049cd92_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/11/29/tunnel-2/) 
# [Tunnel](http://dentedreality.com.au/2013/11/29/tunnel-2/)

Under the Arc de Triomphe





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923530373/) [7:26 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/tunnel-2/ "7:26 am") 
jQuery(document).ready(function(){
var gmap\_mb309924d76339a62323e82e247718923 = {
positions : {
508 : new google.maps.LatLng( '48.873661', '2.296422' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb309924d76339a62323e82e247718923' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb309924d76339a62323e82e247718923.positions ) {
gmap\_mb309924d76339a62323e82e247718923.bounds.extend( gmap\_mb309924d76339a62323e82e247718923.positions[m] );
}
// Render markers
for ( var m in gmap\_mb309924d76339a62323e82e247718923.positions ) {
gmap\_mb309924d76339a62323e82e247718923.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb309924d76339a62323e82e247718923.map,
position : gmap\_mb309924d76339a62323e82e247718923.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb309924d76339a62323e82e247718923.map.setCenter( gmap\_mb309924d76339a62323e82e247718923.positions[508] );
});