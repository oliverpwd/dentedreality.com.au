---
title: ''
date: '2015-02-03T13:09:21+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/929214_1537852256476376_689957214_n.jpg?resize=640%2C640
---

[![2 days ago this was all under 4-5 inches of snow.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/929214_1537852256476376_689957214_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/03/2-days-ago-this-was-all-under-4-5-inches-of-snow/) 

2 days ago this was all under 4-5 inches of snow.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/ypuNM8CmES/) [1:09 pm, February 3, 2015](http://dentedreality.com.au/2015/02/03/2-days-ago-this-was-all-under-4-5-inches-of-snow/ "1:09 pm") 
jQuery(document).ready(function(){
var gmap\_mffff0582c4d7fc3a55f8693006677b12 = {
positions : {
395 : new google.maps.LatLng( '39.73479289', '-104.978539958' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mffff0582c4d7fc3a55f8693006677b12' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mffff0582c4d7fc3a55f8693006677b12.positions ) {
gmap\_mffff0582c4d7fc3a55f8693006677b12.bounds.extend( gmap\_mffff0582c4d7fc3a55f8693006677b12.positions[m] );
}
// Render markers
for ( var m in gmap\_mffff0582c4d7fc3a55f8693006677b12.positions ) {
gmap\_mffff0582c4d7fc3a55f8693006677b12.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mffff0582c4d7fc3a55f8693006677b12.map,
position : gmap\_mffff0582c4d7fc3a55f8693006677b12.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mffff0582c4d7fc3a55f8693006677b12.map.setCenter( gmap\_mffff0582c4d7fc3a55f8693006677b12.positions[395] );
});