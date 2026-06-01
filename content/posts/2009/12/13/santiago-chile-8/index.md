---
title: Santiago, Chile
date: '2009-12-13T15:23:39+00:00'
format: image
service: flickr
tags:
- buildings
- Chile
- Santiago
- skyline
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4203462404_f061708163_o.jpg?resize=607%2C455
---

[![Santiago, Chile](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4203462404_f061708163_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/12/13/santiago-chile-8/) 
# [Santiago, Chile](http://dentedreality.com.au/2009/12/13/santiago-chile-8/)





* #[buildings](http://dentedreality.com.au/tags/buildings/)
* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4203462404/) [3:23 pm, December 13, 2009](http://dentedreality.com.au/2009/12/13/santiago-chile-8/ "3:23 pm") 
jQuery(document).ready(function(){
var gmap\_m68154e3b591dbb4f377058a414316c0e = {
positions : {
456 : new google.maps.LatLng( '-33.427334', '-70.619167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m68154e3b591dbb4f377058a414316c0e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m68154e3b591dbb4f377058a414316c0e.positions ) {
gmap\_m68154e3b591dbb4f377058a414316c0e.bounds.extend( gmap\_m68154e3b591dbb4f377058a414316c0e.positions[m] );
}
// Render markers
for ( var m in gmap\_m68154e3b591dbb4f377058a414316c0e.positions ) {
gmap\_m68154e3b591dbb4f377058a414316c0e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m68154e3b591dbb4f377058a414316c0e.map,
position : gmap\_m68154e3b591dbb4f377058a414316c0e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m68154e3b591dbb4f377058a414316c0e.map.setCenter( gmap\_m68154e3b591dbb4f377058a414316c0e.positions[456] );
});