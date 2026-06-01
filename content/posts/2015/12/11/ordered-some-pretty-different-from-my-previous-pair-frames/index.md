---
title: ''
date: '2015-12-11T08:47:04-07:00'
format: image
service: instagram
latitude: '40.7257171'
longitude: '-74.0039422'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/12338745_1706079469610641_73051420_n.jpg?resize=640%2C640
---

[![Ordered some pretty different (from my previous pair) frames.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/12338745_1706079469610641_73051420_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/12/11/ordered-some-pretty-different-from-my-previous-pair-frames/) 

[![Ordered some pretty different (from my previous pair) frames.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/12338745_1706079469610641_73051420_n.jpg?resize=640%2C640)](https://www.instagram.com/p/_KDaWdimFp/)

Ordered some pretty different (from my previous pair) frames.

40.7257171-74.0039422




Posted on [Instagram](https://www.instagram.com/p/_KDaWdimFp/) [8:47 am, December 11, 2015](https://dentedreality.com.au/2015/12/11/ordered-some-pretty-different-from-my-previous-pair-frames/ "8:47 am") 
jQuery(document).ready(function(){
var gmap\_mdb20f969c753773379769a37340bdfa2 = {
positions : {
935 : new google.maps.LatLng( '40.725717076', '-74.003942232' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdb20f969c753773379769a37340bdfa2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdb20f969c753773379769a37340bdfa2.positions ) {
gmap\_mdb20f969c753773379769a37340bdfa2.bounds.extend( gmap\_mdb20f969c753773379769a37340bdfa2.positions[m] );
}
// Render markers
for ( var m in gmap\_mdb20f969c753773379769a37340bdfa2.positions ) {
gmap\_mdb20f969c753773379769a37340bdfa2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdb20f969c753773379769a37340bdfa2.map,
position : gmap\_mdb20f969c753773379769a37340bdfa2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdb20f969c753773379769a37340bdfa2.map.setCenter( gmap\_mdb20f969c753773379769a37340bdfa2.positions[935] );
});