---
title: ''
date: '2014-06-26T19:11:45+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10483542_320128964808237_1605943077_n.jpg?resize=640%2C640
---

[![Impressive.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10483542_320128964808237_1605943077_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/06/26/impressive-2/) 

Impressive.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/puheXcCmCN/) [7:11 pm, June 26, 2014](http://dentedreality.com.au/2014/06/26/impressive-2/ "7:11 pm") 
jQuery(document).ready(function(){
var gmap\_m6065922c100a3e3f3ccf1460597cb4b3 = {
positions : {
577 : new google.maps.LatLng( '40.651684301', '-74.008799354' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6065922c100a3e3f3ccf1460597cb4b3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6065922c100a3e3f3ccf1460597cb4b3.positions ) {
gmap\_m6065922c100a3e3f3ccf1460597cb4b3.bounds.extend( gmap\_m6065922c100a3e3f3ccf1460597cb4b3.positions[m] );
}
// Render markers
for ( var m in gmap\_m6065922c100a3e3f3ccf1460597cb4b3.positions ) {
gmap\_m6065922c100a3e3f3ccf1460597cb4b3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6065922c100a3e3f3ccf1460597cb4b3.map,
position : gmap\_m6065922c100a3e3f3ccf1460597cb4b3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6065922c100a3e3f3ccf1460597cb4b3.map.setCenter( gmap\_m6065922c100a3e3f3ccf1460597cb4b3.positions[577] );
});