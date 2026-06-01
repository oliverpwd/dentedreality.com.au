---
title: Jackolanterns!
date: '2010-10-24T13:56:21-06:00'
format: image
service: flickr
tags:
- halloween
- jackolantern
- pumpkin
- wordpress
latitude: '37.795666'
longitude: '-122.425167'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/10/14185840/5183767570_4a18c58fa9_o.jpg
---

[![Jackolanterns!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/10/14185840/5183767570_4a18c58fa9_o.jpg)](https://dentedreality.com.au/2010/10/24/jackolanterns/) 
# [Jackolanterns!](https://dentedreality.com.au/2010/10/24/jackolanterns/)

[![Jackolanterns!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/10/14185840/5183767570_4a18c58fa9_o.jpg)](http://www.flickr.com/photos/borkazoid/5183767570/)

37.795666-122.425167




* #[halloween](https://dentedreality.com.au/tags/halloween/)
* #[jackolantern](https://dentedreality.com.au/tags/jackolantern/)
* #[pumpkin](https://dentedreality.com.au/tags/pumpkin/)
* #[wordpress](https://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183767570/) [1:56 pm, October 24, 2010](https://dentedreality.com.au/2010/10/24/jackolanterns/ "1:56 pm") 
jQuery(document).ready(function(){
var gmap\_m4608ba6e8bdb5249e9c2ade3d9564908 = {
positions : {
774 : new google.maps.LatLng( '37.795666', '-122.425167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4608ba6e8bdb5249e9c2ade3d9564908' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.positions ) {
gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.bounds.extend( gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.positions[m] );
}
// Render markers
for ( var m in gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.positions ) {
gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.map,
position : gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.map.setCenter( gmap\_m4608ba6e8bdb5249e9c2ade3d9564908.positions[774] );
});