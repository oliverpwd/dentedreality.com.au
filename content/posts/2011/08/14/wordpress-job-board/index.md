---
title: WordPress Job Board
date: '2011-08-14T11:27:26+00:00'
format: image
service: flickr
tags:
- jobs
- wcsf
- wordcampsf
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322992759_58bbf4f75b_o.jpg?resize=607%2C452
---

[![WordPress Job Board](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322992759_58bbf4f75b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/08/14/wordpress-job-board/) 
# [WordPress Job Board](http://dentedreality.com.au/2011/08/14/wordpress-job-board/)

As seen at WordCampSF





* #[jobs](http://dentedreality.com.au/tags/jobs/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wordcampsf](http://dentedreality.com.au/tags/wordcampsf/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322992759/) [11:27 am, August 14, 2011](http://dentedreality.com.au/2011/08/14/wordpress-job-board/ "11:27 am") 
jQuery(document).ready(function(){
var gmap\_m090d41676c9e299b2c5f3f598b8c3f3a = {
positions : {
980 : new google.maps.LatLng( '37.768', '-122.392834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m090d41676c9e299b2c5f3f598b8c3f3a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.positions ) {
gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.bounds.extend( gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.positions[m] );
}
// Render markers
for ( var m in gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.positions ) {
gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.map,
position : gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.map.setCenter( gmap\_m090d41676c9e299b2c5f3f598b8c3f3a.positions[980] );
});