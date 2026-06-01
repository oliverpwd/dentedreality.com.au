---
title: Tim, Shanthi and Me
date: '2008-04-05T02:58:40-06:00'
format: image
service: flickr
tags:
- australia
- beau
- beaulebens
- foresthillwinery
- me
- renniewedding
- shanthi
- tim
- timswedding
- westernaustraliadenmark
latitude: '-34.983877'
longitude: '117.298278'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2433435080_ac2853e3ef_o.jpg
---

[![Tim, Shanthi and Me](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2433435080_ac2853e3ef_o.jpg)](https://dentedreality.com.au/2008/04/05/tim-shanthi-and-me/) 
# [Tim, Shanthi and Me](https://dentedreality.com.au/2008/04/05/tim-shanthi-and-me/)

[![Tim, Shanthi and Me](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2433435080_ac2853e3ef_o.jpg)](http://www.flickr.com/photos/borkazoid/2433435080/)

-34.983877117.298278




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[beau](https://dentedreality.com.au/tags/beau/)
* #[beaulebens](https://dentedreality.com.au/tags/beaulebens/)
* #[foresthillwinery](https://dentedreality.com.au/tags/foresthillwinery/)
* #[me](https://dentedreality.com.au/tags/me/)
* #[renniewedding](https://dentedreality.com.au/tags/renniewedding/)
* #[shanthi](https://dentedreality.com.au/tags/shanthi/)
* #[tim](https://dentedreality.com.au/tags/tim/)
* #[timswedding](https://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](https://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433435080/) [2:58 am, April 5, 2008](https://dentedreality.com.au/2008/04/05/tim-shanthi-and-me/ "2:58 am") 
jQuery(document).ready(function(){
var gmap\_m39cfef96a5cfd3065c1267d05c59d721 = {
positions : {
44 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m39cfef96a5cfd3065c1267d05c59d721' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m39cfef96a5cfd3065c1267d05c59d721.positions ) {
gmap\_m39cfef96a5cfd3065c1267d05c59d721.bounds.extend( gmap\_m39cfef96a5cfd3065c1267d05c59d721.positions[m] );
}
// Render markers
for ( var m in gmap\_m39cfef96a5cfd3065c1267d05c59d721.positions ) {
gmap\_m39cfef96a5cfd3065c1267d05c59d721.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m39cfef96a5cfd3065c1267d05c59d721.map,
position : gmap\_m39cfef96a5cfd3065c1267d05c59d721.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m39cfef96a5cfd3065c1267d05c59d721.map.setCenter( gmap\_m39cfef96a5cfd3065c1267d05c59d721.positions[44] );
});