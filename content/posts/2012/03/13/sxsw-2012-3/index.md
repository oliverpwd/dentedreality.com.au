---
title: SXSW 2012
date: '2012-03-13T18:16:57+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721700024_80a8f493e5_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721700024_80a8f493e5_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/13/sxsw-2012-3/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/13/sxsw-2012-3/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721700024/) [6:16 pm, March 13, 2012](http://dentedreality.com.au/2012/03/13/sxsw-2012-3/ "6:16 pm") 
jQuery(document).ready(function(){
var gmap\_m86cff61228bbfcbc964e119120b0b56e = {
positions : {
189 : new google.maps.LatLng( '30.268833', '-97.736' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m86cff61228bbfcbc964e119120b0b56e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m86cff61228bbfcbc964e119120b0b56e.positions ) {
gmap\_m86cff61228bbfcbc964e119120b0b56e.bounds.extend( gmap\_m86cff61228bbfcbc964e119120b0b56e.positions[m] );
}
// Render markers
for ( var m in gmap\_m86cff61228bbfcbc964e119120b0b56e.positions ) {
gmap\_m86cff61228bbfcbc964e119120b0b56e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m86cff61228bbfcbc964e119120b0b56e.map,
position : gmap\_m86cff61228bbfcbc964e119120b0b56e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m86cff61228bbfcbc964e119120b0b56e.map.setCenter( gmap\_m86cff61228bbfcbc964e119120b0b56e.positions[189] );
});