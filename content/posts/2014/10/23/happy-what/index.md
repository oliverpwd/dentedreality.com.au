---
title: ''
date: '2014-10-23T21:25:52+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10735457_330188877154197_46443496_n.jpg?resize=640%2C640
---

[![Happy What?](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10735457_330188877154197_46443496_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/23/happy-what/) 

Happy What?





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/uhSSSDCmLb/) [9:25 pm, October 23, 2014](http://dentedreality.com.au/2014/10/23/happy-what/ "9:25 pm") 
jQuery(document).ready(function(){
var gmap\_mf1baca548906b941e848bec7391d2e26 = {
positions : {
38 : new google.maps.LatLng( '39.858625236', '-104.672347132' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf1baca548906b941e848bec7391d2e26' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf1baca548906b941e848bec7391d2e26.positions ) {
gmap\_mf1baca548906b941e848bec7391d2e26.bounds.extend( gmap\_mf1baca548906b941e848bec7391d2e26.positions[m] );
}
// Render markers
for ( var m in gmap\_mf1baca548906b941e848bec7391d2e26.positions ) {
gmap\_mf1baca548906b941e848bec7391d2e26.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf1baca548906b941e848bec7391d2e26.map,
position : gmap\_mf1baca548906b941e848bec7391d2e26.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf1baca548906b941e848bec7391d2e26.map.setCenter( gmap\_mf1baca548906b941e848bec7391d2e26.positions[38] );
});