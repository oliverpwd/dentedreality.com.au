---
title: Drain
date: '2013-12-04T10:48:19+00:00'
format: image
service: flickr
tags:
- drain
- france
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900382566_d7a51a2d9f_o.jpg?fit=1500%2C1500
---

[![Drain](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900382566_d7a51a2d9f_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/04/drain/) 
# [Drain](http://dentedreality.com.au/2013/12/04/drain/)





* #[drain](http://dentedreality.com.au/tags/drain/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900382566/) [10:48 am, December 4, 2013](http://dentedreality.com.au/2013/12/04/drain/ "10:48 am") 
jQuery(document).ready(function(){
var gmap\_m5e9a3653ebdd4235089f15f9c8e06ade = {
positions : {
352 : new google.maps.LatLng( '48.855247', '2.340027' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5e9a3653ebdd4235089f15f9c8e06ade' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.positions ) {
gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.bounds.extend( gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.positions[m] );
}
// Render markers
for ( var m in gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.positions ) {
gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.map,
position : gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.map.setCenter( gmap\_m5e9a3653ebdd4235089f15f9c8e06ade.positions[352] );
});