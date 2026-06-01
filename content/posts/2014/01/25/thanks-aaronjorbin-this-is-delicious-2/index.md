---
title: ''
date: '2014-01-25T18:08:47+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/8181e73a861511e38ae512bc234f61c7_8.jpg?resize=640%2C640
---

[![Thanks @aaronjorbin, this is delicious!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/8181e73a861511e38ae512bc234f61c7_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/25/thanks-aaronjorbin-this-is-delicious-2/) 

Thanks @aaronjorbin, this is delicious!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jnBcOhCmDn/) [6:08 pm, January 25, 2014](http://dentedreality.com.au/2014/01/25/thanks-aaronjorbin-this-is-delicious-2/ "6:08 pm") 
jQuery(document).ready(function(){
var gmap\_m813a5bd6b802df6b5cd08cc18dee4aec = {
positions : {
754 : new google.maps.LatLng( '40.669361667', '-73.984991667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m813a5bd6b802df6b5cd08cc18dee4aec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.positions ) {
gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.bounds.extend( gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.positions[m] );
}
// Render markers
for ( var m in gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.positions ) {
gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.map,
position : gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.map.setCenter( gmap\_m813a5bd6b802df6b5cd08cc18dee4aec.positions[754] );
});