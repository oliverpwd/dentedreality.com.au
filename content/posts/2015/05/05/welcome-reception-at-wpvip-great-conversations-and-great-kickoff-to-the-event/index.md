---
title: ''
date: '2015-05-05T16:15:52+00:00'
format: image
service: instagram
tags:
- photo
- wpvip
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11199440_896315847116670_1740172295_n.jpg?resize=640%2C640
---

[![Welcome reception at #wpvip. Great conversations and great kickoff to the event.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11199440_896315847116670_1740172295_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/05/welcome-reception-at-wpvip-great-conversations-and-great-kickoff-to-the-event/) 

Welcome reception at #wpvip. Great conversations and great kickoff to the event.





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wpvip](http://dentedreality.com.au/tags/wpvip/)

Posted on [Instagram](https://instagram.com/p/2URBg0imKE/) [4:15 pm, May 5, 2015](http://dentedreality.com.au/2015/05/05/welcome-reception-at-wpvip-great-conversations-and-great-kickoff-to-the-event/ "4:15 pm") 
jQuery(document).ready(function(){
var gmap\_mf8b17b4ee5185322b2ff7693cf97593c = {
positions : {
659 : new google.maps.LatLng( '38.256673012', '-122.333844107' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf8b17b4ee5185322b2ff7693cf97593c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf8b17b4ee5185322b2ff7693cf97593c.positions ) {
gmap\_mf8b17b4ee5185322b2ff7693cf97593c.bounds.extend( gmap\_mf8b17b4ee5185322b2ff7693cf97593c.positions[m] );
}
// Render markers
for ( var m in gmap\_mf8b17b4ee5185322b2ff7693cf97593c.positions ) {
gmap\_mf8b17b4ee5185322b2ff7693cf97593c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf8b17b4ee5185322b2ff7693cf97593c.map,
position : gmap\_mf8b17b4ee5185322b2ff7693cf97593c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf8b17b4ee5185322b2ff7693cf97593c.map.setCenter( gmap\_mf8b17b4ee5185322b2ff7693cf97593c.positions[659] );
});