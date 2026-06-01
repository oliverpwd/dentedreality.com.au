---
title: ''
date: '2014-02-17T09:24:05+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/191ec38a97df11e39f6712f215cd2394_8.jpg?resize=640%2C640
---

[![Awesome; some kids built an igloo in their front yard.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/191ec38a97df11e39f6712f215cd2394_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/02/17/awesome-some-kids-built-an-igloo-in-their-front-yard/) 

Awesome; some kids built an igloo in their front yard.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/khTrQJimDY/) [9:24 am, February 17, 2014](http://dentedreality.com.au/2014/02/17/awesome-some-kids-built-an-igloo-in-their-front-yard/ "9:24 am") 
jQuery(document).ready(function(){
var gmap\_m09b584140f262f626d7818fb86c79846 = {
positions : {
190 : new google.maps.LatLng( '40.665913333', '-73.97767' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m09b584140f262f626d7818fb86c79846' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m09b584140f262f626d7818fb86c79846.positions ) {
gmap\_m09b584140f262f626d7818fb86c79846.bounds.extend( gmap\_m09b584140f262f626d7818fb86c79846.positions[m] );
}
// Render markers
for ( var m in gmap\_m09b584140f262f626d7818fb86c79846.positions ) {
gmap\_m09b584140f262f626d7818fb86c79846.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m09b584140f262f626d7818fb86c79846.map,
position : gmap\_m09b584140f262f626d7818fb86c79846.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m09b584140f262f626d7818fb86c79846.map.setCenter( gmap\_m09b584140f262f626d7818fb86c79846.positions[190] );
});