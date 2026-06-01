---
title: ''
date: '2014-11-29T14:54:51+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10755955_338263369689513_1800062799_n.jpg?resize=640%2C640
---

[![Fitting Room](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10755955_338263369689513_1800062799_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/29/fitting-room/) 

Fitting Room





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/v_90KSCmDL/) [2:54 pm, November 29, 2014](http://dentedreality.com.au/2014/11/29/fitting-room/ "2:54 pm") 
jQuery(document).ready(function(){
var gmap\_m01476e54d12eb86186a512606dd0814d = {
positions : {
759 : new google.maps.LatLng( '39.717139035', '-104.954673768' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m01476e54d12eb86186a512606dd0814d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m01476e54d12eb86186a512606dd0814d.positions ) {
gmap\_m01476e54d12eb86186a512606dd0814d.bounds.extend( gmap\_m01476e54d12eb86186a512606dd0814d.positions[m] );
}
// Render markers
for ( var m in gmap\_m01476e54d12eb86186a512606dd0814d.positions ) {
gmap\_m01476e54d12eb86186a512606dd0814d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m01476e54d12eb86186a512606dd0814d.map,
position : gmap\_m01476e54d12eb86186a512606dd0814d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m01476e54d12eb86186a512606dd0814d.map.setCenter( gmap\_m01476e54d12eb86186a512606dd0814d.positions[759] );
});