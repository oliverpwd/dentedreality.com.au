---
title: Harriman State Park
date: '2013-09-01T07:34:08+00:00'
format: image
tags:
- backpacking
- harriman
- harrimanstatepark
- hiking
- newyork
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/9767906635_30afa561f3_o.jpg?resize=607%2C452
---

[![Harriman State Park](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/9767906635_30afa561f3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/09/01/harriman-state-park-2/) 
# [Harriman State Park](http://dentedreality.com.au/2013/09/01/harriman-state-park-2/)





* #[backpacking](http://dentedreality.com.au/tags/backpacking/)
* #[harriman](http://dentedreality.com.au/tags/harriman/)
* #[harrimanstatepark](http://dentedreality.com.au/tags/harrimanstatepark/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767906635/) [7:34 am, September 1, 2013](http://dentedreality.com.au/2013/09/01/harriman-state-park-2/ "7:34 am") 
jQuery(document).ready(function(){
var gmap\_m8d55152af87d3e5667b1710419fbf5c0 = {
positions : {
659 : new google.maps.LatLng( '41.214666', '-74.167834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8d55152af87d3e5667b1710419fbf5c0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8d55152af87d3e5667b1710419fbf5c0.positions ) {
gmap\_m8d55152af87d3e5667b1710419fbf5c0.bounds.extend( gmap\_m8d55152af87d3e5667b1710419fbf5c0.positions[m] );
}
// Render markers
for ( var m in gmap\_m8d55152af87d3e5667b1710419fbf5c0.positions ) {
gmap\_m8d55152af87d3e5667b1710419fbf5c0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8d55152af87d3e5667b1710419fbf5c0.map,
position : gmap\_m8d55152af87d3e5667b1710419fbf5c0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8d55152af87d3e5667b1710419fbf5c0.map.setCenter( gmap\_m8d55152af87d3e5667b1710419fbf5c0.positions[659] );
});