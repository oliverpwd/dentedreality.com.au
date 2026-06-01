---
title: ''
date: '2013-11-24T14:16:44+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/92ebc1f6553411e399cf1236f53363c7_8.jpg?resize=640%2C640
---

[![Legit Bloody.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/92ebc1f6553411e399cf1236f53363c7_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/11/24/legit-bloody/) 

Legit Bloody.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/hG2u4SimM1/) [2:16 pm, November 24, 2013](http://dentedreality.com.au/2013/11/24/legit-bloody/ "2:16 pm") 
jQuery(document).ready(function(){
var gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7 = {
positions : {
52 : new google.maps.LatLng( '39.717948906', '-104.987604618' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.positions ) {
gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.bounds.extend( gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.positions[m] );
}
// Render markers
for ( var m in gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.positions ) {
gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.map,
position : gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.map.setCenter( gmap\_mf1b3dc8070789ccab9b3bcc03675f6d7.positions[52] );
});