---
title: Sushi
date: '2011-09-02T16:39:21-06:00'
format: image
service: flickr
tags:
- sushi
latitude: '37.790833'
longitude: '-122.420834'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190309/6323523312_39c7ff686f_o.jpg
---

[![Sushi](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190309/6323523312_39c7ff686f_o.jpg)](https://dentedreality.com.au/2011/09/02/sushi/) 
# [Sushi](https://dentedreality.com.au/2011/09/02/sushi/)

[![Sushi](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190309/6323523312_39c7ff686f_o.jpg)](http://www.flickr.com/photos/borkazoid/6323523312/)

37.790833-122.420834




* #[sushi](https://dentedreality.com.au/tags/sushi/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323523312/) [4:39 pm, September 2, 2011](https://dentedreality.com.au/2011/09/02/sushi/ "4:39 pm") 
jQuery(document).ready(function(){
var gmap\_m65b22058f050fa06406ab5d1c51be035 = {
positions : {
15 : new google.maps.LatLng( '37.790833', '-122.420834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m65b22058f050fa06406ab5d1c51be035' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m65b22058f050fa06406ab5d1c51be035.positions ) {
gmap\_m65b22058f050fa06406ab5d1c51be035.bounds.extend( gmap\_m65b22058f050fa06406ab5d1c51be035.positions[m] );
}
// Render markers
for ( var m in gmap\_m65b22058f050fa06406ab5d1c51be035.positions ) {
gmap\_m65b22058f050fa06406ab5d1c51be035.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m65b22058f050fa06406ab5d1c51be035.map,
position : gmap\_m65b22058f050fa06406ab5d1c51be035.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m65b22058f050fa06406ab5d1c51be035.map.setCenter( gmap\_m65b22058f050fa06406ab5d1c51be035.positions[15] );
});