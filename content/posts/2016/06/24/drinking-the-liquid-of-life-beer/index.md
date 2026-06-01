---
title: ''
date: '2016-06-24T02:25:32-06:00'
format: image
service: instagram
tags:
- beer
latitude: '-32.0593642'
longitude: '115.7445621'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13534162_1582356735398505_914064806_n.jpg?fit=640%2C640
---

[![Drinking the liquid of life. #beer](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13534162_1582356735398505_914064806_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/24/drinking-the-liquid-of-life-beer/) 

[![Drinking the liquid of life. #beer](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13534162_1582356735398505_914064806_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BHB8r9xA9cZ/)

Drinking the liquid of life. #beer

-32.0593642115.7445621




* #[beer](https://dentedreality.com.au/tags/beer/)

Posted on [Instagram](https://www.instagram.com/p/BHB8r9xA9cZ/) [2:25 am, June 24, 2016](https://dentedreality.com.au/2016/06/24/drinking-the-liquid-of-life-beer/ "2:25 am") 
jQuery(document).ready(function(){
var gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344 = {
positions : {
872 : new google.maps.LatLng( '-32.059364152365', '115.74456210252' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.positions ) {
gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.bounds.extend( gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.positions[m] );
}
// Render markers
for ( var m in gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.positions ) {
gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.map,
position : gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.map.setCenter( gmap\_m8d620c8a4b84c2c4b2a6d47afd7df344.positions[872] );
});