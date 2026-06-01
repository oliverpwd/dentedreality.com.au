---
title: Lit Up
date: '2013-12-01T13:13:44+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923489755_c203074751_o.jpg?fit=1500%2C1500
---

[![Lit Up](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923489755_c203074751_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/lit-up/) 
# [Lit Up](http://dentedreality.com.au/2013/12/01/lit-up/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923489755/) [1:13 pm, December 1, 2013](http://dentedreality.com.au/2013/12/01/lit-up/ "1:13 pm") 
jQuery(document).ready(function(){
var gmap\_m830c7a7adf06738402b458d20ef511b5 = {
positions : {
573 : new google.maps.LatLng( '48.855827', '2.353255' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m830c7a7adf06738402b458d20ef511b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m830c7a7adf06738402b458d20ef511b5.positions ) {
gmap\_m830c7a7adf06738402b458d20ef511b5.bounds.extend( gmap\_m830c7a7adf06738402b458d20ef511b5.positions[m] );
}
// Render markers
for ( var m in gmap\_m830c7a7adf06738402b458d20ef511b5.positions ) {
gmap\_m830c7a7adf06738402b458d20ef511b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m830c7a7adf06738402b458d20ef511b5.map,
position : gmap\_m830c7a7adf06738402b458d20ef511b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m830c7a7adf06738402b458d20ef511b5.map.setCenter( gmap\_m830c7a7adf06738402b458d20ef511b5.positions[573] );
});