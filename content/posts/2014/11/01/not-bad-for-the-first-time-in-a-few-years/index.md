---
title: ''
date: '2014-11-01T22:54:48+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10747889_1503682476553144_1932195881_n.jpg?resize=640%2C640
---

[![Not bad for the first time in a few years.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10747889_1503682476553144_1932195881_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/01/not-bad-for-the-first-time-in-a-few-years/) 

Not bad for the first time in a few years.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/u4nncFCmB2/) [10:54 pm, November 1, 2014](http://dentedreality.com.au/2014/11/01/not-bad-for-the-first-time-in-a-few-years/ "10:54 pm") 
jQuery(document).ready(function(){
var gmap\_mbebf635305941bfbd14b0e4a9fe57cf7 = {
positions : {
722 : new google.maps.LatLng( '39.78002775', '-104.915695301' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbebf635305941bfbd14b0e4a9fe57cf7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.positions ) {
gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.bounds.extend( gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.positions[m] );
}
// Render markers
for ( var m in gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.positions ) {
gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.map,
position : gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.map.setCenter( gmap\_mbebf635305941bfbd14b0e4a9fe57cf7.positions[722] );
});