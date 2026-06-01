---
title: ''
date: '2014-11-28T17:34:40+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10809798_836747483050426_125438873_n1.jpg?resize=640%2C640
---

[![Nice work on the sunset, Colorado!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10809798_836747483050426_125438873_n1.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/28/nice-work-on-the-sunset-colorado/) 

Nice work on the sunset, Colorado!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/v9rTz8CmPw/) [5:34 pm, November 28, 2014](http://dentedreality.com.au/2014/11/28/nice-work-on-the-sunset-colorado/ "5:34 pm") 
jQuery(document).ready(function(){
var gmap\_m5871b5e5198b82f8c5169acda277d09a = {
positions : {
850 : new google.maps.LatLng( '39.73473', '-104.978486667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5871b5e5198b82f8c5169acda277d09a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5871b5e5198b82f8c5169acda277d09a.positions ) {
gmap\_m5871b5e5198b82f8c5169acda277d09a.bounds.extend( gmap\_m5871b5e5198b82f8c5169acda277d09a.positions[m] );
}
// Render markers
for ( var m in gmap\_m5871b5e5198b82f8c5169acda277d09a.positions ) {
gmap\_m5871b5e5198b82f8c5169acda277d09a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5871b5e5198b82f8c5169acda277d09a.map,
position : gmap\_m5871b5e5198b82f8c5169acda277d09a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5871b5e5198b82f8c5169acda277d09a.map.setCenter( gmap\_m5871b5e5198b82f8c5169acda277d09a.positions[850] );
});