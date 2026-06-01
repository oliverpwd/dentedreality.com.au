---
title: ''
date: '2016-03-01T20:11:39+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/12724739_188763748158985_1899635494_n.jpg?fit=640%2C640
---

[![Caucusing is bananas!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/12724739_188763748158985_1899635494_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/03/01/caucusing-is-bananas/) 

Caucusing is bananas!





Posted on [Instagram](https://www.instagram.com/p/BCb2JTqCmDk/) [8:11 pm, March 1, 2016](http://dentedreality.com.au/2016/03/01/caucusing-is-bananas/ "8:11 pm") 
jQuery(document).ready(function(){
var gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961 = {
positions : {
699 : new google.maps.LatLng( '39.7557716', '-104.9677887' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.positions ) {
gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.bounds.extend( gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.positions[m] );
}
// Render markers
for ( var m in gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.positions ) {
gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.map,
position : gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.map.setCenter( gmap\_m8a9cd4e4e3ca38ea73b51ce58efd2961.positions[699] );
});