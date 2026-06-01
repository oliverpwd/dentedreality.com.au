---
title: Melbourne From Above
date: '2014-03-28T13:46:20+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927930283_3f8b673bef_o.jpg?resize=607%2C455
---

[![Melbourne From Above](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927930283_3f8b673bef_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/melbourne-from-above-2/) 
# [Melbourne From Above](http://dentedreality.com.au/2014/03/28/melbourne-from-above-2/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927930283/) [1:46 pm, March 28, 2014](http://dentedreality.com.au/2014/03/28/melbourne-from-above-2/ "1:46 pm") 
jQuery(document).ready(function(){
var gmap\_m463d00d4dc42f528269ec889d66f95bc = {
positions : {
360 : new google.maps.LatLng( '-37.821659', '144.964783' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m463d00d4dc42f528269ec889d66f95bc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m463d00d4dc42f528269ec889d66f95bc.positions ) {
gmap\_m463d00d4dc42f528269ec889d66f95bc.bounds.extend( gmap\_m463d00d4dc42f528269ec889d66f95bc.positions[m] );
}
// Render markers
for ( var m in gmap\_m463d00d4dc42f528269ec889d66f95bc.positions ) {
gmap\_m463d00d4dc42f528269ec889d66f95bc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m463d00d4dc42f528269ec889d66f95bc.map,
position : gmap\_m463d00d4dc42f528269ec889d66f95bc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m463d00d4dc42f528269ec889d66f95bc.map.setCenter( gmap\_m463d00d4dc42f528269ec889d66f95bc.positions[360] );
});