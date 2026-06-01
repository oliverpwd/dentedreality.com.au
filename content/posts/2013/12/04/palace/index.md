---
title: Palace
date: '2013-12-04T10:24:47+00:00'
format: image
service: flickr
tags:
- france
- lake
- palace
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923551263_6bf232ec2c_o.jpg?fit=1500%2C1500
---

[![Palace](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923551263_6bf232ec2c_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/04/palace/) 
# [Palace](http://dentedreality.com.au/2013/12/04/palace/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[lake](http://dentedreality.com.au/tags/lake/)
* #[palace](http://dentedreality.com.au/tags/palace/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923551263/) [10:24 am, December 4, 2013](http://dentedreality.com.au/2013/12/04/palace/ "10:24 am") 
jQuery(document).ready(function(){
var gmap\_mca16b1131732c0294db2231cea56ee72 = {
positions : {
945 : new google.maps.LatLng( '48.846722', '2.33695' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mca16b1131732c0294db2231cea56ee72' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mca16b1131732c0294db2231cea56ee72.positions ) {
gmap\_mca16b1131732c0294db2231cea56ee72.bounds.extend( gmap\_mca16b1131732c0294db2231cea56ee72.positions[m] );
}
// Render markers
for ( var m in gmap\_mca16b1131732c0294db2231cea56ee72.positions ) {
gmap\_mca16b1131732c0294db2231cea56ee72.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mca16b1131732c0294db2231cea56ee72.map,
position : gmap\_mca16b1131732c0294db2231cea56ee72.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mca16b1131732c0294db2231cea56ee72.map.setCenter( gmap\_mca16b1131732c0294db2231cea56ee72.positions[945] );
});