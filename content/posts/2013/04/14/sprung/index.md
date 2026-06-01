---
title: Sprung
date: '2013-04-14T11:05:46-06:00'
format: image
service: flickr
tags:
- flickriosapp:filter=nofilter
- uploaded:by=flickrmobile
latitude: '40.668'
longitude: '-73.982334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/04/14190857/8649740866_2cccbf34b2_o.jpg
---

[![Sprung](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/04/14190857/8649740866_2cccbf34b2_o.jpg)](https://dentedreality.com.au/2013/04/14/sprung/) 
# [Sprung](https://dentedreality.com.au/2013/04/14/sprung/)

[![Sprung](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/04/14190857/8649740866_2cccbf34b2_o.jpg)](http://www.flickr.com/photos/borkazoid/8649740866/)

40.668-73.982334




* #[flickriosapp:filter=nofilter](https://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8649740866/) [11:05 am, April 14, 2013](https://dentedreality.com.au/2013/04/14/sprung/ "11:05 am") 
jQuery(document).ready(function(){
var gmap\_m107538e7547928491ffbed16c1e8ae9e = {
positions : {
650 : new google.maps.LatLng( '40.668', '-73.982334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m107538e7547928491ffbed16c1e8ae9e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m107538e7547928491ffbed16c1e8ae9e.positions ) {
gmap\_m107538e7547928491ffbed16c1e8ae9e.bounds.extend( gmap\_m107538e7547928491ffbed16c1e8ae9e.positions[m] );
}
// Render markers
for ( var m in gmap\_m107538e7547928491ffbed16c1e8ae9e.positions ) {
gmap\_m107538e7547928491ffbed16c1e8ae9e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m107538e7547928491ffbed16c1e8ae9e.map,
position : gmap\_m107538e7547928491ffbed16c1e8ae9e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m107538e7547928491ffbed16c1e8ae9e.map.setCenter( gmap\_m107538e7547928491ffbed16c1e8ae9e.positions[650] );
});