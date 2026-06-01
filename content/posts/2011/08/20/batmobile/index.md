---
title: Batmobile
date: '2011-08-20T15:19:07-06:00'
format: image
service: flickr
tags:
- black
- bmw
latitude: '37.789833'
longitude: '-122.420667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/08/14190307/6323520864_26d7c04c47_o.jpg
---

[![Batmobile](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/08/14190307/6323520864_26d7c04c47_o.jpg)](https://dentedreality.com.au/2011/08/20/batmobile/) 
# [Batmobile](https://dentedreality.com.au/2011/08/20/batmobile/)

[![Batmobile](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/08/14190307/6323520864_26d7c04c47_o.jpg)](http://www.flickr.com/photos/borkazoid/6323520864/)

Awesome matte black BMW on Polk.

37.789833-122.420667




* #[black](https://dentedreality.com.au/tags/black/)
* #[bmw](https://dentedreality.com.au/tags/bmw/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323520864/) [3:19 pm, August 20, 2011](https://dentedreality.com.au/2011/08/20/batmobile/ "3:19 pm") 
jQuery(document).ready(function(){
var gmap\_meb72038dc3932eb8ec1abc2c58023639 = {
positions : {
310 : new google.maps.LatLng( '37.789833', '-122.420667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meb72038dc3932eb8ec1abc2c58023639' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meb72038dc3932eb8ec1abc2c58023639.positions ) {
gmap\_meb72038dc3932eb8ec1abc2c58023639.bounds.extend( gmap\_meb72038dc3932eb8ec1abc2c58023639.positions[m] );
}
// Render markers
for ( var m in gmap\_meb72038dc3932eb8ec1abc2c58023639.positions ) {
gmap\_meb72038dc3932eb8ec1abc2c58023639.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meb72038dc3932eb8ec1abc2c58023639.map,
position : gmap\_meb72038dc3932eb8ec1abc2c58023639.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meb72038dc3932eb8ec1abc2c58023639.map.setCenter( gmap\_meb72038dc3932eb8ec1abc2c58023639.positions[310] );
});