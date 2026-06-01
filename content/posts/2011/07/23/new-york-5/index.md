---
title: New York
date: '2011-07-23T18:03:12+00:00'
format: image
service: flickr
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322933801_11b03c83c2_o.jpg?resize=607%2C813
---

[![New York](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322933801_11b03c83c2_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/07/23/new-york-5/) 
# [New York](http://dentedreality.com.au/2011/07/23/new-york-5/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322933801/) [6:03 pm, July 23, 2011](http://dentedreality.com.au/2011/07/23/new-york-5/ "6:03 pm") 
jQuery(document).ready(function(){
var gmap\_m348f0f292e93a029b0f7b3c8d45517a1 = {
positions : {
96 : new google.maps.LatLng( '40.7315', '-73.982' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m348f0f292e93a029b0f7b3c8d45517a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m348f0f292e93a029b0f7b3c8d45517a1.positions ) {
gmap\_m348f0f292e93a029b0f7b3c8d45517a1.bounds.extend( gmap\_m348f0f292e93a029b0f7b3c8d45517a1.positions[m] );
}
// Render markers
for ( var m in gmap\_m348f0f292e93a029b0f7b3c8d45517a1.positions ) {
gmap\_m348f0f292e93a029b0f7b3c8d45517a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m348f0f292e93a029b0f7b3c8d45517a1.map,
position : gmap\_m348f0f292e93a029b0f7b3c8d45517a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m348f0f292e93a029b0f7b3c8d45517a1.map.setCenter( gmap\_m348f0f292e93a029b0f7b3c8d45517a1.positions[96] );
});