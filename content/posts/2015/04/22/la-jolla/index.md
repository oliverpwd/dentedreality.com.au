---
title: ''
date: '2015-04-22T12:52:05+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/04/11111447_1577960865825057_1730997086_n.jpg?resize=640%2C640
---

[![La Jolla](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/04/11111447_1577960865825057_1730997086_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/04/22/la-jolla/) 

La Jolla





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/1ybXjfimBr/) [12:52 pm, April 22, 2015](http://dentedreality.com.au/2015/04/22/la-jolla/ "12:52 pm") 
jQuery(document).ready(function(){
var gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab = {
positions : {
650 : new google.maps.LatLng( '32.842471667', '-117.25927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.positions ) {
gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.bounds.extend( gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.positions[m] );
}
// Render markers
for ( var m in gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.positions ) {
gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.map,
position : gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.map.setCenter( gmap\_m3fd192a86e7e7b8b9d4ab6c035dfc8ab.positions[650] );
});