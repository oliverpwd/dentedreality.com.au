---
title: ''
date: '2014-12-25T20:06:55+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10864900_549398041861952_633682571_n.jpg?resize=640%2C640
---

[![This morning it was clear and sunny. It's a Christmas miracle (of crazy weather)](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10864900_549398041861952_633682571_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/25/this-morning-it-was-clear-and-sunny-its-a-christmas-miracle-of-crazy-weather/) 

This morning it was clear and sunny. It’s a Christmas miracle (of crazy weather)





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/xDeMmNCmOX/) [8:06 pm, December 25, 2014](http://dentedreality.com.au/2014/12/25/this-morning-it-was-clear-and-sunny-its-a-christmas-miracle-of-crazy-weather/ "8:06 pm") 
jQuery(document).ready(function(){
var gmap\_m448b6f1a5709514347235b9950ad1e22 = {
positions : {
573 : new google.maps.LatLng( '39.747285927', '-105.019419198' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m448b6f1a5709514347235b9950ad1e22' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m448b6f1a5709514347235b9950ad1e22.positions ) {
gmap\_m448b6f1a5709514347235b9950ad1e22.bounds.extend( gmap\_m448b6f1a5709514347235b9950ad1e22.positions[m] );
}
// Render markers
for ( var m in gmap\_m448b6f1a5709514347235b9950ad1e22.positions ) {
gmap\_m448b6f1a5709514347235b9950ad1e22.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m448b6f1a5709514347235b9950ad1e22.map,
position : gmap\_m448b6f1a5709514347235b9950ad1e22.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m448b6f1a5709514347235b9950ad1e22.map.setCenter( gmap\_m448b6f1a5709514347235b9950ad1e22.positions[573] );
});