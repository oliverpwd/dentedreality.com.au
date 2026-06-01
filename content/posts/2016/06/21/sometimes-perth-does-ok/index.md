---
title: ''
date: '2016-06-21T01:26:23-06:00'
format: image
service: instagram
latitude: '-31.9594633'
longitude: '115.8589507'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13408689_256804524696634_106375870_n.jpg?fit=640%2C640
---

[![Sometimes Perth does OK.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13408689_256804524696634_106375870_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/21/sometimes-perth-does-ok/) 

[![Sometimes Perth does OK.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13408689_256804524696634_106375870_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BG6HiHrCmIg/)

Sometimes Perth does OK.

-31.9594633115.8589507




Posted on [Instagram](https://www.instagram.com/p/BG6HiHrCmIg/) [1:26 am, June 21, 2016](https://dentedreality.com.au/2016/06/21/sometimes-perth-does-ok/ "1:26 am") 
jQuery(document).ready(function(){
var gmap\_me1507a3110ab7dabd0915cfb7ac71ddd = {
positions : {
542 : new google.maps.LatLng( '-31.95946331416', '115.85895072715' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me1507a3110ab7dabd0915cfb7ac71ddd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.positions ) {
gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.bounds.extend( gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.positions[m] );
}
// Render markers
for ( var m in gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.positions ) {
gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.map,
position : gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.map.setCenter( gmap\_me1507a3110ab7dabd0915cfb7ac71ddd.positions[542] );
});