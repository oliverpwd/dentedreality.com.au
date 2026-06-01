---
title: ''
date: '2017-04-21T19:00:52-06:00'
format: image
service: instagram
tags:
- jetpack
latitude: '35.0805111'
longitude: '-106.6239609'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/18011914_1913521032250714_1368001909033533440_n.jpg?fit=640%2C640
---

[![#jetpack meetup with the local @wordpress crew](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/18011914_1913521032250714_1368001909033533440_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/04/21/jetpack-meetup-with-the-local-wordpress-crew/) 

[![#jetpack meetup with the local @wordpress crew](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/18011914_1913521032250714_1368001909033533440_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BTKx3XIhnip/)

#jetpack meetup with the local @wordpress crew

35.0805111-106.6239609




* #[jetpack](https://dentedreality.com.au/tags/jetpack/)

Posted on [Instagram](https://www.instagram.com/p/BTKx3XIhnip/) [7:00 pm, April 21, 2017](https://dentedreality.com.au/2017/04/21/jetpack-meetup-with-the-local-wordpress-crew/ "7:00 pm") 
jQuery(document).ready(function(){
var gmap\_m94857d6f6226018f0d78a35fdd23314c = {
positions : {
931 : new google.maps.LatLng( '35.080511066667', '-106.6239609' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m94857d6f6226018f0d78a35fdd23314c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m94857d6f6226018f0d78a35fdd23314c.positions ) {
gmap\_m94857d6f6226018f0d78a35fdd23314c.bounds.extend( gmap\_m94857d6f6226018f0d78a35fdd23314c.positions[m] );
}
// Render markers
for ( var m in gmap\_m94857d6f6226018f0d78a35fdd23314c.positions ) {
gmap\_m94857d6f6226018f0d78a35fdd23314c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m94857d6f6226018f0d78a35fdd23314c.map,
position : gmap\_m94857d6f6226018f0d78a35fdd23314c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m94857d6f6226018f0d78a35fdd23314c.map.setCenter( gmap\_m94857d6f6226018f0d78a35fdd23314c.positions[931] );
});