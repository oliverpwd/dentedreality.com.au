---
title: ''
date: '2014-04-27T10:25:43+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10254228_231522107046711_446851925_n.jpg?resize=640%2C640
---

[![The Quays](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10254228_231522107046711_446851925_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/27/the-quays/) 

The Quays





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/nTFlESCmEg/) [10:25 am, April 27, 2014](http://dentedreality.com.au/2014/04/27/the-quays/ "10:25 am") 
jQuery(document).ready(function(){
var gmap\_mc13de695a532a203c9f82fac026d70e3 = {
positions : {
41 : new google.maps.LatLng( '53.3455693', '-6.263109778' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc13de695a532a203c9f82fac026d70e3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc13de695a532a203c9f82fac026d70e3.positions ) {
gmap\_mc13de695a532a203c9f82fac026d70e3.bounds.extend( gmap\_mc13de695a532a203c9f82fac026d70e3.positions[m] );
}
// Render markers
for ( var m in gmap\_mc13de695a532a203c9f82fac026d70e3.positions ) {
gmap\_mc13de695a532a203c9f82fac026d70e3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc13de695a532a203c9f82fac026d70e3.map,
position : gmap\_mc13de695a532a203c9f82fac026d70e3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc13de695a532a203c9f82fac026d70e3.map.setCenter( gmap\_mc13de695a532a203c9f82fac026d70e3.positions[41] );
});