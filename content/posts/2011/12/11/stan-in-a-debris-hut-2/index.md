---
title: Stan in a debris hut
date: '2011-12-11T08:34:02+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- stan
- survival
- wilderness
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812215658_8480dd4bff_o.jpg?resize=607%2C813
---

[![Stan in a debris hut](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812215658_8480dd4bff_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/12/11/stan-in-a-debris-hut-2/) 
# [Stan in a debris hut](http://dentedreality.com.au/2011/12/11/stan-in-a-debris-hut-2/)





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[stan](http://dentedreality.com.au/tags/stan/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812215658/) [8:34 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/stan-in-a-debris-hut-2/ "8:34 am") 
jQuery(document).ready(function(){
var gmap\_m9769f852542eacce380655f8f9c762d6 = {
positions : {
295 : new google.maps.LatLng( '38.000833', '-122.611167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9769f852542eacce380655f8f9c762d6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9769f852542eacce380655f8f9c762d6.positions ) {
gmap\_m9769f852542eacce380655f8f9c762d6.bounds.extend( gmap\_m9769f852542eacce380655f8f9c762d6.positions[m] );
}
// Render markers
for ( var m in gmap\_m9769f852542eacce380655f8f9c762d6.positions ) {
gmap\_m9769f852542eacce380655f8f9c762d6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9769f852542eacce380655f8f9c762d6.map,
position : gmap\_m9769f852542eacce380655f8f9c762d6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9769f852542eacce380655f8f9c762d6.map.setCenter( gmap\_m9769f852542eacce380655f8f9c762d6.positions[295] );
});