---
title: Beautiful Islands
date: '2006-12-28T18:54:29-06:00'
format: image
service: flickr
tags:
- boat
- island
- islands
- phuket
- thailand
- thailand06
latitude: '8.095005'
longitude: '98.457927'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2006/12/14184346/348096649_47e4a08fc6_o.jpg
---

[![Beautiful Islands](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2006/12/14184346/348096649_47e4a08fc6_o.jpg)](https://dentedreality.com.au/2006/12/28/beautiful-islands/) 
# [Beautiful Islands](https://dentedreality.com.au/2006/12/28/beautiful-islands/)

[![Beautiful Islands](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2006/12/14184346/348096649_47e4a08fc6_o.jpg)](http://www.flickr.com/photos/borkazoid/348096649/)

They’re everywhere

8.09500598.457927




* #[boat](https://dentedreality.com.au/tags/boat/)
* #[island](https://dentedreality.com.au/tags/island/)
* #[islands](https://dentedreality.com.au/tags/islands/)
* #[phuket](https://dentedreality.com.au/tags/phuket/)
* #[thailand](https://dentedreality.com.au/tags/thailand/)
* #[thailand06](https://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348096649/) [6:54 pm, December 28, 2006](https://dentedreality.com.au/2006/12/28/beautiful-islands/ "6:54 pm") 
jQuery(document).ready(function(){
var gmap\_m5c1f0677a1336fd5c3caa2855a5126ae = {
positions : {
120 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5c1f0677a1336fd5c3caa2855a5126ae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.positions ) {
gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.bounds.extend( gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.positions[m] );
}
// Render markers
for ( var m in gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.positions ) {
gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.map,
position : gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.map.setCenter( gmap\_m5c1f0677a1336fd5c3caa2855a5126ae.positions[120] );
});