---
title: ''
date: '2014-11-05T11:33:43+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10731889_411672112318152_324990653_n.jpg?resize=640%2C640
---

[![Bacon for the people.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10731889_411672112318152_324990653_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/05/bacon-for-the-people/) 

Bacon for the people.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/vBzt_xCmAE/) [11:33 am, November 5, 2014](http://dentedreality.com.au/2014/11/05/bacon-for-the-people/ "11:33 am") 
jQuery(document).ready(function(){
var gmap\_med93385011f3db7b7a33c1ece084a344 = {
positions : {
145 : new google.maps.LatLng( '40.340397801', '-105.571785767' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_med93385011f3db7b7a33c1ece084a344' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_med93385011f3db7b7a33c1ece084a344.positions ) {
gmap\_med93385011f3db7b7a33c1ece084a344.bounds.extend( gmap\_med93385011f3db7b7a33c1ece084a344.positions[m] );
}
// Render markers
for ( var m in gmap\_med93385011f3db7b7a33c1ece084a344.positions ) {
gmap\_med93385011f3db7b7a33c1ece084a344.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_med93385011f3db7b7a33c1ece084a344.map,
position : gmap\_med93385011f3db7b7a33c1ece084a344.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_med93385011f3db7b7a33c1ece084a344.map.setCenter( gmap\_med93385011f3db7b7a33c1ece084a344.positions[145] );
});