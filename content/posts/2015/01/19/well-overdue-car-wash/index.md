---
title: ''
date: '2015-01-19T10:09:51+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10932478_1551149241833998_447953455_n.jpg?resize=640%2C640
---

[![Well overdue car wash.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10932478_1551149241833998_447953455_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/01/19/well-overdue-car-wash/) 

Well overdue car wash.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/yCxvYEimOO/) [10:09 am, January 19, 2015](http://dentedreality.com.au/2015/01/19/well-overdue-car-wash/ "10:09 am") 
jQuery(document).ready(function(){
var gmap\_m00d952735adbc7bffba4fd5c0c1476c4 = {
positions : {
959 : new google.maps.LatLng( '39.720888739', '-104.986908017' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m00d952735adbc7bffba4fd5c0c1476c4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m00d952735adbc7bffba4fd5c0c1476c4.positions ) {
gmap\_m00d952735adbc7bffba4fd5c0c1476c4.bounds.extend( gmap\_m00d952735adbc7bffba4fd5c0c1476c4.positions[m] );
}
// Render markers
for ( var m in gmap\_m00d952735adbc7bffba4fd5c0c1476c4.positions ) {
gmap\_m00d952735adbc7bffba4fd5c0c1476c4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m00d952735adbc7bffba4fd5c0c1476c4.map,
position : gmap\_m00d952735adbc7bffba4fd5c0c1476c4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m00d952735adbc7bffba4fd5c0c1476c4.map.setCenter( gmap\_m00d952735adbc7bffba4fd5c0c1476c4.positions[959] );
});