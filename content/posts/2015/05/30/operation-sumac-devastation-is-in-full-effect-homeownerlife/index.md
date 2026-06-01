---
title: ''
date: '2015-05-30T18:27:12+00:00'
format: image
service: instagram
tags:
- homeownerlife
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11352054_1589689934619130_587261559_n.jpg?resize=640%2C640
---

[![Operation Sumac Devastation is in full effect #homeownerlife](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11352054_1589689934619130_587261559_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/30/operation-sumac-devastation-is-in-full-effect-homeownerlife/) 

Operation Sumac Devastation is in full effect #homeownerlife





* #[homeownerlife](http://dentedreality.com.au/tags/homeownerlife/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/3U37O6CmAH/) [6:27 pm, May 30, 2015](http://dentedreality.com.au/2015/05/30/operation-sumac-devastation-is-in-full-effect-homeownerlife/ "6:27 pm") 
jQuery(document).ready(function(){
var gmap\_m257b035bc52c690f9632451a46177d98 = {
positions : {
539 : new google.maps.LatLng( '39.760080844', '-104.969575854' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m257b035bc52c690f9632451a46177d98' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m257b035bc52c690f9632451a46177d98.positions ) {
gmap\_m257b035bc52c690f9632451a46177d98.bounds.extend( gmap\_m257b035bc52c690f9632451a46177d98.positions[m] );
}
// Render markers
for ( var m in gmap\_m257b035bc52c690f9632451a46177d98.positions ) {
gmap\_m257b035bc52c690f9632451a46177d98.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m257b035bc52c690f9632451a46177d98.map,
position : gmap\_m257b035bc52c690f9632451a46177d98.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m257b035bc52c690f9632451a46177d98.map.setCenter( gmap\_m257b035bc52c690f9632451a46177d98.positions[539] );
});