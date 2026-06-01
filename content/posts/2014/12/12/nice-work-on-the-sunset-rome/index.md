---
title: ''
date: '2014-12-12T18:41:11+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10864868_927810720570657_331105310_n.jpg?resize=640%2C640
---

[![Nice work on the sunset, Rome.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10864868_927810720570657_331105310_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/12/nice-work-on-the-sunset-rome/) 

Nice work on the sunset, Rome.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/wh2DPvCmKx/) [6:41 pm, December 12, 2014](http://dentedreality.com.au/2014/12/12/nice-work-on-the-sunset-rome/ "6:41 pm") 
jQuery(document).ready(function(){
var gmap\_m39f5617627125268ac8217cc35d9ba25 = {
positions : {
883 : new google.maps.LatLng( '41.90467', '12.483025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m39f5617627125268ac8217cc35d9ba25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m39f5617627125268ac8217cc35d9ba25.positions ) {
gmap\_m39f5617627125268ac8217cc35d9ba25.bounds.extend( gmap\_m39f5617627125268ac8217cc35d9ba25.positions[m] );
}
// Render markers
for ( var m in gmap\_m39f5617627125268ac8217cc35d9ba25.positions ) {
gmap\_m39f5617627125268ac8217cc35d9ba25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m39f5617627125268ac8217cc35d9ba25.map,
position : gmap\_m39f5617627125268ac8217cc35d9ba25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m39f5617627125268ac8217cc35d9ba25.map.setCenter( gmap\_m39f5617627125268ac8217cc35d9ba25.positions[883] );
});