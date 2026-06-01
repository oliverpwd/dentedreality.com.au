---
title: ''
date: '2017-05-21T18:06:25+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18580319_1737146032968812_6141087137677705216_n.jpg?fit=640%2C640&ssl=1
---

[![Some tricky descents, when you're carrying a 30lb pack.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18580319_1737146032968812_6141087137677705216_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/05/21/some-tricky-descents-when-youre-carrying-a-30lb-pack/) 

Some tricky descents, when you’re carrying a 30lb pack.





Posted on [Instagram](https://www.instagram.com/p/BUX7ezABFdZ/) [6:06 pm, May 21, 2017](https://dentedreality.com.au/2017/05/21/some-tricky-descents-when-youre-carrying-a-30lb-pack/ "6:06 pm") 
jQuery(document).ready(function(){
var gmap\_m7efc9c39dbc3aad964e19a45fc583b54 = {
positions : {
971 : new google.maps.LatLng( '39.7683409616', '-105.215712653' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7efc9c39dbc3aad964e19a45fc583b54' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7efc9c39dbc3aad964e19a45fc583b54.positions ) {
gmap\_m7efc9c39dbc3aad964e19a45fc583b54.bounds.extend( gmap\_m7efc9c39dbc3aad964e19a45fc583b54.positions[m] );
}
// Render markers
for ( var m in gmap\_m7efc9c39dbc3aad964e19a45fc583b54.positions ) {
gmap\_m7efc9c39dbc3aad964e19a45fc583b54.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7efc9c39dbc3aad964e19a45fc583b54.map,
position : gmap\_m7efc9c39dbc3aad964e19a45fc583b54.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7efc9c39dbc3aad964e19a45fc583b54.map.setCenter( gmap\_m7efc9c39dbc3aad964e19a45fc583b54.positions[971] );
});