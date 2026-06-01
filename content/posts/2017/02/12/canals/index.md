---
title: ''
date: '2017-02-12T17:19:05+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16464243_781587468658055_8821088542164779008_n.jpg?fit=640%2C640
---

[![Canals.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16464243_781587468658055_8821088542164779008_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/12/canals/) 

Canals.





Posted on [Instagram](https://www.instagram.com/p/BQbnB2cjL7A/) [5:19 pm, February 12, 2017](http://dentedreality.com.au/2017/02/12/canals/ "5:19 pm") 
jQuery(document).ready(function(){
var gmap\_m4b468848a0cc94c959bcdaa1140edba7 = {
positions : {
142 : new google.maps.LatLng( '52.3731', '4.8922' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4b468848a0cc94c959bcdaa1140edba7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4b468848a0cc94c959bcdaa1140edba7.positions ) {
gmap\_m4b468848a0cc94c959bcdaa1140edba7.bounds.extend( gmap\_m4b468848a0cc94c959bcdaa1140edba7.positions[m] );
}
// Render markers
for ( var m in gmap\_m4b468848a0cc94c959bcdaa1140edba7.positions ) {
gmap\_m4b468848a0cc94c959bcdaa1140edba7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4b468848a0cc94c959bcdaa1140edba7.map,
position : gmap\_m4b468848a0cc94c959bcdaa1140edba7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4b468848a0cc94c959bcdaa1140edba7.map.setCenter( gmap\_m4b468848a0cc94c959bcdaa1140edba7.positions[142] );
});