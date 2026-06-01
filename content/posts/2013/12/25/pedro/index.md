---
title: Pedro!
date: '2013-12-25T08:35:23+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
- pedro
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924231245_92e2a6732e_o.jpg?resize=607%2C809
---

[![Pedro!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924231245_92e2a6732e_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/12/25/pedro/) 
# [Pedro!](http://dentedreality.com.au/2013/12/25/pedro/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[pedro](http://dentedreality.com.au/tags/pedro/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924231245/) [8:35 am, December 25, 2013](http://dentedreality.com.au/2013/12/25/pedro/ "8:35 am") 
jQuery(document).ready(function(){
var gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3 = {
positions : {
440 : new google.maps.LatLng( '19.318655', '-70.711167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.positions ) {
gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.bounds.extend( gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.positions[m] );
}
// Render markers
for ( var m in gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.positions ) {
gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.map,
position : gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.map.setCenter( gmap\_mc1af9ee2c6f0bf9db7a1f564a6e335d3.positions[440] );
});