---
title: ''
date: '2013-11-17T01:55:02+00:00'
format: image
tags:
- cinge70
- getstung
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/ccfd22244f4c11e38eb61290a76b76ec_8.jpg?resize=640%2C640
---

[![Free drinks thanks to #cinge70! #getstung](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/ccfd22244f4c11e38eb61290a76b76ec_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/11/17/free-drinks-thanks-to-cinge70-getstung/) 

Free drinks thanks to #cinge70! #getstung





* #[cinge70](http://dentedreality.com.au/tags/cinge70/)
* #[getstung](http://dentedreality.com.au/tags/getstung/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/gzgSbTCmHv/) [1:55 am, November 17, 2013](http://dentedreality.com.au/2013/11/17/free-drinks-thanks-to-cinge70-getstung/ "1:55 am") 
jQuery(document).ready(function(){
var gmap\_m053382db7b41722fdce0eaba59a7a919 = {
positions : {
154 : new google.maps.LatLng( '39.757614769', '-104.990527234' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m053382db7b41722fdce0eaba59a7a919' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m053382db7b41722fdce0eaba59a7a919.positions ) {
gmap\_m053382db7b41722fdce0eaba59a7a919.bounds.extend( gmap\_m053382db7b41722fdce0eaba59a7a919.positions[m] );
}
// Render markers
for ( var m in gmap\_m053382db7b41722fdce0eaba59a7a919.positions ) {
gmap\_m053382db7b41722fdce0eaba59a7a919.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m053382db7b41722fdce0eaba59a7a919.map,
position : gmap\_m053382db7b41722fdce0eaba59a7a919.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m053382db7b41722fdce0eaba59a7a919.map.setCenter( gmap\_m053382db7b41722fdce0eaba59a7a919.positions[154] );
});