---
title: Chicken Lasagne
date: '2010-01-06T13:44:29+00:00'
format: image
tags:
- chicken
- Chile
- claypot
- lasagne
- Santiago
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/01/4268731717_ae23c36b71_o.jpg?resize=607%2C455
---

[![Chicken Lasagne](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/01/4268731717_ae23c36b71_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/01/06/chicken-lasagne/) 
# [Chicken Lasagne](http://dentedreality.com.au/2010/01/06/chicken-lasagne/)





* #[chicken](http://dentedreality.com.au/tags/chicken/)
* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[claypot](http://dentedreality.com.au/tags/claypot/)
* #[lasagne](http://dentedreality.com.au/tags/lasagne/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4268731717/) [1:44 pm, January 6, 2010](http://dentedreality.com.au/2010/01/06/chicken-lasagne/ "1:44 pm") 
jQuery(document).ready(function(){
var gmap\_m5552fd33f376090288a386f54028704a = {
positions : {
424 : new google.maps.LatLng( '-33.423334', '-70.6165' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5552fd33f376090288a386f54028704a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5552fd33f376090288a386f54028704a.positions ) {
gmap\_m5552fd33f376090288a386f54028704a.bounds.extend( gmap\_m5552fd33f376090288a386f54028704a.positions[m] );
}
// Render markers
for ( var m in gmap\_m5552fd33f376090288a386f54028704a.positions ) {
gmap\_m5552fd33f376090288a386f54028704a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5552fd33f376090288a386f54028704a.map,
position : gmap\_m5552fd33f376090288a386f54028704a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5552fd33f376090288a386f54028704a.map.setCenter( gmap\_m5552fd33f376090288a386f54028704a.positions[424] );
});