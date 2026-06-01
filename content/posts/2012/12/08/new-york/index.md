---
title: New York
date: '2012-12-08T12:27:13+00:00'
format: image
service: flickr
tags:
- newyork
- traffic
- view
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8459273497_5e4167d702_o.jpg?resize=607%2C813
---

[![New York](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8459273497_5e4167d702_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/12/08/new-york/) 
# [New York](http://dentedreality.com.au/2012/12/08/new-york/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[traffic](http://dentedreality.com.au/tags/traffic/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459273497/) [12:27 pm, December 8, 2012](http://dentedreality.com.au/2012/12/08/new-york/ "12:27 pm") 
jQuery(document).ready(function(){
var gmap\_m9c019ead3469259a0500b79a20d9b74a = {
positions : {
706 : new google.maps.LatLng( '40.756', '-73.990167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9c019ead3469259a0500b79a20d9b74a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9c019ead3469259a0500b79a20d9b74a.positions ) {
gmap\_m9c019ead3469259a0500b79a20d9b74a.bounds.extend( gmap\_m9c019ead3469259a0500b79a20d9b74a.positions[m] );
}
// Render markers
for ( var m in gmap\_m9c019ead3469259a0500b79a20d9b74a.positions ) {
gmap\_m9c019ead3469259a0500b79a20d9b74a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9c019ead3469259a0500b79a20d9b74a.map,
position : gmap\_m9c019ead3469259a0500b79a20d9b74a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9c019ead3469259a0500b79a20d9b74a.map.setCenter( gmap\_m9c019ead3469259a0500b79a20d9b74a.positions[706] );
});