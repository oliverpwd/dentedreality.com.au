---
title: Me and Ray
date: '2011-06-14T12:17:02+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- ray
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/6323451744_d285fdbaea_o.jpg?resize=607%2C813
---

[![Me and Ray](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/06/6323451744_d285fdbaea_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/06/14/me-and-ray/) 
# [Me and Ray](http://dentedreality.com.au/2011/06/14/me-and-ray/)

At SXSW





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[ray](http://dentedreality.com.au/tags/ray/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323451744/) [12:17 pm, June 14, 2011](http://dentedreality.com.au/2011/06/14/me-and-ray/ "12:17 pm") 
jQuery(document).ready(function(){
var gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff = {
positions : {
239 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.positions ) {
gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.bounds.extend( gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.positions[m] );
}
// Render markers
for ( var m in gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.positions ) {
gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.map,
position : gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.map.setCenter( gmap\_m0bab0ef574a2b93d839ec57b63b8f3ff.positions[239] );
});