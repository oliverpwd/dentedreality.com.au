---
title: ''
date: '2016-01-16T09:52:26+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12519275_926141227461657_196762595_n.jpg?fit=640%2C640
---

[![So many penguins!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12519275_926141227461657_196762595_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/01/16/so-many-penguins/) 

So many penguins!





Posted on [Instagram](https://www.instagram.com/p/BAm3glOimIA/) [9:52 am, January 16, 2016](http://dentedreality.com.au/2016/01/16/so-many-penguins/ "9:52 am") 
jQuery(document).ready(function(){
var gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31 = {
positions : {
798 : new google.maps.LatLng( '-34.19589664', '18.449739053' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.positions ) {
gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.bounds.extend( gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.positions[m] );
}
// Render markers
for ( var m in gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.positions ) {
gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.map,
position : gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.map.setCenter( gmap\_m3e37df4e2d48f6f0a0ae5f61e1108c31.positions[798] );
});