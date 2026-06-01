---
title: ''
date: '2011-06-28T16:23:48+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/9b13dfb62ba14d3581a221ac90fea4f5_7.jpg?resize=607%2C607
---

[![F-Yeah Fried Chicken](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/9b13dfb62ba14d3581a221ac90fea4f5_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/06/28/f-yeah-fried-chicken/) 

F-Yeah Fried Chicken





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/GkfEV/) [4:23 pm, June 28, 2011](http://dentedreality.com.au/2011/06/28/f-yeah-fried-chicken/ "4:23 pm") 
jQuery(document).ready(function(){
var gmap\_m708efb647aeff6a9ffcd0711a6c30032 = {
positions : {
482 : new google.maps.LatLng( '37.792816', '-122.421378493' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m708efb647aeff6a9ffcd0711a6c30032' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m708efb647aeff6a9ffcd0711a6c30032.positions ) {
gmap\_m708efb647aeff6a9ffcd0711a6c30032.bounds.extend( gmap\_m708efb647aeff6a9ffcd0711a6c30032.positions[m] );
}
// Render markers
for ( var m in gmap\_m708efb647aeff6a9ffcd0711a6c30032.positions ) {
gmap\_m708efb647aeff6a9ffcd0711a6c30032.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m708efb647aeff6a9ffcd0711a6c30032.map,
position : gmap\_m708efb647aeff6a9ffcd0711a6c30032.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m708efb647aeff6a9ffcd0711a6c30032.map.setCenter( gmap\_m708efb647aeff6a9ffcd0711a6c30032.positions[482] );
});