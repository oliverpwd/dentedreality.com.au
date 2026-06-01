---
title: ''
date: '2016-02-03T22:28:51+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12598983_919176704819767_767886471_n.jpg?fit=640%2C640
---

[![Belize](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12598983_919176704819767_767886471_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/02/03/belize/) 

Belize





Posted on [Instagram](https://www.instagram.com/p/BBWkYj2imHB/) [10:28 pm, February 3, 2016](http://dentedreality.com.au/2016/02/03/belize/ "10:28 pm") 
jQuery(document).ready(function(){
var gmap\_m1b9a4f44ffdfd25a98541973781e9960 = {
positions : {
418 : new google.maps.LatLng( '17.960086941', '-87.934275823' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1b9a4f44ffdfd25a98541973781e9960' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1b9a4f44ffdfd25a98541973781e9960.positions ) {
gmap\_m1b9a4f44ffdfd25a98541973781e9960.bounds.extend( gmap\_m1b9a4f44ffdfd25a98541973781e9960.positions[m] );
}
// Render markers
for ( var m in gmap\_m1b9a4f44ffdfd25a98541973781e9960.positions ) {
gmap\_m1b9a4f44ffdfd25a98541973781e9960.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1b9a4f44ffdfd25a98541973781e9960.map,
position : gmap\_m1b9a4f44ffdfd25a98541973781e9960.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1b9a4f44ffdfd25a98541973781e9960.map.setCenter( gmap\_m1b9a4f44ffdfd25a98541973781e9960.positions[418] );
});