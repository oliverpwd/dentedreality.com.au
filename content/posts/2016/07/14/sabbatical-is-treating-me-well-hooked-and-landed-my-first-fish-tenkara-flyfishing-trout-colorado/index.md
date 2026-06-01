---
title: ''
date: '2016-07-14T15:31:43-06:00'
format: image
service: instagram
tags:
- colorado
- flyfishing
- Tenkara
- trout
latitude: '39.4912781'
longitude: '-105.0936483'
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13696592_1219514978078925_14285858_n.jpg?fit=640%2C640
---

[![Sabbatical is treating me well. Hooked and landed my first fish. #tenkara #flyfishing #trout #colorado](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13696592_1219514978078925_14285858_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/14/sabbatical-is-treating-me-well-hooked-and-landed-my-first-fish-tenkara-flyfishing-trout-colorado/) 

[![Sabbatical is treating me well. Hooked and landed my first fish. #tenkara #flyfishing #trout #colorado](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13696592_1219514978078925_14285858_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BH22jkzASzM/)

Sabbatical is treating me well. Hooked and landed my first fish. #tenkara #flyfishing #trout #colorado

39.4912781-105.0936483




* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[flyfishing](https://dentedreality.com.au/tags/flyfishing/)
* #[Tenkara](https://dentedreality.com.au/tags/tenkara/)
* #[trout](https://dentedreality.com.au/tags/trout/)

Posted on [Instagram](https://www.instagram.com/p/BH22jkzASzM/) [3:31 pm, July 14, 2016](https://dentedreality.com.au/2016/07/14/sabbatical-is-treating-me-well-hooked-and-landed-my-first-fish-tenkara-flyfishing-trout-colorado/ "3:31 pm") 
jQuery(document).ready(function(){
var gmap\_m328deb30ac8d070935c861a286cf940d = {
positions : {
878 : new google.maps.LatLng( '39.491278115858', '-105.09364828697' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m328deb30ac8d070935c861a286cf940d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m328deb30ac8d070935c861a286cf940d.positions ) {
gmap\_m328deb30ac8d070935c861a286cf940d.bounds.extend( gmap\_m328deb30ac8d070935c861a286cf940d.positions[m] );
}
// Render markers
for ( var m in gmap\_m328deb30ac8d070935c861a286cf940d.positions ) {
gmap\_m328deb30ac8d070935c861a286cf940d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m328deb30ac8d070935c861a286cf940d.map,
position : gmap\_m328deb30ac8d070935c861a286cf940d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m328deb30ac8d070935c861a286cf940d.map.setCenter( gmap\_m328deb30ac8d070935c861a286cf940d.positions[878] );
});