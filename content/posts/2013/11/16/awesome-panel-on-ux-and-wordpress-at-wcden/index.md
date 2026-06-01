---
title: ''
date: '2013-11-16T17:19:53+00:00'
format: image
tags:
- photo
- wcden
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/d5b9fda84f0411e384041243d2856edf_8.jpg?resize=640%2C640
---

[![Awesome panel on UX and @WordPress at #wcden](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/d5b9fda84f0411e384041243d2856edf_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/11/16/awesome-panel-on-ux-and-wordpress-at-wcden/) 

Awesome panel on UX and @WordPress at #wcden





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcden](http://dentedreality.com.au/tags/wcden/)

Posted on [Instagram](http://instagram.com/p/gylVV4imGV/) [5:19 pm, November 16, 2013](http://dentedreality.com.au/2013/11/16/awesome-panel-on-ux-and-wordpress-at-wcden/ "5:19 pm") 
jQuery(document).ready(function(){
var gmap\_mf779c79964ae0b954bb845f3e4667453 = {
positions : {
83 : new google.maps.LatLng( '39.749240095', '-105.022607462' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf779c79964ae0b954bb845f3e4667453' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf779c79964ae0b954bb845f3e4667453.positions ) {
gmap\_mf779c79964ae0b954bb845f3e4667453.bounds.extend( gmap\_mf779c79964ae0b954bb845f3e4667453.positions[m] );
}
// Render markers
for ( var m in gmap\_mf779c79964ae0b954bb845f3e4667453.positions ) {
gmap\_mf779c79964ae0b954bb845f3e4667453.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf779c79964ae0b954bb845f3e4667453.map,
position : gmap\_mf779c79964ae0b954bb845f3e4667453.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf779c79964ae0b954bb845f3e4667453.map.setCenter( gmap\_mf779c79964ae0b954bb845f3e4667453.positions[83] );
});