---
title: Geographer
date: '2012-03-03T20:09:04+00:00'
format: image
service: flickr
tags:
- band
- geographer
- livemusic
- music
- theindependent
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/6813467292_4ae7b3f060_o.jpg?resize=607%2C452
---

[![Geographer](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/6813467292_4ae7b3f060_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/03/geographer-2/) 
# [Geographer](http://dentedreality.com.au/2012/03/03/geographer-2/)

At The Independent





* #[band](http://dentedreality.com.au/tags/band/)
* #[geographer](http://dentedreality.com.au/tags/geographer/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[theindependent](http://dentedreality.com.au/tags/theindependent/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813467292/) [8:09 pm, March 3, 2012](http://dentedreality.com.au/2012/03/03/geographer-2/ "8:09 pm") 
jQuery(document).ready(function(){
var gmap\_m8f189f81014e94225af2f8e031bfa1c7 = {
positions : {
463 : new google.maps.LatLng( '37.775666', '-122.437667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8f189f81014e94225af2f8e031bfa1c7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8f189f81014e94225af2f8e031bfa1c7.positions ) {
gmap\_m8f189f81014e94225af2f8e031bfa1c7.bounds.extend( gmap\_m8f189f81014e94225af2f8e031bfa1c7.positions[m] );
}
// Render markers
for ( var m in gmap\_m8f189f81014e94225af2f8e031bfa1c7.positions ) {
gmap\_m8f189f81014e94225af2f8e031bfa1c7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8f189f81014e94225af2f8e031bfa1c7.map,
position : gmap\_m8f189f81014e94225af2f8e031bfa1c7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8f189f81014e94225af2f8e031bfa1c7.map.setCenter( gmap\_m8f189f81014e94225af2f8e031bfa1c7.positions[463] );
});