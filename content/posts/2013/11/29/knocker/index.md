---
title: Knocker
date: '2013-11-29T05:17:31+00:00'
format: image
service: flickr
tags:
- door
- france
- knocker
- lion
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923913664_427984ddbd_o.jpg?resize=607%2C809
---

[![Knocker](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923913664_427984ddbd_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/29/knocker/) 
# [Knocker](http://dentedreality.com.au/2013/11/29/knocker/)





* #[door](http://dentedreality.com.au/tags/door/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[knocker](http://dentedreality.com.au/tags/knocker/)
* #[lion](http://dentedreality.com.au/tags/lion/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923913664/) [5:17 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/knocker/ "5:17 am") 
jQuery(document).ready(function(){
var gmap\_m84e5914de444b769c355edc9c5633863 = {
positions : {
446 : new google.maps.LatLng( '48.877786', '2.330574' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m84e5914de444b769c355edc9c5633863' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m84e5914de444b769c355edc9c5633863.positions ) {
gmap\_m84e5914de444b769c355edc9c5633863.bounds.extend( gmap\_m84e5914de444b769c355edc9c5633863.positions[m] );
}
// Render markers
for ( var m in gmap\_m84e5914de444b769c355edc9c5633863.positions ) {
gmap\_m84e5914de444b769c355edc9c5633863.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m84e5914de444b769c355edc9c5633863.map,
position : gmap\_m84e5914de444b769c355edc9c5633863.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m84e5914de444b769c355edc9c5633863.map.setCenter( gmap\_m84e5914de444b769c355edc9c5633863.positions[446] );
});