---
title: ''
date: '2015-05-23T15:35:37+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/10424637_1010570742289309_835958717_n.jpg?resize=640%2C640
---

[![Building Gap](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/10424637_1010570742289309_835958717_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/23/building-gap/) 

Building Gap





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/3Ciub5imDx/) [3:35 pm, May 23, 2015](http://dentedreality.com.au/2015/05/23/building-gap/ "3:35 pm") 
jQuery(document).ready(function(){
var gmap\_mb10aa31a1d3370e4721478c9632ad919 = {
positions : {
392 : new google.maps.LatLng( '37.765003333', '-122.413345' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb10aa31a1d3370e4721478c9632ad919' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb10aa31a1d3370e4721478c9632ad919.positions ) {
gmap\_mb10aa31a1d3370e4721478c9632ad919.bounds.extend( gmap\_mb10aa31a1d3370e4721478c9632ad919.positions[m] );
}
// Render markers
for ( var m in gmap\_mb10aa31a1d3370e4721478c9632ad919.positions ) {
gmap\_mb10aa31a1d3370e4721478c9632ad919.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb10aa31a1d3370e4721478c9632ad919.map,
position : gmap\_mb10aa31a1d3370e4721478c9632ad919.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb10aa31a1d3370e4721478c9632ad919.map.setCenter( gmap\_mb10aa31a1d3370e4721478c9632ad919.positions[392] );
});