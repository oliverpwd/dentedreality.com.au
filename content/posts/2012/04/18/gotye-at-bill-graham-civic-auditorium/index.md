---
title: Gotye at Bill Graham Civic Auditorium
date: '2012-04-18T18:12:30-06:00'
format: image
service: flickr
tags:
- billgraham
- gotye
- livemusic
- sanfrancisco
latitude: '37.777666'
longitude: '-122.417334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/04/14190603/7770685062_1d24ec3ed7_o.jpg
---

[![Gotye at Bill Graham Civic Auditorium](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/04/14190603/7770685062_1d24ec3ed7_o.jpg)](https://dentedreality.com.au/2012/04/18/gotye-at-bill-graham-civic-auditorium/) 
# [Gotye at Bill Graham Civic Auditorium](https://dentedreality.com.au/2012/04/18/gotye-at-bill-graham-civic-auditorium/)

[![Gotye at Bill Graham Civic Auditorium](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/04/14190603/7770685062_1d24ec3ed7_o.jpg)](http://www.flickr.com/photos/borkazoid/7770685062/)

37.777666-122.417334




* #[billgraham](https://dentedreality.com.au/tags/billgraham/)
* #[gotye](https://dentedreality.com.au/tags/gotye/)
* #[livemusic](https://dentedreality.com.au/tags/livemusic/)
* #[sanfrancisco](https://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770685062/) [6:12 pm, April 18, 2012](https://dentedreality.com.au/2012/04/18/gotye-at-bill-graham-civic-auditorium/ "6:12 pm") 
jQuery(document).ready(function(){
var gmap\_mbff312c22eeb49e7649e17b4b983f4b5 = {
positions : {
545 : new google.maps.LatLng( '37.777666', '-122.417334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbff312c22eeb49e7649e17b4b983f4b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbff312c22eeb49e7649e17b4b983f4b5.positions ) {
gmap\_mbff312c22eeb49e7649e17b4b983f4b5.bounds.extend( gmap\_mbff312c22eeb49e7649e17b4b983f4b5.positions[m] );
}
// Render markers
for ( var m in gmap\_mbff312c22eeb49e7649e17b4b983f4b5.positions ) {
gmap\_mbff312c22eeb49e7649e17b4b983f4b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbff312c22eeb49e7649e17b4b983f4b5.map,
position : gmap\_mbff312c22eeb49e7649e17b4b983f4b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbff312c22eeb49e7649e17b4b983f4b5.map.setCenter( gmap\_mbff312c22eeb49e7649e17b4b983f4b5.positions[545] );
});