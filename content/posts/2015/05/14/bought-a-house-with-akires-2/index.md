---
title: ''
date: '2015-05-14T16:45:25+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11232579_1569916823259800_338433152_n.jpg?resize=640%2C640
---

[![Bought a house with @akires!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11232579_1569916823259800_338433152_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/14/bought-a-house-with-akires-2/) 

Bought a house with @akires!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/2rfjvdimCr/) [4:45 pm, May 14, 2015](http://dentedreality.com.au/2015/05/14/bought-a-house-with-akires-2/ "4:45 pm") 
jQuery(document).ready(function(){
var gmap\_m0f9de82b44a4140af7cd9a18d6183f15 = {
positions : {
724 : new google.maps.LatLng( '39.759913333', '-104.969528333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0f9de82b44a4140af7cd9a18d6183f15' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0f9de82b44a4140af7cd9a18d6183f15.positions ) {
gmap\_m0f9de82b44a4140af7cd9a18d6183f15.bounds.extend( gmap\_m0f9de82b44a4140af7cd9a18d6183f15.positions[m] );
}
// Render markers
for ( var m in gmap\_m0f9de82b44a4140af7cd9a18d6183f15.positions ) {
gmap\_m0f9de82b44a4140af7cd9a18d6183f15.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0f9de82b44a4140af7cd9a18d6183f15.map,
position : gmap\_m0f9de82b44a4140af7cd9a18d6183f15.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0f9de82b44a4140af7cd9a18d6183f15.map.setCenter( gmap\_m0f9de82b44a4140af7cd9a18d6183f15.positions[724] );
});