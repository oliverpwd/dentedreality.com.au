---
title: Shake Shack!
date: '2011-07-23T11:26:05+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- shakeshack
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6323457402_f1a64d2418_o.jpg?resize=607%2C813
---

[![Shake Shack!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6323457402_f1a64d2418_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/07/23/shake-shack-2/) 
# [Shake Shack!](http://dentedreality.com.au/2011/07/23/shake-shack-2/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[shakeshack](http://dentedreality.com.au/tags/shakeshack/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323457402/) [11:26 am, July 23, 2011](http://dentedreality.com.au/2011/07/23/shake-shack-2/ "11:26 am") 
jQuery(document).ready(function(){
var gmap\_m17f90725e3a82fa16966030d712a96e0 = {
positions : {
155 : new google.maps.LatLng( '40.741666', '-73.988334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m17f90725e3a82fa16966030d712a96e0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m17f90725e3a82fa16966030d712a96e0.positions ) {
gmap\_m17f90725e3a82fa16966030d712a96e0.bounds.extend( gmap\_m17f90725e3a82fa16966030d712a96e0.positions[m] );
}
// Render markers
for ( var m in gmap\_m17f90725e3a82fa16966030d712a96e0.positions ) {
gmap\_m17f90725e3a82fa16966030d712a96e0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m17f90725e3a82fa16966030d712a96e0.map,
position : gmap\_m17f90725e3a82fa16966030d712a96e0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m17f90725e3a82fa16966030d712a96e0.map.setCenter( gmap\_m17f90725e3a82fa16966030d712a96e0.positions[155] );
});