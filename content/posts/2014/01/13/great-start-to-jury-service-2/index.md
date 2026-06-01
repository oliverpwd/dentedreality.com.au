---
title: ''
date: '2014-01-13T08:37:31+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/c65ce66a7c5711e3a5870ad1d5d3af2d_8.jpg?resize=640%2C640
---

[![Great start to Jury Service...](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/c65ce66a7c5711e3a5870ad1d5d3af2d_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/13/great-start-to-jury-service-2/) 

Great start to Jury Service…





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jHGhkaCmAR/) [8:37 am, January 13, 2014](http://dentedreality.com.au/2014/01/13/great-start-to-jury-service-2/ "8:37 am") 
jQuery(document).ready(function(){
var gmap\_m2ec618a27449d0d3639c17909a2fea29 = {
positions : {
101 : new google.maps.LatLng( '40.694749797', '-73.987275681' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2ec618a27449d0d3639c17909a2fea29' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2ec618a27449d0d3639c17909a2fea29.positions ) {
gmap\_m2ec618a27449d0d3639c17909a2fea29.bounds.extend( gmap\_m2ec618a27449d0d3639c17909a2fea29.positions[m] );
}
// Render markers
for ( var m in gmap\_m2ec618a27449d0d3639c17909a2fea29.positions ) {
gmap\_m2ec618a27449d0d3639c17909a2fea29.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2ec618a27449d0d3639c17909a2fea29.map,
position : gmap\_m2ec618a27449d0d3639c17909a2fea29.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2ec618a27449d0d3639c17909a2fea29.map.setCenter( gmap\_m2ec618a27449d0d3639c17909a2fea29.positions[101] );
});