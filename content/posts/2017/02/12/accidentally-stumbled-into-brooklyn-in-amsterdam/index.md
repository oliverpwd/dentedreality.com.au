---
title: ''
date: '2017-02-12T13:03:25+00:00'
format: image
service: instagram
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16583999_263436457426297_2196019952425631744_n.jpg?fit=640%2C640
---

[![Accidentally stumbled into Brooklyn. In Amsterdam.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16583999_263436457426297_2196019952425631744_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/12/accidentally-stumbled-into-brooklyn-in-amsterdam/) 

Accidentally stumbled into Brooklyn. In Amsterdam.





Posted on [Instagram](https://www.instagram.com/p/BQbJxTCDaol/) [1:03 pm, February 12, 2017](http://dentedreality.com.au/2017/02/12/accidentally-stumbled-into-brooklyn-in-amsterdam/ "1:03 pm") 
jQuery(document).ready(function(){
var gmap\_m80fdc90348ed1844d6539823028e20de = {
positions : {
359 : new google.maps.LatLng( '52.383659560403', '4.9300687139857' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m80fdc90348ed1844d6539823028e20de' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m80fdc90348ed1844d6539823028e20de.positions ) {
gmap\_m80fdc90348ed1844d6539823028e20de.bounds.extend( gmap\_m80fdc90348ed1844d6539823028e20de.positions[m] );
}
// Render markers
for ( var m in gmap\_m80fdc90348ed1844d6539823028e20de.positions ) {
gmap\_m80fdc90348ed1844d6539823028e20de.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m80fdc90348ed1844d6539823028e20de.map,
position : gmap\_m80fdc90348ed1844d6539823028e20de.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m80fdc90348ed1844d6539823028e20de.map.setCenter( gmap\_m80fdc90348ed1844d6539823028e20de.positions[359] );
});