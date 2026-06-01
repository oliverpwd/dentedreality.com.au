---
title: Sushi
date: '2011-09-02T16:35:35+00:00'
format: image
service: flickr
tags:
- sushi
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6322995967_052af8b40e_o.jpg?resize=607%2C452
---

[![Sushi](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6322995967_052af8b40e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/02/sushi-2/) 
# [Sushi](http://dentedreality.com.au/2011/09/02/sushi-2/)





* #[sushi](http://dentedreality.com.au/tags/sushi/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322995967/) [4:35 pm, September 2, 2011](http://dentedreality.com.au/2011/09/02/sushi-2/ "4:35 pm") 
jQuery(document).ready(function(){
var gmap\_m0e02e7cd77958c81102fe4b675e4606e = {
positions : {
459 : new google.maps.LatLng( '37.791', '-122.420834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0e02e7cd77958c81102fe4b675e4606e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0e02e7cd77958c81102fe4b675e4606e.positions ) {
gmap\_m0e02e7cd77958c81102fe4b675e4606e.bounds.extend( gmap\_m0e02e7cd77958c81102fe4b675e4606e.positions[m] );
}
// Render markers
for ( var m in gmap\_m0e02e7cd77958c81102fe4b675e4606e.positions ) {
gmap\_m0e02e7cd77958c81102fe4b675e4606e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0e02e7cd77958c81102fe4b675e4606e.map,
position : gmap\_m0e02e7cd77958c81102fe4b675e4606e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0e02e7cd77958c81102fe4b675e4606e.map.setCenter( gmap\_m0e02e7cd77958c81102fe4b675e4606e.positions[459] );
});