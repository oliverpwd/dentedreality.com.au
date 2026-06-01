---
title: ''
date: '2011-07-11T23:50:34+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/e53aafceb030473f914d4e5612f50a85_7.jpg?resize=607%2C607
---

[![Home-made Rack o' Lamb](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/e53aafceb030473f914d4e5612f50a85_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/07/11/home-made-rack-o-lamb/) 

Home-made Rack o’ Lamb





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/HevYt/) [11:50 pm, July 11, 2011](http://dentedreality.com.au/2011/07/11/home-made-rack-o-lamb/ "11:50 pm") 
jQuery(document).ready(function(){
var gmap\_m6ae7e32af4f8d53ba592402d01db7d41 = {
positions : {
827 : new google.maps.LatLng( '37.79135', '-122.4177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6ae7e32af4f8d53ba592402d01db7d41' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6ae7e32af4f8d53ba592402d01db7d41.positions ) {
gmap\_m6ae7e32af4f8d53ba592402d01db7d41.bounds.extend( gmap\_m6ae7e32af4f8d53ba592402d01db7d41.positions[m] );
}
// Render markers
for ( var m in gmap\_m6ae7e32af4f8d53ba592402d01db7d41.positions ) {
gmap\_m6ae7e32af4f8d53ba592402d01db7d41.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6ae7e32af4f8d53ba592402d01db7d41.map,
position : gmap\_m6ae7e32af4f8d53ba592402d01db7d41.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6ae7e32af4f8d53ba592402d01db7d41.map.setCenter( gmap\_m6ae7e32af4f8d53ba592402d01db7d41.positions[827] );
});