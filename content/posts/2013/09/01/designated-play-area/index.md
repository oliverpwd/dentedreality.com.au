---
title: Designated Play Area
date: '2013-09-01T09:04:31+00:00'
format: image
tags:
- backpacking
- harriman
- harrimanstatepark
- hiking
- newyork
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/9767703852_8f52ce4f8b_o.jpg?resize=607%2C452
---

[![Designated Play Area](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/9767703852_8f52ce4f8b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/09/01/designated-play-area/) 
# [Designated Play Area](http://dentedreality.com.au/2013/09/01/designated-play-area/)





* #[backpacking](http://dentedreality.com.au/tags/backpacking/)
* #[harriman](http://dentedreality.com.au/tags/harriman/)
* #[harrimanstatepark](http://dentedreality.com.au/tags/harrimanstatepark/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767703852/) [9:04 am, September 1, 2013](http://dentedreality.com.au/2013/09/01/designated-play-area/ "9:04 am") 
jQuery(document).ready(function(){
var gmap\_m7143e85c87e20e27703c003de85347a1 = {
positions : {
92 : new google.maps.LatLng( '41.193166', '-74.1825' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7143e85c87e20e27703c003de85347a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7143e85c87e20e27703c003de85347a1.positions ) {
gmap\_m7143e85c87e20e27703c003de85347a1.bounds.extend( gmap\_m7143e85c87e20e27703c003de85347a1.positions[m] );
}
// Render markers
for ( var m in gmap\_m7143e85c87e20e27703c003de85347a1.positions ) {
gmap\_m7143e85c87e20e27703c003de85347a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7143e85c87e20e27703c003de85347a1.map,
position : gmap\_m7143e85c87e20e27703c003de85347a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7143e85c87e20e27703c003de85347a1.map.setCenter( gmap\_m7143e85c87e20e27703c003de85347a1.positions[92] );
});