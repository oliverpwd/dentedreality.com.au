---
title: ''
date: '2016-09-14T11:18:29+00:00'
format: image
service: instagram
tags:
- a8cgm
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14262635_1109745092440659_1205513473_n.jpg?fit=640%2C640
---

[![So many of us on this flight! #a8cgm](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14262635_1109745092440659_1205513473_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/14/so-many-of-us-on-this-flight-a8cgm/) 

So many of us on this flight! #a8cgm





* #[a8cgm](http://dentedreality.com.au/tags/a8cgm/)

Posted on [Instagram](https://www.instagram.com/p/BKWC3Gsg0IP/) [11:18 am, September 14, 2016](http://dentedreality.com.au/2016/09/14/so-many-of-us-on-this-flight-a8cgm/ "11:18 am") 
jQuery(document).ready(function(){
var gmap\_mad82f0003642766786ad91ba6707e5d9 = {
positions : {
562 : new google.maps.LatLng( '39.855096', '-104.673738' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mad82f0003642766786ad91ba6707e5d9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mad82f0003642766786ad91ba6707e5d9.positions ) {
gmap\_mad82f0003642766786ad91ba6707e5d9.bounds.extend( gmap\_mad82f0003642766786ad91ba6707e5d9.positions[m] );
}
// Render markers
for ( var m in gmap\_mad82f0003642766786ad91ba6707e5d9.positions ) {
gmap\_mad82f0003642766786ad91ba6707e5d9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mad82f0003642766786ad91ba6707e5d9.map,
position : gmap\_mad82f0003642766786ad91ba6707e5d9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mad82f0003642766786ad91ba6707e5d9.map.setCenter( gmap\_mad82f0003642766786ad91ba6707e5d9.positions[562] );
});