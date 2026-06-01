---
title: Jetpack!
date: '2011-08-12T06:41:11+00:00'
format: image
service: flickr
tags:
- automattic
- jetpack
- wcsf
- wordcampsf
- wordpress
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323519052_3b6ce2c22b_o.jpg?resize=607%2C452
---

[![Jetpack!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323519052_3b6ce2c22b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/08/12/jetpack-2/) 
# [Jetpack!](http://dentedreality.com.au/2011/08/12/jetpack-2/)

Jetpack booth/stand at WordCampSF





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[jetpack](http://dentedreality.com.au/tags/jetpack/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wordcampsf](http://dentedreality.com.au/tags/wordcampsf/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323519052/) [6:41 am, August 12, 2011](http://dentedreality.com.au/2011/08/12/jetpack-2/ "6:41 am") 
jQuery(document).ready(function(){
var gmap\_m871580a02508c0f6e2413fcce0a8d145 = {
positions : {
852 : new google.maps.LatLng( '37.768', '-122.392834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m871580a02508c0f6e2413fcce0a8d145' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m871580a02508c0f6e2413fcce0a8d145.positions ) {
gmap\_m871580a02508c0f6e2413fcce0a8d145.bounds.extend( gmap\_m871580a02508c0f6e2413fcce0a8d145.positions[m] );
}
// Render markers
for ( var m in gmap\_m871580a02508c0f6e2413fcce0a8d145.positions ) {
gmap\_m871580a02508c0f6e2413fcce0a8d145.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m871580a02508c0f6e2413fcce0a8d145.map,
position : gmap\_m871580a02508c0f6e2413fcce0a8d145.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m871580a02508c0f6e2413fcce0a8d145.map.setCenter( gmap\_m871580a02508c0f6e2413fcce0a8d145.positions[852] );
});