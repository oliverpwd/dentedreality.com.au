---
title: ''
date: '2015-09-22T16:11:29+00:00'
format: image
service: instagram
tags:
- clouds
- sky
- tree
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11849456_515682915261506_1510556947_n.jpg?resize=640%2C640
---

[![Backyard vibes #sky #clouds #tree](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11849456_515682915261506_1510556947_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/09/22/backyard-vibes-sky-clouds-tree/) 

Backyard vibes #sky #clouds #tree





* #[clouds](http://dentedreality.com.au/tags/clouds/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[tree](http://dentedreality.com.au/tags/tree/)

Posted on [Instagram](https://instagram.com/p/78vz50CmD4/) [4:11 pm, September 22, 2015](http://dentedreality.com.au/2015/09/22/backyard-vibes-sky-clouds-tree/ "4:11 pm") 
jQuery(document).ready(function(){
var gmap\_m4ea5caadd7fdf65664f0b343c381f1fc = {
positions : {
331 : new google.maps.LatLng( '39.7392', '-104.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4ea5caadd7fdf65664f0b343c381f1fc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.positions ) {
gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.bounds.extend( gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.positions[m] );
}
// Render markers
for ( var m in gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.positions ) {
gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.map,
position : gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.map.setCenter( gmap\_m4ea5caadd7fdf65664f0b343c381f1fc.positions[331] );
});