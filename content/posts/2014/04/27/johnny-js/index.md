---
title: ''
date: '2014-04-27T05:50:35+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/b4efec44cdf911e3a1ce0002c9c613c0_8.jpg?resize=640%2C640
---

[![Johnny J's](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/b4efec44cdf911e3a1ce0002c9c613c0_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/27/johnny-js/) 

Johnny J’s





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/nSmGAKCmJN/) [5:50 am, April 27, 2014](http://dentedreality.com.au/2014/04/27/johnny-js/ "5:50 am") 
jQuery(document).ready(function(){
var gmap\_m398223824fcda028483767b8418984ad = {
positions : {
213 : new google.maps.LatLng( '53.348138889', '-6.277158887' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m398223824fcda028483767b8418984ad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m398223824fcda028483767b8418984ad.positions ) {
gmap\_m398223824fcda028483767b8418984ad.bounds.extend( gmap\_m398223824fcda028483767b8418984ad.positions[m] );
}
// Render markers
for ( var m in gmap\_m398223824fcda028483767b8418984ad.positions ) {
gmap\_m398223824fcda028483767b8418984ad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m398223824fcda028483767b8418984ad.map,
position : gmap\_m398223824fcda028483767b8418984ad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m398223824fcda028483767b8418984ad.map.setCenter( gmap\_m398223824fcda028483767b8418984ad.positions[213] );
});