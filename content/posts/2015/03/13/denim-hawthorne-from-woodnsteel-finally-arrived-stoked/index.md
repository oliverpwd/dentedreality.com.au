---
title: ''
date: '2015-03-13T15:03:33+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/03/11049420_829850543774395_810631554_n.jpg?resize=640%2C640
---

[![Denim Hawthorne from @woodnsteel finally arrived! Stoked!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/03/11049420_829850543774395_810631554_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/03/13/denim-hawthorne-from-woodnsteel-finally-arrived-stoked/) 

Denim Hawthorne from @woodnsteel finally arrived! Stoked!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/0Lqnf8CmN1/) [3:03 pm, March 13, 2015](http://dentedreality.com.au/2015/03/13/denim-hawthorne-from-woodnsteel-finally-arrived-stoked/ "3:03 pm") 
jQuery(document).ready(function(){
var gmap\_m0079351b28a762261d0704655be66ed4 = {
positions : {
617 : new google.maps.LatLng( '39.734795', '-104.978553333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0079351b28a762261d0704655be66ed4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0079351b28a762261d0704655be66ed4.positions ) {
gmap\_m0079351b28a762261d0704655be66ed4.bounds.extend( gmap\_m0079351b28a762261d0704655be66ed4.positions[m] );
}
// Render markers
for ( var m in gmap\_m0079351b28a762261d0704655be66ed4.positions ) {
gmap\_m0079351b28a762261d0704655be66ed4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0079351b28a762261d0704655be66ed4.map,
position : gmap\_m0079351b28a762261d0704655be66ed4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0079351b28a762261d0704655be66ed4.map.setCenter( gmap\_m0079351b28a762261d0704655be66ed4.positions[617] );
});