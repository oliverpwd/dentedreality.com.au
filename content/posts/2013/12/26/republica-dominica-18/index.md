---
title: Republica Dominica
date: '2013-12-26T10:55:58+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901125236_d18b208729_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901125236_d18b208729_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/26/republica-dominica-18/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/26/republica-dominica-18/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901125236/) [10:55 am, December 26, 2013](http://dentedreality.com.au/2013/12/26/republica-dominica-18/ "10:55 am") 
jQuery(document).ready(function(){
var gmap\_maf518293f4ae091ff99e2346c74f07fa = {
positions : {
173 : new google.maps.LatLng( '19.580002', '-70.745025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf518293f4ae091ff99e2346c74f07fa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf518293f4ae091ff99e2346c74f07fa.positions ) {
gmap\_maf518293f4ae091ff99e2346c74f07fa.bounds.extend( gmap\_maf518293f4ae091ff99e2346c74f07fa.positions[m] );
}
// Render markers
for ( var m in gmap\_maf518293f4ae091ff99e2346c74f07fa.positions ) {
gmap\_maf518293f4ae091ff99e2346c74f07fa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf518293f4ae091ff99e2346c74f07fa.map,
position : gmap\_maf518293f4ae091ff99e2346c74f07fa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf518293f4ae091ff99e2346c74f07fa.map.setCenter( gmap\_maf518293f4ae091ff99e2346c74f07fa.positions[173] );
});