---
title: ''
date: '2010-11-30T19:12:56+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/daa371185d8d4d83aed63e924b733a6c_7.jpg?resize=607%2C607
---

[![FSM FTW](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/daa371185d8d4d83aed63e924b733a6c_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/11/30/fsm-ftw/) 

FSM FTW





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/auw6/) [7:12 pm, November 30, 2010](http://dentedreality.com.au/2010/11/30/fsm-ftw/ "7:12 pm") 
jQuery(document).ready(function(){
var gmap\_m7bd9118b468584013e752512b41c238a = {
positions : {
623 : new google.maps.LatLng( '37.782858', '-122.390978' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7bd9118b468584013e752512b41c238a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7bd9118b468584013e752512b41c238a.positions ) {
gmap\_m7bd9118b468584013e752512b41c238a.bounds.extend( gmap\_m7bd9118b468584013e752512b41c238a.positions[m] );
}
// Render markers
for ( var m in gmap\_m7bd9118b468584013e752512b41c238a.positions ) {
gmap\_m7bd9118b468584013e752512b41c238a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7bd9118b468584013e752512b41c238a.map,
position : gmap\_m7bd9118b468584013e752512b41c238a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7bd9118b468584013e752512b41c238a.map.setCenter( gmap\_m7bd9118b468584013e752512b41c238a.positions[623] );
});