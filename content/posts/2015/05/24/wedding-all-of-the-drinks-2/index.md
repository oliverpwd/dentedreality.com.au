---
title: ''
date: '2015-05-24T21:44:39+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11352928_100811016925150_61436987_n.jpg?resize=640%2C640
---

[![Wedding. All of the drinks.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11352928_100811016925150_61436987_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/24/wedding-all-of-the-drinks-2/) 

Wedding. All of the drinks.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/3FxwJ3CmOR/) [9:44 pm, May 24, 2015](http://dentedreality.com.au/2015/05/24/wedding-all-of-the-drinks-2/ "9:44 pm") 
jQuery(document).ready(function(){
var gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11 = {
positions : {
824 : new google.maps.LatLng( '37.720214891', '-122.193466532' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.positions ) {
gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.bounds.extend( gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.positions[m] );
}
// Render markers
for ( var m in gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.positions ) {
gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.map,
position : gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.map.setCenter( gmap\_m6556c3dc9f3856ac1a6cd0bc7b44ce11.positions[824] );
});