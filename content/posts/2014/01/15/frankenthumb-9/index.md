---
title: Frankenthumb
date: '2014-01-15T18:17:08+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901683321_d63c4f8355_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901683321_d63c4f8355_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/15/frankenthumb-9/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/15/frankenthumb-9/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901683321/) [6:17 pm, January 15, 2014](http://dentedreality.com.au/2014/01/15/frankenthumb-9/ "6:17 pm") 
jQuery(document).ready(function(){
var gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4 = {
positions : {
168 : new google.maps.LatLng( '40.669411', '-73.98497' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.positions ) {
gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.bounds.extend( gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.positions[m] );
}
// Render markers
for ( var m in gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.positions ) {
gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.map,
position : gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.map.setCenter( gmap\_m0d8561dfb56d85e0b1531fba98f7bbf4.positions[168] );
});