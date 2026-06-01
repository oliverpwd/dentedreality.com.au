---
title: NERT Citywide Drill, 2011
date: '2011-04-16T07:51:50+00:00'
format: image
service: flickr
tags:
- nert
- sanfrancisco
- sffd
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802145435_7221f0d458_o.jpg?resize=607%2C452
---

[![NERT Citywide Drill, 2011](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802145435_7221f0d458_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-4/) 
# [NERT Citywide Drill, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-4/)





* #[nert](http://dentedreality.com.au/tags/nert/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sffd](http://dentedreality.com.au/tags/sffd/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802145435/) [7:51 am, April 16, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-4/ "7:51 am") 
jQuery(document).ready(function(){
var gmap\_m5059ea7fbb464a2a752f28ff5d3ade01 = {
positions : {
645 : new google.maps.LatLng( '37.759833', '-122.415501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5059ea7fbb464a2a752f28ff5d3ade01' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.positions ) {
gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.bounds.extend( gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.positions[m] );
}
// Render markers
for ( var m in gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.positions ) {
gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.map,
position : gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.map.setCenter( gmap\_m5059ea7fbb464a2a752f28ff5d3ade01.positions[645] );
});