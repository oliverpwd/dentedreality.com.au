---
title: ''
date: '2013-07-21T18:55:21+00:00'
format: image
service: instagram
tags:
- photo
- wcsf
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9f62888cf25811e2904822000a1fc3ed_7.jpg?resize=607%2C607
---

[![Working on my #WCSF talk. With a view.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9f62888cf25811e2904822000a1fc3ed_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2013/07/21/working-on-my-wcsf-talk-with-a-view/) 

Working on my #WCSF talk. With a view.





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)

Posted on [Instagram](http://instagram.com/p/cC6dXKCmJL/) [6:55 pm, July 21, 2013](http://dentedreality.com.au/2013/07/21/working-on-my-wcsf-talk-with-a-view/ "6:55 pm") 
jQuery(document).ready(function(){
var gmap\_mea67b56a2d8dfc7ec54c884b550d3337 = {
positions : {
549 : new google.maps.LatLng( '40.669166667', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mea67b56a2d8dfc7ec54c884b550d3337' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mea67b56a2d8dfc7ec54c884b550d3337.positions ) {
gmap\_mea67b56a2d8dfc7ec54c884b550d3337.bounds.extend( gmap\_mea67b56a2d8dfc7ec54c884b550d3337.positions[m] );
}
// Render markers
for ( var m in gmap\_mea67b56a2d8dfc7ec54c884b550d3337.positions ) {
gmap\_mea67b56a2d8dfc7ec54c884b550d3337.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mea67b56a2d8dfc7ec54c884b550d3337.map,
position : gmap\_mea67b56a2d8dfc7ec54c884b550d3337.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mea67b56a2d8dfc7ec54c884b550d3337.map.setCenter( gmap\_mea67b56a2d8dfc7ec54c884b550d3337.positions[549] );
});