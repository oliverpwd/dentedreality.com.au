---
title: ''
date: '2016-01-21T20:59:36+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12545409_928277220574273_589491920_n.jpg?fit=640%2C640
---

[![Denver Rodeo!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12545409_928277220574273_589491920_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/01/21/denver-rodeo/) 

Denver Rodeo!





Posted on [Instagram](https://www.instagram.com/p/BA071duimAM/) [8:59 pm, January 21, 2016](http://dentedreality.com.au/2016/01/21/denver-rodeo/ "8:59 pm") 
jQuery(document).ready(function(){
var gmap\_m57645cee9a2637778ebf901b0cc11157 = {
positions : {
820 : new google.maps.LatLng( '39.779132714', '-104.970766349' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m57645cee9a2637778ebf901b0cc11157' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m57645cee9a2637778ebf901b0cc11157.positions ) {
gmap\_m57645cee9a2637778ebf901b0cc11157.bounds.extend( gmap\_m57645cee9a2637778ebf901b0cc11157.positions[m] );
}
// Render markers
for ( var m in gmap\_m57645cee9a2637778ebf901b0cc11157.positions ) {
gmap\_m57645cee9a2637778ebf901b0cc11157.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m57645cee9a2637778ebf901b0cc11157.map,
position : gmap\_m57645cee9a2637778ebf901b0cc11157.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m57645cee9a2637778ebf901b0cc11157.map.setCenter( gmap\_m57645cee9a2637778ebf901b0cc11157.positions[820] );
});