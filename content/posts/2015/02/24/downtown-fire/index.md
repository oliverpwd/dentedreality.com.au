---
title: ''
date: '2015-02-24T15:04:52+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10983680_926240757394246_1431819641_n.jpg?resize=640%2C640
---

[![Downtown fire!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10983680_926240757394246_1431819641_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/24/downtown-fire/) 

Downtown fire!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/zgAHo6imNB/) [3:04 pm, February 24, 2015](http://dentedreality.com.au/2015/02/24/downtown-fire/ "3:04 pm") 
jQuery(document).ready(function(){
var gmap\_m9665c98ab7fbc190817c6b69cef284d6 = {
positions : {
886 : new google.maps.LatLng( '39.771572093', '-105.193440156' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9665c98ab7fbc190817c6b69cef284d6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9665c98ab7fbc190817c6b69cef284d6.positions ) {
gmap\_m9665c98ab7fbc190817c6b69cef284d6.bounds.extend( gmap\_m9665c98ab7fbc190817c6b69cef284d6.positions[m] );
}
// Render markers
for ( var m in gmap\_m9665c98ab7fbc190817c6b69cef284d6.positions ) {
gmap\_m9665c98ab7fbc190817c6b69cef284d6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9665c98ab7fbc190817c6b69cef284d6.map,
position : gmap\_m9665c98ab7fbc190817c6b69cef284d6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9665c98ab7fbc190817c6b69cef284d6.map.setCenter( gmap\_m9665c98ab7fbc190817c6b69cef284d6.positions[886] );
});