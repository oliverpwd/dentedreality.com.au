---
title: Rose & Randy’s Wedding
date: '2013-10-12T15:21:04+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- wedding
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291040545_678a9e3182_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291040545_678a9e3182_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-4/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-4/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291040545/) [3:21 pm, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-4/ "3:21 pm") 
jQuery(document).ready(function(){
var gmap\_m06713ae8b9c23620196bc7d84d1728a4 = {
positions : {
948 : new google.maps.LatLng( '38.414', '-122.551' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m06713ae8b9c23620196bc7d84d1728a4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m06713ae8b9c23620196bc7d84d1728a4.positions ) {
gmap\_m06713ae8b9c23620196bc7d84d1728a4.bounds.extend( gmap\_m06713ae8b9c23620196bc7d84d1728a4.positions[m] );
}
// Render markers
for ( var m in gmap\_m06713ae8b9c23620196bc7d84d1728a4.positions ) {
gmap\_m06713ae8b9c23620196bc7d84d1728a4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m06713ae8b9c23620196bc7d84d1728a4.map,
position : gmap\_m06713ae8b9c23620196bc7d84d1728a4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m06713ae8b9c23620196bc7d84d1728a4.map.setCenter( gmap\_m06713ae8b9c23620196bc7d84d1728a4.positions[948] );
});