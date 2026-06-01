---
title: BBQ
date: '2010-12-25T09:15:22+00:00'
format: image
service: flickr
tags:
- bbq
- meat
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434095305_cb9c75b522_o.jpg?resize=607%2C452
---

[![BBQ](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434095305_cb9c75b522_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/25/bbq-3/) 
# [BBQ](http://dentedreality.com.au/2010/12/25/bbq-3/)





* #[bbq](http://dentedreality.com.au/tags/bbq/)
* #[meat](http://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434095305/) [9:15 am, December 25, 2010](http://dentedreality.com.au/2010/12/25/bbq-3/ "9:15 am") 
jQuery(document).ready(function(){
var gmap\_me6f9056a3d4aff94045c5e525e1ef6f0 = {
positions : {
707 : new google.maps.LatLng( '-32.052834', '115.845833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me6f9056a3d4aff94045c5e525e1ef6f0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.positions ) {
gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.bounds.extend( gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.positions[m] );
}
// Render markers
for ( var m in gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.positions ) {
gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.map,
position : gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.map.setCenter( gmap\_me6f9056a3d4aff94045c5e525e1ef6f0.positions[707] );
});