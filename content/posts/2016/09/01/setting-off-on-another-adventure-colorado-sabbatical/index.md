---
title: ''
date: '2016-09-01T15:12:42+00:00'
format: image
service: instagram
tags:
- colorado
- sabbatical
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14099258_608039486024710_1265282958_n.jpg?fit=640%2C640
---

[![Setting off on another adventure. #colorado #sabbatical](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14099258_608039486024710_1265282958_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/01/setting-off-on-another-adventure-colorado-sabbatical/) 

Setting off on another adventure. #colorado #sabbatical





* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[sabbatical](http://dentedreality.com.au/tags/sabbatical/)

Posted on [Instagram](https://www.instagram.com/p/BJ0_VNVgvda/) [3:12 pm, September 1, 2016](http://dentedreality.com.au/2016/09/01/setting-off-on-another-adventure-colorado-sabbatical/ "3:12 pm") 
jQuery(document).ready(function(){
var gmap\_ma92f51a3be4b8fb7f081849251e6767b = {
positions : {
748 : new google.maps.LatLng( '39.837212720699', '-106.31039431177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma92f51a3be4b8fb7f081849251e6767b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma92f51a3be4b8fb7f081849251e6767b.positions ) {
gmap\_ma92f51a3be4b8fb7f081849251e6767b.bounds.extend( gmap\_ma92f51a3be4b8fb7f081849251e6767b.positions[m] );
}
// Render markers
for ( var m in gmap\_ma92f51a3be4b8fb7f081849251e6767b.positions ) {
gmap\_ma92f51a3be4b8fb7f081849251e6767b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma92f51a3be4b8fb7f081849251e6767b.map,
position : gmap\_ma92f51a3be4b8fb7f081849251e6767b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma92f51a3be4b8fb7f081849251e6767b.map.setCenter( gmap\_ma92f51a3be4b8fb7f081849251e6767b.positions[748] );
});