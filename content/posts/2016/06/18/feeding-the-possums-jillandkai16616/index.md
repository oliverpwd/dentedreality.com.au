---
title: ''
date: '2016-06-18T08:32:13-06:00'
format: image
service: instagram
tags:
- jillandkai16616
latitude: '-26.7006463'
longitude: '152.8714575'
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13473149_832135760252568_401305946_n.jpg?fit=640%2C640
---

[![Feeding the Possums. #jillandkai16616](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13473149_832135760252568_401305946_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/18/feeding-the-possums-jillandkai16616/) 

[![Feeding the Possums. #jillandkai16616](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13473149_832135760252568_401305946_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BGzJ4a0imIo/)

Feeding the Possums. #jillandkai16616

-26.7006463152.8714575




* #[jillandkai16616](https://dentedreality.com.au/tags/jillandkai16616/)

Posted on [Instagram](https://www.instagram.com/p/BGzJ4a0imIo/) [8:32 am, June 18, 2016](https://dentedreality.com.au/2016/06/18/feeding-the-possums-jillandkai16616/ "8:32 am") 
jQuery(document).ready(function(){
var gmap\_m40c04b78a8f7327355463a45197d0c8d = {
positions : {
10 : new google.maps.LatLng( '-26.700646319655', '152.87145753495' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m40c04b78a8f7327355463a45197d0c8d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m40c04b78a8f7327355463a45197d0c8d.positions ) {
gmap\_m40c04b78a8f7327355463a45197d0c8d.bounds.extend( gmap\_m40c04b78a8f7327355463a45197d0c8d.positions[m] );
}
// Render markers
for ( var m in gmap\_m40c04b78a8f7327355463a45197d0c8d.positions ) {
gmap\_m40c04b78a8f7327355463a45197d0c8d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m40c04b78a8f7327355463a45197d0c8d.map,
position : gmap\_m40c04b78a8f7327355463a45197d0c8d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m40c04b78a8f7327355463a45197d0c8d.map.setCenter( gmap\_m40c04b78a8f7327355463a45197d0c8d.positions[10] );
});