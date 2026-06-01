---
title: ''
date: '2011-02-28T19:00:32+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/c13bd15087c14901abdea0567adc68d4_7.jpg?resize=607%2C607
---

[![Police Training?](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/c13bd15087c14901abdea0567adc68d4_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/02/28/police-training/) 

Police Training?





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/B6zGj/) [7:00 pm, February 28, 2011](http://dentedreality.com.au/2011/02/28/police-training/ "7:00 pm") 
jQuery(document).ready(function(){
var gmap\_m7da900da93be59998281cf037ab9ffb4 = {
positions : {
91 : new google.maps.LatLng( '37.782741', '-122.388024' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7da900da93be59998281cf037ab9ffb4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7da900da93be59998281cf037ab9ffb4.positions ) {
gmap\_m7da900da93be59998281cf037ab9ffb4.bounds.extend( gmap\_m7da900da93be59998281cf037ab9ffb4.positions[m] );
}
// Render markers
for ( var m in gmap\_m7da900da93be59998281cf037ab9ffb4.positions ) {
gmap\_m7da900da93be59998281cf037ab9ffb4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7da900da93be59998281cf037ab9ffb4.map,
position : gmap\_m7da900da93be59998281cf037ab9ffb4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7da900da93be59998281cf037ab9ffb4.map.setCenter( gmap\_m7da900da93be59998281cf037ab9ffb4.positions[91] );
});