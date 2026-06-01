---
title: ''
date: '2010-10-31T03:25:51+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/67638a86154b4ebeb97578f62950d2af_7.jpg?resize=607%2C607
---

[![Chum Li v Guile (?)](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/67638a86154b4ebeb97578f62950d2af_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/10/31/chum-li-v-guile/) 

Chum Li v Guile (?)





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/HGyI/) [3:25 am, October 31, 2010](http://dentedreality.com.au/2010/10/31/chum-li-v-guile/ "3:25 am") 
jQuery(document).ready(function(){
var gmap\_mb55bfed6578793bd93ca5319033078b3 = {
positions : {
46 : new google.maps.LatLng( '37.78952045', '-122.420632' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb55bfed6578793bd93ca5319033078b3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb55bfed6578793bd93ca5319033078b3.positions ) {
gmap\_mb55bfed6578793bd93ca5319033078b3.bounds.extend( gmap\_mb55bfed6578793bd93ca5319033078b3.positions[m] );
}
// Render markers
for ( var m in gmap\_mb55bfed6578793bd93ca5319033078b3.positions ) {
gmap\_mb55bfed6578793bd93ca5319033078b3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb55bfed6578793bd93ca5319033078b3.map,
position : gmap\_mb55bfed6578793bd93ca5319033078b3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb55bfed6578793bd93ca5319033078b3.map.setCenter( gmap\_mb55bfed6578793bd93ca5319033078b3.positions[46] );
});