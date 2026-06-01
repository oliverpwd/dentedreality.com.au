---
title: Republica Dominica
date: '2013-12-26T16:31:57+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901117301_f0b7bdc5c2_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901117301_f0b7bdc5c2_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/26/republica-dominica-15/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/26/republica-dominica-15/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901117301/) [4:31 pm, December 26, 2013](http://dentedreality.com.au/2013/12/26/republica-dominica-15/ "4:31 pm") 
jQuery(document).ready(function(){
var gmap\_me77c3b37d02bdff626e619b6bf5c9d6a = {
positions : {
375 : new google.maps.LatLng( '19.450813', '-70.694253' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me77c3b37d02bdff626e619b6bf5c9d6a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.positions ) {
gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.bounds.extend( gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.positions[m] );
}
// Render markers
for ( var m in gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.positions ) {
gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.map,
position : gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.map.setCenter( gmap\_me77c3b37d02bdff626e619b6bf5c9d6a.positions[375] );
});