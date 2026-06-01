---
title: Real Eggs
date: '2010-12-24T05:19:54+00:00'
format: image
service: flickr
tags:
- australia
- eggs
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434094931_5a69931b0b_o.jpg?resize=607%2C452
---

[![Real Eggs](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434094931_5a69931b0b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/24/real-eggs/) 
# [Real Eggs](http://dentedreality.com.au/2010/12/24/real-eggs/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[eggs](http://dentedreality.com.au/tags/eggs/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434094931/) [5:19 am, December 24, 2010](http://dentedreality.com.au/2010/12/24/real-eggs/ "5:19 am") 
jQuery(document).ready(function(){
var gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb = {
positions : {
128 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.positions ) {
gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.bounds.extend( gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.positions[m] );
}
// Render markers
for ( var m in gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.positions ) {
gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.map,
position : gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.map.setCenter( gmap\_mdba9f62b1c3780e5961dfa7ff86de6bb.positions[128] );
});