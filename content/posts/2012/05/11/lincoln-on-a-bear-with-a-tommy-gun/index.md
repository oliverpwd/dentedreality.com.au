---
title: Lincoln, on a Bear, with a Tommy Gun
date: '2012-05-11T17:39:46-06:00'
format: image
service: flickr
tags:
- bear
- lincoln
- machinegun
- painting
- tommygun
latitude: '37.797333'
longitude: '-122.410167'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/05/14190611/7770795950_6f202fddd3_o-1024x764.jpg?resize=607%2C452&ssl=1
---

[![Lincoln, on a Bear, with a Tommy Gun](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/05/14190611/7770795950_6f202fddd3_o-1024x764.jpg?resize=607%2C452&ssl=1)](https://dentedreality.com.au/2012/05/11/lincoln-on-a-bear-with-a-tommy-gun/) 
# [Lincoln, on a Bear, with a Tommy Gun](https://dentedreality.com.au/2012/05/11/lincoln-on-a-bear-with-a-tommy-gun/)

[![Lincoln, on a Bear, with a Tommy Gun](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/05/14190611/7770795950_6f202fddd3_o-1024x764.jpg?resize=607%2C452&ssl=1)](http://www.flickr.com/photos/borkazoid/7770795950/)

37.797333-122.410167




* #[bear](https://dentedreality.com.au/tags/bear/)
* #[lincoln](https://dentedreality.com.au/tags/lincoln/)
* #[machinegun](https://dentedreality.com.au/tags/machinegun/)
* #[painting](https://dentedreality.com.au/tags/painting/)
* #[tommygun](https://dentedreality.com.au/tags/tommygun/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770795950/) [5:39 pm, May 11, 2012](https://dentedreality.com.au/2012/05/11/lincoln-on-a-bear-with-a-tommy-gun/ "5:39 pm") 
jQuery(document).ready(function(){
var gmap\_mf97b4929d251061c0b86949f9d5d1f7d = {
positions : {
504 : new google.maps.LatLng( '37.797333', '-122.410167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf97b4929d251061c0b86949f9d5d1f7d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf97b4929d251061c0b86949f9d5d1f7d.positions ) {
gmap\_mf97b4929d251061c0b86949f9d5d1f7d.bounds.extend( gmap\_mf97b4929d251061c0b86949f9d5d1f7d.positions[m] );
}
// Render markers
for ( var m in gmap\_mf97b4929d251061c0b86949f9d5d1f7d.positions ) {
gmap\_mf97b4929d251061c0b86949f9d5d1f7d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf97b4929d251061c0b86949f9d5d1f7d.map,
position : gmap\_mf97b4929d251061c0b86949f9d5d1f7d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf97b4929d251061c0b86949f9d5d1f7d.map.setCenter( gmap\_mf97b4929d251061c0b86949f9d5d1f7d.positions[504] );
});