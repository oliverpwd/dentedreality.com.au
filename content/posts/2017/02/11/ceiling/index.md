---
title: ''
date: '2017-02-11T07:54:14+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16583590_1631273167175225_6117240491407835136_n.jpg?fit=640%2C640
---

[![Ceiling](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16583590_1631273167175225_6117240491407835136_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/11/ceiling/) 

Ceiling





Posted on [Instagram](https://www.instagram.com/p/BQYBl6Xj8kQ/) [7:54 am, February 11, 2017](http://dentedreality.com.au/2017/02/11/ceiling/ "7:54 am") 
jQuery(document).ready(function(){
var gmap\_m42f1c52b06425079a52fca2e3f86debd = {
positions : {
259 : new google.maps.LatLng( '52.35995', '4.8853799' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m42f1c52b06425079a52fca2e3f86debd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m42f1c52b06425079a52fca2e3f86debd.positions ) {
gmap\_m42f1c52b06425079a52fca2e3f86debd.bounds.extend( gmap\_m42f1c52b06425079a52fca2e3f86debd.positions[m] );
}
// Render markers
for ( var m in gmap\_m42f1c52b06425079a52fca2e3f86debd.positions ) {
gmap\_m42f1c52b06425079a52fca2e3f86debd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m42f1c52b06425079a52fca2e3f86debd.map,
position : gmap\_m42f1c52b06425079a52fca2e3f86debd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m42f1c52b06425079a52fca2e3f86debd.map.setCenter( gmap\_m42f1c52b06425079a52fca2e3f86debd.positions[259] );
});