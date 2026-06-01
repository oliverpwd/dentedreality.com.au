---
title: Frankenthumb
date: '2014-01-08T11:42:11+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901697452_d63732cb86_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901697452_d63732cb86_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/08/frankenthumb-14/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/08/frankenthumb-14/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901697452/) [11:42 am, January 8, 2014](http://dentedreality.com.au/2014/01/08/frankenthumb-14/ "11:42 am") 
jQuery(document).ready(function(){
var gmap\_mefe1ef5ea55a337509f4818b3a3c2097 = {
positions : {
287 : new google.maps.LatLng( '40.669441', '-73.984925' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mefe1ef5ea55a337509f4818b3a3c2097' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mefe1ef5ea55a337509f4818b3a3c2097.positions ) {
gmap\_mefe1ef5ea55a337509f4818b3a3c2097.bounds.extend( gmap\_mefe1ef5ea55a337509f4818b3a3c2097.positions[m] );
}
// Render markers
for ( var m in gmap\_mefe1ef5ea55a337509f4818b3a3c2097.positions ) {
gmap\_mefe1ef5ea55a337509f4818b3a3c2097.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mefe1ef5ea55a337509f4818b3a3c2097.map,
position : gmap\_mefe1ef5ea55a337509f4818b3a3c2097.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mefe1ef5ea55a337509f4818b3a3c2097.map.setCenter( gmap\_mefe1ef5ea55a337509f4818b3a3c2097.positions[287] );
});