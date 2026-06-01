---
title: T-Bone Adams
date: '2012-02-22T14:33:54-07:00'
format: image
service: flickr
tags:
- graffiti
- mdawaffe
- mike
latitude: '37.759666'
longitude: '-122.414834'
image: http://dentedreality.com.au/wp-content/uploads/2012/02/6813461086_a6f069bc4f_o-1024x764.jpg
---

[![T-Bone Adams](http://dentedreality.com.au/wp-content/uploads/2012/02/6813461086_a6f069bc4f_o-1024x764.jpg)](https://dentedreality.com.au/2012/02/22/t-bone-adams/) 
# [T-Bone Adams](https://dentedreality.com.au/2012/02/22/t-bone-adams/)

[![T-Bone Adams](http://dentedreality.com.au/wp-content/uploads/2012/02/6813461086_a6f069bc4f_o-1024x764.jpg)](http://www.flickr.com/photos/borkazoid/6813461086/)

37.759666-122.414834




* #[graffiti](https://dentedreality.com.au/tags/graffiti/)
* #[mdawaffe](https://dentedreality.com.au/tags/mdawaffe/)
* #[mike](https://dentedreality.com.au/tags/mike/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813461086/) [2:33 pm, February 22, 2012](https://dentedreality.com.au/2012/02/22/t-bone-adams/ "2:33 pm") 
jQuery(document).ready(function(){
var gmap\_m8e9189948913f0b2e7a79c491f471db1 = {
positions : {
427 : new google.maps.LatLng( '37.759666', '-122.414834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8e9189948913f0b2e7a79c491f471db1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8e9189948913f0b2e7a79c491f471db1.positions ) {
gmap\_m8e9189948913f0b2e7a79c491f471db1.bounds.extend( gmap\_m8e9189948913f0b2e7a79c491f471db1.positions[m] );
}
// Render markers
for ( var m in gmap\_m8e9189948913f0b2e7a79c491f471db1.positions ) {
gmap\_m8e9189948913f0b2e7a79c491f471db1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8e9189948913f0b2e7a79c491f471db1.map,
position : gmap\_m8e9189948913f0b2e7a79c491f471db1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8e9189948913f0b2e7a79c491f471db1.map.setCenter( gmap\_m8e9189948913f0b2e7a79c491f471db1.positions[427] );
});