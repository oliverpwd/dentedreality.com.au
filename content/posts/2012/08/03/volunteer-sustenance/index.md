---
title: ''
date: '2012-08-03T22:08:44-06:00'
format: image
service: instagram
tags:
- photo
latitude: '37.7552307'
longitude: '-122.4183969'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/08/14191046/51c5e91eddd911e1b1c522000a1e86b4_7.jpg
---

[![Volunteer sustenance.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/08/14191046/51c5e91eddd911e1b1c522000a1e86b4_7.jpg)](https://dentedreality.com.au/2012/08/03/volunteer-sustenance/) 

[![Volunteer sustenance.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/08/14191046/51c5e91eddd911e1b1c522000a1e86b4_7.jpg)](http://instagram.com/p/N44xt4CmBm/)

Volunteer sustenance.

37.7552307-122.4183969




* #[photo](https://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/N44xt4CmBm/) [10:08 pm, August 3, 2012](https://dentedreality.com.au/2012/08/03/volunteer-sustenance/ "10:08 pm") 
jQuery(document).ready(function(){
var gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c = {
positions : {
772 : new google.maps.LatLng( '37.755230703', '-122.418396935' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.positions ) {
gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.bounds.extend( gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.positions[m] );
}
// Render markers
for ( var m in gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.positions ) {
gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.map,
position : gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.map.setCenter( gmap\_m57a5e81ee1367a7c17ad6d152ffa7b7c.positions[772] );
});