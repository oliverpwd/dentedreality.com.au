---
title: ''
date: '2017-11-19T18:43:25+00:00'
format: image
service: instagram
tags:
- nofilter
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/11/23734175_1952497725000665_7653840873494413312_n.jpg?fit=640%2C640&ssl=1
---

[![Impressive sunset, Denver. #nofilter](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/11/23734175_1952497725000665_7653840873494413312_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/11/19/impressive-sunset-denver-nofilter/) 

[![Impressive sunset, Denver. #nofilter](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/11/23734175_1952497725000665_7653840873494413312_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BbsvQgshpLt/)

Impressive sunset, Denver. #nofilter





* #[nofilter](https://dentedreality.com.au/tags/nofilter/)

Posted on [Instagram](https://www.instagram.com/p/BbsvQgshpLt/) [6:43 pm, November 19, 2017](https://dentedreality.com.au/2017/11/19/impressive-sunset-denver-nofilter/ "6:43 pm") 
jQuery(document).ready(function(){
var gmap\_m48ba06b55ce0d3fcd5a942226ce4d475 = {
positions : {
843 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m48ba06b55ce0d3fcd5a942226ce4d475' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.positions ) {
gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.bounds.extend( gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.positions[m] );
}
// Render markers
for ( var m in gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.positions ) {
gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.map,
position : gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.map.setCenter( gmap\_m48ba06b55ce0d3fcd5a942226ce4d475.positions[843] );
});