---
title: ''
date: '2014-10-19T00:25:45+00:00'
format: image
tags:
- fishing
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10731671_292843497589063_1424520080_n.jpg?resize=640%2C640
---

[![Boulder Creek #fishing](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10731671_292843497589063_1424520080_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/19/boulder-creek-fishing/) 

Boulder Creek #fishing





* #[fishing](http://dentedreality.com.au/tags/fishing/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/uUu5WaimDh/) [12:25 am, October 19, 2014](http://dentedreality.com.au/2014/10/19/boulder-creek-fishing/ "12:25 am") 
jQuery(document).ready(function(){
var gmap\_m80db0db73d803a48468f9deed71f5852 = {
positions : {
798 : new google.maps.LatLng( '40.01528055', '-105.313941667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m80db0db73d803a48468f9deed71f5852' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m80db0db73d803a48468f9deed71f5852.positions ) {
gmap\_m80db0db73d803a48468f9deed71f5852.bounds.extend( gmap\_m80db0db73d803a48468f9deed71f5852.positions[m] );
}
// Render markers
for ( var m in gmap\_m80db0db73d803a48468f9deed71f5852.positions ) {
gmap\_m80db0db73d803a48468f9deed71f5852.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m80db0db73d803a48468f9deed71f5852.map,
position : gmap\_m80db0db73d803a48468f9deed71f5852.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m80db0db73d803a48468f9deed71f5852.map.setCenter( gmap\_m80db0db73d803a48468f9deed71f5852.positions[798] );
});