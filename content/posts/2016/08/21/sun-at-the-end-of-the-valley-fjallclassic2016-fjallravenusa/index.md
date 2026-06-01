---
title: ''
date: '2016-08-21T21:36:21+00:00'
format: image
service: instagram
tags:
- fjallclassic2016
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/14099318_1082232038534413_1571635623_n.jpg?fit=640%2C640
---

[![Sun at the end of the valley. #fjallclassic2016 @fjallravenusa](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/14099318_1082232038534413_1571635623_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/21/sun-at-the-end-of-the-valley-fjallclassic2016-fjallravenusa/) 

Sun at the end of the valley. #fjallclassic2016 @fjallravenusa





* #[fjallclassic2016](http://dentedreality.com.au/tags/fjallclassic2016/)

Posted on [Instagram](https://www.instagram.com/p/BJZWfjVA3Cy/) [9:36 pm, August 21, 2016](http://dentedreality.com.au/2016/08/21/sun-at-the-end-of-the-valley-fjallclassic2016-fjallravenusa/ "9:36 pm") 
jQuery(document).ready(function(){
var gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad = {
positions : {
218 : new google.maps.LatLng( '40.5113831', '-106.0084839' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.positions ) {
gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.bounds.extend( gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.positions[m] );
}
// Render markers
for ( var m in gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.positions ) {
gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.map,
position : gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.map.setCenter( gmap\_mae9ccb533c36f9511f5a4e6b8a1314ad.positions[218] );
});