---
title: ''
date: '2014-04-27T10:27:20+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10311085_575083319276683_53957193_n.jpg?resize=640%2C640
---

[![FLOWERS](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10311085_575083319276683_53957193_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/27/flowers/) 

FLOWERS





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/nTFw4RCmEv/) [10:27 am, April 27, 2014](http://dentedreality.com.au/2014/04/27/flowers/ "10:27 am") 
jQuery(document).ready(function(){
var gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca = {
positions : {
185 : new google.maps.LatLng( '53.339558769', '-6.271746832' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.positions ) {
gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.bounds.extend( gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.positions[m] );
}
// Render markers
for ( var m in gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.positions ) {
gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.map,
position : gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.map.setCenter( gmap\_m39bb56e0eb0ae7dbaba29f0124df88ca.positions[185] );
});