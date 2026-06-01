---
title: Holmenkollen Ski Jump
date: '2011-10-29T10:01:47+00:00'
format: image
service: flickr
tags:
- holmenkollen
- norway
- Oslo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812168656_d7984a6c5c_o.jpg?resize=607%2C452
---

[![Holmenkollen Ski Jump](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812168656_d7984a6c5c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/29/holmenkollen-ski-jump/) 
# [Holmenkollen Ski Jump](http://dentedreality.com.au/2011/10/29/holmenkollen-ski-jump/)





* #[holmenkollen](http://dentedreality.com.au/tags/holmenkollen/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812168656/) [10:01 am, October 29, 2011](http://dentedreality.com.au/2011/10/29/holmenkollen-ski-jump/ "10:01 am") 
jQuery(document).ready(function(){
var gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0 = {
positions : {
101 : new google.maps.LatLng( '59.9645', '10.666333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.positions ) {
gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.bounds.extend( gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.positions[m] );
}
// Render markers
for ( var m in gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.positions ) {
gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.map,
position : gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.map.setCenter( gmap\_m1af5709b089f4cffeaf3a51d74ef5eb0.positions[101] );
});