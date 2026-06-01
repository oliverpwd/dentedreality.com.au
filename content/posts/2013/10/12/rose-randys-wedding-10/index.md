---
title: Rose & Randy’s Wedding
date: '2013-10-12T10:31:46+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- vision:text=0506
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291463184_6b12f02e33_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291463184_6b12f02e33_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-10/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-10/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[vision:text=0506](http://dentedreality.com.au/tags/visiontext0506/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291463184/) [10:31 am, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-10/ "10:31 am") 
jQuery(document).ready(function(){
var gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f = {
positions : {
185 : new google.maps.LatLng( '38.417333', '-122.547167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.positions ) {
gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.bounds.extend( gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.positions[m] );
}
// Render markers
for ( var m in gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.positions ) {
gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.map,
position : gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.map.setCenter( gmap\_m71a7692c7faf1c3ea89c5cbf07861f0f.positions[185] );
});