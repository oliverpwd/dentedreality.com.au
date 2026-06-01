---
title: ''
date: '2016-07-30T10:15:51-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '48.0940577'
longitude: '-91.0634457'
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13649117_1753861264862938_1343437918_n.jpg?fit=640%2C640
---

[![Pit stop #bwca](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13649117_1753861264862938_1343437918_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/pit-stop-bwca/) 

[![Pit stop #bwca](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13649117_1753861264862938_1343437918_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIffIGvgBSM/)

Pit stop #bwca

48.0940577-91.0634457




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIffIGvgBSM/) [10:15 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/pit-stop-bwca/ "10:15 am") 
jQuery(document).ready(function(){
var gmap\_m90285d078543a172c68fd7efc181f2d0 = {
positions : {
944 : new google.maps.LatLng( '48.0940577', '-91.0634457' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m90285d078543a172c68fd7efc181f2d0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m90285d078543a172c68fd7efc181f2d0.positions ) {
gmap\_m90285d078543a172c68fd7efc181f2d0.bounds.extend( gmap\_m90285d078543a172c68fd7efc181f2d0.positions[m] );
}
// Render markers
for ( var m in gmap\_m90285d078543a172c68fd7efc181f2d0.positions ) {
gmap\_m90285d078543a172c68fd7efc181f2d0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m90285d078543a172c68fd7efc181f2d0.map,
position : gmap\_m90285d078543a172c68fd7efc181f2d0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m90285d078543a172c68fd7efc181f2d0.map.setCenter( gmap\_m90285d078543a172c68fd7efc181f2d0.positions[944] );
});