---
title: ''
date: '2016-09-10T18:16:51+00:00'
format: image
service: instagram
tags:
- 14er
- grayspeak
- torreyspeak
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14309794_1254426704609254_516670059_n.jpg?fit=640%2C640
---

[![Today's hike: our 2nd AND 3rd #14er. #grayspeak and #torreyspeak.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14309794_1254426704609254_516670059_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/10/todays-hike-our-2nd-and-3rd-14er-grayspeak-and-torreyspeak/) 

Today’s hike: our 2nd AND 3rd #14er. #grayspeak and #torreyspeak.





* #[14er](http://dentedreality.com.au/tags/14er/)
* #[grayspeak](http://dentedreality.com.au/tags/grayspeak/)
* #[torreyspeak](http://dentedreality.com.au/tags/torreyspeak/)

Posted on [Instagram](https://www.instagram.com/p/BKMfj3UAEVp/) [6:16 pm, September 10, 2016](http://dentedreality.com.au/2016/09/10/todays-hike-our-2nd-and-3rd-14er-grayspeak-and-torreyspeak/ "6:16 pm") 
jQuery(document).ready(function(){
var gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a = {
positions : {
59 : new google.maps.LatLng( '39.642777777778', '-105.82111111111' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.positions ) {
gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.bounds.extend( gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.positions[m] );
}
// Render markers
for ( var m in gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.positions ) {
gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.map,
position : gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.map.setCenter( gmap\_mee9aeeffb7079e6fa9f9053c0a4aa62a.positions[59] );
});