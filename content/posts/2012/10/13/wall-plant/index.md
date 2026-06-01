---
title: Wall Plant
date: '2012-10-13T12:53:49+00:00'
format: image
service: flickr
tags:
- cute
- feature
- plant
- wall
image: http://dentedreality.com.au/wp-content/uploads/2012/10/8244795813_e0f509c112_o-764x1024.jpg
---

[![Wall Plant](http://dentedreality.com.au/wp-content/uploads/2012/10/8244795813_e0f509c112_o-764x1024.jpg)](https://dentedreality.com.au/2012/10/13/wall-plant/) 
# [Wall Plant](https://dentedreality.com.au/2012/10/13/wall-plant/)

[![Wall Plant](http://dentedreality.com.au/wp-content/uploads/2012/10/8244795813_e0f509c112_o-764x1024.jpg)](http://www.flickr.com/photos/borkazoid/8244795813/)





* #[cute](https://dentedreality.com.au/tags/cute/)
* #[feature](https://dentedreality.com.au/tags/feature/)
* #[plant](https://dentedreality.com.au/tags/plant/)
* #[wall](https://dentedreality.com.au/tags/wall/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244795813/) [12:53 pm, October 13, 2012](https://dentedreality.com.au/2012/10/13/wall-plant/ "12:53 pm") 
jQuery(document).ready(function(){
var gmap\_m1ef997de4cbc454aebd440f79309dc13 = {
positions : {
625 : new google.maps.LatLng( '40.664', '-73.987334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1ef997de4cbc454aebd440f79309dc13' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1ef997de4cbc454aebd440f79309dc13.positions ) {
gmap\_m1ef997de4cbc454aebd440f79309dc13.bounds.extend( gmap\_m1ef997de4cbc454aebd440f79309dc13.positions[m] );
}
// Render markers
for ( var m in gmap\_m1ef997de4cbc454aebd440f79309dc13.positions ) {
gmap\_m1ef997de4cbc454aebd440f79309dc13.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1ef997de4cbc454aebd440f79309dc13.map,
position : gmap\_m1ef997de4cbc454aebd440f79309dc13.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1ef997de4cbc454aebd440f79309dc13.map.setCenter( gmap\_m1ef997de4cbc454aebd440f79309dc13.positions[625] );
});