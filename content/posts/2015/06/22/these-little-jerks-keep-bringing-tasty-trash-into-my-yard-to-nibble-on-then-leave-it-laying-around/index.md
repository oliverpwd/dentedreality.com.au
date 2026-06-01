---
title: ''
date: '2015-06-22T14:12:24+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11378508_919204028143050_1987043619_n.jpg?resize=640%2C640
---

[![These little jerks keep bringing tasty trash into my yard to nibble on, then leave it laying around.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11378508_919204028143050_1987043619_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/22/these-little-jerks-keep-bringing-tasty-trash-into-my-yard-to-nibble-on-then-leave-it-laying-around/) 

These little jerks keep bringing tasty trash into my yard to nibble on, then leave it laying around.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/4PpDKpCmLQ/) [2:12 pm, June 22, 2015](http://dentedreality.com.au/2015/06/22/these-little-jerks-keep-bringing-tasty-trash-into-my-yard-to-nibble-on-then-leave-it-laying-around/ "2:12 pm") 
jQuery(document).ready(function(){
var gmap\_mf026d1e02af8a4d9ec626c040782c467 = {
positions : {
407 : new google.maps.LatLng( '39.759913333', '-104.969528333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf026d1e02af8a4d9ec626c040782c467' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf026d1e02af8a4d9ec626c040782c467.positions ) {
gmap\_mf026d1e02af8a4d9ec626c040782c467.bounds.extend( gmap\_mf026d1e02af8a4d9ec626c040782c467.positions[m] );
}
// Render markers
for ( var m in gmap\_mf026d1e02af8a4d9ec626c040782c467.positions ) {
gmap\_mf026d1e02af8a4d9ec626c040782c467.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf026d1e02af8a4d9ec626c040782c467.map,
position : gmap\_mf026d1e02af8a4d9ec626c040782c467.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf026d1e02af8a4d9ec626c040782c467.map.setCenter( gmap\_mf026d1e02af8a4d9ec626c040782c467.positions[407] );
});