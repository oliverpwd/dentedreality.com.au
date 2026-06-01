---
title: ''
date: '2016-05-25T22:13:46+00:00'
format: image
service: instagram
tags:
- fatbike
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/05/13108971_1567440666888636_1047798140_n.jpg?fit=640%2C640
---

[![#fatbike maiden voyage](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/05/13108971_1567440666888636_1047798140_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/05/25/fatbike-maiden-voyage/) 

#fatbike maiden voyage





* #[fatbike](http://dentedreality.com.au/tags/fatbike/)

Posted on [Instagram](https://www.instagram.com/p/BF200kICmI3/) [10:13 pm, May 25, 2016](http://dentedreality.com.au/2016/05/25/fatbike-maiden-voyage/ "10:13 pm") 
jQuery(document).ready(function(){
var gmap\_me9d2ee55274cce631397d79caec8f7ec = {
positions : {
129 : new google.maps.LatLng( '39.653993679535', '-105.36743885992' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me9d2ee55274cce631397d79caec8f7ec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me9d2ee55274cce631397d79caec8f7ec.positions ) {
gmap\_me9d2ee55274cce631397d79caec8f7ec.bounds.extend( gmap\_me9d2ee55274cce631397d79caec8f7ec.positions[m] );
}
// Render markers
for ( var m in gmap\_me9d2ee55274cce631397d79caec8f7ec.positions ) {
gmap\_me9d2ee55274cce631397d79caec8f7ec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me9d2ee55274cce631397d79caec8f7ec.map,
position : gmap\_me9d2ee55274cce631397d79caec8f7ec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me9d2ee55274cce631397d79caec8f7ec.map.setCenter( gmap\_me9d2ee55274cce631397d79caec8f7ec.positions[129] );
});