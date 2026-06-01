---
title: ''
date: '2014-12-19T19:08:37+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10349807_1592315807665619_2125271457_n.jpg?resize=640%2C640
---

[![I guess @wonderboymusic has been here before.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10349807_1592315807665619_2125271457_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/19/i-guess-wonderboymusic-has-been-here-before/) 

I guess @wonderboymusic has been here before.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/wz6wZAimAr/) [7:08 pm, December 19, 2014](http://dentedreality.com.au/2014/12/19/i-guess-wonderboymusic-has-been-here-before/ "7:08 pm") 
jQuery(document).ready(function(){
var gmap\_m71c5b223d0c615996889d9dfc080a73e = {
positions : {
728 : new google.maps.LatLng( '40.721008151', '-73.997675974' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m71c5b223d0c615996889d9dfc080a73e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m71c5b223d0c615996889d9dfc080a73e.positions ) {
gmap\_m71c5b223d0c615996889d9dfc080a73e.bounds.extend( gmap\_m71c5b223d0c615996889d9dfc080a73e.positions[m] );
}
// Render markers
for ( var m in gmap\_m71c5b223d0c615996889d9dfc080a73e.positions ) {
gmap\_m71c5b223d0c615996889d9dfc080a73e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m71c5b223d0c615996889d9dfc080a73e.map,
position : gmap\_m71c5b223d0c615996889d9dfc080a73e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m71c5b223d0c615996889d9dfc080a73e.map.setCenter( gmap\_m71c5b223d0c615996889d9dfc080a73e.positions[728] );
});