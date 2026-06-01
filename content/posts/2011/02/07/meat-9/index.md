---
title: Meat!
date: '2011-02-07T14:10:21+00:00'
format: image
service: flickr
tags:
- '4505'
- 4505meats
- butchery
- lamb
- meat
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802053863_a953e8915d_o.jpg?resize=607%2C452
---

[![Meat!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802053863_a953e8915d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/07/meat-9/) 
# [Meat!](http://dentedreality.com.au/2011/02/07/meat-9/)

Butchering a lamb with 4505 Meats





* #[4505](http://dentedreality.com.au/tags/4505/)
* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[butchery](http://dentedreality.com.au/tags/butchery/)
* #[lamb](http://dentedreality.com.au/tags/lamb/)
* #[meat](http://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802053863/) [2:10 pm, February 7, 2011](http://dentedreality.com.au/2011/02/07/meat-9/ "2:10 pm") 
jQuery(document).ready(function(){
var gmap\_mdde75c46cc714fa03d9364bcfbe68852 = {
positions : {
584 : new google.maps.LatLng( '37.778333', '-122.425667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdde75c46cc714fa03d9364bcfbe68852' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdde75c46cc714fa03d9364bcfbe68852.positions ) {
gmap\_mdde75c46cc714fa03d9364bcfbe68852.bounds.extend( gmap\_mdde75c46cc714fa03d9364bcfbe68852.positions[m] );
}
// Render markers
for ( var m in gmap\_mdde75c46cc714fa03d9364bcfbe68852.positions ) {
gmap\_mdde75c46cc714fa03d9364bcfbe68852.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdde75c46cc714fa03d9364bcfbe68852.map,
position : gmap\_mdde75c46cc714fa03d9364bcfbe68852.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdde75c46cc714fa03d9364bcfbe68852.map.setCenter( gmap\_mdde75c46cc714fa03d9364bcfbe68852.positions[584] );
});