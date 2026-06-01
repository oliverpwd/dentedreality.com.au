---
title: ''
date: '2015-06-30T03:39:10+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/10009893_1525748944347102_719279687_n.jpg?resize=640%2C640
---

[![Tinto de verano in a plaza at 10pm in a t-shirt and shorts because Spain.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/10009893_1525748944347102_719279687_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/30/tinto-de-verano-in-a-plaza-at-10pm-in-a-t-shirt-and-shorts-because-spain/) 

Tinto de verano in a plaza at 10pm in a t-shirt and shorts because Spain.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/4jG8T6imKx/) [3:39 am, June 30, 2015](http://dentedreality.com.au/2015/06/30/tinto-de-verano-in-a-plaza-at-10pm-in-a-t-shirt-and-shorts-because-spain/ "3:39 am") 
jQuery(document).ready(function(){
var gmap\_m62439a4737228f186b4ecfe37c41894a = {
positions : {
91 : new google.maps.LatLng( '40.412310419', '-3.70451405' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m62439a4737228f186b4ecfe37c41894a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m62439a4737228f186b4ecfe37c41894a.positions ) {
gmap\_m62439a4737228f186b4ecfe37c41894a.bounds.extend( gmap\_m62439a4737228f186b4ecfe37c41894a.positions[m] );
}
// Render markers
for ( var m in gmap\_m62439a4737228f186b4ecfe37c41894a.positions ) {
gmap\_m62439a4737228f186b4ecfe37c41894a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m62439a4737228f186b4ecfe37c41894a.map,
position : gmap\_m62439a4737228f186b4ecfe37c41894a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m62439a4737228f186b4ecfe37c41894a.map.setCenter( gmap\_m62439a4737228f186b4ecfe37c41894a.positions[91] );
});