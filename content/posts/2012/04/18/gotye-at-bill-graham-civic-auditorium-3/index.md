---
title: Gotye at Bill Graham Civic Auditorium
date: '2012-04-18T17:46:16+00:00'
format: image
service: flickr
tags:
- billgraham
- gotye
- livemusic
- sanfrancisco
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/04/7770684224_5474a41798_o.jpg?resize=607%2C452
---

[![Gotye at Bill Graham Civic Auditorium](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/04/7770684224_5474a41798_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/04/18/gotye-at-bill-graham-civic-auditorium-3/) 
# [Gotye at Bill Graham Civic Auditorium](http://dentedreality.com.au/2012/04/18/gotye-at-bill-graham-civic-auditorium-3/)





* #[billgraham](http://dentedreality.com.au/tags/billgraham/)
* #[gotye](http://dentedreality.com.au/tags/gotye/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770684224/) [5:46 pm, April 18, 2012](http://dentedreality.com.au/2012/04/18/gotye-at-bill-graham-civic-auditorium-3/ "5:46 pm") 
jQuery(document).ready(function(){
var gmap\_m33a30e9c3b49a782c6634f205e119d2a = {
positions : {
575 : new google.maps.LatLng( '37.777666', '-122.417334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m33a30e9c3b49a782c6634f205e119d2a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m33a30e9c3b49a782c6634f205e119d2a.positions ) {
gmap\_m33a30e9c3b49a782c6634f205e119d2a.bounds.extend( gmap\_m33a30e9c3b49a782c6634f205e119d2a.positions[m] );
}
// Render markers
for ( var m in gmap\_m33a30e9c3b49a782c6634f205e119d2a.positions ) {
gmap\_m33a30e9c3b49a782c6634f205e119d2a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m33a30e9c3b49a782c6634f205e119d2a.map,
position : gmap\_m33a30e9c3b49a782c6634f205e119d2a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m33a30e9c3b49a782c6634f205e119d2a.map.setCenter( gmap\_m33a30e9c3b49a782c6634f205e119d2a.positions[575] );
});