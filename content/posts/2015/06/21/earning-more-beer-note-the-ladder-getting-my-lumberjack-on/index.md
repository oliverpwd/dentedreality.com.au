---
title: ''
date: '2015-06-21T15:35:36+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11327313_1504002293223195_1167108837_n.jpg?resize=640%2C640
---

[![Earning more beer. Note the ladder. Getting my lumberjack on.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11327313_1504002293223195_1167108837_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/21/earning-more-beer-note-the-ladder-getting-my-lumberjack-on/) 

Earning more beer. Note the ladder. Getting my lumberjack on.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/4NNxrsCmND/) [3:35 pm, June 21, 2015](http://dentedreality.com.au/2015/06/21/earning-more-beer-note-the-ladder-getting-my-lumberjack-on/ "3:35 pm") 
jQuery(document).ready(function(){
var gmap\_m5ac473b108d037ebab6f32e14ab6819d = {
positions : {
613 : new google.maps.LatLng( '39.759913333', '-104.969528333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5ac473b108d037ebab6f32e14ab6819d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5ac473b108d037ebab6f32e14ab6819d.positions ) {
gmap\_m5ac473b108d037ebab6f32e14ab6819d.bounds.extend( gmap\_m5ac473b108d037ebab6f32e14ab6819d.positions[m] );
}
// Render markers
for ( var m in gmap\_m5ac473b108d037ebab6f32e14ab6819d.positions ) {
gmap\_m5ac473b108d037ebab6f32e14ab6819d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5ac473b108d037ebab6f32e14ab6819d.map,
position : gmap\_m5ac473b108d037ebab6f32e14ab6819d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5ac473b108d037ebab6f32e14ab6819d.map.setCenter( gmap\_m5ac473b108d037ebab6f32e14ab6819d.positions[613] );
});