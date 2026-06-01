---
title: Frogner Park
date: '2011-10-28T10:05:12+00:00'
format: image
service: flickr
tags:
- frognerpark
- norway
- Oslo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958277781_88e421168a_o.jpg?resize=607%2C452
---

[![Frogner Park](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958277781_88e421168a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/28/frogner-park/) 
# [Frogner Park](http://dentedreality.com.au/2011/10/28/frogner-park/)

Don’t ask me, I don’t know. This place was \*weird\*!





* #[frognerpark](http://dentedreality.com.au/tags/frognerpark/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958277781/) [10:05 am, October 28, 2011](http://dentedreality.com.au/2011/10/28/frogner-park/ "10:05 am") 
jQuery(document).ready(function(){
var gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a = {
positions : {
659 : new google.maps.LatLng( '59.927666', '10.698666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.positions ) {
gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.bounds.extend( gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.positions[m] );
}
// Render markers
for ( var m in gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.positions ) {
gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.map,
position : gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.map.setCenter( gmap\_mcf1e67469be8b5a7b59a85e78ace0e0a.positions[659] );
});