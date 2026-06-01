---
title: ''
date: '2015-01-24T14:51:38+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10948713_1602741043296248_697664784_n.jpg?resize=640%2C640
---

[![Product of today's meetup.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10948713_1602741043296248_697664784_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/01/24/product-of-todays-meetup/) 

Product of today’s meetup.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/yQJ9nPCmDZ/) [2:51 pm, January 24, 2015](http://dentedreality.com.au/2015/01/24/product-of-todays-meetup/ "2:51 pm") 
jQuery(document).ready(function(){
var gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918 = {
positions : {
364 : new google.maps.LatLng( '39.735538333', '-104.945816667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.positions ) {
gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.bounds.extend( gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.positions ) {
gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.map,
position : gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.map.setCenter( gmap\_m3c6e24de5b1d0fac42ce5ef1b4ab6918.positions[364] );
});