---
title: ''
date: '2017-02-15T00:40:31+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16584896_274236959677382_4393055256594874368_n.jpg?fit=640%2C640
---

[![Bikes for days.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16584896_274236959677382_4393055256594874368_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/15/bikes-for-days/) 

Bikes for days.





Posted on [Instagram](https://www.instagram.com/p/BQhjIwYDcbE/) [12:40 am, February 15, 2017](http://dentedreality.com.au/2017/02/15/bikes-for-days/ "12:40 am") 
jQuery(document).ready(function(){
var gmap\_mdf40c26edfda0b1c6545dd63a82640cc = {
positions : {
710 : new google.maps.LatLng( '52.37667637011', '4.8978638807509' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdf40c26edfda0b1c6545dd63a82640cc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdf40c26edfda0b1c6545dd63a82640cc.positions ) {
gmap\_mdf40c26edfda0b1c6545dd63a82640cc.bounds.extend( gmap\_mdf40c26edfda0b1c6545dd63a82640cc.positions[m] );
}
// Render markers
for ( var m in gmap\_mdf40c26edfda0b1c6545dd63a82640cc.positions ) {
gmap\_mdf40c26edfda0b1c6545dd63a82640cc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdf40c26edfda0b1c6545dd63a82640cc.map,
position : gmap\_mdf40c26edfda0b1c6545dd63a82640cc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdf40c26edfda0b1c6545dd63a82640cc.map.setCenter( gmap\_mdf40c26edfda0b1c6545dd63a82640cc.positions[710] );
});