---
title: ''
date: '2014-12-12T18:38:48+00:00'
format: image
service: instagram
tags:
- nofilter
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10843763_353600064812559_944988131_n.jpg?resize=640%2C640
---

[![The Pantheon #nofilter](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10843763_353600064812559_944988131_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/12/the-pantheon-nofilter/) 

The Pantheon #nofilter





* #[nofilter](http://dentedreality.com.au/tags/nofilter/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/wh1x1SimKh/) [6:38 pm, December 12, 2014](http://dentedreality.com.au/2014/12/12/the-pantheon-nofilter/ "6:38 pm") 
jQuery(document).ready(function(){
var gmap\_m44b62ac486d46a4ae6c9723805169efd = {
positions : {
270 : new google.maps.LatLng( '41.898604', '12.476816' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m44b62ac486d46a4ae6c9723805169efd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m44b62ac486d46a4ae6c9723805169efd.positions ) {
gmap\_m44b62ac486d46a4ae6c9723805169efd.bounds.extend( gmap\_m44b62ac486d46a4ae6c9723805169efd.positions[m] );
}
// Render markers
for ( var m in gmap\_m44b62ac486d46a4ae6c9723805169efd.positions ) {
gmap\_m44b62ac486d46a4ae6c9723805169efd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m44b62ac486d46a4ae6c9723805169efd.map,
position : gmap\_m44b62ac486d46a4ae6c9723805169efd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m44b62ac486d46a4ae6c9723805169efd.map.setCenter( gmap\_m44b62ac486d46a4ae6c9723805169efd.positions[270] );
});